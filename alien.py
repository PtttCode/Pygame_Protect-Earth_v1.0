import pygame
import random

from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self,ai_settings,screen):
        #初始化外星人并设置其初始位置
        super(Alien,self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings

        #加载外星人图像，并设置rect
        self.image=pygame.image.load('images/alien.png')
        self.rect=self.image.get_rect()

        #初始位置
        self.rect.x=random.randint(100, 1100)
        self.rect.y=-random.randint(65, 700)
        print("Alien Position:",self.rect.x,self.rect.y)
        
        #存储外星人的准确位置
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)   

    def update(self):
        self.y+=self.ai_settings.alien_speed_factor
        self.rect.y=self.y

    def blitme(self):
        #指定位置绘制外星人
        self.screen.blit(self.image,self.rect)
