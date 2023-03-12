#Importing Pygame, system and random
import pygame
import sys
import random
#pygame intialisation
pygame.init()

#Creating a class called snake
class Snake(object):
    def __init__(self): #initialising the object's attributes
        self.length=1 #giving the length of the snake
        self.width=0
        self.positions=[((WinWidth/2), (WinHeight/2))] #making a list of the positions of the snake. Making it start at the center of the screen
        self.direction=random.choice([UP, DOWN, LEFT, RIGHT])
        self.color=Green
    
    def head_pos(self): #Getting the position of the head of the snake
        return self.positions[0] #returning data of where the snake is
    
    #defintion of how to take a turn in the game
    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return 
        else:
            self.direction = point 
    
    #moving the snake
    def move(self):
        cur = self.head_pos()
        x, y = self.direction

        #new x and y co-ordinate
        x, y = self.direction
        new = (((cur[0] + (x * Blocksize)) % WinWidth), (cur[1] + (y * Blocksize)) % WinHeight)
        #                  ^                                       ^
        #                  |                                       |
        #            x co-ordinate                            y co-ordinate

        #moving the rest of the body to the next spot
        if len(self.positions)> 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions)>self.length:
                self.positions.pop()
            
                
    #definition of the reset when the snake hits itself
    def reset(self):
        self.length=1
        self.width=1
        self.positions=[((WinWidth/2, WinHeight/2))] #making a list of the positions of the snake. Making it start at the center of the screen
        self.direction=random.choice([UP, DOWN, LEFT, RIGHT])
        

    
    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (Blocksize, Blocksize))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, Black, r, 1)
    
    #keystroke event handling
    def handle_key(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN: #when you have pressed a key
                if event.key==pygame.K_UP: #up arrow pressed
                    self.turn(UP)

                elif event.key==pygame.K_DOWN: #down arrow pressed
                    self.turn(DOWN)
                
                elif event.key==pygame.K_LEFT: #Left arrow pressed
                    self.turn(LEFT)
                
                elif event.key==pygame.K_RIGHT: #down arrow pressed
                    self.turn(RIGHT)           



#Creating a class for the food that the snake will eat called Apple
class Apple(object):
    #initialise the object
    def  __init__(self):
        self.position = (0, 0)
        self.color = Red
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, Grid_Width - 1) * Blocksize, random.randint(0, Grid_Height - 1) * Blocksize)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (Blocksize, Blocksize))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, Black, r, 1)


#define the grid pattern
def Grid_pattern(surface):
   for y in range (0, int(Grid_Height)):
    for x in range(0, int(Grid_Width)):
        if ((x+y) % 2) == 0:
            r=pygame.Rect((x * Blocksize, y * Blocksize), (Blocksize, Blocksize))
            pygame.draw.rect(surface, White, r)
        else:
            rr = pygame.Rect((x * Blocksize, y * Blocksize), (Blocksize, Blocksize))
            pygame.draw.rect(surface, Grey, rr)



#Window dementions (Height and Width)
WinHeight=480
WinWidth=480

#set the block size to what you want
Blocksize=20 

Blocksize = int(Blocksize)

Grid_Width = WinWidth / Blocksize
Grid_Height = WinHeight / Blocksize

#Colours for the game 
White=(255, 255, 255)
Black=(0, 0, 0)
Green=(34, 139, 34)
Red = (255,0,0)
Grey = (169,169,169)

#Font
font = pygame.font.Font('freesansbold.ttf', 30)



#defining the directions from the user
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
def main():
    #initialise pygame
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WinWidth, WinHeight), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    Grid_pattern(surface)

    snake = Snake()
    food = Apple()

    score = 0
    #slider
    
    #while running
    run=True
    
    while run:
        #setting the fps of the game as 10. Can be changed if the user wants it higher or lower. 
        clock.tick(10)
        
        #initialising the movement of the snake in a forever loop
        snake.handle_key()

        #drawing out the grid in a forever loop
        Grid_pattern(surface)

        #initialising the starting movement of the snake.
        snake.move()

        #reverting to original position of the game when you die. I could have done this with a definition of a function but I could not be bothered. So here it is. 
        if snake.head_pos() == food.position:
            snake.length += 1
            score += 1
            food.randomize_position()
        if snake.length==1:
            score=0
            snake.length=1
        if snake.head_pos()==WinHeight:
            score=0
            snake.length=1
        elif snake.head_pos()==WinWidth:
            score=0
            snake.length=1
        
            
        #This creates the text that keeps the score. There are 2 functions of this below and I do not know why but when I remove the second one it does not work. 
        text = font.render("Score {0}".format(score), True, Black)
        screen.blit(text, (5, 10))
        #Draws the snake
        snake.draw(surface)
        #draws the food
        food.draw(surface)
        screen.blit(surface, (0, 0))
        text = font.render("Score {0}".format(score), True, Black)
        screen.blit(text, (5,10))
        
        
        
        pygame.display.update()
        
main()

