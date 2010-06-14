# Vectors and interpolation/01-linearMotion.py
# Linear trajectories
# What happens when you change these values?
# What is the meaning of each of these numbers?
# Can you:
## Make the panda charge at the camera
## Make the panda start at the camera position and go away
## Make the panda start on the left of the screen and move to the right
## Make the panda go twice as fast
from Panda import *

# These define the initial values and rate for x, y, and x.

x0 = 0
dx = 1
y0 = 0
dy = 1
z0 = 0
dz = 1
# This is called a "parametric" equation - you tell the function what
# time it is and the function tells you where you are at that time.
def f(t):
    return P3(x0+dx*t, y0+dy*t, z0+dz*t)

b = panda(position = f(time))

camera.position = P3(0, -10, 0)

start()