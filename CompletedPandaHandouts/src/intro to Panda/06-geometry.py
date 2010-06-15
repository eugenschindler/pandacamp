# intro to Panda/06-geometry.py
from Panda import *

# Place a green floor under the panda at (0,0,0)
# The floor should be at z = 0 and go from -2 to 2 in x and -2 to 2 in y

# Use a slider to move the camera up and down.

# Remember that you only need to tell rectangle 3 points - it computes
# the fourth one.

# Add a picture behind the panda of a real panda - make this connect to the
# floor behind the panda

panda(position = P3(0,0,0))

h = slider(max =2 , init = .5, label = "camera")
camera.position = P3(0, -5, h)
rectangle (P3(-2,2,0), P3(-2,-2,0), P3(2,2,0), color = green)
rectangle (P3(-2,2,0), P3(2,2,0), P3(-2, 2, 4), texture = "band6.jpg")
start()