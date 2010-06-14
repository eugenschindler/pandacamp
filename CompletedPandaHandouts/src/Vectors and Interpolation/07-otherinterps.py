# Vectors and interpolation/07-otherinterps.py
from Panda import *

# You can interpolate colors as well as points in space.
# Create an interpolant that goes between three different colors and set the
# background color of the world using this - interpolate at the current time.

colori = forever(at(red) + to(.4, white) + to(.2, cyan))

world.color = interpolate(time, colori)

# Create a different color interpolant that goes between three different colors.
# Loop forever on this interpolant followed by its reverse (use "reverse").
# Place a panda in the scene colored by this.

colori = at(green) + to(.3, blue) + to(.4, aquamarine)


# Use this same scheme to interpolate between the following three HPRs:

pose1 = HPR(0,0,0)
pose2 = HPR(pi/2, 0, 0)
pose3 = HPR(pi/2, 0, pi)

posei = at(pose1) + to(1, pose2) + to(.5, pose3)

panda(color = interpolate(time, forever(colori + reverse(colori))), hpr = interpolate(time, forever(posei + reverse(posei))))
start()