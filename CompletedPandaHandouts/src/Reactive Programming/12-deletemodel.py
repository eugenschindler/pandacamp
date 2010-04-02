from Panda import *

# The timeIs event happens at given absolute time
# There is also a localTimeIs event
p = panda(position = P3(0,0,0))
def byebye(m, v):
    m.exit()

p.react(timeIs(1), byebye)
# Add a second model that exits at a different time
# Next, delete these models and respond to the lbp event by creating
# a model that moves left and exits after two seconds.
# Finally, alter this to use the current mouse position
# to set the panda direction.  Note that if you have a
# direction d that localTime*d moves you along that direction

# This is a 3-D direction based on the mouse position
dir = P3(getX(mouse), 0, getY(mouse))

start()