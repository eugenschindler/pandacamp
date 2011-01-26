#works but could be combined with something else 1/25/11 (TIFF)
from Panda import *

# Write a function named f that creates a panda.  The location of the panda is p, an argument to f.

def f(p):
    panda(position = p, hpr = HPR(time, 0, 0))
    panda(position = p + P3(0,0,1), hpr = HPR(-time, 0, 0))

# Change f to create two different pandas, one above the other.
# Make the pandas move in some way.

f(P3(1,0,0))
f(P3(-1, 0, 0))
f(P3(0,0,1))

start()