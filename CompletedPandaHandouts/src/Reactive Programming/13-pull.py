from Panda import *

# Pull is like an infinite scroll wheel.
# While the mouse is down, the underlying 2-d
# coordinate drags with the mouse.
text(format("Left button pull: %s", lbuttonPull))
text(format("Right button pull: %s", rbuttonPull))

# Use lbuttonPull and rbuttonPull to adjust
# the location (assume model is on the X-Y plane)
# and heading / size of a model

# Next, use a key to select from one of two models
# and apply adjustments to each.  Note that you have
# to remember the initial value when switching models
# Add a top level "react" to keys to select the model
# A function which creates a controllable model is
# provided.  Add top level reactions to freeze one of
# the models and unfreeze the other on keys to select
# from the two pandas.

def addPull(m):  # Make a model "pullable"
    m.rpull = P2(0,0)  # This is the right pulling signal
    m.lpull = P2(0,0)  # This is the left pulling signal
    # The following adjusts position, HPR, and size according to the pulls
    m.position = P3(getX(m.lpull), 0, getY(m.lpull))
    m.HPR = P3(getX(m.rpull), 0, 0)
    m.size = 1+getY(m.rpull)

def freeze(m):
    # Hold the pulls where they are
    m.rpull = m.rpull.now()
    m.lpull = m.lpull.now()

def unfreeze(m):
    # Move the pulls with the button pulls
    # Why does this work??
    m.rpull = m.rpull.now() - rbuttonPull.now() + rbuttonPull
    m.lpull = m.lpull.now() - lbuttonPull.now() + lbuttonPull
panda(position = P3 (getX(lbuttonPull), 0, getY(lbuttonPull)), size = ((getY(rbuttonPull))))


start()