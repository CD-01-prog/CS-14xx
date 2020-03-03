import shape

class Cloud(Shape):

  def __init__(self, x, y, color, size, type):
    self.color = color
    self.size = size
    self.type = type
    super().__init__(x,y,color)
    Cloud.drawFluffy()
    return 

  def drawFluffy(self):
    pygame.draw.circle(screen, BLUE, [160, 250], 15)
    pygame.draw.circle(screen, BLUE, [140, 240], 15)
    pygame.draw.circle(screen, BLUE, [140, 260], 15)
    pygame.draw.circle(screen, BLUE, [180, 250], 15)
    pygame.draw.circle(screen, BLUE, [170, 260], 15)
    return
