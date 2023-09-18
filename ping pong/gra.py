#Create your own shooter
from random import *
from pygame import *


class GameSprite(sprite.Sprite):
    #konstruktor
    def __init__(self, player_image, player_x, player_y, player_widht, player_height, player_speed):
        super().__init__()
 
        #wgrana grafika
        self.image = transform.scale(image.load(player_image), (40, 110))
        self.speed = player_speed
 
        #hitboxy postaci
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#klasa gracza
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 10:
            self.rect.x -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 100:
            self.rect.x += self.speed
        


score = 0

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost +1
#class ball(GameSprite):
    
    #if self.rect.y is = gracz.rect.y:
    #    self.y = y +100
    #if self.rect.y is = potwor.rect.y:
    #    self.y = y -100
    #if self.rect.x is = gracz.rect.x:
    #    self.x = x +100
    #if self.rect.x is = potwor.rect.x:
    #    self.x = x -100
font.init()
font1 = font.Font(None, 36)

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("pingpong")
background = transform.scale(image.load("background.png"), (win_width, win_height))
mixer.init()
fire = mixer.Sound('metal-pipe-clang.mp3')

gracz = Player("paletka1.png", 20, 200, 10, 100, 2 )
potwory = sprite.Group()
for i in range(5):
    potwor = Enemy('paletka2.png', randint(80, win_width - 80), 0, 80, 50, randint(1, 6))
    potwory.add(potwor)
game = True
finish = False
clock = time.Clock()
FPS = 60


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if gracz.rect.y == potwor.rect.y:
        
    if finish == False:
        window.blit(background,(0,0))
        gracz.update()
        potwory.update()
        gracz.reset()
        potwory.draw(window)
        text = font1.render("Score:" + str(score), 1, (255,255,255))
        window.blit(text, (10, 20))

        text_lose = font1.render("Lost:" + str(score), 1, (255,255,255))
        window.blit(text_lose, (10, 60))
    display.update()
    clock.tick(FPS)