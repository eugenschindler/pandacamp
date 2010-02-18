


from Panda import *

# There are two more interpolation functions to know:
#   forever(i) - repeats an interpolant forever
#   reverse(i) - makes an interpolant go backwards

# Create a function that combines an interpolant with its reverse - use this
# to build the interpolants below
def rev(i):
   return  # Make an interpolant with i followed by it's reverse

# You can interpolate numbers, colors, points, and HPRs.
# Create an interpolant that switches back and forth between two colors
# every second and use this as the world color, interpolating by "time".  Use
# forever to make this repeat indefinitely

world.color = interpolate(time, 

# Place a model on the scene whose size is defined by an interpolant as follows:
# Start at 1 and hold this for 1 second
# Abruptly change to 2 and hold for .2 seconds
# Increase to 3 for .5 seconds
# Mirror and repeat forever

s = 
panda(position = P3(0,0,0), size = interpolate(time, s))

# Finally, two other models that do something with their HPR.  Use the same
# interpolant on each one but negate one of them for a mirroring effect.

h = 
h1 = interpolate(time, h)

panda(position = P3(2, 0, 0), hpr = h1)
panda(position = P3(-2, 0, 0), hpr = -h1)
start()