'''
Created on Aug 24, 2018
@author: Burkhard A. Meier
'''




# imports
import pygame
from pygame.locals import *        

# initialization
pygame.init()  
pygame.display.set_caption('PyGame - Player in Landscape Game') 
                                         
WIDTH, HEIGHT = 600, 400                                        # global variables accessible throught this module
game_surface = pygame.display.set_mode((WIDTH, HEIGHT))         # create the game surface, passing in a size (width, height)
  
fps_clock = pygame.time.Clock()     # create clock instance
FPS = 60                            # frames per second

class Circle():
    def __init__(self, background, x=WIDTH//2, y=HEIGHT//2, radius=20):
        game_surface.blit(background, (0, 0))                               # overwrite background
        pygame.draw.circle(game_surface, (255, 0, 0), (x, y), radius)       # RGB = red
        pygame.display.update()

def run_game():
    # game logic
    background = pygame.Surface(game_surface.get_size())    # create a new surface to be used as the background
    background = background.convert()                       # this call to convert() is important
    background.fill((0, 0, 250))                            # change the background color (RGB)
    
    game_surface.blit(background, (0, 0))                   # "copy" the background pixel colors by "blitting"
    
    circle_ref = Circle(background)       # create a new Circle with default values

    # game loop -----------------------------------------------------------------------------
    run_game = True
    while run_game:
        fps_clock.tick(FPS)                 # run at FPS=60 frames per second

        for event in pygame.event.get():
            if event.type == QUIT:          
                run_game = False
            
        pressed_keys = pygame.key.get_pressed()     # creates a sequence
        
        if pressed_keys[K_UP]:
            print('up arrow key was pressed')
            
        if pressed_keys[K_DOWN]:
            print('K_DOWN arrow key was pressed')  
                      
        if pressed_keys[K_SPACE]:
            print('K_SPACE  key was pressed')
            
        if pressed_keys[K_RIGHT]:
            print('K_RIGHT arrow key was pressed')
            
        if pressed_keys[K_LEFT]:
            print('K_LEFT arrow key was pressed')
                             
#             elif event.type == KEYDOWN and event.key == K_UP:       # up arrow key pressed
#                 Circle(background, 0, 0)                            # create new Circle top left corner
#             
#             elif event.type == KEYDOWN and event.key == K_DOWN:     # down arrow key pressed
#                 Circle(background, WIDTH, HEIGHT)                   # create new Circle bottom right corner
#             
#             elif event.type == KEYDOWN and event.key == K_SPACE:    # spacebar key pressed
#                 Circle(background)                                  # create new Circle center
#             
#             elif event.type == KEYDOWN and event.key == K_RIGHT:    # right key pressed
#                 x = WIDTH // 2
#                 y = HEIGHT // 2
#                 while x < WIDTH:                                    # right border X-dimension
#                     x += 10                                         # move right
#                     y -= 2                                     
#                     Circle(background, x, y)                        # create new Circle 
#                     pygame.time.delay(10)                           # delay by 10 milliseconds
#                 while x > 0:                                        # left border X-dimension
#                     x -= 10                                         # move left 
#                     y += 1 
#                     Circle(background, x, y)                        # create new Circle 
#                     pygame.time.delay(10)                
#                             
#             elif event.type == KEYDOWN and event.key == K_LEFT:     # left key pressed
#                 x = WIDTH // 2
#                 y = HEIGHT // 2
#                 while y < HEIGHT:
#                     y += 5
#                     if 0 < x < WIDTH:
#                         x += 5
#                     Circle(background, x, y)                        # create new Circle 
#                     pygame.time.delay(10)
#                 while y > 0:
#                     y -= 5
#                     if WIDTH > x > 0:
#                         x += 5                                      
#                     Circle(background, x, y)                        # create new Circle 
#                     pygame.time.delay(10)                
                      
        pygame.display.update()                                 # update the display
    
    # End game loop -------------------------------------------------------------------------
       
    # exit game
    pygame.quit()


if __name__ == '__main__':
    run_game()



























