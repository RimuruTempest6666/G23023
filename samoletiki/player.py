import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(PLAYER_FILE_NAME).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = SC_WIDTH//2
        self.rect.bottom = SC_HEIGHT - 20
        self.right_key =  pygame.K_RIGHT
        self.left_key = pygame.K_LEFT
        self.speed = 5
        self.hp = PLAYER_MAX_HP
        self.laser_sprites = []

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

        #nazal probel
        if keys[pygame.K_SPACE]:
            #sozdal novi laser
            laser = Laser(self.rect.centerx, self.rect.top)
            #dobavil v spisok
            self.laser_sprites.append(laser)
        #update vseh laserov
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

    def get_top(self):
        return self.rect.top

    def get_centerx(self):
        return self.rect.centerx



class Laser:
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(LASER_FILE_NAME).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = LASER_SPD

    def update(self):
        self.rect.y -= self.speedy
            

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    
