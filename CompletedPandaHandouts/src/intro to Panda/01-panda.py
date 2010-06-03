# intro to Panda/01-panda.py
from Panda import *


# Create a panda at (0,0,0) and view it from different angles by setting
# the camera in different places
# Use camera.position = P3(x,y,z) to set your camera.
# Use panda(position = P3(x,y,z)) to create a panda
# If you don't assign a position to the panda it will be at position (0,0,0).
# How can you tell how tall the panda is?


# Note that the camera is by default pointed at positive Y
# Note that the bear is standing on the XY plane and facing -Y (the camera)
# Note that the field of view is such that standing 5 back shows z from
#   about -1 to 1
# Try going left (1, -5, 0) or close in (0, -1, 0) or (0, -2 0.5)

# Move the panda to (0,2,0) to see it go away from the camera

panda(position=P3(0,0,0))
camera.position=P3(0,-10,0)

start()