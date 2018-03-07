import pygame
import random
from pygame.sprite import Sprite

class Stone():

    def __init__(self,screen):
        self.screen=screen

        #载入图片
        self.image=pygame.image.load('images/stone1.png')
        '''self.image2=pygame.image.load('images/stone2.png')
        self.image3=pygame.image.load('images/stone3.png')
        self.image4=pygame.image.load('images/stone4.png')'''

        self.rect=self.image.get_rect()
        '''self.rect2=self.image2.get_rect()
        self.rect3=self.image3.get_rect()
        self.rect4=self.image4.get_rect()'''

        #随机置放石头
        self.rect.x=random.randint(120, 1100)
        self.rect.y=random.randint(-50, 500)

        '''self.rect2.x=random.randint(700, 1100)
        self.rect2.y=random.randint(-50, 260)
        
        self.rect3.x=random.randint(0, 650)
        self.rect3.y=random.randint(300, 560)

        self.rect4.x=random.randint(800, 1100)
        self.rect4.y=random.randint(250, 450)'''

        
    def show_stones(self):
        #绘制石头
        self.screen.blit(self.image,self.rect)
        '''self.screen.blit(self.image2,self.rect2)
        self.screen.blit(self.image3,self.rect3)
        self.screen.blit(self.image4,self.rect4)'''
