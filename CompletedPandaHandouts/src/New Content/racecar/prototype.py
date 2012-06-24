# prototype.py
#
# This is the first racecar coding
#

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
s = 2*getY(mouse)-1 # scalar
text(s)
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
