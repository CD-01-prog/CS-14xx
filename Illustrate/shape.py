import math

class Shape:

  def __init__(self, x, y, color)
    self.x = x
    self.y = y
    self.color = color
    return

  def getX(self):
    return self.x
  
  def getY(self):
    return self.y

  def getColor(self):
    return self.color

  def deltaX(self, change):
    self.x = self.x + change
    return

  def deltaY(self, change):
    self.y = self.y + change
    return

  def changeColor(self, change):
    self.color = self.color + change
    return
