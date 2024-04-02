import pygame
from settings import *
from random import randint

class Meteor(pygame.sprite.Sprite):
    def __init__(self, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.damage = 0
        self.random_position()

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top >= SC_HEIGHT:
            self.rect.x = randint(0, SC_WIDTH - self.rect.width)
            self.speedx = randint(-2, 2)
            self.rect.bottom = 0

    def draw(self,screen):
        screen.blit(self.image, self.rect)

    def set_damage(self, damage):
        self.damage = damage
        
    def get_damage(self):
        return self.damage

    def random_position(self):
        self.rect.x = randint(0, SC_WIDTH - self.rect.width)
        self.rect.y = self.rect.height
        self.speedx = randint(-2,2)
        self.speedy = randint(2,6)

        
