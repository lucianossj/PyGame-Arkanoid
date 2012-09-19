
import pygame

from GameModule.Constants import *


class Brick( pygame.sprite.Sprite ):
  def __init__(self, gridx, gridy ):
    super(Brick,self).__init__()
    self.x = gridx
    self.y = gridy
    self.realx = self.x * gfx["grid"][0]
    self.realy = self.y * gfx["grid"][1]

    self.image = None
    self.durability = 1

    self.rect = pygame.Rect(0,0,0,0)
    self.rect.topleft = ( self.realx, self.realy )

  def collision( self, obj ):
    return pygame.sprite.collide_rect( self, obj )

  def getType(self):
    return "brick"


