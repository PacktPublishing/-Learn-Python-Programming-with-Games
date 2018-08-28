'''
Created on Jun 25, 2018
@author: Burkhard A. Meier
'''




import turtle
from time import sleep

from Section1.Video1_FINAL_Setup_Game_Area import create_game_screen, BORDER_WIDTH, BORDER_HEIGHT, GAME_AREA_START_X, GAME_AREA_START_Y


screen = turtle.Screen()        
screen.tracer(2)           # only each n-th (2) regular screen update is really performed


def draw_running_track(draw_turtle, slowtime=0):
    draw_turtle.setheading(90)
    
    sleep(slowtime)
    draw_turtle.circle(-50, 90)                # clockwise, 90 degrees (quarter circle)
    sleep(slowtime)
    draw_turtle.fd(BORDER_WIDTH - 120)
    
    sleep(slowtime)
    draw_turtle.circle(50, 180)                # counter-clockwise, 180 degrees (half circle)
    sleep(slowtime)
    draw_turtle.fd(BORDER_WIDTH - 140)
    
    sleep(slowtime)
    draw_turtle.circle(-50, 180)     
    sleep(slowtime)   
    draw_turtle.fd(BORDER_WIDTH - 180)
    
    sleep(slowtime)
    draw_turtle.circle(50, 180)
    sleep(slowtime)
    draw_turtle.fd(BORDER_WIDTH - 230)

    sleep(slowtime)
    draw_turtle.circle(-50, 180)  
    sleep(slowtime)           
    draw_turtle.fd(BORDER_WIDTH - 290)
    
    sleep(slowtime)
    draw_turtle.circle(50, 90)


def create_running_track():
    track_turtle = turtle.Turtle()
    track_turtle.hideturtle()
    track_turtle.setundobuffer(None)
    track_turtle.speed(0)
    track_turtle.color('yellow', 'brown')
      
    track_turtle.penup()

    start_pos = GAME_AREA_START_X + 10                      # start 10 pixels into the x game area
    track_turtle.setpos(start_pos, GAME_AREA_START_Y)
    track_turtle.pendown()
    track_turtle.pensize(3)

    draw_running_track(track_turtle)                        # now draw the running track
    track_turtle.penup()


def write_labels():
    start_pen = turtle.Turtle()             # create a new turtle to write with
    start_pen.speed(0)             
    start_pen.color('white')
    start_pen.penup()             
    start_pen.setpos(GAME_AREA_START_X -25, GAME_AREA_START_Y -25)  
    start_string = 'START'
    start_pen.write(start_string, align='left', font=('Arial', 14, 'bold'))
    start_pen.hideturtle()
    
    finish_pen = turtle.Turtle()            # create a new turtle to write with
    finish_pen.speed(0)             
    finish_pen.color('red')
    finish_pen.penup()             
    finish_pen.setpos((BORDER_WIDTH // 2) -140, BORDER_HEIGHT // 2)  
    finish_string = 'FINISH'
    finish_pen.write(finish_string, align='left', font=('Arial', 14, 'bold'))
    finish_pen.hideturtle()


def create_track_with_labels():
    create_running_track()
    write_labels()


if __name__ == '__main__':
    create_game_screen()      
    create_track_with_labels()
    turtle.done()                   
    
    
    