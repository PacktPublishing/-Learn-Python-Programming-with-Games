'''
Created on Jun 25, 2018
@author: Burkhard A. Meier
'''





import turtle
from random import randint
from time import time, sleep

from Section1.Video1_FINAL_Setup_Game_Area import create_game_screen, BORDER_WIDTH, GAME_AREA_START_X, GAME_AREA_START_Y
from Section1.Video2_FINAL_Create_Running_Track_Labels import create_track_with_labels
from Section1.Video3_FINAL_Section_labels import write_section_labels


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


# calculate run distances
FIRST_CURVE_DIST = 90

FIRST_STRAIGHT_DIST = BORDER_WIDTH - 120
FIRST_STRAIGHT_DIST_TOTAL = FIRST_CURVE_DIST + FIRST_STRAIGHT_DIST

SECOND_CURVE_DIST = 180
SECOND_CURVE_DIST_TOTAL = FIRST_STRAIGHT_DIST_TOTAL + SECOND_CURVE_DIST

SECOND_STRAIGHT_DIST = BORDER_WIDTH - 140
SECOND_STRAIGHT_DIST_TOTAL = SECOND_CURVE_DIST_TOTAL + SECOND_STRAIGHT_DIST

THIRD_CURVE_DIST = 180
THIRD_CURVE_DIST_TOTAL = SECOND_STRAIGHT_DIST_TOTAL + THIRD_CURVE_DIST

THIRD_STRAIGHT_DIST = BORDER_WIDTH - 180
THIRD_STRAIGHT_DIST_TOTAL = THIRD_CURVE_DIST_TOTAL + THIRD_STRAIGHT_DIST

FOURTH_CURVE_DIST = 180
FOURTH_CURVE_DIST_TOTAL = THIRD_STRAIGHT_DIST_TOTAL + FOURTH_CURVE_DIST

FOURTH_STRAIGHT_DIST = BORDER_WIDTH - 230
FOURTH_STRAIGHT_DIST_TOTAL = FOURTH_CURVE_DIST_TOTAL + FOURTH_STRAIGHT_DIST

FIFTH_CURVE_DIST = 180
FIFTH_CURVE_DIST_TOTAL = FOURTH_STRAIGHT_DIST_TOTAL + FIFTH_CURVE_DIST

FIFTH_STRAIGHT_DIST = BORDER_WIDTH - 290
FIFTH_STRAIGHT_DIST_TOTAL = FIFTH_CURVE_DIST_TOTAL + FIFTH_STRAIGHT_DIST

FINAL_CURVE_DIST = 90
FINAL_CURVE_DIST_TOTAL = FIFTH_STRAIGHT_DIST_TOTAL + FINAL_CURVE_DIST


def run_race(runner, run_distance, total_run_dist):
    total_run_dist += run_distance

    if total_run_dist <= FIRST_CURVE_DIST:                           # 90
        first_curve(runner, run_distance)

    elif (total_run_dist - run_distance) <= FIRST_CURVE_DIST:        # finish running the first curve         
        extra = total_run_dist - FIRST_CURVE_DIST
        first_curve(runner, run_distance - extra)
        run_straight(runner, extra)      
        
    elif (total_run_dist > FIRST_CURVE_DIST) and (total_run_dist <= FIRST_STRAIGHT_DIST_TOTAL):
        run_straight(runner, run_distance)

    elif (total_run_dist - run_distance) <= FIRST_STRAIGHT_DIST_TOTAL:          # finish running the first straight         
        extra = total_run_dist - FIRST_STRAIGHT_DIST_TOTAL
        run_straight(runner, run_distance - extra)
        second_curve(runner, extra)

    elif (total_run_dist > FIRST_STRAIGHT_DIST_TOTAL) and (total_run_dist <= SECOND_CURVE_DIST_TOTAL):
        second_curve(runner, run_distance)
        
    elif (total_run_dist - run_distance) <= SECOND_CURVE_DIST_TOTAL:            # finish running the second curve         
        extra = total_run_dist - SECOND_CURVE_DIST_TOTAL
        second_curve(runner, run_distance - extra)
        run_straight(runner, extra)  
        
    elif (total_run_dist > SECOND_CURVE_DIST_TOTAL) and (total_run_dist <= SECOND_STRAIGHT_DIST_TOTAL):
        run_straight(runner, run_distance)
        
    elif (total_run_dist - run_distance) <= SECOND_STRAIGHT_DIST_TOTAL:         # finish running the second straight         
        extra = total_run_dist - SECOND_STRAIGHT_DIST_TOTAL
        run_straight(runner, run_distance - extra)
        third_curve(runner, extra)
        
    elif (total_run_dist > SECOND_STRAIGHT_DIST_TOTAL) and (total_run_dist <= THIRD_CURVE_DIST_TOTAL):
        third_curve(runner, run_distance)
        
    elif (total_run_dist - run_distance) <= THIRD_CURVE_DIST_TOTAL:             # finish running the third curve         
        extra = total_run_dist - THIRD_CURVE_DIST_TOTAL
        third_curve(runner, run_distance - extra)
        run_straight(runner, extra)                  
        
    elif (total_run_dist > THIRD_CURVE_DIST_TOTAL) and (total_run_dist <= THIRD_STRAIGHT_DIST_TOTAL):
        run_straight(runner, run_distance)    

    elif (total_run_dist - run_distance) <= THIRD_STRAIGHT_DIST_TOTAL:          # finish running the third straight         
        extra = total_run_dist - THIRD_STRAIGHT_DIST_TOTAL
        run_straight(runner, run_distance - extra)
        fourth_curve(runner, extra)
        
    elif (total_run_dist > THIRD_STRAIGHT_DIST_TOTAL) and (total_run_dist <= FOURTH_CURVE_DIST_TOTAL):
        fourth_curve(runner, run_distance)      
        
    elif (total_run_dist - run_distance) <= FOURTH_CURVE_DIST_TOTAL:            # finish running the fourth curve         
        extra = total_run_dist - FOURTH_CURVE_DIST_TOTAL
        fourth_curve(runner, run_distance - extra)
        run_straight(runner, extra)                  
     
    elif (total_run_dist > FOURTH_CURVE_DIST_TOTAL) and (total_run_dist <= FOURTH_STRAIGHT_DIST_TOTAL):
        run_straight(runner, run_distance)   
        
    elif (total_run_dist - run_distance) <= FOURTH_STRAIGHT_DIST_TOTAL:         # finish running the fourth straight         
        extra = total_run_dist - FOURTH_STRAIGHT_DIST_TOTAL
        run_straight(runner, run_distance - extra)
        fifth_curve(runner, extra)

    elif (total_run_dist > FOURTH_STRAIGHT_DIST_TOTAL) and (total_run_dist <= FIFTH_CURVE_DIST_TOTAL):
        fifth_curve(runner, run_distance)          
         
    elif (total_run_dist - run_distance) <= FIFTH_CURVE_DIST_TOTAL:             # finish running the fifth curve         
        extra = total_run_dist - FIFTH_CURVE_DIST_TOTAL
        fifth_curve(runner, run_distance - extra)
        run_straight(runner, extra)   
     
    elif (total_run_dist > FIFTH_CURVE_DIST_TOTAL) and (total_run_dist <= FIFTH_STRAIGHT_DIST_TOTAL):
        run_straight(runner, run_distance) 
               
    elif (total_run_dist - run_distance) <= FIFTH_STRAIGHT_DIST_TOTAL:          # finish running the fifth straight         
        extra = total_run_dist - FIFTH_STRAIGHT_DIST_TOTAL
        run_straight(runner, run_distance - extra)
        final_curve(runner, extra)                       

    elif (total_run_dist > FIFTH_STRAIGHT_DIST_TOTAL) and (total_run_dist <= FINAL_CURVE_DIST_TOTAL):
        final_curve(runner, run_distance) 
        
    elif (total_run_dist - run_distance) <= FINAL_CURVE_DIST_TOTAL:             # finish running the final curve         
        extra = total_run_dist - FINAL_CURVE_DIST_TOTAL
        final_curve(runner, run_distance - extra)
        run_straight(runner, extra)
               
    else:
        print('Passed the Finish line')
        
    return total_run_dist


def create_place_runner(color, speed=1):
    runner = turtle.Turtle()
    runner.hideturtle()
    runner.setundobuffer(None)
    runner.color(color)
    runner.shape('turtle')
    runner.penup()
    runner.setheading(90)
    
    start_pos = GAME_AREA_START_X + 10                      # start 10 pixels into the x game area
    runner.setpos(start_pos, GAME_AREA_START_Y)
    runner.showturtle()
    runner.speed(speed)
    total_run_dist = 0

    return [runner, total_run_dist]


def running_game():
    # create turtle runners from a list of colors
    turtle_colors = ['Blue', 'Orange', 'Red']
    
    # list to hold created turtle runners
    turtle_runners = []
    
    # create runners and add to list
    for idx, turtle_runner in enumerate(turtle_colors):
        turtle_runners.append(create_place_runner(turtle_runner))
    
    # get the screen from any turtle runner
    screen = turtle_runners[0][0].getscreen()
    screen.title("{} Running Game".format(' ' * 108))
    
    winner = None
    total_run_dist = 0
    time_start = time()
    
    # Game loop
    while total_run_dist <= FINAL_CURVE_DIST_TOTAL:                                     # run until a runner crosses the finish line
        sleep(0.05)                                                                     # control the speed of the game
        for idx, turtle_runner in enumerate(turtle_runners):
            run_distance = randint(10, 30)                                              # create a random number to run
            current_runner = turtle_runners[idx]
            runner, total_run_dist = current_runner[0], current_runner[1]               # get runner and current total run
            current_runner[1] = run_race(runner, run_distance, total_run_dist)          # advance each runner and update its total
    
            if total_run_dist >= FINAL_CURVE_DIST_TOTAL:
                winner = current_runner[0].fillcolor()
                print('Runner {} won!'.format(winner))
                break
    
    time_finish = time()
    race_time = time_finish - time_start
    
    screen.title("{}FINISHED!!     Runner  *** {} *** won in {} secs!".format(' ' * 100, winner, int(race_time)))


if __name__ == '__main__':
    create_game_screen()           
    create_track_with_labels() 
    write_section_labels()
    running_game()
    turtle.done()  