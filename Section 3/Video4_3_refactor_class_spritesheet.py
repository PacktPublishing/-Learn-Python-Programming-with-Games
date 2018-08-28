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

spritesheet image was downloaded from:
--------------------------------------
https://opengameart.org
There was no mention of any attribution for this png file.

'''




import pygame
from pygame.locals import *  
from os import path      

pygame.init()  
pygame.display.set_caption('PyGame - Player in Landscape Game') 
                                         
WIDTH, HEIGHT = 900, 550                                    # <== adjust size to your liking                       
game_surface = pygame.display.set_mode((WIDTH, HEIGHT))        
  
fps_clock = pygame.time.Clock()     # create clock instance
FPS = 60                            # frames per second


class Player():
    def __init__(self, player_image, width, height, is_spritesheet=False, num_of_sprites=9):
        
        if not is_spritesheet:
            self.player_img = pygame.image.load(path.join('images', player_image))
            self.player_img_rect = self.player_img.get_rect()  
        
        if is_spritesheet:
            spritesheet = pygame.image.load(path.join('images', player_image)).convert()             
            self.sprite_list = []
     
            for sprite in range(num_of_sprites):                                # first 9 sprites in spritesheet
                sprite_rect = pygame.Rect(sprite * width, 0, width, height)     # get each sprite of 9, row=0
                image = pygame.Surface(sprite_rect.size).convert()
                image.blit(spritesheet, (0, 0), sprite_rect)
                alpha = image.get_at((0, 0))                                # get pixel at top-left corner
                image.set_colorkey(alpha)                                   # important for 'see-through'
                self.sprite_list.append(image)                              # save each sprite in list
             
            self.player_img = self.sprite_list[0]                           # use first sprite in list
            self.player_img_rect = self.player_img.get_rect()
         

def run_game():
    bg_img = pygame.image.load(path.join('images', 'landscape_background_scaled_larger.png'))    
    game_surface.blit(bg_img, (0, 0))
    
    # Player 1 from single sprite
    width, height = 96, 96
    horse_rider = Player('horse.png', width, height)
    horse_rider.player_img_rect.center = width//2, HEIGHT - (height//2)     # position player at left-bottom corner
    
    # Player 2 from sprite sheet
    width, height = 32, 48
    guard = Player('spritesheet.png', width, height, is_spritesheet=True)
    guard.player_img_rect.center = width//2, HEIGHT - (height//2)           # position player at left-bottom corner
    

    # game loop -----------------------------------------------------------------------------
    speed = 5
    player_img_idx = 0
    run_game = True
    while run_game:
        fps_clock.tick(FPS)                 

        for event in pygame.event.get():
            if event.type == QUIT:          
                run_game = False
            
        pressed_keys = pygame.key.get_pressed()     
        
        if pressed_keys[K_UP]:
            horse_rider.player_img_rect.y -= speed                         
             
        if pressed_keys[K_DOWN]:
            horse_rider.player_img_rect.y += speed                 
                      
        if pressed_keys[K_SPACE]: 
            player_img_idx += 1
            if player_img_idx >= 9:
                player_img_idx = 0
            guard.player_img = guard.sprite_list[player_img_idx]
            
        if pressed_keys[K_RIGHT]:
            horse_rider.player_img_rect.x += speed

        if pressed_keys[K_LEFT]:
            horse_rider.player_img_rect.x -= speed

               
        game_surface.blit(bg_img, (0, 0))                     
        game_surface.blit(horse_rider.player_img, horse_rider.player_img_rect) 
        game_surface.blit(guard.player_img, guard.player_img_rect)             
        pygame.display.update()                                 
    
    # End game loop -------------------------------------------------------------------------
       
    # exit game
    pygame.quit()


if __name__ == '__main__':
    run_game()



























