from Panda import *

# The things between the ( and ) in a function are called parameters
# Parameters can be anything - numbers, points, colors, or even models

# Here's a function that makes one model follow another:

def follow(m1, m2):  # Make m2 follow m1
   m2.position = m1.position + (P3(sin(time*2), 0, cos(time)))

p = panda(position = P3(getX(mouse), 0, getY(mouse)))

p1 = panda()
follow(p, p1)
p2 = panda()
follow (p1,p2)
p1.color =  color(sin(time*2), .5, .5)

# Make p1 follow p and p2 follow p1
# Then, add another parameter to follow to give the "following distance":
# have p1 follow p1 by P3(1,0,0) and p2 follow p1 by P3(0,0,1)

start()
