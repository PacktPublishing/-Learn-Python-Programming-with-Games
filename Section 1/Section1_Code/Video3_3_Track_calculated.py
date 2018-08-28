'''
Created on Jul 1, 2018
@author: Burkhard A. Meier
'''






import turtle
from time import sleep

from Section1.Video1_FINAL_Setup_Game_Area import create_game_screen, GAME_AREA_START_X, GAME_AREA_START_Y, BORDER_WIDTH
from Section1.Video2_FINAL_Create_Running_Track_Labels import create_track_with_labels

# calculate run distances
FIRST_CURVE_DIST = 90

FIRST_STRAIGHT_DIST = BORDER_WIDTH - 120

SECOND_CURVE_DIST = 180

SECOND_STRAIGHT_DIST = BORDER_WIDTH - 140

THIRD_CURVE_DIST = 180

THIRD_STRAIGHT_DIST = BORDER_WIDTH - 180

FOURTH_CURVE_DIST = 180

FOURTH_STRAIGHT_DIST = BORDER_WIDTH - 230

FIFTH_CURVE_DIST = 180

FIFTH_STRAIGHT_DIST = BORDER_WIDTH - 290

FINAL_CURVE_DIST = 90


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
    screen.tracer(1)                                        # refresh display screen after one frame

    first_curve(runner, run_dist=FIRST_CURVE_DIST)          # replace hard-coded literals with global variable constants
    sleep(0.5)
    run_straight(runner, run_dist=FIRST_STRAIGHT_DIST)
    sleep(0.5)
    second_curve(runner, run_dist=SECOND_CURVE_DIST)
    sleep(0.5)
    run_straight(runner, run_dist=SECOND_STRAIGHT_DIST)
    sleep(0.5)    
    third_curve(runner, run_dist=THIRD_CURVE_DIST)
    sleep(0.5)
    run_straight(runner, run_dist=THIRD_STRAIGHT_DIST)
    sleep(0.5) 
    fourth_curve(runner, run_dist=FOURTH_CURVE_DIST)
    sleep(0.5)    
    run_straight(runner, run_dist=FOURTH_STRAIGHT_DIST)
    sleep(0.5) 
    fifth_curve(runner, run_dist=FIFTH_CURVE_DIST)
    sleep(0.5)      
    run_straight(runner, run_dist=FIFTH_STRAIGHT_DIST)
    sleep(0.5) 
    final_curve(runner, run_dist=FINAL_CURVE_DIST)
    
            
    screen.update()


if __name__ == '__main__':
    create_game_screen()           
    create_track_with_labels() 
    run_track()
    
    turtle.done()  
    
    
    