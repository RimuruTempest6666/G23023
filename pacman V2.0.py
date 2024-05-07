import pygame
import numpy as np
import tcod
import random
from enum import Enum
from time import sleep
import sys

# Создание перечислений для различных направлений
class Direction(Enum):
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3,
    NONE = 4

# Функция для преобразования экранных координат в координаты лабиринта
def translate_screen_to_maze(in_coords, in_size=32):
    return int(in_coords[0] / in_size), int(in_coords[1] / in_size)

# Функция для преобразования координат лабиринта в экранные координаты
def translate_maze_to_screen(in_coords, in_size=32):
    return in_coords[0] * in_size, in_coords[1] * in_size

# Создание базового класса для игровых объектов
class GameObject:
    def __init__(self, in_surface, x, y,
                 in_size: int, in_color=(255, 0, 0),
                 is_circle: bool = False):
        self._size = in_size
        self._renderer: GameRenderer = in_surface
        self._surface = in_surface._screen
        self.y = y
        self.x = x
        self._color = in_color
        self._circle = is_circle
        self._shape = pygame.Rect(self.x, self.y, in_size, in_size)

    def draw(self):
        """Отрисовка объекта на экране."""
        if self._circle:
            pygame.draw.circle(self._surface,
                               self._color,
                               (self.x + self._size // 2, self.y + self._size // 2),
                               self._size // 2)
        else:
            rect_object = pygame.Rect(self.x, self.y, self._size, self._size)
            pygame.draw.rect(self._surface, self._color, rect_object)

    def tick(self):
        """Обновление состояния объекта."""
        pass

    def get_shape(self):
        """Получение прямоугольной формы объекта."""
        return self._shape

    def set_position(self, in_x, in_y):
        """Установка новой позиции объекта."""
        self.x = in_x
        self.y = in_y

    def get_position(self):
        """Получение текущей позиции объекта."""
        return (self.x, self.y)

# Создание класса для стен
class Wall(GameObject):
    def __init__(self, in_surface, x, y, in_size: int, in_color=(0, 0, 255)):
        super().__init__(in_surface, x * in_size, y * in_size, in_size, in_color)

# Класс для рендеринга игры
class GameRenderer:
    def __init__(self, in_width: int, in_height: int):
        pygame.init()
        self._width = in_width
        self._height = in_height
        self._screen = pygame.display.set_mode((in_width, in_height))
        pygame.display.set_caption('Pacman')
        self._clock = pygame.time.Clock()
        self._done = False
        self._game_objects = []
        self._walls = []
        self._cookies = []
        self._hero: Hero = None
        self._score = 0  # Счетчик очков
        self._font = pygame.font.SysFont(None, 24)  # Шрифт для отображения очков

    def draw_score(self):
        """Отображение очков на экране."""
        score_text = f"Score: {self._score}"
        text_surface = self._font.render(score_text, True, (255, 255, 255))
        self._screen.blit(text_surface, (10, 10))

    def tick(self, in_fps: int):
        black = (0, 0, 0)
        while not self._done:
            for game_object in self._game_objects:
                game_object.tick()
                game_object.draw()

            # Отрисовка очков
            self.draw_score()

            pygame.display.flip()
            self._clock.tick(in_fps)
            self._screen.fill(black)
            self._handle_events()
        print("Game over")

    def add_game_object(self, obj: GameObject):
        """Добавление игрового объекта к списку."""
        self._game_objects.append(obj)

    def add_cookie(self, obj: GameObject):
        """Добавление печенья к списку игровых объектов."""
        self._game_objects.append(obj)
        self._cookies.append(obj)

    def add_wall(self, obj: Wall):
        """Добавление стены к списку игровых объектов."""
        self.add_game_object(obj)
        self._walls.append(obj)

    def get_walls(self):
        """Получение списка всех стен."""
        return self._walls

    def get_cookies(self):
        """Получение списка всех печений."""
        return self._cookies

    def get_game_objects(self):
        """Получение списка всех игровых объектов."""
        return self._game_objects

    def add_hero(self, in_hero):
        """Добавление героя к списку игровых объектов."""
        self.add_game_object(in_hero)
        self._hero = in_hero

    def _handle_events(self):
        """Обработка событий (например, нажатие клавиш)."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._done = True

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self._hero.set_direction(Direction.UP)
        elif pressed[pygame.K_LEFT]:
            self._hero.set_direction(Direction.LEFT)
        elif pressed[pygame.K_DOWN]:
            self._hero.set_direction(Direction.DOWN)
        elif pressed[pygame.K_RIGHT]:
            self._hero.set_direction(Direction.RIGHT)

    def increment_score(self, points):
        """Увеличение очков игрока."""
        self._score += points

# Класс для движущихся объектов
class MovableObject(GameObject):
    def __init__(self, in_surface, x, y, in_size: int, in_color=(255, 0, 0), is_circle: bool = False):
        super().__init__(in_surface, x, y, in_size, in_color, is_circle)
        self.current_direction = Direction.NONE
        self.direction_buffer = Direction.NONE
        self.last_working_direction = Direction.NONE
        self.location_queue = []
        self.next_target = None

    def get_next_location(self):
        """Получение следующей локации."""
        return None if len(self.location_queue) == 0 else self.location_queue.pop(0)

    def set_direction(self, in_direction):
        """Установка направления."""
        self.current_direction = in_direction
        self.direction_buffer = in_direction

    def collides_with_wall(self, in_position):
        """Проверка столкновения с препятствием."""
        collision_rect = pygame.Rect(in_position[0], in_position[1], self._size, self._size)
        collides = False
        walls = self._renderer.get_walls()
        for wall in walls:
            collides = collision_rect.colliderect(wall.get_shape())
            if collides:
                break
        return collides

    def check_collision_in_direction(self, in_direction: Direction):
        """Проверка столкновения в определенном направлении."""
        desired_position = (0, 0)
        if in_direction == Direction.NONE:
            return False, desired_position

        if in_direction == Direction.UP:
            desired_position = (self.x, self.y - 1)
        elif in_direction == Direction.DOWN:
            desired_position = (self.x, self.y + 1)
        elif in_direction == Direction.LEFT:
            desired_position = (self.x - 1, self.y)
        elif in_direction == Direction.RIGHT:
            desired_position = (self.x + 1, self.y)

        return self.collides_with_wall(desired_position), desired_position

    def automatic_move(self, in_direction: Direction):
        """Перемещение в определенном направлении."""
        if in_direction == Direction.UP:
            self.y -= 1
        elif in_direction == Direction.DOWN:
            self.y += 1
        elif in_direction == Direction.LEFT:
            self.x -= 1
        elif in_direction == Direction.RIGHT:
            self.x += 1

    def tick(self):
        """Обновление состояния объекта за каждый кадр."""
        self.reached_target()
        self.automatic_move(self.current_direction)

    def reached_target(self):
        """Проверка достижения цели."""
        pass

# Класс героя Pac-Man
class Hero(MovableObject):
    def __init__(self, in_surface, x, y, in_size: int):
        super().__init__(in_surface, x, y, in_size, (255, 255, 0), False)
        self.last_non_colliding_position = (0, 0)
        self.is_immobilized = False  # Параметр для отслеживания обездвиженности Pac-Man
        self.portal_cooldown = 0  # Время перезагрузки порталов

    def tick(self):
        """Обновление состояния героя."""
        # Проверка порталов
        if self.portal_cooldown > 0:
            self.portal_cooldown -= 1

        # Обработка телепортации через порталы
        if not self.is_immobilized:
            self.handle_portals()
            
        # Обработка вращения лабиринта
        self.handle_maze_rotation()

        # Обработка обездвиженности (ловушек)
        if self.is_immobilized:
            sleep(1)
            self.is_immobilized = False

        # Обработка столкновения с границей
        if self.x < 0:
            self.x = self._renderer._width
        elif self.x > self._renderer._width:
            self.x = 0

        # Обработка столкновения с препятствиями
        if self.check_collision_in_direction(self.direction_buffer)[0]:
            self.automatic_move(self.current_direction)
        else:
            self.set_direction(self.direction_buffer)
            self.automatic_move(self.current_direction)

        # Обработка съеденных печений
        self.handle_cookies()

    def handle_portals(self):
        """Обработка телепортации через порталы."""
        # Имитация порталов, которые телепортируют Pac-Man в случайные места лабиринта
        # Это можно улучшить с учетом реальной карты лабиринта
        if random.randint(1, 100) > 95 and self.portal_cooldown == 0:
            random_x = random.randint(0, self._renderer._width // self._size) * self._size
            random_y = random.randint(0, self._renderer._height // self._size) * self._size
            self.set_position(random_x, random_y)
            self.portal_cooldown = 50  # Устанавливаем перезагрузку порталов

    def handle_maze_rotation(self):
        """Обработка вращения лабиринта."""
        # Имитация вращения лабиринта, которое влияет на направление Pac-Man
        if random.randint(1, 100) > 95:
            self.current_direction = Direction((self.current_direction.value + 1) % 4)

    def handle_cookies(self):
        """Обработка съеденных печений."""
        for cookie in self._renderer.get_cookies():
            if pygame.Rect(self.get_shape()).colliderect(cookie.get_shape()):
                self._renderer.increment_score(10)  # Добавляем очки
                self._renderer._game_objects.remove(cookie)
                self._renderer._cookies.remove(cookie)

# Класс для привидения
class Ghost(MovableObject):
    def __init__(self, in_surface, x, y, in_size, in_color=(255, 0, 0), is_circle=False):
        super().__init__(in_surface, x, y, in_size, in_color, is_circle)
        self.strategies = [self.random_strategy, self.chase_hero_strategy]  # Список стратегий

    def tick(self):
        """Обновление состояния привидения."""
        self.reached_target()
        self.automatic_move(self.current_direction)

        # Используем случайно выбранную стратегию для привидения
        strategy = random.choice(self.strategies)
        strategy()

    def random_strategy(self):
        """Случайное движение."""
        if random.randint(1, 100) > 95:
            self.current_direction = random.choice(list(Direction))

    def chase_hero_strategy(self):
        """Преследование героя."""
        # Привидение будет двигаться в направлении героя
        hero_pos = self._renderer._hero.get_position()
        if hero_pos[0] > self.x:
            self.current_direction = Direction.RIGHT
        elif hero_pos[0] < self.x:
            self.current_direction = Direction.LEFT
        elif hero_pos[1] > self.y:
            self.current_direction = Direction.DOWN
        elif hero_pos[1] < self.y:
            self.current_direction = Direction.UP

        self.automatic_move(self.current_direction)

# Добавление гигантского призрака, который медленный, но занимает больше места
class GiantGhost(Ghost):
    def __init__(self, in_surface, x, y, in_size):
        super().__init__(in_surface, x, y, in_size * 2, (128, 0, 128), is_circle=True)

# Класс для создания ловушек, которые обездвиживают Pac-Man или привидений
class Trap(GameObject):
    def __init__(self, in_surface, x, y, in_size: int, in_color=(255, 0, 0)):
        super().__init__(in_surface, x, y, in_size, in_color, is_circle=True)

    def tick(self):
        """Обработка столкновений с ловушками."""
        # Проверка столкновений с героем
        hero = self._renderer._hero
        if pygame.Rect(self.get_shape()).colliderect(hero.get_shape()):
            hero.is_immobilized = True
            self._renderer._game_objects.remove(self)

        # Проверка столкновений с привидениями
        for game_object in self._renderer._game_objects:
            if isinstance(game_object, Ghost):
                if pygame.Rect(self.get_shape()).colliderect(game_object.get_shape()):
                    game_object.set_direction(Direction.NONE)  # Остановка привидения
                    self._renderer._game_objects.remove(self)

# Функция для отображения начального меню
def main_menu(renderer):
    """Отображение главного меню."""
    pygame.init()
    screen = pygame.display.set_mode((renderer._width, renderer._height))
    pygame.display.set_caption('Pac-Man Menu')
    font = pygame.font.SysFont(None, 36)
    running = True
    while running:
        screen.fill((0, 0, 0))
        title = font.render("Pac-Man", True, (255, 255, 255))
        start = font.render("Start Game", True, (255, 255, 255))
        instructions = font.render("Instructions", True, (255, 255, 255))
        exit_game = font.render("Exit", True, (255, 255, 255))

        # Позиционирование элементов меню
        screen.blit(title, (renderer._width // 2 - title.get_width() // 2, 50))
        screen.blit(start, (renderer._width // 2 - start.get_width() // 2, 150))
        screen.blit(instructions, (renderer._width // 2 - instructions.get_width() // 2, 250))
        screen.blit(exit_game, (renderer._width // 2 - exit_game.get_width() // 2, 350))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if start.get_rect(center=(renderer._width // 2, 150)).collidepoint(pos):
                    # Начать игру
                    running = False
                elif instructions.get_rect(center=(renderer._width // 2, 250)).collidepoint(pos):
                    # Показать инструкции
                    show_instructions(renderer)
                elif exit_game.get_rect(center=(renderer._width // 2, 350)).collidepoint(pos):
                    # Выход из игры
                    pygame.quit()
                    sys.exit()

def show_instructions(renderer):
    """Отображение инструкции."""
    pygame.init()
    screen = pygame.display.set_mode((renderer._width, renderer._height))
    pygame.display.set_caption('Pac-Man Instructions')
    font = pygame.font.SysFont(None, 36)
    running = True
    instructions_text = [
        "Instructions:",
        "1. Use arrow keys to move Pac-Man",
        "2. Collect all cookies for points",
        "3. Avoid ghosts and traps",
        "4. Use portals to teleport",
        "5. Survive as long as possible"
    ]

    while running:
        screen.fill((0, 0, 0))
        y_position = 50
        for line in instructions_text:
            instruction_line = font.render(line, True, (255, 255, 255))
            screen.blit(instruction_line, (50, y_position))
            y_position += 50

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                running = False

# Основная функция
def main():
    """Основная функция программы."""
    # Установка размеров окна
    renderer = GameRenderer(640, 480)

    # Отображение главного меню
    main_menu(renderer)

    # Добавление героя
    hero = Hero(renderer, 160, 160, 32)
    renderer.add_hero(hero)

    # Добавление привидений
    ghost = Ghost(renderer, 128, 128, 32)
    renderer.add_game_object(ghost)

    giant_ghost = GiantGhost(renderer, 384, 384, 32)
    renderer.add_game_object(giant_ghost)

    # Добавление ловушек
    trap = Trap(renderer, 256, 256, 16)
    renderer.add_game_object(trap)

    # Запуск игрового процесса
    renderer.tick(60)

if __name__ == '__main__':
    main()
