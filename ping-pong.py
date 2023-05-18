
from pygame import *
import time 
import pygame
from random import randint 
pygame.init()
clock = pygame.time.Clock()
window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')
background = transform.scale(image.load('фон.jpg'), (960, 750))


x1 = 100
y1 = 350
x2 = 200
y2 = 350
speed = 10
game = True 
finich = False
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x= x
        self.rect.y = y
      
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


font.init()
font1 = font.SysFont('Arial', 36)
font2 = font.SysFont('Arial', 36) 

player_x = 100
player_y = 400
player_speed = 10
player1_x = 400
player1_y = 0
player1_speed = 3
player2_x = 550
player2_y = 400
player2_speed = 0
player3_y = 0
win = font1.render('WIN!!!!', True, (255, 215, 0))
loss = font1.render('LOSS!', False, (255, 215, 0))


player1 = sprite.Group()
player2 = sprite.Group()
ball = sprite.Group()


class Player(GameSprite):
    def update(self):
        if keys_pressed[K_UP] :
            self.rect.y -= speed
        if keys_pressed[K_DOWN] :
            self.rect.y += speed

    def update2(self):        
        if keys_pressed[K_w] :
            self.rect.y -= speed
        if keys_pressed[K_s] :
            self.rect.y += speed
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, -15, 15, 20)
        bullets.add(bullet)
lost = 0

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= 450:
           self.rect.y = 0
           self.rect.x = randint(0, 600)
           
x1 = 20
y1 = 200
x2 = 650
y2 = 200
x3 = 350
y3 = 200 
speed = 8
speed1 = 10
game = True 





player1 = Player('platform.png', x1, y1, speed, 30, 100 )
player2 = Player('platform.png', x2, y2, speed, 30, 100)
ball = GameSprite('мячик1.png', x3, y3, speed1, 120, 80)
    
win1 = 0

while game:
   
        
    for e in event.get():
        if e.type == QUIT:
            game = False
       
    if finich != True:
        window.blit(background, (0,0))
        keys_pressed = key.get_pressed()
        player1.update()
        player2.update2()
        player1.reset()
        player2.reset()
        
        ball.reset()
        ball.update()

       
      


    for e in event.get():
        if e.type == QUIT:
            game = False
    keys_pressed = key.get_pressed()
  


    display.update()
    clock.tick(60)
