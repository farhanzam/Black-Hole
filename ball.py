# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10). 
from prey import Prey
import math

class Ball(Prey):
    _color = "BLUE"
    _radius = 5
    _speed = 5
    
    def __init__(self, x, y):
        super(Ball, self).__init__(x, y, 10, 10, 0, self._speed)
        self.randomize_angle()
    
    def update(self, model):
        self.move()
        self.wall_bounce()
         
    def display(self,canvas):
        canvas.create_oval(self._x - Ball._radius, self._y - Ball._radius,
                            self._x + Ball._radius, self._y + Ball._radius,
                            fill=Ball._color)

