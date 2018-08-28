'''
Created on Jul 1, 2018
@author: Burkhard A. Meier
'''





import turtle
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

screen.update()                         # update the screen


if __name__ == '__main__':
    create_game_screen()
    create_track()
    turtle.done()
    
    
    
    
    