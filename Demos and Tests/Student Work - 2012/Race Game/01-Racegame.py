# 01-racegame.py

from Panda import *

# game music
play("marioBrosTheme.mp3")

# create the vehicle
#car = jeep(size = 0.25)
car = snowCar(size = 0.25)

# create the racetrack
sphere(size = -1000, texture = "sky.jpg")
track = Racetrack("track.txt", model = car)

# Game text
timeMod = var(0)
totalTime = timeMod+60-time
text(format("Total time: %i", totalTime))
text(format("Time: %i", (totalTime)*step(totalTime)))
text(format("Score: %i", track.score))

# set camera
camera.rod(car, distance = 2)

# force constant
fK = 2
# friction constant
fcK = 0.5
# centripetal force threshold
thresh = 50000000
# velocity variable
setType(car.vel, P3Type)
# driving state
def driving(model, p0 = P3(0,0,0), hpr0 = HPR(0,0,0)):
    # vehicle movement variable
    # steering wheel angle
    a = getX(mouse)
    # the force on the vehicle
    f = fK * (getY(mouse)-1)
    # velocity
    velocity = abs(car.vel)*abs(car.vel)
    # friction on vehicle
    # get friction from track
    fcK = track.getFriction(car.position)
    fc = -fcK * velocity
    # speed
    s = integral(f - fc)
    # heading
    h = getH(hpr0) + integral(s * a)
    model.hpr = HPR(h,0,0)
    # velocity
    model.vel = P3C(s,h+pi/2,0)
    # position
    model.position = p0 + integral(car.vel)
    # centripetal force
    # get friction from track
    cK = track.getCent(car.position)
    cent = cK * velocity*velocity * a

    # vehicle reactions
    model.when1(cent > thresh, spin)
    model.when1(track.inWall(car), burn)
    model.when1(track.getCent(car.position) == 0, burn) # when driving into water

# drive reaction
def drive(model, var):
    # preserve state
    p = now(model.position)
    hpr = now(model.hpr)
    # drive!
    driving(model, p, hpr)


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

'''
def powerUp(model, var):
    p = now(model.position)
    s = shakenSparkles(position = p)
    s.react1(localTimeIs(1), stopIt)

def explosion(model, var):
    p = now(model.position)
    s = fireish(position = p)
    s.react1(localTimeIs(1), stopIt)
'''

# for boost
def fast(model, var):
    p = now(model.position)
    s = shakenSparkles(position = p)
    s.react1(localTimeIs(1), stopIt)

# for defense
def untouchable(model, var):
    pass

# for charge
def addTime(model, var):
    p = now(model.position)
    s = shakenSparkles(position = p)
    s.react1(localTimeIs(1), stopIt)
    timeMod.add(30)

# for glide
def flying(model, var):
    p = now(model.position)
    s = fireish(position = p)
    s.react1(localTimeIs(1), stopIt)
    hpr = now(model.hpr)
    v = model.vel
    fly(model,p,hpr,v)

def fly(model, p0 = P3(0,0,0), hpr0 = HPR(0,0,0), v0 = 0):
    # vehicle movement variable
    # steering wheel angle
    a = getX(mouse)
    # the force on the vehicle
    f = fK * (getY(mouse)-1)
    # velocity
    velocity = abs(v0)+abs(car.vel)*abs(car.vel)
    # friction on vehicle
    # get friction from track
    fcK = track.getFriction(car.position)
    fc = -fcK * velocity
    # speed
    s = integral(f - fc)
    # heading
    h = getH(hpr0) + integral(s * a)
    model.hpr = HPR(h,0,0)
    # velocity
    model.vel = P3C(s,h+pi/2,0)
    # position
    model.position = p0 + integral(car.vel) + step(3-localTime)*P3(0,0,1)
    
    model.react1(localTimeIs(10), drive)

# for hp
def fixScore(model, var):
    track.score.add(-now(track.score))
    p = now(model.position)
    if track.score <= 0:
        s = shakenSparkles(position = p)
        s.react1(localTimeIs(1), stopIt)
    else:
        s = fireish(position = p)
        s.react1(localTimeIs(1), stopIt)
    

# for offense
def noBad(model, var):
    pass

# for speed
def goSlow(model, var):
    p = now(model.position)
    s = shakenSparkles(position = p)
    s.react1(localTimeIs(1), stopIt)

# for turn
# spin reaction
def spin(model, var):
    # preserve state
    p = now(model.position)
    s = fireish(position = p)
    s.react1(localTimeIs(1), stopIt)
    hpr = now(model.hpr)
    v = now(model.vel)
    # spin out!
    spinning(model, p, hpr, v)

# for weight
def stopage(model, var):
    p = now(model.position)
    s = fireish(position = p)
    s.react1(localTimeIs(1), stopIt)
    hpr = now(model.hpr)
    # spin out!
    stopped(model, p, hpr)

def stopped(model, p0, hpr0):
    model.position = p0
    model.hpr = hpr0
    model.react1(localTimeIs(3), drive)

# for questionBlock
def rando(model, var):
    randomChoice(items2)[1](model,var)

# end item reactions

def endGame(model, var):
    resetWorld()
    text(format("Game Over! Your scored %i", track.score), position = P3(0,0,-7), size = 3)

# item generation
items = [[questionBlock,rando],[boost,fast],[charge,addTime],[defense,untouchable],[glide,flying],[hp,fixScore],[offense,noBad],[speed,goSlow],[turn,spin],[weight,stopage]]
items2 = [[hp,fixScore,0],[turn,spin,-1],[glide,flying,-1],[boost,fast,5],[weight,stopage,-1],[speed,goSlow,10],[questionBlock,rando,1]]
siz = len(items2)
def generateObj(model, var):
    num = randomInt(siz)-1
    track.placeObj(items2[num][0], reaction = items2[num][1], score = items2[num][2], duration = 30, sound = "good.mp3")
'''
def generateObj(model, var):
    num = random01()
    if num > 0.5:
        track.placeObj(hp if random01() > 0.5 else questionBlock, position = P3(randomRange(5,track.w-5),randomRange(5,track.h-5),0), score = 1, reaction = powerUp, duration = 30, sound = "good.mp3")
    else:
        track.placeObj(offense if random01() > 0.5 else questionBlock, position = P3(randomRange(5,track.w-5),randomRange(5,track.h-5),0), score = -1, reaction = explosion, duration = 30, sound = "good.mp3")
'''
# generate the items
a = alarm(step = 2)
react(a, generateObj)
when(totalTime < 0, endGame)

for i in range(100):
    generateObj(None,None)

# go for a drive!
#startPos = P3(20,15,0) # the vehicle will be reset to these
startPos = P3(23,23,0)
startHPR = HPR(pi/2,0,0)
driving(car, startPos, startHPR)
#track.placeObj(hp if random01() > 0.5 else questionBlock, score = 1, reaction = powerUp, duration = 30, sound = "good.mp3")

# run loop
start()
