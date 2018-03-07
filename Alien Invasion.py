import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
from bullet import Bullet
from gamestats import GameStats
from button import Button
from score import Score
from stone import Stone
import game_functions as func

def run_game():
    #init游戏并创建一个窗口对象
    pygame.init()
    ai_settings=Settings()#创建Settings类的实例
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("地球保卫战 v1.0")

    #创建实例
    sscol=Group()
    stone=Stone(screen)
    stats=GameStats(ai_settings)
    bullets=Group()
    ship=Ship(ai_settings,screen)
    sscol.add(ship)
    aliens=Group()
    button=Button(ai_settings,screen,"Play")
    score=Score(ai_settings,screen,stats)

    
    while True:

        #帧数
        pygame.time.Clock().tick(120)
        #监视键盘和鼠标事件
        func.check_events(ai_settings,screen,ship,aliens,bullets,button,stats,score)

        #决定游戏是否开始
        if stats.game_status:
            ship.update()
            func.release_bullet(ai_settings,bullets,screen,aliens,stats,score)
            func.update_alien(ai_settings,screen,aliens,ship,stats,bullets,score,stone,sscol)
        
        
            #每次循环都重绘屏幕
        func.update_screen(ai_settings,screen,ship,bullets,aliens,stats,button,score,stone)
       

run_game()
