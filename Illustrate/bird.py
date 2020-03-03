import shape

class Bird(Shape):

  def __init__(self, x, y, color, type):
    self.color = color
    self.type = type
    super().__init__(x,y,color)
    if self.type == 'arched':
      Bird.drawtypeArch()
    else:
      Bird.drawtypeStright()
    return

  def drawtypeArch(self)
    pygame.draw.arc(screen, BLACK,[210, 75, 150, 125], 0, pi/2, 2)
    pygame.draw.arc(screen, BLACK,[360,75,150,125], pi/2, pi, 2)
    return

  def drawtypeStright(self)
    pygame.draw.line(screen, GREEN, [100, 100], [140,50], 5)
    pygame.draw.line(screen, GREEN, [100,100], [40,50], 5)
    retrun
