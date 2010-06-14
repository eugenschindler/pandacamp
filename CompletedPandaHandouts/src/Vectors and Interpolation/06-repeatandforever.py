
from Panda import *

# There are two ways to repeat an interpolant:
# repeat(3, i) would repeat an interpolant i 3 times.
# cycle(i) repeats it forever
# Rewrite the previous example using repeat.

t = slider(max = 10, init = 0)

i1 = move(.5, P3(.3, 0, 0)) + move(.5, P3(0, 0, .3))

i2 = at(P3(0,0,0)) + repeat(3, i1) + move(1, P3(0,-2,0)) + repeat(3, i1)

panda(position = interpolate(t, i2))

# Write an interpolant for numbers that goes back and forth between -.2 and .2 forever.
# Use this to make a panda go up and down by setting its pitch

panda(position = P3(-2, 0, 0), hpr = HPR(0, interpolate(time, at(-.2) + forever(move(.3, .4) + move(.3, -.4))),0))
start()

