import pygame
import sys
import random

#settings
FPS = 80
SC_WIDTH = 1000
SC_HEIGHT = 700
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DodgerBlue = (30, 144, 255)
speed = 7
speedy = 3
CACTUS_W = 87
CACTUS_H = 100
CHOCOLATE_W = 173
CHOCOLATE_H = 90
PLAYER_W = 142
PLAYER_H = 200


#car
class Player(pygame.sprite.Sprite):

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
        if self.rect.right >= SC_WIDTH:
            self.rect.right = SC_WIDTH


    def draw(self, screen):
        screen.blit(self.image, self.rect)




#препятствия
class Havchik(pygame.sprite.Sprite):
    
    def __init__(self, filename, edible):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.edible = edible
        self.rect.x = random.randrange(0,SC_WIDTH - self.rect.width)
        self.rect.bottom = random.randrange(-SC_HEIGHT, 0)
        self.speed = speedy


    def update(self):
        self.rect.y += self.speed
        
        if self.rect.top >= SC_HEIGHT:
            self.rect.bottom = 0
            self.rect.x = random.randrange(0, SC_WIDTH - self.rect.width)


    def draw(self, screen):
        screen.blit(self.image, self.rect)


    def get_edible(self):
        return self.edible


#ochki
class Text_obj:

    def __init__(self, x, y, score, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.score = score
        self.font = pygame.font.SysFont('arial', 32)


    def update(self, score):
        self.score = score
        self.text = self.font.render(str(self.score), True, WHITE)
        self.text_rect = self.text.get_rect()
        self.text_rect = (self.x, self.y)


    def draw(self):
        self.screen.blit(self.text, self.text_rect)








# создание объектов and groups
pygame.init()
screen = pygame.display.set_mode((SC_WIDTH, SC_HEIGHT))
clock = pygame.time.Clock()
player = Player(SC_WIDTH / 2, SC_HEIGHT - PLAYER_H, "Neko.png" , pygame.K_RIGHT, pygame.K_LEFT)



#groups
all_sprites = pygame.sprite.Group
items = pygame.sprite.Group

all_sprites.add(player)

for i in range(5):
    chocolate = Havchik("chocolate.png", True)
    all_sprites.add(chocolate)
    items.add(chocolate)
for i in range(5):
    cactus = Havchik("cactus.png", False)
    all_sprites.add(chocolate)
    items.add(cactus)


#peremennie
score = 0
hp = 100
text_score = Text_obj(10, 10, str(score), screen)
text_hp = Text_obj(10, 50, str(hp), screen)

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
    all_sprites.update()

    text_score.update(score)
    text_hp.update(hp)


    #collisions
    hits = pygame.sprite.spritecollide(player, items, True)
    for hit in hits:
        if hit.get_edible() == True:
            score += 10
            chocolate = Havchik("chocolate.png", True)
            all_sprites.add(chocolate)
            items.add(chocolate)

        elif hit.get_edible() == False:
            hp -= 20
            cactus = Havchik("cactus.png", False)
            all_sprites.add(chocolate)
            items.add(cactus)



          
    # обновление экрана
    screen.fill(BLACK)
    all_sprites.draw(screen)

    text_score.draw()
    text_hp.draw()
    
    pygame.display.update()








































