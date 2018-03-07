import pygame,sys

class Settings():
    #初始化游戏设置

    
    def __init__(self):
        #屏幕设置
        
        self.screen_width=1200
        self.screen_height=700
        self.bg_color=(230,230,230)

        #飞船设置
        self.ship_limit=3

        #子弹设置
        self.bullet_width=4
        self.bullet_height=7
        self.bullet_color=(60,60,60)
        self.bullet_allowed=5

        #音效设置
        self.bullet_voice=pygame.mixer.Sound("voice/bullet_voice1.wav")
        self.explosion_voice=pygame.mixer.Sound("voice/boom2.wav")
        self.dead_voice=pygame.mixer.Sound("voice/gameover.ogg")
        self.space_appear=pygame.mixer.Sound("voice/appear.wav")


        #等级设置
        self.speedup_scale=1.1
        self.alien_speedup=1.06
        self.initialize_dynamic_setting()


    def initialize_dynamic_setting(self):
        #初始化随游戏进行而变化的设置
        self.ship_speed_factor=3.5
        self.bullet_speed_factor=8
        self.alien_speed_factor=1
        self.score_get=1
        

    def increase_speed(self):
        #提高速度
        self.ship_speed_factor*=self.speedup_scale
        self.bullet_speed_factor*=self.speedup_scale
        self.alien_speed_factor*=self.alien_speedup
        self.score_get*=2
        
