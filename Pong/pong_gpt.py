import pygame
import random

# Инициализация Pygame
pygame.init()

# Установка экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")



# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Переменные игры
player1_score = 0
player2_score = 0
ball_speed_x = 5 * random.choice((1, -1))
ball_speed_y = 5 * random.choice((1, -1))
player1_speed = 0
player2_speed = 0
game_font = pygame.font.Font("freesansbold.ttf", 32)

# Определение игровых объектов
player1 = pygame.Rect(WIDTH - 20, HEIGHT // 2 - 60, 10, 120)
player2 = pygame.Rect(10, HEIGHT // 2 - 60, 10, 120)
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)

# Игровой цикл
running = True
clock = pygame.time.Clock()

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (WIDTH // 2, HEIGHT // 2)
    ball_speed_x *= random.choice((1, -1))
    ball_speed_y *= random.choice((1, -1))

def draw_score():
    player1_text = game_font.render(str(player1_score), True, RED)
    player2_text = game_font.render(str(player2_score), True, BLUE)
    screen.blit(player1_text, (WIDTH // 2 + 40, 10))
    screen.blit(player2_text, (WIDTH // 2 - 60, 10))

def draw_objects():
    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)
    pygame.draw.ellipse(screen, WHITE, ball)

# Главный игровой цикл
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player1_speed = -7
            elif event.key == pygame.K_DOWN:
                player1_speed = 7
            elif event.key == pygame.K_w:
                player2_speed = -7
            elif event.key == pygame.K_s:
                player2_speed = 7
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player1_speed = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                player2_speed = 0

    # Движение игроков
    player1.y += player1_speed
    player2.y += player2_speed

    # Движение мяча
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Обработка столкновений мяча с верхней и нижней стенкой
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        pygame.mixer.Sound.play(bounce_sound)
        ball_speed_y *= -1

    # Обработка столкновений мяча с ракетками
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1

    # Обработка выхода мяча за границы экрана
    if ball.left <= 0:
        pygame.mixer.Sound.play(score_sound)
        player2_score += 1
        ball_restart()
    elif ball.right >= WIDTH:
        pygame.mixer.Sound.play(score_sound)
        player1_score += 1
        ball_restart()

    # Отрисовка фона
    screen.fill(BLACK)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Отрисовка игровых объектов и счета
    draw_objects()
    draw_score()

    # Обновление экрана
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
