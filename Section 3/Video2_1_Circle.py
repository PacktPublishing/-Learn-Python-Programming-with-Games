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
    def __init__(self, x=WIDTH//2, y=HEIGHT//2, radius=20):
        pygame.draw.circle(game_surface, (255, 0, 0), (x, y), radius)      # RGB = red


def run_game():
    # game logic
    background = pygame.Surface(game_surface.get_size())    # create a new surface to be used as the background
    background = background.convert()                       # this call to convert() is important
    background.fill((0, 0, 250))                            # change the background color (RGB)
    
    game_surface.blit(background, (0, 0))                   # "copy" the background pixel colors by "blitting"
    
    circle_ref = Circle()       # create a new Circle with default values

    # game loop
    run_game = True
    while run_game:
        fps_clock.tick(FPS)                 # run at FPS=60 frames per second
        
        for event in pygame.event.get():
            if event.type == QUIT:          
                run_game = False
            
            elif event.type == KEYDOWN and event.key == K_UP:       # up arrow key pressed
                game_surface.blit(background, (0, 0))               # overwrite background
                Circle(0, 0)                                        # create new Circle top left corner
            
            elif event.type == KEYDOWN and event.key == K_DOWN:     # down arrow key pressed
                game_surface.blit(background, (0, 0))               # overwrite background
                Circle(WIDTH, HEIGHT)                               # create new Circle bottom right corner
            
            elif event.type == KEYDOWN and event.key == K_SPACE:    # spacebar key pressed
                game_surface.blit(background, (0, 0))               # overwrite background
                Circle()                                            # create new Circle center

        pygame.display.update()                                 # update the display for the changed background
       
    # exit game
    pygame.quit()


if __name__ == '__main__':
    run_game()



























