# This module defines a vegan class of Hunters, who actively avoid eating prey.
#     But sometimes, they end up breaking this commitment. If they do eat any 
#     prey, they turn green to denote turning "sick". They revert to yellow if
#     they start shrinking again.

from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Special(Pulsator, Mobile_Simulton):
    _speed = 5
    _hunt_dist = 200
    
    def __init__(self, x, y):
        Pulsator.__init__(self, x, y)
        Mobile_Simulton.__init__(self, x, y, 2 * self._init_radius, 
                                 2 * self._init_radius, 0, self._speed)
        self._color = "YELLOW"
        self.randomize_angle()

    def update(self, model):
        self.move()
        self.wall_bounce()
        xsize = self.get_dimension()[0]
        Pulsator.update(self, model)
        new_xsize = self.get_dimension()[0]
        if new_xsize > xsize: # it has sinned (ate something)
            self._color = "GREEN"
        if new_xsize < xsize: # it has atoned for its sins (not eaten in the last 30 cycles)
            self._color = "YELLOW"
            
        
        # find closest prey, change direction to angle toward it
        def predicate(o):
            return isinstance(o, Prey) and self.distance(o.get_location()) <= Special._hunt_dist
        potential_prey = model.find(predicate)
        if len(potential_prey) == 0:  # if no prey are within 200, exit 
            return
        prey = sorted(potential_prey, key=lambda p: self.distance(p.get_location()))[0]
        p_x, p_y = prey.get_location()
        h_x, h_y = self.get_location()
        x_dif, y_dif = p_x - h_x, p_y - h_y
        hunt_angle = atan2(x_dif, y_dif)
        self.set_angle(hunt_angle)
            
