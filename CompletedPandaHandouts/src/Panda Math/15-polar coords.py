#INCOMPLETE 1/25/11 TIFF
from Panda import *

# The following allows you to specify a distance and angle using sliders
dist = slider(min = 0, max = 3, label = "dist")
ang = slider(min = 0, max = 2*pi, label = "angle")
text(format("Distance: %f", dist))
text(format("Angle: %f", ang))
# Use P2Polar to make a two dimensional point
point =
# The getX and getY functions extract the X and Y coordinates from a point -
# use these to turn a 2 dimensional point into a 3-D point
p = jeep(position = P3(   )
# Remove the sliders and use "time" to control the distance
# or angle.  What happens when:
## The angle is constant and the distance varies?
## The distance is constant and the angle varies?
## Both the distance and angle increase with time

# Cylindrical coordinates are just polar coords with a
# z tacked on at the end.
# P3C(dist, ang, z) is a point in which x and y are
# computed from dist and ang while z is the same.
# Use P3C to create a trajectory where the dist is constant
# while ang and z increase with time.
start()