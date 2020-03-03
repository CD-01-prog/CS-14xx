import shape

class House(Shape):

  def __init__(self, x, y, colorbody, colorroof, size):
    self.colorbody = colorbody
    self.colorroof = colorroof
    self.size = size
    super().__init__(x,y,color)
    House.drawHouse()
    return

  def drawHouse(self)
    pygame.draw.rect(screen, BLACK, [(size[0]/4+10), (size[0]/2 + 50), size[1]/2, size[1]/2 + 50])
    pygame.draw.polygon(screen, BLACK, [[size[0]/4, size[1]- 150], [size[0]/2 - 25, size[1]/2 - 100], [size[0]/1.5, size[1] - 150]], 5)
    return
