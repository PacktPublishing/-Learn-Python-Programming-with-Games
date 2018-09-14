'''
Created on Sep 2, 2018
@author: Burkhard A. Meier


Space background image was downloaded from:
--------------------------------------
https://opengameart.org

No attribution required for this png file.

'''




import pygame
from pygame.locals import *  
from os import path     


pygame.init()  
pygame.display.set_caption('PyGame - Starships and Asteroids game') 
                                         
WIDTH, HEIGHT = 900, 600                                    # <== adjust size to your liking                       
game_surface = pygame.display.set_mode((WIDTH, HEIGHT))        
  
fps_clock = pygame.time.Clock()     # create clock instance
FPS = 60                            # frames per second

green = pygame.Color('green')       # define color

# line corner coordinates
LEFT_BOTTOM_X = (10, HEIGHT -10)
LEFT_BOTTOM_Y = (WIDTH -10, HEIGHT -10)
LEFT_TOP_X = (100, 10)
LEFT_TOP_Y = (WIDTH - 100, 10)

BOTTOM_LINE = (LEFT_BOTTOM_X, LEFT_BOTTOM_Y)    # tuple of coordinates
TOP_LINE = (LEFT_TOP_X, LEFT_TOP_Y)    
LEFT_LINE = (LEFT_BOTTOM_X, LEFT_TOP_X)
RIGHT_LINE = (LEFT_BOTTOM_Y, LEFT_TOP_Y)


def run_3d_game():    
    bg_img = pygame.image.load(path.join('images', 'space_background.png'))    
    game_surface.blit(bg_img, (0, 0))
    
    # game loop ------------------------------------------------------------
    run_game = True
    while run_game:
        fps_clock.tick(FPS)                 

        for event in pygame.event.get():
            if event.type == QUIT:          
                run_game = False    
    
        game_surface.blit(bg_img, (0, 0))  
        pygame.draw.line(game_surface, green, *BOTTOM_LINE, 10)     # use * to unpack tuple for (start_pos, end_pos)                                                                   
        pygame.draw.line(game_surface, green, *TOP_LINE, 6)         # line(Surface, color, start_pos, end_pos, width=1) -> Rect
        pygame.draw.line(game_surface, green, *LEFT_LINE, 6)       
        pygame.draw.line(game_surface, green, *RIGHT_LINE, 6)                                                      
                                                                    
        pygame.display.update()
    # End game loop --------------------------------------------------------
    pygame.quit()

if __name__ == '__main__':
    run_3d_game()






























