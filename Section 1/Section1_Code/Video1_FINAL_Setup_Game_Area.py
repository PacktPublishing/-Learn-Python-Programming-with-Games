'''
Created on Jun 25, 2018
@author: Burkhard A. Meier
'''




import turtle

# define screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

GAME_AREA_START_X = -((SCREEN_WIDTH // 2) -50)
GAME_AREA_START_Y = -((SCREEN_HEIGHT // 2) -50)

BORDER_WIDTH = SCREEN_WIDTH -100
BORDER_HEIGHT = SCREEN_HEIGHT -100

def setup_screen():
    screen = turtle.Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)           
    screen.bgcolor('gray')

def draw_game_area():
    area_turtle = turtle.Turtle()
    area_turtle.setundobuffer(None)                             # no undo buffer to speed up the drawing
    area_turtle.hideturtle()
    area_turtle.speed(0)                                        # 0 is the fastest
    area_turtle.color('black', 'green')                         # pencolor, fillcolor
    area_turtle.penup()                                         # don't draw while moving into position
    area_turtle.setpos(GAME_AREA_START_X, GAME_AREA_START_Y)    # left bottom
    area_turtle.pendown()                                       # now start drawing
    area_turtle.pensize(4)
    
    area_turtle.begin_fill()                    # start filling in the game area
    for _border in range(2):
        area_turtle.fd(BORDER_WIDTH)
        area_turtle.lt(90)
        area_turtle.fd(BORDER_HEIGHT)
        area_turtle.lt(90)
    area_turtle.end_fill()

def create_game_screen():
    setup_screen()
    draw_game_area()


if __name__ == '__main__':
    create_game_screen()            # call the function
    turtle.done()                   # keep the game window up
    
    
