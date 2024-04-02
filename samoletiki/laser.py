import pygame
from player import Player
from settings import *
from random import randint

class Laser:
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(LASER_FILE_NAME).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = player.get_top()
        self.laser_spd = 10

    def update(self):
        self.y -= self.laser_spd
        if self.rect.bottom.y < 0:
            self.rect.center = player.get_top()
            

    def draw(self, screen):
        screen.blit(self.image, self.rect)




















