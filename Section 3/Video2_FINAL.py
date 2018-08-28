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
# FPS = 30                            # reduced game speed

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
    x_pos, y_pos = WIDTH//2, HEIGHT//2
    speed = 5
    run_game = True
    while run_game:
        fps_clock.tick(FPS)                 # run at FPS=60 frames per second

        for event in pygame.event.get():
            if event.type == QUIT:          
                run_game = False
            
        pressed_keys = pygame.key.get_pressed()     # creates a sequence
        
        if pressed_keys[K_UP]:
            y_pos -= speed
            Circle(background, x_pos, y_pos)                             
            
        if pressed_keys[K_DOWN]:
            y_pos += speed
            Circle(background, x_pos, y_pos)                  
                      
        if pressed_keys[K_SPACE]:
            Circle(background)                                  # create new Circle center
            
        if pressed_keys[K_RIGHT]:
            x_pos += speed
            Circle(background, x_pos, y_pos)
            
        if pressed_keys[K_LEFT]:
            x_pos -= speed
            Circle(background, x_pos, y_pos)
                                             
                      
        pygame.display.update()                                 # update the display
    
    # End game loop -------------------------------------------------------------------------
       
    # exit game
    pygame.quit()


if __name__ == '__main__':
    run_game()



























