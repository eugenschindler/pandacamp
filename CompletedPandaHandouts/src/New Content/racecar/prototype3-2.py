# prototype1.py
#
# This is the first racecar coding
#

from Panda import *

items = [boost, charge, defense, glide, hp, offense, questionBlock, speed, turn, weight]

# create the scene
#grassScene()

# create the racetrack
track = Racetrack("maze2.txt")
for i in range(20):
    for j in range(20):
        track.item(items[int(randomRange(0,9))], P3(int(randomRange(5,track.w-5)),int(randomRange(5,track.h-5)),0))

# create the vehicle
car = jeep(size = 0.25)

# set camera
#camera.position = P3(0,5,1)
#camera.hpr = HPR(pi,0,0)
camera.rod(car, distance = 2)
#camera.position = P3(20,20,75)
#camera.hpr = HPR(0,-pi/2,0)


# force constant
fK = slider(label = "Force constant", min = 0, max = 5, init = 2)
# friction constant
fcK = slider(label = "Friction", min = 0, max = 10, init = 0.5)
# centripetal force threshold
thresh = slider(label = "Centripetal threshold", min = 0.01, max = 2, init = 1.5)
# velocity variable
setType(car.vel, P3Type)
#text(format("Velocity: %f", abs(car.vel)*abs(car.vel)))

# driving state
def driving(model, p0 = P3(0,0,0), hpr0 = HPR(0,0,0)):
    # vehicle movement variable
    # steering wheel angle
    a = getX(mouse)
    # the force on the vehicle
    f = fK * (getY(mouse)-1)
    # velocity
    #velocity = abs(car.vel)
    velocity = abs(car.vel)*abs(car.vel)
    # friction on vehicle
    fcK2 = track.getFriction(car.position)
    text(fcK2)
    fc = -fcK2 * velocity
    # speed
    s = integral(f - fc)
    # heading
    h = getH(hpr0) + integral(s * -a)
    car.hpr = HPR(h,0,0)
    # velocity
    car.vel = P3C(s,h+pi/2,0)
    # position
    car.position = p0 + integral(car.vel)
    #car.position = P3(20*getX(mouse)+20, 20*getY(mouse)+20, 0)
    # centripetal force
    cent = abs(velocity*velocity * a)

    # spin out the vehicle
    car.when1(cent > thresh, spin)
    #car.when1(track.inWall(car), burn)
    text(track.getFriction(car.position))


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


# burning state
def burning(model, p0):
    # burning
    model.position = p0
    f = fireish(position = p0+P3(0,0,0.5), size = (1-localTime)/3)

    # reset the model
    model.react1(localTimeIs(3), drive)

# burning reaction
def burn(model, var):
    # preserve state
    p = now(model.position)

    # burning!
    burning(model, p)


# go for a drive!
driving(car, P3(13,13,0), HPR(0,0,0))

# run loop
start()
