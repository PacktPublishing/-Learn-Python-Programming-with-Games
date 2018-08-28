'''
Created on Jun 25, 2018
@author: Burkhard A. Meier
'''






import turtle
from time import sleep

from Section1.Video1_FINAL_Setup_Game_Area import create_game_screen, GAME_AREA_START_X, GAME_AREA_START_Y, BORDER_WIDTH
from Section1.Video2_FINAL_Create_Running_Track_Labels import create_track_with_labels


screen = turtle.Screen()


# running sections
def run_straight(runner, run_dist):   
    runner.fd(run_dist)
    
def first_curve(runner, run_dist):   
    runner.circle(-50, run_dist)            # clockwise
    
def second_curve(runner, run_dist):         
    runner.circle(50, run_dist)             # counter-clockwise

def third_curve(runner, run_dist): 
    runner.circle(-50, run_dist)            # clockwise
    
def fourth_curve(runner, run_dist):         
    runner.circle(50, run_dist)             # counter-clockwise
    
def fifth_curve(runner, run_dist): 
    runner.circle(-50, run_dist)            # clockwise
    
def final_curve(runner, run_dist):         
    runner.circle(50, run_dist)             # counter-clockwise


def run_track():
    # use the code that draws the track to run the track
    runner = turtle.Turtle()
    runner.penup()
    runner.color('blue', 'red')
    runner.pensize(5)
    runner.shape('turtle')
    runner.setheading(90)
    
    # position runner at start of track
    start_pos = GAME_AREA_START_X + 10                      # start 10 pixels into the x game area
    runner.setpos(start_pos, GAME_AREA_START_Y)
    runner.pendown()
    
    # run the track
    sleep(0.5)
    screen.tracer(1)

    # use track sections
    first_curve(runner, run_dist=90)                        # replace the draw_running_track() call
    sleep(0.5)
    run_straight(runner, run_dist=BORDER_WIDTH - 120)
    sleep(0.5)
    second_curve(runner, run_dist=180)
    sleep(0.5)
    run_straight(runner, run_dist=BORDER_WIDTH - 140)
    sleep(0.5)    
    third_curve(runner, run_dist=180)
    sleep(0.5)
    run_straight(runner, run_dist=BORDER_WIDTH - 180)
    sleep(0.5) 
    fourth_curve(runner, run_dist=180)
    sleep(0.5)    
    run_straight(runner, run_dist=BORDER_WIDTH - 230)
    sleep(0.5) 
    fifth_curve(runner, run_dist=180)
    sleep(0.5)      
    run_straight(runner, run_dist=BORDER_WIDTH - 290)
    sleep(0.5) 
    final_curve(runner, run_dist=90)
    
            
    screen.update()


if __name__ == '__main__':
    create_game_screen()           
    create_track_with_labels() 
    run_track()
    
    turtle.done()  
    
    
    