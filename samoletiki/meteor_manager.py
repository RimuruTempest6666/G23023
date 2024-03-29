import pygame
from settings import *
from meteor import Meteor
from random import randint

class MeteorManager:
    def __init__(self):
        filename_list = ["Meteors//meteorBrown_big1.png", "Meteors//meteorBrown_big2.png",
                         "Meteors//meteorBrown_big3.png", "Meteors//meteorBrown_big4.png",
                         "Meteors//meteorBrown_med1.png", "Meteors//meteorBrown_med3.png",
                         "Meteors//meteorBrown_small1.png", "Meteors//meteorBrown_small2.png",
                         "Meteors//meteorBrown_tiny1.png", "Meteors//meteorBrown_tiny2.png"]
        self.meteors = []
        for filename in filename_list:
            x = randint(0, SC_WIDTH)
            y = randint(-SC_HEIGHT, 0)
            meteor = Meteor(x, y, filename)
            self.meteors.append(meteor)


        def update(self):
            for meteor in self.meteors:
                meteor.update()
                if meteor.rect.right <= 0 or meteor.rect.left >= SC_WIDTH \
                or meteor.rect.top >= SC_HEIGHT:
                    meteor.rect.x = randint(0, SC_WIDTH)
                    meteor.rect.y = randint(-SC_HEIGHT, 0)

                    meteor.speedx = randint(-2,2)
                    meteor.speedy = randint(2,6)





















            
        
