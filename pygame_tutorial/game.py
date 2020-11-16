import sys
import pygame
import random

from pygame.locals import *



class Background(pygame.sprite.Sprite):
    def __init__(self, location):
        super().__init__()
        self.raw_image = pygame.image.load("ground.png")
        self.image = pygame.transform.scale(self.raw_image, (800, 600))
        self.rect = self.image.get_rect()
        self.rect.topleft = location

class Mouse(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.raw_image = pygame.image.load("mouse.png")
        self.image = pygame.transform.scale(self.raw_image, (200, 200))
        self.rect = self.image.get_rect()
        self.rect.topleft = position
def random_position(hole):

    # x=random.randint(0,700)
    # y=random.randint(100,500)
    # return x,y
    pos = random.choice(hole)
    return pos

# 遊戲主程式
hole=[[100,100],[300,100],[500,100],[100,300],[300,300],[500,300]]

pygame.init()


pygame.display.set_caption('Hit Mouse')
canvas = pygame.display.set_mode((800, 600))

position=random_position(hole)
mouse = Mouse(position)
reload_mouse_event=USEREVENT
pygame.time.set_timer(reload_mouse_event, 3000)
points = 0
score_font = pygame.font.SysFont(None, 48)
time_font = pygame.font.SysFont(None, 32)
gameover_font =pygame.font.SysFont(None, 64)
main_clock = pygame.time.Clock()

timer_event=USEREVENT+1
pygame.time.set_timer(timer_event, 1000)
timer=15
start=True


hit_sound=pygame.mixer.Sound("hit.ogg")
hit_sound.set_volume(0.5)
while start:
    # 迭代整個事件迴圈，若有符合事件則對應處理
    for event in pygame.event.get():
        # 當使用者結束視窗，程式也結束
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == reload_mouse_event:
            mouse.kill()
            position = random_position(hole)
            mouse = Mouse(position)
        elif event.type == MOUSEBUTTONDOWN:
            if position[0] < pygame.mouse.get_pos()[0] < position[0] + 200 and position[1] < pygame.mouse.get_pos()[1] < position[1] + 200:
                mouse.kill()
                position = random_position(hole)
                mouse = Mouse(position)
                points += 5
                hit_sound.play()
        elif event.type == timer_event:
            timer-=1

    canvas.fill((255, 255, 255))
    background = Background([0, 0])
    score=score_font.render("Points:{}".format(points), True, (0, 0, 0))
    time=time_font.render("Time:{}".format(timer),True,(0,0,0))
    canvas.blit(background.image, background.rect)
    canvas.blit(mouse.image,mouse.rect)
    canvas.blit(score,(10,0))
    canvas.blit(time,(10,50))
    pygame.display.update()
    main_clock.tick(60)
    if timer <= 0:
        start=False

while not start:
    canvas.fill((255, 255, 255))
    background = Background([0, 0])
    canvas.blit(background.image, background.rect)
    gameover=gameover_font.render("GameOver,Your Score is {}".format(points),True,(0,0,0))
    canvas.blit(gameover,(100,300))
    pygame.display.update()
    for event in pygame.event.get():
        # 當使用者結束視窗，程式也結束
        if event.type == QUIT:
            pygame.quit()
            sys.exit()