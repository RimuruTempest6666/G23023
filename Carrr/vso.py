import pygame
import sys
import random

#settings
FPS = 60
SC_WIDTH = 1000
SC_HEIGHT = 700
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DodgerBlue = (30, 144, 255)
speed = 7
speedy = 5
CACTUS_W = 87
CACTUS_H = 100
CAR_W = 112
CAR_H = 258

#car
class Car(pygame.sprite.Sprite):

    def __init__(self, x, y, filename, right_key, left_key):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.right_key = right_key
        self.left_key = left_key
        self.speed = speed

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[self.right_key]:
           self.rect.x += self.speed
        elif keys[self.left_key]:
            self.rect.x -= self.speed

        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.x >= SC_WIDTH - CAR_W:
            self.rect.x = SC_WIDTH - CAR_W
        if self.rect.y >= SC_HEIGHT:
            self.rect.y = SC_HEIGHT

    def draw(self, screen):
        screen.blit(self.image, self.rect)




#препятствия
class Cactus(pygame.sprite.Sprite):
    
    def __init__(self, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,SC_WIDTH - CACTUS_W)
        self.rect.bottom = 0
        self.speed = speedy


    def update(self):
        self.rect.y += self.speed
        
        if self.rect.top >= SC_HEIGHT:
            self.rect.bottom = 0
            self.rect.x = random.randrange(0, SC_WIDTH - CACTUS_W)


    def draw(self, screen):
        screen.blit(self.image, self.rect)








# создание объектов
pygame.init()
screen = pygame.display.set_mode((SC_WIDTH, SC_HEIGHT))
clock = pygame.time.Clock()
car = Car(SC_WIDTH / 2, SC_HEIGHT / 2, "masina.png" , pygame.K_RIGHT, pygame.K_LEFT)
cactusi = []
for i in range(5):
    cactus1 = Cactus("cactus.png")
    cactusi.append(cactus1)

# главный цикл
while True:
    # задержка
    clock.tick(FPS)
    # цикл обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # изменение объектов, update
    car.update()
    for cactus1 in cactusi:
        cactus1.update()


          
    # обновление экрана
    screen.fill(BLACK)
    car.draw(screen)
    for cactus1 in cactusi:
        cactus1.draw(screen)
    pygame.display.update()

