'''
Created on Aug 25, 2018
@author: Burkhard A. Meier

Horse images were downloaded from: 
----------------------------------
https://opengameart.org/content/dark-soldier-on-a-horse-valyria-tear
Attribution Instructions: 
from Lilou (Valyria Tear) 

The free GIMP editor was used to export the .xcf files into .png format

'''




# imports
import pygame
from pygame.locals import *  
from os import path      

# initialization
pygame.init()  
pygame.display.set_caption('PyGame - Player in Landscape Game') 
                                         
WIDTH, HEIGHT = 600, 400                                        # global variables accessible throught this module
game_surface = pygame.display.set_mode((WIDTH, HEIGHT))         # create the game surface, passing in a size (width, height)
  
fps_clock = pygame.time.Clock()     # create clock instance
FPS = 60                            # frames per second


class Player():
    def __init__(self):
        self.player_img = pygame.image.load(path.join('images', 'horse.png'))
        self.player_img_rect = self.player_img.get_rect()
        
# game logic
def run_game():
    background = pygame.Surface(game_surface.get_size())    # create a new surface to be used as the background
    background = background.convert()                       # this call to convert() is important
    background.fill((0, 0, 250))                            # change the background color (RGB)    
    game_surface.blit(background, (0, 0))                   # "copy" the background pixel colors by "blitting"
    
    player = Player()
    print('Player x position: ', player.player_img_rect.x)

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
                      
        if pressed_keys[K_SPACE]: pass

            
        if pressed_keys[K_RIGHT]:
            player.player_img_rect.x += speed

        if pressed_keys[K_LEFT]:
            player.player_img_rect.x -= speed


        game_surface.blit(background, (0, 0))                                     
        game_surface.blit(player.player_img, player.player_img_rect)    # create player after changing x, y      
        pygame.display.update()                                 
    
    # End game loop -------------------------------------------------------------------------
       
    # exit game
    pygame.quit()


if __name__ == '__main__':
    run_game()



























