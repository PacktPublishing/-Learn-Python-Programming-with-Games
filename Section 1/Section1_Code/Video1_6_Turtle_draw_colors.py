'''
Created on Jul 1, 2018
@author: Burkhard A. Meier
'''





# module imports
import turtle


our_turtle = turtle.Turtle()        # save turtle instance in local variable

our_turtle.color('blue')            # set color to blue
our_turtle.hideturtle()             # hide the turtle

for _draw in range(20):
    our_turtle.forward(50)          # move forward 50 pixels
    our_turtle.left(85)             # turn left 85 degrees

our_turtle.color('red')             # set color to red
our_turtle.penup()                  # stop drawing
our_turtle.forward(100)             # move the turtle pen
our_turtle.pendown()                # start drawing

for _draw in range(50):
    our_turtle.forward(40)          # move forward 40 pixels
    our_turtle.left(100)            # turn left 100 degrees

turtle.done()                       # keep the window up




















