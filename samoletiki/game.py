import pygame
import sys
from settings import *
from player import Player
from meteor import Meteor
from meteor_manager import MeteorManager
from text_obj import Text_obj
from player import Laser

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SC_WIDTH, SC_HEIGHT))
        self.clock = pygame.time.Clock()
        self.run = True
        self.player = Player()
        self.meteor_manager = MeteorManager()
        self.hp = PLAYER_MAX_HP
        self.text_hp = Text_obj(SC_WIDTH - 100, 10, str(self.hp))
        self.laser = Laser(self.player.get_centerx(), self.player.get_top())
        

        
    def play(self):
        while self.run:
            self.check_events()
            self.update()
            self.check_collisions()
            self.draw()
            self.clock.tick(FPS)

    def check_events(self):
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        self.player.update()
        self.meteor_manager.update()
        self.text_hp.update(self.player.get_hp())
        self.laser.update()

    def check_collisions(self):
        for mateor in self.meteor_manager.meteors:
            if self.player.rect.colliderect(self.meteor.rect):
               self.player.reduce_hp(meteor.get_damage())
               meteor.random_position()


    def draw(self):
        self.screen.fill(BLACK)
        self.player.draw(self.screen)
        self.meteor_manager.draw(self.screen)
        self.text_hp.draw(self.screen)
        self.laser.draw(self.screen)
        pygame.display.update()

