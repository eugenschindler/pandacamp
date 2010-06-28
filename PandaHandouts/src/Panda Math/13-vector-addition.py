from Panda import *

# We use P3 as both a place and as a vector.  A vector is an "arrow" - something
# that moves you from one place to another.
# When you add or subtract P3s you're using vectors.
# There's nothing special about vector addition - it just adds corresponding
# elements of each vector.

# Here's a trajectory centered at P3(1, 1, -.5):
def f(t):
    return P3(cos(t) + 1, 1, sin(t) - 0.5)

# Change this to use vector addition and the unit circle to get the same
# thing

def unitcircle(t):
    return P3(cos(t), 0, sin(t))

def g(t):
    return  # Use vector addition here!

# If you do this right both balls will be in the same place

soccerBall(size = .5, position = f(time))

soccerBall(size = .5, position = g(time))

# You can multiply a scalar (an ordinary number) by a vector.
# What happens if you multiply the unit circle by 2?

# You can add two trajectories - add a circle of radius .5 travelling 10 times
# faster than the unit circle to the unit circle

# soccerBall(size = .5, position = unitcircle(time) + ???)

start()