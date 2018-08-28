'''
Created on Jun 25, 2018
@author: Burkhard A. Meier
'''






import turtle
from time import sleep

from Section1.Video1_FINAL_Setup_Game_Area import create_game_screen, GAME_AREA_START_X, GAME_AREA_START_Y
from Section1.Video2_FINAL_Create_Running_Track_Labels import create_track_with_labels, draw_running_track


def run_track():
    # use the code that draws the track to run the track
    runner = turtle.Turtle()
    runner.penup()
    runner.color('blue', 'red')                             # pencolor, fillcolor
    runner.pensize(5)
    runner.shape('turtle')
    
    # position runner at start of track
    start_pos = GAME_AREA_START_X + 10                      # start 10 pixels into the x game area
    runner.setpos(start_pos, GAME_AREA_START_Y)
    runner.pendown()
    
    # run the track
    sleep(1)
    draw_running_track(runner, slowtime=1)


if __name__ == '__main__':
    create_game_screen()           
    create_track_with_labels() 
    run_track()
    
    turtle.done()  
    
    




    