#!/usr/bin/python2.7

from Models import *
from Constants import *

import json

class Mapper:
  brickTypes = [ "solid", "ghost", "simple" ]

  def __init__( self, objects ):
    self.objects = objects

  def load( self, level ):
    file_ = json.load( open( "Resources/levels/" + levels[level] ) )
    self.objects.setBackground( "Resources/bg/" + file_["bg"] )

    for row in xrange( len( file_["data"] ) ):
      for column in xrange( len( file_["data"][0] ) ):
        if file_["data"][row][column] != None:
          self.objects.setGrid( row, column, self.getBrick(file_["data"][row][column], row, column ) )

  def getBrick( self, name, gridx, gridy ):
    if name not in Mapper.brickTypes:
      return None
    else:
      if name == "solid":
        return SolidBrick( gridx, gridy )
      elif name == "ghost":
        return GhostBrick( gridx, gridy )
      elif name == "simple":
        return SimpleBrick( gridx, gridy )
