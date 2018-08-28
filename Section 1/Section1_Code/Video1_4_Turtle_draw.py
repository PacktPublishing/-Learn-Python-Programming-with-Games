'''
Created on Jul 1, 2018
@author: Burkhard A. Meier
'''





# module imports
import turtle


our_turtle = turtle.Turtle()        # save turtle instance in local variable

our_turtle.color('blue')            # set color to blue

for _draw in range(4):
    our_turtle.forward(50)          # move forward 50 pixels
    our_turtle.left(90)             # turn left 90 degrees

turtle.done()                       # keep the window up





















