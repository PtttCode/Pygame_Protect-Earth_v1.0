import pygame.font

class Button():

    def __init__(self,ai_settings,screen,msg):
        self.screen=screen
        self.screen_rect=screen.get_rect()

        #初始化按钮属性
        self.width=260
        self.height=120
        self.button_color=(190,190,190)
        self.text_color=(255,255,255)
        self.font=pygame.font.SysFont(None,130)

        #创建rect对象，并使其居中
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center

        #填充信息
        self.prep_msg(msg)


    def prep_msg(self,msg):
        #将msg渲染为图像，并使其居中
        self.msg_image=self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center


    def draw_button(self):
        #绘制按钮和填充文本
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
