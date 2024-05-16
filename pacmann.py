import pygame
import sys
import random

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = 'right'

    def move(self, direction):
        self.direction = direction
        if self.direction == 'up':
            self.y -= 0.1
        elif self.direction == 'down':
            self.y += 0.1
        elif self.direction == 'left':
            self.x -= 0.1
        elif self.direction == 'right':
            self.x += 0.1

        # Проверяем, не выходит ли игрок за пределы экрана
        if self.x < 0:
            self.x = 0
        elif self.x > SCREEN_WIDTH / BLOCK_SIZE - 1:
            self.x = SCREEN_WIDTH / BLOCK_SIZE - 1
        if self.y < 0:
            self.y = 0
        elif self.y > SCREEN_HEIGHT / BLOCK_SIZE - 1:
            self.y = SCREEN_HEIGHT / BLOCK_SIZE - 1

class Eat:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_eaten(self, player):
        return int(self.x) == int(player.x) and int(self.y) == int(player.y)

class Score:
    def __init__(self):
        self.value = 0

    def increase(self):
        self.value += 1

# Инициализация Pygame
pygame.init()

# Определение констант
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLOCK_SIZE = 20
EAT_SIZE = BLOCK_SIZE // 2

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pac-Man')

# Создание объектов
player = Player(10, 10)
eats = [Eat(random.randint(0, SCREEN_WIDTH // EAT_SIZE - 1), random.randint(0, SCREEN_HEIGHT // EAT_SIZE - 1)) for _ in range(10)]
score = Score()

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обработка зажатых клавиш
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.move('up')
    if keys[pygame.K_DOWN]:
        player.move('down')
    if keys[pygame.K_LEFT]:
        player.move('left')
    if keys[pygame.K_RIGHT]:
        player.move('right')

    # Проверка, была ли съедена еда
    for eat in eats:
        if eat.is_eaten(player):
            score.increase()
            eats.remove(eat)
            eats.append(Eat(random.randint(0, SCREEN_WIDTH // BLOCK_SIZE - 1), random.randint(0, SCREEN_HEIGHT // BLOCK_SIZE - 1)))

    # Отрисовка игрового поля
    screen.fill(BLACK)
    pygame.draw.circle(screen, YELLOW, (int((player.x + 0.5) * BLOCK_SIZE), int((player.y + 0.5) * BLOCK_SIZE)), BLOCK_SIZE // 2)
    for eat in eats:
        pygame.draw.circle(screen, WHITE, (int((eat.x + 0.5) * BLOCK_SIZE), int((eat.y + 0.5) * BLOCK_SIZE)), EAT_SIZE)

    # Отображение счета
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {score.value}', True, WHITE)
    screen.blit(score_text, (10, 10))

    # Обновление экрана
    pygame.display.flip()

    # Задержка для контроля частоты обновления экрана
    pygame.time.delay(10)

# Выход из Pygame
pygame.quit()
sys.exit()




