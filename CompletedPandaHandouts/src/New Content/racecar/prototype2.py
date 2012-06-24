# prototype1.py
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
a = -0.2 * getX(mouse)

# force on vehicle
# force constant
fK = slider(label = "force constant", min = 0, max = 5, init = 2)
# the force
f = fK * getY(mouse)

# velocity
setType(car.vel,P3Type)
#velocity = abs(car.vel)
velocity = abs(car.vel)*abs(car.vel)
text(format("Velocity: %f", velocity))

# friction on vehicle
# friction constant
fcK = slider(label = "friction", min = 0, max = 10, init = 0.5)
# the friction
fc = -fcK * velocity

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
