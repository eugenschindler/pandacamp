# 01-racecar.py
#
# In virtual worlds there are different ways to recreate movement seen in the real world.
# In this file we try to recreate the movement of a car using
# Read the code along with the comments and try to understand how the behavior of a real car is being recreated.
# 
# Run the file and drive the car around using the mouse to steer (move left and right) and to accelerate (move up and down).
# Does this car behave like a real car?
# Try running the next file and compare the two. Does this still seem realistic?

from Panda import *

# create the scene
grassScene()

# create the vehicle
car = jeep()

# set camera
camera.position = P3(0,5,1)
camera.hpr = HPR(pi,0,0)

# vehicle movement variables
# steering wheel angle
# speed
a=.2*getX(mouse)
sK = 2
s = 2*getY(mouse)-sK # scalar
# heading
h = integral(s*-a)
# velocity
v = P3C(s,h+pi/2,0)
# position
p = integral(v)

# move vehicle
car.position = p
car.hpr = HPR(h,0,0)

# run loop
start()
