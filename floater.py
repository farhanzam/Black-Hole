# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage 


# from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random
import math


class Floater(Prey): 
    _color = "RED"
    _radius = 5
    _init_speed = 5
    
    def __init__(self, x, y):
        super(Floater, self).__init__(x, y, 10, 10, 0, self._init_speed)
        self.randomize_angle()
    
    def update(self, model):
        if random() < 0.3:
            # randomize speed
            speed_update = random() - 0.5
            new_speed = self.get_speed() + speed_update
            if new_speed < 3:
                self.set_speed(3)
            elif new_speed > 7:
                self.set_speed(7)
            else:
                self.set_speed(new_speed)
            # randomize angle
            angle_update = random() - 0.5
            new_angle = (self.get_angle() + angle_update) % (2 * math.pi)
            self.set_angle(new_angle)            
        self.move()
        self.wall_bounce()
         
    def display(self,canvas):
        canvas.create_oval(self._x - Floater._radius, self._y - Floater._radius,
                            self._x + Floater._radius, self._y + Floater._radius,
                            fill= Floater._color)
