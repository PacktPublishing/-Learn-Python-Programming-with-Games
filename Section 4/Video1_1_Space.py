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
                                         
WIDTH, HEIGHT = 900, 550                                    # <== adjust size to your liking                       
game_surface = pygame.display.set_mode((WIDTH, HEIGHT))        
  
fps_clock = pygame.time.Clock()     # create clock instance
FPS = 60                            # frames per second

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
        pygame.display.update()
    # End game loop --------------------------------------------------------
    pygame.quit()

if __name__ == '__main__':
    run_3d_game()






























