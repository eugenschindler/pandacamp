# 03-racecar.py
#
# To make a virtual racecar more realistic it needs to be able to crash.
# Real cars often crash when they turn sharply at a high speed.
# This is because of centripetal force.
#
# Run the program and see how your driving affects the centripetal force.
# Make sure to move he sliders to understand how the force and friction affect this.
#
# Read the code and the comments.
# Notice how the car is in a state of driving.
# We use states to create different behavior when different things happen.
#
# Write a state that makes the car crash when the centripetal force reaches a certain point.
# You will need to use "when1" and a reaction to do this.
# A spinning reaction has been written as a demonstration.
# You will need to call this from "when1" and write a spinning state.
# When the car is done spinning you will need to use "react1" and a drive reaction to get back to a driving state.
# Write this code.
#

from Panda import *

# create the scene
grassScene()

# create the vehicle
car = jeep()

# set camera
camera.position = P3(0,5,1)
camera.hpr = HPR(pi,0,0)


# force constant
fK = slider(label = "Force constant", min = 0, max = 5, init = 2)
# friction constant
fcK = slider(label = "Friction", min = 0, max = 10, init = 0.5)
# velocity variable
setType(car.vel, P3Type)

# driving state
def driving(model, p0 = P3(0,0,0), hpr0 = HPR(0,0,0)):
    # vehicle movement variable
    # steering wheel angle
    a = -0.2 * getX(mouse)
    # the force on the vehicle
    f = fK * (getY(mouse)-1)
    # velocity
    velocity = abs(car.vel)
    # friction on vehicle
    fc = -fcK * velocity
    # speed
    s = integral(f - fc)
    # heading
    h = getH(hpr0) + integral(s * -a)
    car.hpr = HPR(h,0,0)
    # velocity
    car.vel = P3C(s,h+pi/2,0)
    # position
    car.position = p0 + integral(car.vel)
    # centripetal force
    cent = velocity*velocity * a

    # spin out the vehicle
    car.when1(cent > 1.5, spin)

# drive reaction
def drive(model, var):
    # preserve state
    p = now(model.position)
    hpr = now(model.hpr)

    # drive!
    driving(model, p, hpr)


# spinning state
def spinning(model, p0, hpr0, v0):
    # spinning
    p = p0 + integral(v0 * (1 - localTime / 3))
    model.position = p
    hpr = hpr0 + HPR(integral(20 * (1 - localTime / 3)),0,0)
    model.hpr = hpr

    # drive away
    model.react1(localTimeIs(3), drive)


# spin reaction
def spin(model, var):

    # preserve state
    p = now(model.position)
    hpr = now(model.hpr)
    v = now(model.vel)

    # spin out!
    spinning(model, p, hpr, v)



# go for a drive!
driving(car)

# run loop
start()
