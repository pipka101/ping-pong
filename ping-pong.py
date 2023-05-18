
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
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
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
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= speed
        if keys_pressed[K_RIGHT] and self.rect.x < 595:
            self.rect.x += speed
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
           
x1 = 100
y1 = 350
x2 = 200
y2 = 350
speed = 10
game = True 





player1 = Player('platform.png', player_x, player_y, player_speed, 65, 65 )
player2 = Player('platform.png', 80, player1_y, randint(2, 3), 50, 50)
ball = GameSprite('мячик1.png', randint(80, 600), player3_y, randint(1, 2), 50, 50)
    
win1 = 0

while game:
   
        
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_w:
                player.fire()

    if finich != True:
        window.blit(background, (0,0))
        keys_pressed = key.get_pressed()
        player1.reset()
        player2.reset()
        
        ball.reset()
        ball.update()
        player1.update()
        player2.update()
       
        text_losts = font2.render('Пропущено: ' + str(lost), 1, (255, 255, 255))
        window.blit(text_losts, (10, 20))   
        win2 = font2.render('Счет: ' + str(win1), 1, (255, 255, 255))
        window.blit(win2, (10, 50))


    for e in event.get():
        if e.type == QUIT:
            game = False
    keys_pressed = key.get_pressed()

    if keys_pressed[K_LEFT] and x1 > 5:
        x1 -= speed
    if keys_pressed[K_RIGHT] and x1 < 595:
        x1 += speed
    if keys_pressed[K_UP] and y1 > 5:
        y1 -= speed
    if keys_pressed[K_DOWN] and y1 < 395:
        y1 += speed
    if keys_pressed[K_a] and x2 > 5:
        x2 -= speed
    if keys_pressed[K_d] and x2 < 595:
        x2 += speed
    if keys_pressed[K_w] and y2 > 5:
        y2 -= speed
    if keys_pressed[K_s] and y2 < 395:
        y2 += speed


    display.update()
    clock.tick(60)


