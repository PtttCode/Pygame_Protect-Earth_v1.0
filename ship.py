import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self,ai_settings,screen):
        #初始化飞船并设置初始位置
        super(Ship,self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings

        #加载飞船图像并获取外接矩形
        self.image=pygame.image.load('images/ship.png')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #将每艘新飞船放在屏幕底部中央
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        print(self.rect.bottom,self.rect.center)
        self.center=float(self.rect.centerx)
        self.centery=float(self.rect.y)
        self.mark_y=self.rect.y

        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False


    def update(self):
        #根据移动标志调整飞船的位置
        #右移
        if self.moving_right and self.rect.right <self.screen_rect.right:
            self.center+=self.ai_settings.ship_speed_factor
        #左移
        if self.moving_left and self.rect.left>=0:
            self.center-=self.ai_settings.ship_speed_factor
        #上移
        if self.moving_up and self.rect.top>=0:
            self.centery-=self.ai_settings.ship_speed_factor
        #下移
        if self.moving_down and self.rect.bottom<=self.screen_rect.bottom:
            self.centery+=self.ai_settings.ship_speed_factor

        

        self.rect.centerx=self.center
        self.rect.y=self.centery

    def center_ship(self):
        self.center=self.screen_rect.centerx
        self.centery=self.mark_y

    def blitme(self):
        #在指定位置刷新飞船
        self.screen.blit(self.image,self.rect)
