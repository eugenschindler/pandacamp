# Vectors and interpolation/07-otherinterps.py
from Panda import *

# You can interpolate colors as well as points in space.
# Create an interpolant that goes between three different colors and set the
# background color of the world using this - interpolate at the current time.

wcolori =

world.color = interpolate(time, wcolori)

# Create a different color interpolant that goes between three different colors.
# Loop forever on this interpolant followed by its reverse (use "reverse").
# Place a panda in the scene colored by this.

# pcolori =


# Use this same scheme to interpolate between the following three HPRs:

pose1 = HPR(0,0,0)
pose2 = HPR(pi/2, 0, 0)
pose3 = HPR(pi/2, 0, pi)

#posei = # Interpolate between the three poses above
#
#panda(color = interpolate(time, )),   # Put the interpolant and reverses here
#      hpr = interpolate(time, ))
start()