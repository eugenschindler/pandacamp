from Panda import *

# Simple recursion (counting)

# Define a function to make a line of pandas of a given length
# You need the following:
#   A parameter "number" which tells you how many more panda to make
#   A parameter "place" which tells you where the last panda was placed
# Inside the function, you need to use "if" to determine whether
# we need more pandas.


def col(t):
    return interpolate(t, forever(at(red) + to(.5, purple) + to(.5, blue) + to(1, white) + to(2, color(.2,.4, .8))+ to(1, red)))
def unboom(p, v):
  p.stop()
def explode(p, v):
    w = warpSpeed(color = p.color.now(), position = p.position.now(), birthRate = 0.05, litterSize = 2)
    w.react(localTimeIs(.2), unboom)
    p.exit()

# This function puts a line of panda
def pandaLine(number, place):
    if number > 0:
        p = panda(position=P3(place,0,0),hpr=HPR(0,time*4+place/5.0,0),color=col(time+place/2.5))
        p.react(timeIs(50 + place/10.0), explode)
        pandaLine(number-1,place+1)
world.color = green
        # Place a panda at P3(place, 0, 0)
        # Continue the panda line by calling pandaLine
        # What should the new value of place be?
        # What should the new value of number be?

# Make a line of 10 pandas that starts at P3(-4,0,0)
pandaLine(40,-20)
camera.position = P3(0, -4-time, .5)
# Can you make a line of 20 pandas?
# Can you put two pandas in a stack at each position?
# Can you have the roll change as well as the position?
# Can you make the line rise?

start()