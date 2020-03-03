import pygame
import math
from math import pi

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
    Picture.image()
    return

  def image():
    Backround(WHITE)
    House(20, 50, BLACK, BLACK, 50)
    Bird(100, 175, BLACK, 'arched')
    Bird(125, 200, BLACK, 'stright')
    Cloud(375, 275, GREY, 20, 'fluffy')
    Sun(390, 290, WHITE, 30)
    StickPerson(220, 150, BLACK, 'stright')
    return


class Shape:

  def __init__(self, x, y, color):
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

class Sun(Shape):

  def __init__(self, x, y, color,size):
    self.color = color
    self.size = size
    super().__init__(x,y,color)
    Sun.drawSun()
    return

  def drawSun():
    pygame.draw.ellipse(screen, RED, [600, 00, 200, 100], 0)
    return

class StickPerson(Shape):

  def __init__(self, x, y, color, name):
    self.color = color
    self.type = name
    super().__init__(x,y,color)
    StickPerson.drawPerson()
    return

  def drawPerson():
    pygame.draw.aaline(screen, GREEN, [150, 600],[140, 580], True)
    pygame.draw.aaline(screen, GREEN, [130, 600],[140, 580], True)
    pygame.draw.aaline(screen, GREEN, [140, 580],[140, 560], True)
    pygame.draw.aaline(screen, GREEN, [140, 570],[150, 580], True)
    pygame.draw.aaline(screen, GREEN, [140, 570],[130, 580], True)
    pygame.draw.circle(screen, GREEN, [140, 560], 5)
    return

class House(Shape):

  def __init__(self, x, y, colorbody, colorroof, size):
    self.colorbody = colorbody
    self.colorroof = colorroof
    self.size = size
    super().__init__(x,y, colorbody)
    House.drawHouse()
    return

  def drawHouse():
    pygame.draw.rect(screen, BLACK, [(size[0]/4+10), (size[0]/2 + 50), size[1]/2, size[1]/2 + 50])
    pygame.draw.polygon(screen, BLACK, [[size[0]/4, size[1]- 150], [size[0]/2 - 25, size[1]/2 - 100], [size[0]/1.5, size[1] - 150]], 5)
    return

class Cloud(Shape):

  def __init__(self, x, y, color, size, name):
    self.color = color
    self.size = size
    self.type = name
    super().__init__(x,y,color)
    Cloud.drawFluffy()
    return 

  def drawFluffy():
    pygame.draw.circle(screen, GREY, [160, 250], 15)
    pygame.draw.circle(screen, GREY, [140, 240], 15)
    pygame.draw.circle(screen, GREY, [140, 260], 15)
    pygame.draw.circle(screen, GREY, [180, 250], 15)
    pygame.draw.circle(screen, GREY, [170, 260], 15)
    return

class Bird(Shape):

  def __init__(self, x, y, color, name):
    self.color = color
    self.type = name
    super().__init__(x,y,color)
    if self.type == 'arched':
      Bird.drawtypeArch()
    else:
      Bird.drawtypeStright()
    return

  def drawtypeArch():
    pygame.draw.arc(screen, BLACK,[210, 75, 150, 125], 0, pi/2, 2)
    pygame.draw.arc(screen, BLACK,[360,75,150,125], pi/2, pi, 2)
    return

  def drawtypeStright():
    pygame.draw.line(screen, GREEN, [100, 100], [140,50], 5)
    pygame.draw.line(screen, GREEN, [100,100], [40,50], 5)
    return
    
class Backround:

  def __init__(self, color):
    self.color = color
    Backround.fillScreen()
    return

  def fillScreen():
    screen.fill(WHITE)
    return
 
# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
 
# Set the height and width of the screen
size = [800, 600]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Illustrate")
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
while not done:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
 
    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
     
    # Clear the screen and set the screen background
    h8 = Picture(screen)
    #i9
    #j10
    #k11
    #l12
    
    
    
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()
