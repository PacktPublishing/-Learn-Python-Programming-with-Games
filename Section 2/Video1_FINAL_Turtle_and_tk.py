'''
Created on Aug 14, 2018
@author: Burkhard A. Meier
'''


import tkinter as tk
from PIL import Image, ImageTk
import turtle


# define screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

GAME_AREA_START_X = -((SCREEN_WIDTH // 2) -50)
GAME_AREA_START_Y = -((SCREEN_HEIGHT // 2) -50)

BORDER_WIDTH = SCREEN_WIDTH -100
BORDER_HEIGHT = SCREEN_HEIGHT -100


class GameArea(turtle.RawTurtle):               # inherent/extend RawTurtle
    def __init__(self, tk_canvas):
        super().__init__(tk_canvas)             # initialize the super class (RawTurtle)
        self.tk_canvas = tk_canvas
        self.hideturtle()                       # hide the RawTurtle
        screen = self.getscreen()         
        screen.bgcolor('gray')
        screen.tracer(2)                        # delay drawing by two frames
        self.draw_game_area()
        screen.update()                         # update the screen

    def draw_game_area(self):
        area_turtle = turtle.RawTurtle(self.tk_canvas)
        area_turtle.setundobuffer(None)                             # no undo buffer to speed up the drawing
        area_turtle.hideturtle()
        area_turtle.speed(0)                                        # 0 is the fastest
        area_turtle.color('black', 'green')                         # pencolor, fillcolor
        area_turtle.penup()                                         # don't draw while moving into position
        area_turtle.setpos(GAME_AREA_START_X, GAME_AREA_START_Y)    # left bottom
        area_turtle.pendown()                                       # now start drawing
        area_turtle.pensize(4)
        
        area_turtle.begin_fill()                    # start filling in the game area
        for _border in range(2):
            area_turtle.fd(BORDER_WIDTH)
            area_turtle.lt(90)
            area_turtle.fd(BORDER_HEIGHT)
            area_turtle.lt(90)
        area_turtle.end_fill()


class CanvasAndCar():
    def __init__(self, win):
        self.canvas = tk.Canvas(win, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)      # create a tkinter canvas
        self.canvas.pack()                                                          # use the pack() manager
        
    def after_turtle_game_area_creation(self):
        self.car_pos_x = 0                          # center of canvas
        self.car_pos_y = 0                          # turtle screen coords are 0,0 in center  

        self.img_file = 'car.png'                               # our .png image file located in the same folder as this .py file     
        self.place_car()                                        # call the method to position the car

    def place_car(self):
        image = Image.open(self.img_file)                       # open the image
        self.car_image = ImageTk.PhotoImage(image)              # pass the image into PhotoImage. Use self.car_image or image might not show
        self.car_canvas = self.canvas.create_image(self.car_pos_x, self.car_pos_y,
                                                   image=self.car_image)         
        

win = tk.Tk()                                   # create a tkinter window
car_game = CanvasAndCar(win)                    # create CanvasAndCar and save class instance in variable or image might not show
game_area = GameArea(car_game.canvas)           # create class instance, pass in canvas
car_game.after_turtle_game_area_creation()
win.mainloop()                                  # start the tkinter main gui event loop







