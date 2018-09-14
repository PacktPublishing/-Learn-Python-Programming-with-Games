'''
Created on Sep 13, 2018
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
from random import randrange

# Initialize pygame and set title
pygame.init()  
pygame.display.set_caption('PyGame - Starships and Asteroids game') 

# Module level global variables                                          
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

# define colors
GREEN = pygame.Color('green')       
RED = pygame.Color('red')
WHITE = pygame.Color('white')
BLACK = pygame.Color('black')
GREY = pygame.Color('grey')
YELLOW = pygame.Color('yellow')
BLUE = pygame.Color('blue')


def rotation_matrix_3d(angle_x, angle_y, angle_z):           
    sx, cx = sin(angle_x), cos(angle_x)
    sy, cy = sin(angle_y), cos(angle_y)
    sz, cz = sin(angle_z), cos(angle_z)
        
    return [
        (cy*cz, -cy*sz, sy),                                # new x
        (cx*sz + sx*sy*cz, cx*cz - sz*sx*sy, -cy*sx),       # new y
        (sz*sx - cx*sy*cz, cx*sz*sy + sx*cz, cx*cy)         # new z
    ]


rotation_xyz = [0, 0, 0]                # list of xyz rotation values

def rotate(axis, degrees):
    rotation_xyz[axis] += degrees       # update the list in index position, in/decrementing the value  


class Shape():
    def __init__(self, vertices, shape_points): 
        self.vertices = vertices
        self.shape_points = shape_points
        self.shape_multiplier = 40
    
    def position_shape(self, vector):    
        SCREEN = (WIDTH, HEIGHT)
        return [round((self.shape_multiplier * coordinate) + (screen_size / 2)) 
                for coordinate, screen_size in zip(vector, SCREEN)]
    
    def draw_shape(self, color=WHITE):
        position = self.vertices.dot(rotation_matrix_3d(*rotation_xyz))                  # dot-scalar product using rotation matrix
        for vector1, vector2 in self.shape_points:
            start = position[vector1]
            end = position[vector2]
            pygame.draw.line(game_surface, color, self.position_shape(start), self.position_shape(end), 4)


class StarshipShape(Shape):
    # class attribute
    starship_position = [WIDTH_CENTER_X + 100, HEIGHT_CENTER_Y]              # starship starting position
    
    def __init__(self):
        vertices = np.array(((1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -2, -2)))    # x, y, z values of points in 3D space
        shape_points = ((0, 1), (0, 2), (2, 3), (1, 3))                          # connecting the points
        super().__init__(vertices, shape_points)                                 # init super class
        self.shape_multiplier = 15                                               # reduce size of spaceship
        
 
    # overwriting base class method
    def position_shape(self, vertices):    
        return [round((self.shape_multiplier * coordinate) + (starship_pos)) 
                for coordinate, starship_pos in zip(vertices, StarshipShape.starship_position)]


class Weapon():
    # class attribute
    weapon_position = [StarshipShape.starship_position[0],
                       StarshipShape.starship_position[1]]    
    
    def position_weapon(self):
        return [StarshipShape.starship_position[0],
                       StarshipShape.starship_position[1]]

    def fire(self, new_pos=3):
        Weapon.weapon_position[0] += new_pos
        Weapon.weapon_position[1] += new_pos
        
        if (Weapon.weapon_position[0] > WIDTH) or (Weapon.weapon_position[1] > HEIGHT):
            Weapon.weapon_position = self.position_weapon()
        fire_x, fire_y = self.weapon_position
        self.weapon_rect = pygame.Rect(fire_x, fire_y, 15, 15)
        pygame.draw.rect(game_surface, RED, self.weapon_rect, 0)        


class AsteroidShape(Shape):
    # class attribute
    asteroid_position = [WIDTH_CENTER_X - 100, HEIGHT_CENTER_Y]
    asteroid_counter = 0
    
    def __init__(self):
        vertices = np.array(((1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1), 
                             (-1, -1, -1), (2, 2, -1)) )                        # 6 points
        shape_points = ((0, 1), (0, 2), (2, 3), (1, 3),                         # flat square
                        (0, 4), (1, 4), (2, 4), (3, 4),                         # pyramid roof on top of square
                        (0, 5), (1, 5), (2, 5), (3, 5),
                        (0, 3), (0, 2))                                         # 14 connections of the points
        super().__init__(vertices, shape_points)
        self.shape_multiplier = 10
        self.speed = 7000

    # overwriting base class method
    def position_shape(self, vertices):      
        self.create_random() 
        return [round((self.shape_multiplier * coordinate) + (asteroid_pos)) 
                for coordinate, asteroid_pos in zip(vertices, AsteroidShape.asteroid_position)]

    def create_random(self):
        AsteroidShape.asteroid_counter += 1
        if AsteroidShape.asteroid_counter == self.speed:
            start = randrange(20, WIDTH) 
            end = randrange(20, HEIGHT)
            AsteroidShape.asteroid_counter = 0
            AsteroidShape.asteroid_position = start, end

  
class TriangleShape(Shape):
    def __init__(self):
        vertices = np.array(((1, 1, 1), (1, 1, -1), (-1, 1, 1))) 
        shape_points = ((0, 1), (0,2), (1, 2))  
        super().__init__(vertices, shape_points)

class FlyingStickShape(Shape):
    def __init__(self):
        vertices = np.array(((-1, -1, -1), (1, -1, 1), (1, -1, 1)))         # creates a deeper looking effect        
        shape_points = ((0, 1), (0, 2))
        super().__init__(vertices, shape_points)

class FlyingStickCenterShape(Shape):
    def __init__(self):
        vertices = np.array(((-1, -1, -1), (1, 1, 1), (1, 1, 1)))           # ties stick to center, use spacebar to see       
        shape_points = ((0, 1), (0, 2))
        super().__init__(vertices, shape_points)

class FlyingDotShape(Shape):
    def __init__(self):
        vertices = np.array(((1, 1, 1), (1, 1, 1)))             # creates a very small flying dot. Press and hold a key down       
        shape_points = ((0, 1), (0, 1))
        super().__init__(vertices, shape_points)
                        

def draw_background_and_lines(bg_img):
    game_surface.blit(bg_img, (0, 0))                           # blit the image, erasing previous shapes                                                                       
    pygame.draw.line(game_surface, GREEN, *BOTTOM_LINE, 10)     # use * to unpack tuple for (start_pos, end_pos)                                                                   
    pygame.draw.line(game_surface, GREEN, *TOP_LINE, 6)         # line(Surface, color, start_pos, end_pos, width=1)
    pygame.draw.line(game_surface, GREEN, *LEFT_LINE, 6)        # draw frame lines onto imaged surface 
    pygame.draw.line(game_surface, GREEN, *RIGHT_LINE, 6)   

       
def keypress_rotation(rotate_by=0.05, move_ship=10):
    X, Y, Z = 0, 1, 2
    rotate_counter_clockwise = rotate_by         
    rotate_clockwise = -rotate_counter_clockwise       # negate value    
    
    pressed_keys = pygame.key.get_pressed()            # use the top-left keyboard keys: q,a,w,s,e,d
      
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
    
    # new Starship movements
    if pressed_keys[pygame.K_RIGHT]: StarshipShape.starship_position[0] += move_ship           
    elif pressed_keys[pygame.K_LEFT]: StarshipShape.starship_position[0] -= move_ship   
    
    if pressed_keys[pygame.K_UP]: StarshipShape.starship_position[1] -= move_ship           
    elif pressed_keys[pygame.K_DOWN]: StarshipShape.starship_position[1] += move_ship   
            
    
def run_3d_game():    
    bg_img = pygame.image.load(path.join('images', 'space_background.png'))    
    game_surface.blit(bg_img, (0, 0))
    
    fps_clock = pygame.time.Clock()  
    FPS = 60                            # frames per second
       
    # game loop ------------------------------------------------------------
    run_game = True
    while run_game:
        fps_clock.tick(FPS)
        #----------------------------------------------------------
        for event in pygame.event.get():
            if event.type == QUIT:          
                run_game = False    
        #----------------------------------------------------------
        draw_background_and_lines(bg_img)                                                  
        #----------------------------------------------------------
        keypress_rotation(rotate_by=0.05, move_ship=10)        
        #----------------------------------------------------------

        StarshipShape().draw_shape()
        ship_x, ship_y = StarshipShape.starship_position
        ship_rect = pygame.Rect(ship_x -35, ship_y -40, 85, 85)
        pygame.draw.rect(game_surface, BLUE, ship_rect, 1)
 
        AsteroidShape().draw_shape(GREY)   
        ast_x, ast_y = AsteroidShape.asteroid_position 
        asteroid_rect = pygame.Rect(ast_x -20, ast_y -35, 60, 70)
        pygame.draw.rect(game_surface, YELLOW, asteroid_rect, 1)
        
        if ship_rect.colliderect(asteroid_rect):
            print('Starship collision!') 
            AsteroidShape().draw_shape(RED)
            StarshipShape().draw_shape(RED)
        
        weapon = Weapon()
        weapon.position_weapon()
        weapon.fire()
        if weapon.weapon_rect.colliderect(asteroid_rect):
            print('Weapon collision!') 
            AsteroidShape().draw_shape(RED)
                          
        TriangleShape().draw_shape(BLACK)
        FlyingStickShape().draw_shape(RED)
          
        little_dot = FlyingDotShape()           
        little_dot.shape_multiplier = 200
        little_dot.draw_shape(GREEN)
 
        little_dot = FlyingDotShape()           
        little_dot.shape_multiplier = 220
        little_dot.draw_shape(RED)   
                 
        #----------------------------------------------------------                                                                                       
        pygame.display.update()
        
    # End game loop --------------------------------------------------------
    pygame.quit()

if __name__ == '__main__':
    run_3d_game()






























