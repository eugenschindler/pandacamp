from Panda import *
sonic (position = P3 (1,1,1))
x = slider(min = -10, max = 10, init = 0, label = "right/left")
y = slider(min = -10, max = 10, init = -5, label = "back/forward")
z = slider(min = -10, max = 10, init = 0, label = "up/down")
panda (position = P3 (3,1,0))
soccerball (position = P3 (3,1,1))
r = slider(max = 2*pi, label = "roll")
# Create a panda at (1,0,0) and a bunny at (-1,0,0) and view from different angles
# Try some other models.  Where is the "grab point" on each model?
# How big are these objects?  Which way do they face?

start()