from Panda import *

# One-time reactions
# Time and localtime
# Clock
# One-time reactions


def goto0(model, value):
    model.position = P3(0,0,0)  # Put the model at (0,0,0) when reacting
    model.hpr = HPR(0,0,0)

def rise(model, value):     # Rise up from (0,0,0)
    model.position = P3(0,0,localTime/4)
    model.hpr = HPR(localTime, 0, 0)

p = panda()  # Make a panda
p.react(lbp, goto0)  # Tell it to go to P3(0,0,0) when the left mouse button is pressed
p.react(rbp, rise) 

start()