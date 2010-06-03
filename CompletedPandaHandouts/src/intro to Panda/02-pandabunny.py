# intro to Panda/02-pandabunny.py
from Panda import *

# Create a panda at (1,0,0) and a bunny at (-1,0,0) and view from different angles
# Try some other models.  Where is the "grab point" on each model?
# How big are these objects?  Which way do they face?

camera.position=P3(0,-10,0)

panda(position=P3(1,0,0))
bunny(position=P3(-1,0,0))

start()