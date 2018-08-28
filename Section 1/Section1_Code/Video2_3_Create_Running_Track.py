'''
Created on Jun 25, 2018
@author: Burkhard A. Meier
'''




import turtle

from Section1.Video1_FINAL_Setup_Game_Area import create_game_screen, BORDER_WIDTH, GAME_AREA_START_X, GAME_AREA_START_Y


screen = turtle.Screen()        
screen.tracer(2)           # only each n-th (2) regular screen update is really performed


def draw_running_track(draw_turtle):
    draw_turtle.setheading(90)

    draw_turtle.circle(-50, 90)                # clockwise, 90 degrees (quarter circle)
    draw_turtle.fd(BORDER_WIDTH - 120)         # fd is short for forward

    draw_turtle.circle(50, 180)                # counter-clockwise, 180 degrees (half circle)
    draw_turtle.fd(BORDER_WIDTH - 140)

    draw_turtle.circle(-50, 180)        
    draw_turtle.fd(BORDER_WIDTH - 180)

    draw_turtle.circle(50, 180)
    draw_turtle.fd(BORDER_WIDTH - 230)

    draw_turtle.circle(-50, 180)             
    draw_turtle.fd(BORDER_WIDTH - 290)

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


if __name__ == '__main__':
    create_game_screen()      
    create_running_track()
    turtle.done()                   
    
    
    