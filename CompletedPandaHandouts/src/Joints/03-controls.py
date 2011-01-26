#works 1/25/11 (TIFF)
from Panda import *

camera.position = P3(0, -20, .5)
world.color = black
ambientLight(color = gray)
directionalLight(color = white, hpr = HPR(2,.5, 0))

# If a model has lots of joints, it's a pain to have to control each one
# separately.  Every model has a special input called "control".  A control is

# The "control" function takes a name and a value - the name is one of the
# model attributes like position, size, or a joint name.  The value is what
# you want to set that attribute to.

# Use + to combine controls.  If the same name is defined in two different
# controls, the leftmost one is chosen.

# This control defines a position and hpr.  Add controls for size and color
c = control("position", P3(time, 0, 0)) + control("hpr", HPR(time, 0, 0))


p = panda()
p.size=time
p.control = c
# Once this is done, create a control signal that is a copy of the one above
# except that the position is (1,0,0) over.  You need 

start()