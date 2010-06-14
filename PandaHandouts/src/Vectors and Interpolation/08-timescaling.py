# Vectors and interpolation/08-timescaling.py
from Panda import *

# This path is a square
path = at(P3(-1.5,0,-1.5)) + forever(move(1, P3(3, 0, 0)) + move(1, P3(0,0,3)) + move(1, P3(-3, 0, 0)) + move(1, P3(0,0,-3)))
# How long does this path take to traverse?
# This is a function definition - it launches a panda using t as the time base,
# p0 as the initial position, and painted the given color.
def go(t,  color):
    panda(position = interpolate(t, path), color = color)
    
go(time, red)
# Create a second panda that follow the same path at the opposite side of the square, ahead of the original
# Create another panda that goes twice as fast
# Create a panda that is exactly 1 second behind the first one
# Can you make one that speeds up more and more?


start()
