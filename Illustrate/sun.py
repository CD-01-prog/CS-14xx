import shape

class Sun(Shape):

  def __init__(self, x, y, color size):
    self.color = color
    self.size = size
    super().__init__(x,y,color)
    Sun.drawSun()
    return

  def drawSun(self):
    pygame.draw.ellipse(screen, RED, [600, 00, 200, 100], 0)
    return
