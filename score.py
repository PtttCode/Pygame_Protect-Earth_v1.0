import pygame.font
from pygame.sprite import Group

from ship import Ship

class Score():
    #显示得分类

    def __init__(self,ai_settings,screen,stats):
        #初始化
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.ai_settings=ai_settings
        self.stats=stats

        #显示得分信息时用的字体设置
        self.text_color=(210,210,210)
        self.text_color2=(10,10,10)
        self.font=pygame.font.SysFont(None,120)
        self.font2=pygame.font.SysFont(None,50)

        #准备初始分图像
        self.prep_score()
        self.prep_highest_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        #渲染为图像
        score_get=self.stats.score
        score_str="{:,}".format(score_get)
        self.score_image=self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)

        self.score_rect=self.score_image.get_rect()
        self.score_rect.centerx=self.screen_rect.centerx
        self.score_rect.centery=self.screen_rect.centery


    def prep_highest_score(self):
        #最高分图像
        highest_score_get=self.stats.highest_score
        highest_score_str="{:,}".format(highest_score_get)
        self.highest_score_image=self.font2.render(highest_score_str,True,self.text_color2,self.ai_settings.bg_color)

        self.highest_score_rect=self.highest_score_image.get_rect()
        self.highest_score_rect.centerx=self.screen_rect.centerx
        self.highest_score_rect.top=self.screen_rect.top


    def prep_level(self):
        #等级显示
        level_get=self.stats.level
        level_str="{:,}".format(level_get)
        self.level_image=self.font2.render(level_str,True,self.text_color2,self.ai_settings.bg_color)

        self.level_rect=self.level_image.get_rect()
        self.level_rect.right=self.screen_rect.right
        self.level_rect.top=self.screen_rect.top
        

    def prep_ships(self):
        #显示剩余的船
        self.ships=Group()
        for ship_num in range(self.stats.ships_left):
            ship=Ship(self.ai_settings,self.screen)
            ship.rect.x=ship_num*ship.rect.width+10*(ship_num+1)
            ship.rect.y=10
            self.ships.add(ship)


    def show_score(self):
        #显示得分
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.highest_score_image,self.highest_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.ships.draw(self.screen)

