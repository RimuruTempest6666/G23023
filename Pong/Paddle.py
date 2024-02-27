import pygame
from settings import *

class Paddle:

    def __init__(self, x, y, color, screen, up_key, down_key):
       self.x = x
       self.y = y
       self.color = color
       self.width = P_WIDTH
       self.width1 = P_HEIGHT
       self.height = P_HEIGHT
       self.height1 = P_WIDTH
       self.speedy = P_SPEEDY
       self.speedx = P_SPEEDY
       self.screen = screen
       self.up_key = up_key
       self.down_key = down_key

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[self.up_key]:
           self.y -= self.speedy
        elif keys[self.down_key]:
            self.y += self.speedy

        if self.y <= 0:
            self.y = 0
        if self.y >= SC_HEIGHT - P_HEIGHT:
            self.y = SC_HEIGHT - P_HEIGHT


    def update1(self):
        keys = pygame.key.get_pressed()
        if keys[self.up_key]:
           self.x -= self.speedx
        elif keys[self.down_key]:
            self.x += self.speedx

        if self.x <= 0:
            self.x = 0
        if self.x >= SC_WIDTH - P_HEIGHT:
            self.x = SC_WIDTH - P_HEIGHT


            

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

    def draw1(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width1, self.height1))



    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
    
            
