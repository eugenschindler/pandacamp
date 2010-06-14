
from Panda import *
# Relative interpolation means that instead of knowing exactly where you want to go
# you know the way to go to get there.

# move is similar to at except that it tells you how far to go from the current place.

# Create an interpolant which moves a panda in a square path starting at (0,0,0).  Take .5 seconds to traverse each side.

p = 
t = slider(min = 0, max = 4, init = 0)

panda(position = interpolate(t, p))
start()