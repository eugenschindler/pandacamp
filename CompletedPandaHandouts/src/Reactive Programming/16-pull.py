from Panda import *

# Pull is like an infinite scroll wheel.
# While the mouse is down, the underlying 2-d
# coordinate drags with the mouse.
text(format("Left button pull: %s", lbuttonPull))


# Run this code to observe the value of the pull

def addPull(m):  # Make a model "pullable"
    m.pull = P2(0,0)  # This signal tracks the pulling on an individual model
    m.size = 1+getY(m.pull)   # Use this to set the size
    m.react(leftClick(m), unfreeze)  # When clicking on the model, unfreeze
    m.react(lbr, freeze)     # When the mouse goes back up freeze again

def freeze(m, v):
    m.pull = m.pull.now()   # Remember the current value

def unfreeze(m, v):
    m.pull = m.pull.now() - lbuttonPull.now() + lbuttonPull  #

# Create a few models and make each one of them adjustable
p = panda()
addPull(p)
j = jeep(position = P3(2, 0, 0))
addPull(j)


start()