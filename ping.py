from pygame import*
from random import randint

win_width = 700
win_height = 500
window = display.set_mode((win_width,win_height))
display.set_caption("pinGponG")

clock = time.Clock()

FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))
class Player(GameSprite):
    def mov1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 20:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height-50:
            self.rect.y += self.speed
    
    def mov2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 20:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height-50:
            self.rect.y += self.speed

player1 = Player("racket.png",40,170,100,130,4)
player2 = Player("racket.png",win_width-120,170,100,130,4)
class Ballt(GameSprite):
    pass

ball = Ballt("ball.png",win_width/2,win_height/2,50,50,5)

game = True
finish = False
while game:
    window.fill((255,255,155))
    player1.reset()
    player2.reset()
    player1.mov1()
    player2.mov2()
    ball.reset()
    for e in event.get():
        if e.type == QUIT:
            game = False


    display.update()
    clock.tick(FPS)