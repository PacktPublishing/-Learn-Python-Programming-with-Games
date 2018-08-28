'''
Created on Aug 24, 2018
@author: Burkhard A. Meier
'''




# imports
import pygame
from pygame.locals import *         # imports lots of constants (e.g. K_UP, K_SPACE)

# initialization
pygame.init()                                           # don't forget to make this initialization call
game_surface = pygame.display.set_mode((600, 400))      # create the game surface, passing in a size (width, height)
pygame.display.set_caption('PyGame - Player in Landscape Game')   # change Window Title

fps_clock = pygame.time.Clock()     # create clock instance
FPS = 60                            # frames per second

def run_game():
    # game logic
    background = pygame.Surface(game_surface.get_size())    # create a new surface to be used as the background
    background = background.convert()                       # this call to convert() is important
    background.fill((0, 0, 250))                            # change the background color (RGB)
    
    game_surface.blit(background, (0, 0))                   # "copy" the background pixel colors by "blitting"
    pygame.display.update()                                 # have to update the display for the changed background
    
    # game loop
    run_game = True
    while run_game:
        fps_clock.tick(FPS)                 # run at FPS = 60 frames per second
        
        for event in pygame.event.get():
            if event.type == QUIT:          # from pygame.locals import *, no need to prepend pygame.QUIT
                run_game = False
    
    # exit game
    pygame.quit()


if __name__ == '__main__':
    run_game()



























