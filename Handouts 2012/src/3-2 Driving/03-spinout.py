from Panda import *
#
friction = slider(min = 0, max = 2, init = .4, label = "friction")
text(format("Friction: %f", friction))

# create the vehicle
car = jeep(size = .25)
# create the scene
track = Racetrack("oval.txt", model = car)

setType(car.velocity,P3Type)
setType(car.angle, numType)

# car.when(car)
# set camera
#camera.position = P3(18,6,50)
#camera.hpr = HPR(0, -pi/2, 0)
#camera.hpr = HPR(pi+integral(hold(0, key("left-arrow", .3) + key("right-arrow", -.3) + key(" ", 0))),0,0)  #  Lets you turn your head
camera.rod(car, distance = 2)
text(abs(car.angle*abs(car.velocity)*abs(car.velocity)))
def crash(m, v):
    print "Crashing"
    car.position = now(car.position)
    car.hpr = now(car.hpr)
    fireish(position = now(car.position), duration = 2, size = .3*(2 - localTime))
    m.react1(localTimeIs(2), restartCar)

def restartCar(m, v):
    driving(m)


def driving(model, p0 = P3(5,3,0), h0 = pi/2):
    # vehicle movement variable
    # steering wheel angle
    # a is the angle of the steering wheel - the .2 gives this a realistic range
    model.angle=-.5*getX(mouse)
    # speed

    # The frictional force is proportional to the car velocity and goes against the direction of travel
    fc = -friction * abs(car.velocity)
    # s is the speed of the car
    force = 2*(getY(mouse)+1) # this is now a force instead of a speed.  Range is 0 to 4
    # speed
    speed = integral(force + fc)
    # the current heading is the integral of the turning rate
    heading = integral(speed*model.angle) + h0
    # velocity vector has the magnitude of the speed and direction of the heading.  The pi/2 is because
    # the jeep model faces -y.
    model.velocity = P3C(speed,heading-pi/2,0)
    # Car position is the integral of the velocity
    model.position = p0 + integral(car.velocity)

    model.hpr = HPR(heading,0,0)
    model.when1(track.inWall(car), crash)
    model.when1(abs(model.angle*abs(model.velocity)*abs(model.velocity)) > 15, spin)
    # the force on the vehicle

    # centripetal force
    # cent = velocity*velocity * a

    # spin out the vehicle
    # car.when1(cent > 1.5, spin)

def drive(model, var):
    driving(model, p0 = now(model.position), h0 = now(model.hpr).h)
    
def spin(model, var):

    # preserve state
    p = now(model.position)
    hpr = now(model.hpr)
    v = now(model.velocity)

    # spin out!
    spinning(model, p, hpr, v)

def spinning(model, p0, hpr0, v0):
    # spinning
    p = p0 + integral(v0 * (1 - localTime / 2))
    model.position = p
    hpr = hpr0 + HPR(integral(20 * (1 - localTime / 2)),0,0)
    model.hpr = hpr

    # drive away
    model.react1(localTimeIs(2), drive)


# run loop

driving(car)
start()
'''
from Panda import *

car = jeep(size = 0.25)

# create the racetrack
track = Racetrack("oval.txt", model = car)

# set camera
camera.position = P3(0,5,1)
camera.hpr = HPR(pi,0,0)


# force constant
fK = slider(label = "Force to spinout", min = 0, max = 5, init = 2)
# friction constant
fcK = slider(label = "Friction", min = 0, max = 10, init = 0.5)
# velocity variable
setType(car.velocity, P3Type)

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
'''