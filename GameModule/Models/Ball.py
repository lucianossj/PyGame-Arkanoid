# Encoding: utf-8

import pygame

class Ball(pygame.sprite.Sprite):
  def __init__(self):
    super(Ball,self).__init__()
    # Definiujemy to jako listy z racji tego, że krotki są unmutable - wolę modyfikować aktualne obiekty niż tworzyć cały czas nowe...
    self.position = [320,450]
    self.velocity = [0,0]
    self.w = 10
    self.h = 10


    self.image = pygame.image.load( "Resources/ball/ball.png" ).convert_alpha()
    self.rect = self.image.get_rect() 
    self.rect.topleft = self.position

  def reset(self):  
    self.position = [320,450]
    self.velocity = [0,0]

  def pos(self):
    return (self.position[0], self.position[1])

  def speed(self):
    return self.velocity

  def speedChange(self, vx, vy):
    self.velocity[0] = vx
    self.velocity[1] = vy

  def collideWithWall(self):
    return self.position[0] <= 0 or self.position[0] >= 629 or self.position[1] <= 0 or self.position[1] >= 469

  def collision(self, obj):
    return pygame.sprite.collide_rect(self,obj)

  def move( self, x, y ):
    self.position[0] = min( (self.position[0]+x, 629) )
    self.position[0] = max( (self.position[0], 0) )
    self.position[1] = min( (self.position[1]+y, 469) )
    self.position[1] = max( (self.position[1], 0) )
    self.rect.topleft = self.pos()

  def xInvert(self):
    self.velocity[0] = -self.velocity[0]

  def yInvert(self):
    self.velocity[1] = -self.velocity[1]
