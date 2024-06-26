import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(PLAYER_FILE_NAME).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = SC_WIDTH//2
        self.rect.bottom = SC_HEIGHT - 20
        self.hp = PLAYER_MAX_HP
        self.laser_sprites = []
        self.fire_timer = pygame.time.get_ticks()
        self.right_key =  pygame.K_RIGHT
        self.left_key = pygame.K_LEFT
        self.speed = 5

        
    def update(self):
        keys = pygame.key.get_pressed()
        now = pygame.time.get_ticks()

        if keys[self.right_key]:
           self.rect.x += self.speed
        elif keys[self.left_key]:
            self.rect.x -= self.speed

        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.right >= SC_WIDTH:
            self.rect.right = SC_WIDTH

        #нажали пробел
        if keys[pygame.K_SPACE] and now - self.fire_timer > FIRE_DELAY:
            self.fire_timer = now
    
            #создали новый лазер
            laser = Laser(self.rect.centerx, self.rect.top)
            #добавили в список лазеров
            self.laser_sprites.append(laser)
        #update всех лазеров
        for laser in self.laser_sprites:
            laser.update()
            if laser.rect.bottom < 0:
                self.laser_sprites.remove(laser)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        for laser in self.laser_sprites:
            screen.blit(laser.image, laser.rect)

    def get_hp(self):
        return self.hp

    def reduce_hp(self, damage):
        self.hp -= damage

    def get_centerx(self):
        return self.rect.centerx

    def get_top(self):
        return self.rect.top

class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(LASER_FILE_NAME).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = LASER_SPEEDY
        

    def update(self):
        self.rect.y -= self.speedy

    def draw(self, screen):
        screen.blit(self.image, self.rect)










