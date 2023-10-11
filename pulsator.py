# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions 

from blackhole import Black_Hole


class Pulsator(Black_Hole): 
    _hunger_time = 30
    
    def __init__(self, x, y):
        super(Pulsator, self).__init__(x, y)
        self.cycle_since_eating = 0

    def update(self, model):
        if len(super(Pulsator, self).update(model)) > 0:
            self.cycle_since_eating = 0
            self.change_dimension(1, 1)
            self.radius += 0.5
        else:
            self.cycle_since_eating += 1
            if self.cycle_since_eating > self._hunger_time:
                self.change_dimension(-1, -1)
                self.radius -= 0.5
                self.cycle_since_eating = 0
            x, y = self.get_dimension()
            if x <= 0 and y <= 0:
                model.all_objs.remove(self)
                
                
    def a(self): print("p")
        
    
    
