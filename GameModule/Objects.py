#!/usr/bin/python2.7
# Encoding: utf-8

import pygame

from Constants import *
from Models import *

class Objects:
  def __init__( self ):
    self.gridObjects = [ [ None for i in xrange( gfx["screen"][1]/gfx["grid"][1] ) ] for j in xrange( gfx["screen"][0]/gfx["grid"][0] ) ]
    self.__powerups = []
    self.__balls = [ Ball() ]
    self.__pad = Pad()
    self.__bg = None

  # Nos fornece apenas os elementos de grade existentes.
  def grid(self):
    ret = []
    for i in xrange(len(self.gridObjects)):
      ret += filter( lambda x: x != None, self.gridObjects[i] )
    return ret

  def pad(self):
    return self.__pad

  def balls(self):
    return self.__balls

  def background(self):
    return self.__bg

  def addBall( self, ball ):
    self.__balls.append( ball )

  def removeBall( self, ball ):
    self.__balls.pop( self.__balls.index(ball) )

  def setGrid( self, x, y, obj ):
    #    print self.gridObjects[x][y]
    self.gridObjects[x][y] = obj
    #    print self.gridObjects[x][y]

  def setBackground( self, fileName ):
    self.__bg = pygame.image.load( fileName ).convert_alpha()  
   
  def spawnPowerup( self, startx, starty ):
    self.__powerups.append( Powerup(startx,starty) ) 

  def updatePowerups(self):
    for power in self.__powerups:
      power.update()

  def powerups(self):
    return self.__powerups

  def deletePowerup(self, powerup):
    tmp = self.__powerups[-1]
    obj_i = self.__powerups.index( powerup )
    if tmp == self.__powerups[obj_i]:
      self.__powerups.pop()
      return
    else:
      self.__powerups[obj_i] = tmp
      self.__powerups.pop()
