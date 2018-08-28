'''
Created on Aug 14, 2018
@author: Burkhard A. Meier
'''


import tkinter as tk
from PIL import Image, ImageTk


class CanvasAndCar():
    def __init__(self, win):
        self.canvas = tk.Canvas(win, width=700, height=500)     # create a tkinter canvas
        self.canvas.pack()                                      # use the pack() manager
        self.canvas.update()                                    # call update() or winfo_ won't work
        self.car_pos_x = self.canvas.winfo_width() // 2         # center of canvas
        self.car_pos_y = self.canvas.winfo_height() // 2   
        
        self.img_file = 'car.png'                               # our .png image file located in the same folder as this .py file     
        self.place_car()                                        # call the method to position the car

    def place_car(self):
        image = Image.open(self.img_file)                       # open the image
        self.car_image = ImageTk.PhotoImage(image)              # pass the image into PhotoImage. Use self.car_image or image might not show
        self.car_canvas = self.canvas.create_image(self.car_pos_x, self.car_pos_y,
                                                   image=self.car_image)         
        

win = tk.Tk()                       # create a tkinter window
car_game = CanvasAndCar(win)        # create CanvasAndCar and save class instance in variable or image might not show
win.mainloop()                      # start the tkinter main gui event loop







