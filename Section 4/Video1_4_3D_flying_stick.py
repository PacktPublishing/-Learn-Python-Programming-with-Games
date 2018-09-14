'''
Created on Sep 4, 2018
@author: Burkhard A. Meier


Space background image was downloaded from:
--------------------------------------
https://opengameart.org
No attribution required for this png file.

'''




import pygame
from pygame.locals import *  
from os import path     
import numpy as np                      # import numpy module and alias as "np"
from math import cos, sin


pygame.init()  
pygame.display.set_caption('PyGame - Starships and Asteroids game') 
                                         
WIDTH, HEIGHT = 900, 600                                    # <== adjust size to your liking  
WIDTH_CENTER_X = WIDTH // 2
HEIGHT_CENTER_Y = HEIGHT // 2                     
game_surface = pygame.display.set_mode((WIDTH, HEIGHT))        
    
# line corner coordinates
LEFT_BOTTOM_X = (10, HEIGHT -10)
LEFT_BOTTOM_Y = (WIDTH -10, HEIGHT -10)
LEFT_TOP_X = (100, 10)
LEFT_TOP_Y = (WIDTH - 100, 10)

BOTTOM_LINE = (LEFT_BOTTOM_X, LEFT_BOTTOM_Y)    # tuple of coordinates
TOP_LINE = (LEFT_TOP_X, LEFT_TOP_Y)    
LEFT_LINE = (LEFT_BOTTOM_X, LEFT_TOP_X)
RIGHT_LINE = (LEFT_BOTTOM_Y, LEFT_TOP_Y)

GREEN = pygame.Color('green')       # define colors
RED = pygame.Color('red')
WHITE = pygame.Color('white')
  
fps_clock = pygame.time.Clock()     # create clock instance
FPS = 60                            # frames per second


def rotation_matrix_3d(angle_x, angle_y, angle_z):           
    sx, cx = sin(angle_x), cos(angle_x)
    sy, cy = sin(angle_y), cos(angle_y)
    sz, cz = sin(angle_z), cos(angle_z)
        
    return [
        (cy*cz, -cy*sz, sy),
        (cx*sz + sx*sy*cz, cx*cz - sz*sx*sy, -cy*sx),
        (sz*sx - cx*sy*cz, cx*sz*sy + sx*cz, cx*cy)
    ]


rotation_xyz = [0, 0, 0]                # list of xyz rotation values

def rotate(axis, degrees):
    rotation_xyz[axis] += degrees       # update the list in index position, in/decrementing the value  
    
    
def run_3d_game():    
    bg_img = pygame.image.load(path.join('images', 'space_background.png'))    
    game_surface.blit(bg_img, (0, 0))
    X, Y, Z = 0, 1, 2
    rotate_counter_clockwise = 0.05         
    rotate_clockwise = -rotate_counter_clockwise       # negate value
    
    # game loop ------------------------------------------------------------
    run_game = True
    while run_game:
        fps_clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == QUIT:          
                run_game = False    

        #----------------------------------------------------------
        game_surface.blit(bg_img, (0, 0))                           # blit the image, erasing previous shapes        
                                                                    # draw frame lines onto imaged surface 
        pygame.draw.line(game_surface, GREEN, *BOTTOM_LINE, 10)     # use * to unpack tuple for (start_pos, end_pos)                                                                   
        pygame.draw.line(game_surface, GREEN, *TOP_LINE, 6)         # line(Surface, color, start_pos, end_pos, width=1)
        pygame.draw.line(game_surface, GREEN, *LEFT_LINE, 6)       
        pygame.draw.line(game_surface, GREEN, *RIGHT_LINE, 6)                                                      

        #----------------------------------------------------------
        pressed_keys = pygame.key.get_pressed()                     # use the top-left keyboard keys: q,a,w,s,e,d
          
        if pressed_keys[pygame.K_q]: rotate(axis=X, degrees=rotate_counter_clockwise)           
        elif pressed_keys[pygame.K_a]: rotate(axis=X, degrees=rotate_clockwise)  
             
        if pressed_keys[pygame.K_w]: rotate(axis=Y, degrees=rotate_counter_clockwise)
        elif pressed_keys[pygame.K_s]: rotate(axis=Y, degrees=rotate_clockwise)
        
        if pressed_keys[pygame.K_e]: rotate(axis=Z, degrees=rotate_counter_clockwise)
        elif pressed_keys[pygame.K_d]: rotate(axis=Z, degrees=rotate_clockwise)
            
        if pressed_keys[pygame.K_SPACE]:                # pressing spacebar creates an random looking effect
            rotate(axis=X, degrees=WIDTH_CENTER_X)
            rotate(axis=Y, degrees=HEIGHT_CENTER_Y)
            rotate(axis=Z, degrees=WIDTH_CENTER_X)
        #----------------------------------------------------------

        def position_shape(vector, SHAPE_MULTIPLIER=80):
            SCREEN = (WIDTH, HEIGHT)
            return [round((SHAPE_MULTIPLIER * coordinate) + (screen_size / 2)) for coordinate, screen_size in zip(vector, SCREEN)]
 
        def draw_shape(vertices, shape_points, color=WHITE):
            position = vertices.dot(rotation_matrix_3d(*rotation_xyz))                  # dot-scalar product using rotation matrix
            for vector1, vector2 in shape_points:
                start = position[vector1]
                end = position[vector2]
                pygame.draw.line(game_surface, color, position_shape(start), position_shape(end), 4)


        vertices_dancing_stick = np.array(((-1, -1, -1), (1, -1, 1), (1, -1, 1)))       # creates a deeper looking effect        
        shape_points_2 = ((0, 1), (0, 2))
        draw_shape(vertices_dancing_stick, shape_points_2, RED)
                                                                                        
        pygame.display.update()
        
    # End game loop --------------------------------------------------------
    pygame.quit()

if __name__ == '__main__':
    run_3d_game()






























