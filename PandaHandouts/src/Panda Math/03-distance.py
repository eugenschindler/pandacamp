
# Measuring distance using "dist"
from Panda import *

p1 = P3(0,0,0)
v1 = P3(1,1,1)
p2 = P3(2,0,0)
v2 = P3(-1, 1, 1)

m1 = soccerBall(position = p1 + v1*time)
m2 = soccerBall(position = p2 + v2*time)
# Display the distance between the balls using "text"

start()
# The position of the ball is its center.
# Observe the distance as the balls move together  and
# then apart.  Change the trajectories - what happens to the distance?
# How is this distance computed?
# Change one of the balls to move according to a slider and
# place the other at (0,0,0).  How does the distance work in this case?

