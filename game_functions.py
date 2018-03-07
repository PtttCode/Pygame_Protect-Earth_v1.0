import sys
import pygame
import random
import json
from time import sleep

from bullet import Bullet
from alien import Alien
from stone import Stone

#创建碰撞检测组
collisions=pygame.sprite.Group()
ship_collisions=pygame.sprite.Group()

#爆炸所需变量
ticks=0
cycle=30
#爆炸图片列表的变量
num=0

#存储爆炸图片到列表 enemy1_down_surface
enemy1_down_surface = []
image=pygame.image.load('images/explosion/exps_01.png')
enemy1_down_surface.append(image)
image=pygame.image.load('images/explosion/exps_02.png')
enemy1_down_surface.append(image)
image=pygame.image.load('images/explosion/exps_03.png')
enemy1_down_surface.append(image)
image=pygame.image.load('images/explosion/exps_04.png')
enemy1_down_surface.append(image)
image=pygame.image.load('images/explosion/exps_05.png')
enemy1_down_surface.append(image)
image=pygame.image.load('images/explosion/exps_06.png')
enemy1_down_surface.append(image)
image=pygame.image.load('images/explosion/exps_07.png')
enemy1_down_surface.append(image)
image=pygame.image.load('images/explosion/exps_08.png')
enemy1_down_surface.append(image)
image=pygame.image.load('images/explosion/exps_09.png')
enemy1_down_surface.append(image)
image=pygame.image.load('images/explosion/exps_10.png')
enemy1_down_surface.append(image)
image=pygame.image.load('images/explosion/exps_11.png')
enemy1_down_surface.append(image)
image=pygame.image.load('images/explosion/exps_12.png')
enemy1_down_surface.append(image)
image=pygame.image.load('images/explosion/exps_13.png')
enemy1_down_surface.append(image)
image=pygame.image.load('images/explosion/exps_14.png')
enemy1_down_surface.append(image)
image=pygame.image.load('images/explosion/exps_15.png')
enemy1_down_surface.append(image)
image=pygame.image.load('images/explosion/exps_16.png')
enemy1_down_surface.append(image)




def check_events(ai_settings,screen,ship,aliens,bullets,button,stats,score):
    #响应按键和鼠标事件
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type==pygame.KEYDOWN:
            check_keydown(event,ai_settings,screen,ship,bullets,stats)
        elif event.type==pygame.KEYUP:
            check_keyup(event,ship)
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,button,ship,aliens,bullets,mouse_x,mouse_y,score)



def check_play_button(ai_settings,screen,stats,button,ship,aliens,bullets,mouse_x,mouse_y,score):
    #开始游戏
    button_clicked=button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_status:
        #隐藏光标
        pygame.mouse.set_visible(False)
        #显示飞船生命
        score.prep_ships()
        #重置游戏信息
        stats.reset_stats()
        stats.game_status=True

        #清空外星人列表
        aliens.empty()
        bullets.empty()

        ai_settings.space_appear.play()

        '''#创建一群新的外星人和飞船
        create_fleet(ai_settings,screen,aliens)
        ship.center_ship()'''

#按下状态                
def check_keydown(event,ai_settings,screen,ship,bullets,stats):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=True
    elif event.key==pygame.K_LEFT:
        ship.moving_left=True
    elif event.key==pygame.K_UP:
        ship.moving_up=True
    elif event.key==pygame.K_DOWN:
        ship.moving_down=True
    elif event.key==pygame.K_x:
        fire(ai_settings,screen,ship,bullets,stats)
    elif event.key==pygame.K_q:
        pygame.quit()
        sys.exit()


 #松开状态
def check_keyup(event,ship):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=False
    elif event.key==pygame.K_LEFT:
        ship.moving_left=False
    elif event.key==pygame.K_UP:
        ship.moving_up=False
    elif event.key==pygame.K_DOWN:
        ship.moving_down=False

#开火
def fire(ai_settings,screen,ship,bullets,stats):
    #创建一颗子弹，并加入到编组[Group（bullets）]中
    if len(bullets)<ai_settings.bullet_allowed and stats.game_status:
        #子弹音效
        ai_settings.bullet_voice.play()
        new_bullet=Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)



#爆炸效果
def explosion_play(screen,collision):
    #全局num，不然会出现bug
    global num

    #调用碰撞精灵单位的坐标
    for exp in collision:
        #调用第num张爆炸图片
        screen.blit(enemy1_down_surface[num],exp.rect)
        #让图片切换速度减慢
        if ticks%(cycle//2)==0:
            if num<15:
                num+=1
            else:
                #清空碰撞组 num复位
                collisions.remove(exp)
                num=0
                print("boom!")


def alien_explosion(ai_settings,aliens,bullets,screen,stats,score):
    #全局num，不然会出现bug
    global num 

    #检测子弹与外星人碰撞
    col=pygame.sprite.groupcollide(aliens,bullets,True,True)
    #击毁加分
    if col:
        stats.score+=ai_settings.score_get
        score.prep_score()
        #爆炸音效
        ai_settings.explosion_voice.play()

        
    #检查是否超过记录    
    check_highest_score(stats,score)

    #添加到collisions精灵里    
    collisions.add(col)

    #调用碰撞效果
    explosion_play(screen,collisions)


def ship_hit(ai_settings,screen,aliens,ship,stats,bullets,score):
    #飞船数-1
    if stats.ships_left>1:
        stats.ships_left-=1
        #ai_settings.bullet_voice_on=False
        score.prep_ships()
    else:
        ai_settings.dead_voice.play()
        stats.game_status=False
        pygame.mouse.set_visible(True)
        #重置飞船生命值
        stats.ships_left=ai_settings.ship_limit

        #更新最高记录到json文件
        if stats.score>=stats.highest_score:
            filename='record.json'
            with open(filename,'w') as f_obj:
                json.dump(stats.score,f_obj)
                print("New Record!!")
        print("Game Over")

    # 清空外星人列表
    aliens.empty()
    bullets.empty()
    sleep(1)
    
    if stats.game_status:
        #新建外星人
        #ai_settings.bullet_voice_on=True
        create_fleet(ai_settings,screen,aliens)
         #重新开始音效
        ai_settings.space_appear.play()
    ship.center_ship()
 

    
def release_bullet(ai_settings,bullets,screen,aliens,stats,score):
    #移动子弹
    bullets.update()
    
    #释放子弹内存
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
            
    #若外星人死完了，创建新的外星人
    if len(aliens)==0:
        bullets.empty()
        ai_settings.increase_speed()
        #升级
        stats.level+=1
        score.prep_level()
        print("升级！")
        create_fleet(ai_settings,screen,aliens)


def update_alien(ai_settings,screen,aliens,ship,stats,bullets,score,stone,sscol):
    #移动外星人
    aliens.update()
    
    #检测外星人是否移出界面并释放
    for alien in aliens.copy():
        if alien.rect.top>=ai_settings.screen_height:
            print("Miss!")
            ship_hit(ai_settings,screen,aliens,ship,stats,bullets,score)

    #检测飞机和外星人是否相撞
    if pygame.sprite.spritecollideany(ship,aliens):
        print("Ship Hit!!!")
        ship_hit(ai_settings,screen,aliens,ship,stats,bullets,score)

    if pygame.sprite.spritecollideany(stone,sscol):
        print("Hit Stone!!!")
        explosion_play(screen,sscol)
        ship_hit(ai_settings,screen,aliens,ship,stats,bullets,score)
    

def create_fleet(ai_settings,screen,aliens):
    #创建外星人群
    for alien_number in range(random.randint(1,10)):
        alien=Alien(ai_settings,screen)
        aliens.add(alien)
        

def check_highest_score(stats,score):
    #确认是否破纪录
    if stats.score>stats.highest_score:
        stats.highest_score=stats.score
        score.prep_highest_score()


def update_screen(ai_settings,screen,ship,bullets,aliens,stats,button,score,stone):
    #刷新屏幕
    #每次循环都重绘屏幕
    screen.fill(ai_settings.bg_color)

    #Play按钮
    if not stats.game_status:
        button.draw_button()
        stats.level=0
        stats.score=0
        score.prep_score()
        score.prep_level()
    else:
        score.show_score()

    #画石头
    stone.show_stones()
    #重绘子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
            
    ship.blitme()
    aliens.draw(screen)
    alien_explosion(ai_settings,aliens,bullets,screen,stats,score)

    #让最近绘制的屏幕可见(应该是刷新)
    pygame.display.flip()
