# A Hunter class is derived from a Pulsator and then Mobile_Simulton base.
#   It inherits updating+displaying from Pusator/Mobile_Simulton: it pursues
#   any close prey, or moves in a straight line (see Mobile_Simultion).

from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator, Mobile_Simulton):
    _speed = 5
    _hunt_dist = 200
    
    def __init__(self, x, y):
        Pulsator.__init__(self, x, y)
        Mobile_Simulton.__init__(self, x, y, 2 * self._init_radius, 
                                 2 * self._init_radius, 0, self._speed)
        self.randomize_angle()
        
    def update(self, model):
        self.move()
        self.wall_bounce()
        Pulsator.update(self, model)
        # find closest prey, change direction to angle toward it
        def predicate(o):
            return isinstance(o, Prey) and self.distance(o.get_location()) <= Hunter._hunt_dist
        potential_prey = model.find(predicate)
        if len(potential_prey) == 0:  # if no prey are within 200, exit 
            return
        prey = sorted(potential_prey, key=lambda p: self.distance(p.get_location()))[0]
        p_x, p_y = prey.get_location()
        h_x, h_y = self.get_location()
        x_dif, y_dif = p_x - h_x, p_y - h_y
        hunt_angle = atan2(y_dif, x_dif)
        self.set_angle(hunt_angle)
