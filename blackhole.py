# A Black_Hole is derived from a Simulton base; it updates by finding+removing
#   any objects (derived from a Prey base) whose center is crosses inside its
#   radius (and returns a set of all eaten simultons); it displays as a black
#   circle with a radius of 10 (e.g., a width/height 20).
# Calling get_dimension for the width/height (for containment and displaying)'
#   will facilitate inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):  
    _color = "BLACK"
    _init_radius = 10
    
    def __init__(self, x, y):
        Simulton.__init__(self, 
                          x, 
                          y, 
                          2 * Black_Hole._init_radius, 
                          2 * Black_Hole._init_radius)
        self.radius = Black_Hole._init_radius 
        
    def __contains__(self, xy):
        return self.distance(xy) <= self.radius
    
    def update(self, model):
        def predicate(o):
            return isinstance(o, Prey) and self.__contains__((o._x, o._y))
        to_eat = model.find(predicate)
        for o in to_eat:
            model.all_objs.remove(o)
        return to_eat
         
    def display(self,canvas):
        w, h = self.get_dimension()
        canvas.create_oval(self._x - (w / 2), self._y - (h / 2),
                            self._x + (w / 2), self._y + (h / 2),
                            fill= self._color)
