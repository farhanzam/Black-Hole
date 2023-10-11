import controller
import model   # Calling update in update_all passes a reference to this model

# Use the reference to this module to pass it to update methods

from ball       import  Ball
from blackhole  import  Black_Hole
from floater    import  Floater
from hunter     import  Hunter
from pulsator   import  Pulsator
from pickle import TRUE
from itertools import cycle
from special import Special

# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running = False
cycle_count = 0
all_objs = set()
sel_obj = None


#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running,cycle_count,all_objs
    running     = False
    cycle_count = 0
    all_objs       = set()


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#step just one update in the simulation
def step():
    global running, cycle_count
    running = False
    cycle_count += 1
    for b in set(all_objs):
        b.update(model)
    display_all()
    
    
    


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global sel_obj
    sel_obj = kind


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    global sel_obj
    if sel_obj == 'Ball':
        add(Ball(x, y))
    if sel_obj == 'Floater':
        add(Floater(x, y))
    if sel_obj == 'Black_Hole':
        add(Black_Hole(x, y))
    if sel_obj == 'Pulsator':
        add(Pulsator(x, y))
    if sel_obj == 'Hunter':
        add(Hunter(x, y))
    if sel_obj == 'special':
        add(Special(x, y))
    if sel_obj == 'Remove':
        remove((x, y))


#add simulton s to the simulation
def add(s):
    global all_objs
    all_objs.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    global all_objs
    to_remove = []
    for obj in all_objs:
        if obj.contains(s):
            to_remove.append(obj)
    for obj in to_remove:
        all_objs.remove(obj)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    return [obj for obj in all_objs if p(obj)]


#Simulation: for each simulton in the model, call its update, passing it model
#Loop over a set containing all the simultons; do not use type or isinstance:
#  let each simulton's update do the needed work, without this function knowing
#  what kinds of simultons are in the simulation
def update_all():
    global cycle_count
    if running:
        cycle_count += 1
        for b in set(all_objs):
            b.update(model)

#Animation: clear then canvas; for each simulton in the model, call display
#  (a) delete all simultons on the canvas; (b) call display on all simultons
#  being simulated, adding back each to the canvas, often in a new location;
#  (c) update the label defined in the controller showing progress 
#Loop over a set containing all the simultons; do not use type or isinstance:
#  let each simulton's display do the needed work, without this function knowing
#  what kinds of simultons are in the simulation
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for b in all_objs:
        b.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(len(all_objs))+" all_objs/"+str(cycle_count)+" cycles")
