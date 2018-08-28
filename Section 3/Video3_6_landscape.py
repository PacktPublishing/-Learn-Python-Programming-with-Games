'''
Created on Aug 25, 2018
@author: Burkhard A. Meier


Horse images were downloaded from: 
----------------------------------
https://opengameart.org/content/dark-soldier-on-a-horse-valyria-tear
Attribution Instructions: 
from Lilou (Valyria Tear) 

Landscape image was downloaded from:
------------------------------------
https://opengameart.org/content/seamless-hd-landscape-in-parts
Copyright/Attribution Notice: 
Credit as PWL is appreciated.

-----------------------------------------------------------------------
The free GIMP editor was used to export the .xcf files into .png format
The large landscape image was scaled down using GIMP as well.
'''

import pygame
from pygame.locals import *  
from os import path      

pygame.init()  
pygame.display.set_caption('PyGame - Player in Landscape Game') 
                                         
WIDTH, HEIGHT = 600, 400                                        # global variables accessible through this module
game_surface = pygame.display.set_mode((WIDTH, HEIGHT))         # create the game surface
  
fps_clock = pygame.time.Clock()     # create clock instance
FPS = 60                            # frames per second


class Player():
    def __init__(self):
        self.player_img = pygame.image.load(path.join('images', 'horse.png'))
        self.player_img_rect = self.player_img.get_rect()
        

def run_game():
    bg_img = pygame.image.load(path.join('images', 'landscape_background_scaled.png'))    
    game_surface.blit(bg_img, (0, 0))
    
    player = Player()
    player.player_img_rect.center = 96//2, HEIGHT - (96//2)     # position player at left-bottom corner

    # game loop -----------------------------------------------------------------------------
    speed = 5
    run_game = True
    while run_game:
        fps_clock.tick(FPS)                 # run at FPS=60 frames per second

        for event in pygame.event.get():
            if event.type == QUIT:          
                run_game = False
            
        pressed_keys = pygame.key.get_pressed()     # creates a sequence
        
        if pressed_keys[K_UP]:
            player.player_img_rect.y -= speed                         
             
        if pressed_keys[K_DOWN]:
            player.player_img_rect.y += speed                 
                      
        if pressed_keys[K_SPACE]: 
            center_x = WIDTH // 2
            center_y = HEIGHT // 2
            player.player_img_rect.center = center_x, center_y
            
        if pressed_keys[K_RIGHT]:
            player.player_img_rect.x += speed

        if pressed_keys[K_LEFT]:
            player.player_img_rect.x -= speed

               
        game_surface.blit(bg_img, (0, 0))                     
        game_surface.blit(player.player_img, player.player_img_rect)              
        pygame.display.update()                                 
    
    # End game loop -------------------------------------------------------------------------
       
    # exit game
    pygame.quit()


if __name__ == '__main__':
    run_game()



























