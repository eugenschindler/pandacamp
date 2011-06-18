
from Panda import *

# There are two ways to repeat an interpolant:
# repeat(3, i) would repeat an interpolant i 3 times.
# forever(i) repeats it forever
# Write an interpolant that makes the panda move in a stairstep pattern for three steps.
# Then add a move somewhere else and do the stairstep again.

t = slider(max = 10, init = 0)

stairstep = # Put a stairstep here


panda(position = interpolate(t, ))  # Repeat the stairstep here

# Write an interpolant for numbers that goes back and forth between -.2 and .2 forever.
# Use this to make a panda go up and down by setting its pitch

# wiggle =
# panda(position = P3(-2, 0, 0), hpr = HPR(0, interpolate(time, wiggle),0))
start()

