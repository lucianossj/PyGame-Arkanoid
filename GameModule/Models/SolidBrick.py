
import pygame

from Brick import Brick

class SolidBrick(Brick):
  def __init__( self, gridx, gridy ):
    super(SolidBrick, self).__init__( gridx, gridy )
    self.image = pygame.image.load( "Resources/br/3.png" ).convert_alpha()
    oldPos = self.rect.topleft
    self.rect = self.image.get_rect()
    self.rect.topleft = oldPos
    self.durability = 2

  def getType(self):
    return "solid"
