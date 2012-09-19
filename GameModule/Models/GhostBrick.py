
import pygame 

from Brick import Brick

class GhostBrick(Brick):
  def __init__(self, gridx, gridy ):
    super(GhostBrick, self).__init__( gridx, gridy )

    self.image = pygame.image.load( "Resources/br/2.png" ).convert_alpha()
    oldPos = self.rect.topleft
    self.rect = self.image.get_rect()
    self.rect.topleft = oldPos

  def getType(self):
    return "ghost"
