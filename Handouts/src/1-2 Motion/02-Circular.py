from Panda import *

# Sine and cosine are functions used in math that connect all the
# coordinates on a cicle.
# Watch the panda move and try to figure out the initial value, amplitude, and
# the period.  Now change the sin to cos and try to figure out the same things.
# Next add a cos or sin to the z direction. Figure out the center of the circle,
# and try to get the panda to move faster.

# Try this: Manipulate the functions by adding, subtracting, and multipling
# the time variables and the sine and cosine functions. Don.t forget to try
# decimals.

pos = P3(sin(time), 0, 0)
p = panda(position = pos)
text(p.position)

start()