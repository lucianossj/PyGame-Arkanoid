import pygame

from GameModule.Constants import *

class Powerup(pygame.sprite.Sprite):
  def __init__(self, startgridx, startgridy):
    super(Powerup,self).__init__()

    font = pygame.font.SysFont( "sans-serif", 18 )
    pLetter = font.render( "P", True, (255,0,0) )
    box = pygame.Surface( (32,32) )
    box.fill( (0,0,0) )
    box.blit( pLetter, (16 - pLetter.get_size()[0]/2, 16 - pLetter.get_size()[1]/2) )

    self.x, self.y = startgridx * gfx["grid"][0] + 4, startgridy * gfx["grid"][1] - 20

    self.image = box
    self.rect = self.image.get_rect()
    self.rect.topleft = (self.x,self.y)

  def update(self):
    self.y += 5
    self.rect.topleft = (self.x,self.y)

  def collision(self, obj):
    return pygame.sprite.collide_rect( self, obj )
