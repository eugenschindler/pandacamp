# 01-racegame.py

from Panda import *

# game music
#play("marioBrosTheme.mp3")

# create the vehicle
car = jeep(size = 0.25)

# create the racetrack
track = Racetrack("track.txt", model = car)


# Game text

text(format("Time: %i", (60-time)*step(60-time)))
text(format("Score: %i", track.score))

# set camera
camera.rod(car, distance = 2)

# force constant
fK = 2
# friction constant
fcK = 0.5
# centripetal force threshold
thresh = 10
# velocity variable
setType(car.vel, P3Type)
sv = var(.8)
soundmove = Sound("engine.wav", loopCount = 0)
def faster(m, v):
    sv.times(1.1)
    soundmove.setRate(sv.get())
def slower(m, v):
    sv.times(1/1.1)
    soundmove.setRate(sv.get())
react(key("arrow_up"), faster)
react(key("arrow_down"), slower)
panda(size = .2, position = P3(5,5,0))

# driving state
def driving(model, p0 = P3(0,0,0), hpr0 = HPR(0,0,0)):
    # vehicle movement variable
    # steering wheel angle
#    a = getX(mouse)
    
    
#    soundmove.play()

#    play("engine.mp3")
    a1 = hold(0, key("arrow_right",  1) + keyUp("arrow_right",  0))
    a2 = hold(0, key("arrow_left",  -1) + keyUp("arrow_left",  0))
    a3 = hold(0, key("arrow_up",  -1) + keyUp("arrow_up",  0))
    a4 = hold(0, key("arrow_down",  1) + keyUp("arrow_down",  0))
    kee = a1 + a2
    spd = a3 + a4
    
#    sv.set(spd)
#    soundmove.setRate(sv.get()) #sv.get()
    
#    model.a = accum(0, key("arrow_right",  lambda x:x+.1)  + key("arrow_left", lambda x:x-.1))
    setType(model.a, numType)
    decay = -1.95*model.a
    model.a = integral(kee + decay)
#    text(model.a)
    # the force on the vehicle
    f = fK * integral(spd)
    # velocity
    velocity = abs(car.vel)*abs(car.vel)
    # friction on vehicle
    # get friction from track
    fcK = track.friction(car.position)
    fc = -fcK * velocity
    # speed
    s = integral(f - fc)*10
    # heading
    h = getH(hpr0) + integral(s * model.a)
    car.hpr = HPR(h,0,0)
    # velocity
    car.vel = P3C(s,h+pi/2,0)

    
    # position
    car.position = p0 + integral(car.vel)
    # centripetal force
    # get friction from track
    cK = track.cent(car.position)
    cent = cK * velocity * velocity * model.a

    # vehicle reactions
    car.when1(cent > thresh, spin)
    car.when1(track.inWall(car), burn)
    car.when1(track.cent(car.position) == 0, burn) # when driving into water

# drive reaction
def drive(model, var):
    # preserve state
    p = now(model.position)
    hpr = now(model.hpr)
    # drive!
    driving(model, p, hpr)


def jump(model, var):
    p = now(model.position)
    vel = now(car.vel)
    newvel = P3(getX(vel), getY(vel), 1)
    pointForward(model)
    model.when1(getZ(model.position) < 0, drive)
    model.velocity = newvel + integral(P3(0,0,-2.3))
    model.position = p + integral(model.velocity)
    
# begin driving reactions

# spinning state
def spinning(model, p0, hpr0, v0):
    # spinning
    p = p0 + integral(v0 * (1 - localTime / 3))
    model.position = p
    hpr = hpr0 + HPR(integral(20 * (1 - localTime / 3)),0,0)
    model.hpr = hpr
    play("bad.mp3")
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
def burning(model, p0, hpr0):
    # burning
    p = p0*step(1-localTime) + step(localTime-1)*startPos
    model.position = p
    model.hpr = hpr0*step(1-localTime) + step(localTime-1)*startHPR
    s = fireish(position = p0)
    s.react1(localTimeIs(1), stopIt)
    play("bad.mp3")
    # reset the model
    model.react1(localTimeIs(1), drive)


# burning reaction
def burn(model, var):
    # preserve state
    p = now(model.position)
    hpr = now(model.hpr)
    # burning!
    burning(model, p, hpr)

# end driving reactions

# begin item reactions

def powerUp(model, var):
    p = now(model.position)
    s = shakenSparkles(position = p)
    s.react1(localTimeIs(1), stopIt)

def explosion(model, var):
    p = now(model.position)
    s = fireish(position = p)
    s.react1(localTimeIs(1), stopIt)

# end item reactions

# item generation
def generateObj(model, var):
    num = random01()
    if num > 0.5:
        track.placeObj(hp if random01() > 0.5 else questionBlock, position = P3(randomRange(5,track.xmax-5),randomRange(5,track.ymax-5),0), score = 1, reaction = powerUp, duration = 30, sound = "good.mp3")
    else:
        track.placeObj(offense if random01() > 0.5 else questionBlock, position = P3(randomRange(5,track.xmax-5),randomRange(5,track.ymax-5),0), score = -1, reaction = explosion, duration = 30, sound = "good.mp3")

# generate the items
a = alarm(step = 2)
react(a, generateObj)


#
#kee = key("space", car.vel)
#
#print kee

# go for a drive!
startPos = P3(20,15,0) # the vehicle will be reset to these
startHPR = HPR(pi/2,0,0)
driving(car, startPos, startHPR)
#car.when1(dist(car.position, P3(5,5,0))<.5, jump)


# run loop
'''
camera.position = P3(11,16,60)
camera.hpr = HPR(0, -pi/2, 0)
car.position = P3(10*(getX(mouse) + 1), 10*(getY(mouse) + 1), 0)
text(track.cent(car.position))
text(track.inWall(car))
text(car.position)'''

start()
