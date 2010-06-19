from Panda import *
# time is something that is always going as the program runs:

def goto0(model, value):
    model.position = P3(0,0,0)  # Put the model at (0,0,0) when reacting

def rise(model, value):     # Rise up from (0,0,0)
    model.position = P3(0,0,time/4)

p = panda()  # Make a panda
p.react(lbp, goto0)  # Tell it to go to P3(0,0,0) when the left mouse button is pressed
p.react(rbp, rise)  # Tell it rise when the right mouse button is pressed

# What if you want to restart at 0 when you press the right button?
# Change time to localTime in rise and see what happens.

# Instead of changing the position, use time to change the heading.  How does localTime differ from time in this case?

start()