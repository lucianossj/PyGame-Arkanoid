import pygame
from GameModule.Constants import *

class Pad(pygame.sprite.Sprite):
  def __init__(self):
    super(Pad,self).__init__()

    self.gridWidth = 3

    self.position = [280,460]

    self.graphics = {
      "left": pygame.image.load( "Resources/pad/pad-left.png" ).convert_alpha(),
      "mid": pygame.image.load( "Resources/pad/pad-mid.png" ).convert_alpha(),
      "right": pygame.image.load( "Resources/pad/pad-right.png" ).convert_alpha()
    }

    self.rect = pygame.Rect( self.position[0], self.position[1], self.gridWidth * gfx["grid"][0], gfx["grid"][1] )
    self.rect.topleft = self.pos()

    self.lastMove = -1

  def reset(self):
    self.gridWidth = 3

    self.position = [280,460]
    self.lastMove = -1

  def move( self, x ):
    self.lastMove = x

    oldPosition = self.position[0]
    self.position[0] = max( [ min( [self.position[0] + x, 640 - (self.gridWidth * gfx["grid"][0])] ), 0 ] )
    self.rect.topleft = self.pos()
    return self.position[0] != oldPosition

  def setWidth( self, w ):
    self.gridWidth = w
    self.rect = pygame.Rect( self.position[0], self.position[1], self.gridWidth * gfx["grid"][0], gfx["grid"][1] )

  def makeSurface( self ):
    surface = pygame.Surface( (self.gridWidth * gfx["grid"][0], gfx["grid"][1] ) )
    surface.fill( (87,27,12) )
    surface.set_colorkey( (87,27,12) )

    for i in xrange(self.gridWidth):
      if i == 0:
        surface.blit( self.graphics["left"], (i*gfx["grid"][0],0) )
      elif i == self.gridWidth-1:
        surface.blit( self.graphics["right"], (i*gfx["grid"][0],0 ) )
      else:
        surface.blit( self.graphics["mid"], (i*gfx["grid"][0],0) )

    return surface

  def pos(self):
    return (self.position[0],self.position[1])
