# naming issues again 1/25/11 TIFF
from Panda import *

# How can we tell if a point is inside a sphere?
# Inside a rectangular region?

# Use sliders to adjust the position of the small ball
x = slider(min = -3, max = 3, label = "x")
y = slider(min = -3, max = 3, label = "y")
z = slider(min = -3, max = 3, label = "z")

# The large ball is always at (0,0,0) and has a radius of 2
b1 = soccerBall(position = P3(0,0,0), size = 2) 
b2 = soccerBall(position = P3(x, y, z), size = 0.1)
# Show where the little ball is
text(format("Small ball is at: (%7.3f, %7.3f, %7.3f)",
          getX(b2.position), getY(b2.position), getZ(b2.position)))

# Use this function to determine whether two balls touch.

def insideSphere(ball1, ball2):
    return 

# What if a model isn't a sphere?  Try changing the big ball to a panda and
# see how well you can do.  How would you use a box instead of a sphere?

isInside = insideSphere(b2.position, b1.position, b1.size, b2.size)
# Use the world color to indicate whether the balls touch
world.color = choose(isInside, blue, red)
