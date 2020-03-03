import shape

class StickPerson(Shape):

  def __init__(self, x, y, color, type):
    self.color = color
    self.type = type
    super().__init__(x,y,color)
    StickPerson.drawPerson()
    return

  def drawPerson(self):
    pygame.draw.aaline(screen, GREEN, [150, 600],[140, 580], True)
    pygame.draw.aaline(screen, GREEN, [130, 600],[140, 580], True)
    pygame.draw.aaline(screen, GREEN, [140, 580],[140, 560], True)
    pygame.draw.aaline(screen, GREEN, [140, 570],[150, 580], True)
    pygame.draw.aaline(screen, GREEN, [140, 570],[130, 580], True)
    pygame.draw.circle(screen, GREEN, [140, 560], 5)
    return
