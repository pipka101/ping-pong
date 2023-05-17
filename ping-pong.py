
from pygame import *
import time 
import pygame
from random import randint 
pygame.init()
clock = pygame.time.Clock()
window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')
background = transform.scale(image.load('.jpg'), (700, 500))


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
mixer.init()
mixer.music.load('space.ogg')
money = mixer.Sound('fire.ogg')
mixer.music.play()
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
win = font1.render('YOU WIN!!!!', True, (255, 215, 0))
loss = font1.render('YOU LOSER!', False, (255, 215, 0))
class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color1, color2, color3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


asteroids = sprite.Group()
monsters = sprite.Group()
bullets = sprite.Group()


class Player(GameSprite):
    def update(self):
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= speed
        if keys_pressed[K_RIGHT] and self.rect.x < 595:
