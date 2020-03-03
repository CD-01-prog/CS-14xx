import random
import pygame

class Ball:
    def __init__(self,size,min_x,max_x,min_y,max_y,left_paddle_x,right_paddle_x):
        self.mX = min_x
        self.mY = min_y
        self.mMinX = min_x
        self.mMaxX = max_x
        self.mMinY = min_y
        self.mMaxY = max_y
        self.mSize = size
        self.mDX = 0
        self.mDY = 0
        self.mLeftPaddleX = left_paddle_x
        self.mLeftPaddleMinY = min_y
        self.mLeftPaddleMaxY = max_y
        self.mRightPaddleX = right_paddle_x
        self.mRightPaddleMinY = min_y
        self.mRightPaddleMaxY = max_y
        return

    def getX(self):
        return self.mX

    def getY(self):
        return self.mY

    def getSize(self):
        return self.mSize

    def getDX(self):
        return self.mDX

    def getDY(self):
        return self.mDY

    def getMinX(self):
        return self.mMinX

    def getMaxX(self):
        return self.mMaxX

    def getMinY(self):
        return self.mMinY

    def getMaxY(self):
        return self.mMaxY

    def getLeftPaddleX(self):
        return self.mLeftPaddleX

    def getLeftPaddleMinY(self):
        return self.mLeftPaddleMinY

    def getLeftPaddleMaxY(self):
        return self.mLeftPaddleMaxY

    def getRightPaddleX(self):
        return self.mRightPaddleX

    def getRightPaddleMinY(self):
        return self.mRightPaddleMinY

    def getRightPaddleMaxY(self):
        return self.mRightPaddleMaxY

    def setPosition(self, x, y):
        if x >= self.mMinX and \
           x <= self.mMaxX - self.mSize and \
           y >= self.mMinY and \
           y <= self.mMaxY - self.mSize:
           self.mX, self.mY = x, y

    def setSpeed(self, dx, dy):
        self.mDX, self.mDY = dx, dy

    def setLeftPaddleY(self, paddle_min_y, paddle_max_y):
        if paddle_min_y >= self.mLeftPaddleMinY and \
           paddle_min_y < paddle_max_y and \
           paddle_max_y <= self.mLeftPaddleMaxY:
            self.mLeftPaddleMinY = paddle_min_y
            self.mLeftPaddleMaxY = paddle_max_y

    def setRightPaddleY(self, paddle_min_y, paddle_max_y):
        if paddle_min_y >= self.mRightPaddleMinY and \
           paddle_min_y < paddle_max_y and \
           paddle_max_y <= self.mRightPaddleMaxY:
            self.mRightPaddleMinY = paddle_min_y
            self.mRightPaddleMaxY = paddle_max_y

    def checkTop(self, new_y):
        if new_y > self.mMinY:
            return new_y
        self.mDY *= -1
        return self.mMinY + (self.mMinY - new_y)

    def checkBottom(self, new_y):
        if new_y <= self.mMaxY - self.mSize:
            return new_y
        self.mDY *= -1
        return self.mMaxY*2 - self.mSize*2 - new_y

    def checkLeft(self, new_x):
        if new_x >= self.mMinX:
            return new_x
        self.setSpeed(0,0)
        return self.mMinX


    def checkRight(self, new_x):
        if new_x <= self.mMaxX - self.mSize:
            return new_x
        self.setSpeed(0, 0)
        return self.mMaxX - self.mSize

    def checkLeftPaddle(self, new_x, new_y):
        if self.mX < self.mLeftPaddleX or \
           new_x > self.mLeftPaddleX or \
           self.mDX >= 0:
            return new_x

        midY = int((self.mY + new_y)/2)
        if not(midY <= self.mLeftPaddleMaxY and \
               midY >= self.mLeftPaddleMinY):
            return new_x

        self.mDX *= -1
        return self.mLeftPaddleX + (self.mLeftPaddleX - new_x)


    def checkRightPaddle(self, new_x, new_y):
        if self.mX > self.mRightPaddleX + self.mSize or \
           new_x < self.mRightPaddleX - self.mSize or \
           self.mDX <= 0:
            return new_x

        midY = int((self.mY + new_y)/2)
        if not(midY <= self.mRightPaddleMaxY and \
               midY >= self.mRightPaddleMinY):
            return new_x

        self.mDX *= -1
        return self.mRightPaddleX*2 - self.mSize*2 - new_x

    def move(self, dt):
        new_x = self.mX + self.mDX * dt
        new_y = self.mY + self.mDY * dt

        new_y = self.checkTop(new_y)
        new_y = self.checkBottom(new_y)

        new_x = self.checkLeft(new_x)
        new_x = self.checkRight(new_x)

        new_x = self.checkLeftPaddle(new_x, new_y)
        new_x = self.checkRightPaddle(new_x, new_y)

        self.mX = new_x
        self.mY = new_y

    def serveLeft(self, x, min_y, max_y, min_dx, max_dx, min_dy, max_dy):
        self.mX = x
        self.mY = random.uniform(min_y, max_y)
        self.mDX = random.uniform(min_dx, max_dx)
        self.mDY = random.uniform(min_dy, max_dy)

    def serveRight(self, x, min_y, max_y, min_dx, max_dx, min_dy, max_dy):
        self.mX = x
        self.mY = random.uniform(min_y, max_y)
        self.mDX = random.uniform(-min_dx, -max_dx)
        self.mDY = random.uniform(min_dy, max_dy)

    def draw(self, surface):
        r = pygame.Rect(self.mX, self.mY, self.mSize, self.mSize)
        pygame.draw.rect(surface, (255, 255, 255), r, 0)
        return

#
# You should not need to edit this file.

class Game:
    def __init__( self, name, width, height, frames_per_second ):
        self.width = width
        self.height = height
        self.frames_per_second = frames_per_second
        self.on = True

        self.screen = pygame.display.set_mode(
                # set the size
                ( width, height ),

                # use double-buffering for smooth animation
                pygame.DOUBLEBUF |

                # apply alpha blending
                pygame.SRCALPHA)

        # set the title of the window
        pygame.display.set_caption( name )
        
        # set time tracking
        self.clock = pygame.time.Clock( )
        self.this_frame_time = pygame.time.get_ticks( ) / 1000.
        self.last_frame_time = self.this_frame_time
        return

    def get_frame_time( self ):
        return self.this_frame_time
        
    def get_delta_time( self ):
        return self.delta_time
        
    def game_logic( self, keys, newkeys, buttons, newbuttons, mouse_position, dt ):
        raise NotImplementedError( )
        return

    def paint(self, surface):
        raise NotImplementedError( )
        return

    def main_loop( self ):
        keys = set( )
        buttons = set( )
        mouse_position = ( 1, 1 )
        self.last_frame_time = pygame.time.get_ticks( ) / 1000.

        while True:
            self.clock.tick( self.frames_per_second )

            newkeys = set( )
            newbuttons = set( )
            for e in pygame.event.get( ):
                # did the user try to close the window?
                if e.type == pygame.QUIT:
                    pygame.quit()
                    return

                # did the user just press the escape key?
                if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

                # track which mouse buttons are currently pressed
                if e.type == pygame.MOUSEBUTTONDOWN:
                    buttons.add( e.button )
                    newbuttons.add( e.button )
                    mouse_position = e.pos

                if e.type == pygame.MOUSEBUTTONUP:
                    buttons.discard( e.button )
                    mouse_position = e.pos

                if e.type == pygame.MOUSEMOTION:
                    mouse_position = e.pos
                
                # track which keys are currently set
                if e.type == pygame.KEYDOWN:
                    keys.add( e.key )
                    newkeys.add( e.key )
                if e.type == pygame.KEYUP:
                    keys.discard( e.key )

            self.this_frame_time = pygame.time.get_ticks( ) / 1000.
            self.delta_time = ( self.this_frame_time - self.last_frame_time )
            self.last_frame_time = self.this_frame_time
            if self.on:
                self.game_logic( keys, newkeys, buttons, newbuttons, mouse_position, self.delta_time )
                self.paint( self.screen )

            pygame.display.flip( )
        return

PADDLE_COLOR = (255,255,255)

class Paddle:

    def __init__(self,x,y,width,height,speed,min_y,max_y):
        self.mX = x
        self.mY = y
        self.mWidth = width
        self.mHeight = height
        self.mSpeed = speed
        self.mMinY = min_y
        self.mMaxY = max_y
        return

    def getX(self):
        return self.mX

    def getY(self):
        return self.mY

    def getWidth(self):
        return self.mWidth

    def getHeight(self):
        return self.mHeight

    def getSpeed(self):
        return self.mSpeed

    def getMinY(self):
        return self.mMinY

    def getMaxY(self):
        return self.mMaxY

    def getRightX(self):
        return self.mX + self.mWidth

    def getBottomY(self):
        return self.mY + self.mHeight

    def setPosition(self, y):
        if y+self.mHeight <= self.mMaxY and y >= self.mMinY:
            self.mY = y

    def moveUp(self, dt):
        new_y = self.mY - self.mSpeed * dt

        if new_y >= self.mMinY:
            self.mY = new_y
        else:
            self.mY = self.mMinY

    def moveDown(self, dt):
        new_y = self.mY + self.mSpeed * dt

        if new_y + self.mHeight <= self.mMaxY:
            self.mY = new_y
        else:
            self.mY = self.mMaxY - self.mHeight

    def draw(self, surface):
        r = pygame.Rect(self.mX, self.mY, self.mWidth, self.mHeight)
        pygame.draw.rect(surface, PADDLE_COLOR, r, 0)

LEFT = 1
RIGHT = 2
LEFT_WIN = 3
RIGHT_WIN = 4

class Pong:

    def __init__( self, width, height ):
        self.mWidth = width
        self.mHeight = height

        score_width = 80
        score_height = 40
        score_x = self.mWidth / 2 - score_width / 2
        score_y = 40
        self.mScoreBoard = ScoreBoard( score_x, score_y, score_width, score_height )
        
        wall_size = 10
        self.mLeftWall = Wall( 0, 0, wall_size, self.mHeight )
        self.mRightWall = Wall( self.mWidth-wall_size, 0, wall_size, self.mHeight )
        self.mTopWall = Wall( 0, 0, self.mWidth, wall_size )
        self.mBottomWall = Wall( 0, self.mHeight-wall_size, self.mWidth, wall_size )

        paddle_margin = 20
        paddle_width = 20
        paddle_height = 100
        paddle_speed = self.mHeight / 1.25
        self.mLeftPaddle = Paddle( self.mLeftWall.getRightX( ) + paddle_margin,
                                          self.mHeight / 2 - paddle_height / 2,
                                          paddle_width, paddle_height,
                                          paddle_speed,
                                          self.mTopWall.getBottomY( ),
                                          self.mBottomWall.getY( ) )
        
        self.mRightPaddle = Paddle( self.mRightWall.getX( ) - paddle_margin - paddle_width,
                                           self.mHeight / 2 - paddle_height / 2,
                                           paddle_width, paddle_height,
                                           paddle_speed,
                                           self.mTopWall.getBottomY( ),
                                           self.mBottomWall.getY( ) )
        
        size = 20
        self.mBall = Ball( size, 
                                self.mLeftWall.getRightX( ),
                                self.mRightWall.getX( ),
                                self.mTopWall.getBottomY( ),
                                self.mBottomWall.getY( ),
                                self.mLeftPaddle.getRightX( ),
                                self.mRightPaddle.getX( ) )
        self.serveBall( )
        
        self.mBall.setLeftPaddleY( self.mLeftPaddle.getY( ), self.mLeftPaddle.getBottomY( ) )
        self.mBall.setRightPaddleY( self.mRightPaddle.getY( ), self.mRightPaddle.getBottomY( ) )

        return

    def serveBall( self ):
        min_dx = self.mWidth / 2.0
        max_dx = self.mWidth / 1.5
        max_dy = self.mHeight / 1.0
        min_dy = -max_dy
        if self.mScoreBoard.getServeStatus( ) == LEFT:
            self.mBall.serveLeft( self.mLeftPaddle.getRightX( ) + self.mBall.getSize( ),
                                  self.mLeftPaddle.getY( ),
                                  self.mLeftPaddle.getBottomY( ),
                                  min_dx, max_dx, min_dy, max_dy )
            self.mScoreBoard.swapServe( )
            self.mBallMoving = True
        elif self.mScoreBoard.getServeStatus( ) == RIGHT:
            self.mBall.serveRight( self.mRightPaddle.getX( ) - self.mBall.getSize( ),
                                   self.mRightPaddle.getY( ),
                                   self.mRightPaddle.getBottomY( ),
                                   min_dx, max_dx, min_dy, max_dy )
            self.mScoreBoard.swapServe( )
            self.mBallMoving = True
        return

    def update( self, dt, keys ):

        if self.mBall.getDX( ) != 0:
            self.mBall.move( dt )

            if pygame.K_w in keys:
                self.mLeftPaddle.moveUp( dt )
                self.mBall.setLeftPaddleY( self.mLeftPaddle.getY( ), self.mLeftPaddle.getBottomY( ) )
            elif pygame.K_s in keys:
                self.mLeftPaddle.moveDown( dt )
                self.mBall.setLeftPaddleY( self.mLeftPaddle.getY( ), self.mLeftPaddle.getBottomY( ) )

            if pygame.K_UP in keys:
                self.mRightPaddle.moveUp( dt )
                self.mBall.setRightPaddleY( self.mRightPaddle.getY( ), self.mRightPaddle.getBottomY( ) )
            elif pygame.K_DOWN in keys:
                self.mRightPaddle.moveDown( dt )
                self.mBall.setRightPaddleY( self.mRightPaddle.getY( ), self.mRightPaddle.getBottomY( ) )

        else:
            if self.mBallMoving:
                self.mBallMoving = False
                if self.mBall.getX( ) < self.mWidth / 2:
                    self.mScoreBoard.scoreRight( )
                else:
                    self.mScoreBoard.scoreLeft( )
                    
            if( ( self.mScoreBoard.getServeStatus( ) == LEFT and
                  pygame.K_d in keys ) or
                ( self.mScoreBoard.getServeStatus( ) == RIGHT and
                  pygame.K_LEFT in keys ) ):
                self.serveBall( )
            
        return

    def draw( self, surface ):
        color = ( 0, 0, 0 )
        surface.fill( color )
        self.mTopWall.draw( surface )
        self.mBottomWall.draw( surface )
        self.mLeftWall.draw( surface )
        self.mRightWall.draw( surface )
        self.mScoreBoard.draw( surface )
        self.mLeftPaddle.draw( surface )
        self.mRightPaddle.draw( surface )
        self.mBall.draw( surface )

        return

SCOREBOARD_COLOR = (230, 230, 230)

class ScoreBoard:

    def __init__(self,x,y,width,height):
        self.mX = x
        self.mY = y
        self.mWidth = width
        self.mHeight = height
        self.mLeftScore = 0
        self.mRightScore = 0
        self.mServeStatus = 1

    def getX(self):
        return self.mX

    def getY(self):
        return self.mY

    def getWidth(self):
        return self.mWidth

    def getHeight(self):
        return self.mHeight

    def getLeftScore(self):
        return self.mLeftScore

    def getRightScore(self):
        return self.mRightScore

    def getServeStatus(self):
        return self.mServeStatus

    def isGameOver(self):
        return self.mServeStatus == 3 or self.mServeStatus == 4

    def scoreLeft(self):
        if self.isGameOver():
            return
        self.mLeftScore += 1
        if self.mLeftScore >= 9:
            self.mServeStatus = 3


    def scoreRight(self):
        if self.isGameOver():
            return
        self.mRightScore += 1
        if self.mRightScore >= 9:
            self.mServeStatus = 4

    def swapServe(self):
        if self.mServeStatus == 1:
            self.mServeStatus = 2
        elif self.mServeStatus == 2:
            self.mServeStatus = 1

    def draw(self,surface):
        r = pygame.Rect(self.mX, self.mY, self.mWidth, self.mHeight)
        pygame.draw.rect(surface, SCOREBOARD_COLOR, r, 0)

        c_l_x = self.mX + self.mWidth * .25
        c_l_y = self.mY + self.mHeight * .5
        c_r_x = self.mX + self.mWidth * .75
        c_r_y = self.mY + self.mHeight * .5

        left_score_text = Text(str(self.mLeftScore), c_l_x, c_l_y)
        right_score_text = Text(str(self.mRightScore), c_r_x, c_r_y)

        left_score_text.draw(surface)
        right_score_text.draw(surface)

class Text:

    def __init__( self, string, x, y ):
        self.mX = x
        self.mY = y
        self.mString = string
        self.mColor = ( 0, 0, 0 )
        font_height = 24
        self.mFont = pygame.font.SysFont( "Courier New", font_height )
        return

    def setText( self, string ):
        self.mString = string
        return

    def setColor( self, color ):
        self.mColor = color
        return

    def setSize( self, size ):
        self.mFont = pygame.font.SysFont( "Courier New", size )
        return

    def draw( self, surface ):
        text_object = self.mFont.render( self.mString, False, self.mColor )
        text_rect = text_object.get_rect( )
        text_rect.center = ( int( self.mX ), int( self.mY ) )
        surface.blit( text_object, text_rect )
        return

WALL_COLOR = (10, 255, 10)

class Wall:

    def __init__(self,x,y,width,height):
        self.mX = x
        self.mY = y
        self.mWidth = width
        self.mHeight = height
        return

    def getX(self):
        return self.mX

    def getY(self):
        return self.mY

    def getWidth(self):
        return self.mWidth

    def getHeight(self):
        return self.mHeight

    def getRightX(self):
        return self.mX + self.mWidth

    def getBottomY(self):
        return self.mY + self.mHeight

    def draw(self, surface):
        r = pygame.Rect(self.mX, self.mY, self.mWidth, self.mHeight)
        pygame.draw.rect(surface, WALL_COLOR, r, 0)



# YOU SHOULD CONFIGURE THESE TO MATCH YOUR GAME
# window title bar text
TITLE = "Pong"
# pixels width
WINDOW_WIDTH  = 800
# pixels high
WINDOW_HEIGHT = 600
# frames per second
DESIRED_RATE  = 30

class PygameApp( Game ):

    def __init__( self, title, width, height, frame_rate ):

        Game.__init__( self, title, width, height, frame_rate )
        
        # create a game instance
        # YOU SHOULD CHANGE THIS TO IMPORT YOUR GAME MODULE
        self.mGame = Pong( width, height )
        return
        
        
    def game_logic( self, keys, newkeys, buttons, newbuttons, mouse_position, dt ):
        # keys contains all keys currently held down
        # newkeys contains all keys pressed since the last frame
        # Use pygame.K_? as the keyboard keys.
        # Examples: pygame.K_a, pygame.K_UP, etc.
        # if pygame.K_UP in newkeys:
        #    The user just pressed the UP key
        #
        # buttons contains all mouse buttons currently held down
        # newbuttons contains all buttons pressed since the last frame
        # Use 1, 2, 3 as the mouse buttons
        # if 3 in buttons:
        #    The user is holding down the right mouse button
        #
        # mouse_position contains x and y location of mouse in window
        # dt contains the number of seconds since last frame
        
        x = mouse_position[ 0 ]
        y = mouse_position[ 1 ]

        # Update the state of the game instance
        # YOU SHOULD CHANGE THIS TO IMPORT YOUR GAME MODULE
        self.mGame.update( dt, keys )

        return
    
    def paint( self, surface ):
        # Draw the current state of the game instance
        self.mGame.draw( surface )
        return

def main( ):
    pygame.font.init( )
    game = PygameApp( TITLE, WINDOW_WIDTH, WINDOW_HEIGHT, DESIRED_RATE )
    game.main_loop( )
    
if __name__ == "__main__":
    main( )

main()
