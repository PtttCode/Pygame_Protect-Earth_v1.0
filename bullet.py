import pygame,sys
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self,ai_settings,screen,ship):
        #在飞船所处的位置创建一个子弹对象
        super(Bullet,self).__init__()
        self.screen=screen

        self.rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top

        #转化为单精度
        self.y=float(self.rect.y)

        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor
        #声音开关

    def update(self):
        #向上移动子弹
        self.y-=self.speed_factor
        self.rect.y=self.y


    def draw_bullet(self):
        #刷新子弹
        pygame.draw.rect(self.screen,self.color,self.rect)


    '''def bullet_voice(self):
        #子弹声效
        self.soundwav=pygame.mixer.Sound("voice/bullet_voice.ogg") 
        self.soundwav.play()'''

