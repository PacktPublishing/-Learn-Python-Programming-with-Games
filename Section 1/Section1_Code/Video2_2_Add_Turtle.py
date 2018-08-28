'''
Created on Jul 1, 2018
@author: Burkhard A. Meier
'''





import turtle
from time import sleep
from Section1.Video1_FINAL_Setup_Game_Area import create_game_screen, BORDER_HEIGHT, GAME_AREA_START_Y


BORDER_HEIGHT_HALF = BORDER_HEIGHT // 2

screen = turtle.Screen()
screen.tracer(2)                        # delay drawing by two frames

def create_track():
    track_turtle = turtle.Turtle()
    track_turtle.setundobuffer(None)
    track_turtle.hideturtle()
    track_turtle.speed(0)
    track_turtle.color('black', 'brown')
    
    track_turtle.penup()
    track_turtle.begin_fill()
    start_pos = 20
    track_turtle.setpos(start_pos, GAME_AREA_START_Y)
    track_turtle.pendown()
    track_turtle.setpos(start_pos, BORDER_HEIGHT_HALF)
    track_turtle.setpos(-start_pos, BORDER_HEIGHT_HALF)
    track_turtle.setpos(-start_pos, GAME_AREA_START_Y)
    track_turtle.setpos(start_pos, GAME_AREA_START_Y)
    track_turtle.end_fill()


def add_turtle_runner():
    running_turtle = turtle.Turtle()
    running_turtle.shape('turtle')
    running_turtle.setundobuffer(None)
    running_turtle.penup()
    running_turtle.speed(0)
    running_turtle.color('orange', 'blue')              # outside turtle color orange, turtle fill area is blue
    
    running_turtle.setpos(0, GAME_AREA_START_Y)
    running_turtle.setheading(90)
    running_turtle.showturtle()
    
    for run in range(BORDER_HEIGHT):
        running_turtle.setpos(0, GAME_AREA_START_Y + run)
        print(run)
        if run % 12:
            running_turtle.setpos(0 + 1, GAME_AREA_START_Y + run)   # wiggle the turtle runner
        sleep(0.01)

screen.update()                         # update the screen


if __name__ == '__main__':
    create_game_screen()
    create_track()
    add_turtle_runner()
    turtle.done()
    