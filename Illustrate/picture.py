# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
GREY = (135, 135, 135)

class Picture:

  def __init__(self, size):
    self.size = size
    return

  def image(self):
    backround.Backround(BLUE, self.size)
    house.House( 200, 150, BLACK, RED, 20)
    stickperson.StickPerson(220, 150, BLACK, stright)
    sun.Sun(390, 290, WHITE)
    cloud.Cloud( 375, 275, GREY, fluffy)
    bird.Bird(100, 175, BLACK, arched)
    bird.Bird(125, 200, BLACK, stright)
    bird.Bird(150, 225, BLACK, arched)
    return
