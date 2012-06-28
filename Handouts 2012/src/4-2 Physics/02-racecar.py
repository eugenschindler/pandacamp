# 02-racecare.py
#
# In this file we try to recreate the movement of a real car by creating what's called a force based controller.
# A force based controller means we make the car move using the same physics that would make a real car move.
#
# Read through the code and the comments and try to understand how the physics work.
# Run the file. Is this behavior realistic?
#
# To see how the force (fK) and friction (fcK) affect the vehicle add a slider for each that allows you to change their constant values while running the file.
# Run the file and see how this changes the behavior of the car.
#
# Next, change the velocity (fc). Try squaring it or dividing by two.
# Run the program and see how the car behaves.
# How long does it take to reach terminal velocity?

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
a = -0.2 * getX(mouse)

# force on vehicle
# force constant
fK = 2
# the force
f = fK * (getY(mouse)-1)

# friction on vehicle
# friction constant
fcK = 0.5
# the friction
setType(car.vel,P3Type)
fc = -fcK * abs(car.vel)

# speed
s = integral(f - fc)

# heading
h = integral(s * -a)
car.hpr = HPR(h,0,0)

# velocity
car.vel = P3C(s,h+pi/2,0)

# position
car.position = integral(car.vel)


# run loop
start()
