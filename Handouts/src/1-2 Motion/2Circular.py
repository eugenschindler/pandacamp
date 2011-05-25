from Panda import *

# Sine and cosine are functions used in math that connect all the
# coordinates on a cicle.

# Try this: Manipulate the functions by adding, subtracting, and multipling
# the t variables and the sine and cosine functions. Don.t forget to try
# decimals.

pos = P3(sin(time), 0, cos(time))
pos2 = P3(sin(3*time), 0, cos(3*time))
panda(position = pos)

# Try this: multiply, add and subtract the pos and pos2 together.  What is
# happening?


start()