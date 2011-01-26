#syntax erroe: invalid synstax needs fixing as of 1/25/11 (TIFF)  -- Works as of 1/26/11 (Michael Reed)
from Panda import *

#  A "periodic" function is one that repeats itself over and over
#  We've seen a lot already: sin, cos, and forever are all periodic.

# You can make your own periodic functions by using "fraction"

# What happens if you put "fraction(time)" into the location of a model?
# As in P3(time-2, 0, fraction(time))

# If you take any function and apply it to fraction(time) instead of time
# you get a periodic function.

# Make the following function periodic and use it as the position of a model:

def f(x):
    return x*x

# Try this function instead of f: t * (1-t) - what do you get?
# How can you make it go faster?  Bigger?

p= panda()

# How could you make it repeat the first 2 seconds of a
# function over and over?
start()