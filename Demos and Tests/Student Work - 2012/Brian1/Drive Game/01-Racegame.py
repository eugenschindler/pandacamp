from Panda import *

car=truck(size = 0.25)
text(car.position)
setType(car.velocity, P3Type)
setType(car.angle, numType)
track = Racetrack("track.txt", model = car)
text(format("Score: %i", track.score))
camera.flatrod(car, distance = 2)
spinThresh = 10   # Force at which we spin out
engineForce = 5   # Power of the engine
frictionForce = 10    # Scales track friction

carhit = Sound("break.wav", volume = 150)
soundwipeout = Sound("screetch.wav", loopCount = 12)
soundwipeout.setRate(3)
soundmove = Sound("engine.wav", loopCount = 0)

movingFire1 = fireish(size = 0.5)
movingFire1.position = P3(20, 10+cos(time)*2, -0.75)
movingFireBall1 = sphere(size = 0.5, texture = "fireball.jpg")
movingFireBall1.position = P3(20, 10+cos(time)*2, 0.5)
movingFireBall1.hpr = HPR(time, time, time)

movingFire2 = fireish(size = 0.5)
movingFire2.position = P3(25+sin(-time/5), 10+cos(time)*4, -0.75+sin(time/2))
movingFireBall2 = sphere(size = 0.5, texture = "fireball.jpg")
movingFireBall2.position = P3(25+sin(-time/5), 10+cos(time)*4, 0.5+sin(time/2))
movingFireBall2.hpr = HPR(time, time, time)

movingFire3 = fireish(size = 2)
movingFire3.position = P3(45+sin(-time/5), 19+cos(time)*cos(time/4)*2, -0.75+sin(time/5))
movingFireBall3 = sphere(size = 2, texture = "fireball.jpg")
movingFireBall3.position = P3(45+sin(-time/5), 19+cos(time)*cos(time/4)*2, 0.5+sin(time/5))
movingFireBall3.hpr = HPR(-time, time*5, time)

movingFire4 = fireish(size = 1.25)
movingFire4.position = P3(62, 17+((cos(time)*4)*(cos(time)*4)), -0.75)
movingFireBall4 = sphere(size = 0.5, texture = "fireball.jpg")
movingFireBall4.position = P3(62, 17+((cos(time)*4)*(cos(time)*4)), 0.5)
movingFireBall4.hpr = HPR(time, time, -time)

movingFire5 = fireish(size = 1.25)
movingFire5.position = P3(68+(sin(time*time)), 12+(cos(time*sin(time))*2), -0.75)
movingFireBall5 = sphere(size = 0.5, texture = "fireball.jpg")
movingFireBall5.position = P3(68+(sin(time*time)), 12+(cos(time*sin(time))*2), 0.5)
movingFireBall5.hpr = HPR(time, time, time)

movingFire6 = fireish(size = 1)
movingFire6.position = P3(64+sin(time*cos(time)), 4+cos(time*sin(time*cos(time))), -0.75)
movingFireBall6 = sphere(size = 1, texture = "fireball.jpg")
movingFireBall6.position = P3(64+sin(time*cos(time)), 4+cos(time*sin(time*cos(time))), 0.5)
movingFireBall6.hpr = HPR(time, time, time)

blackHole1 = sphere(texture = "bp.jpg")
blackHole1.size = sin(time)*3
blackHole1.position = P3(55,8,0)
blackHole1.hpr = HPR(time, time, time)

blackHole2 = sphere(texture = "bp.jpg")
blackHole2.size = sin(time)*3
blackHole2.position = P3(6+sin(time*time),22+sin(time),(sin(time)*5)-2)
blackHole2.hpr = HPR(time, time, time)

blackHole3 = sphere(texture = "bp.jpg")
blackHole3.size = sin(time)*3
blackHole3.position = P3(18,2+sin(time),(sin(time)*5)-2)
blackHole3.hpr = HPR(time, time, time)

panda1 = panda()
panda1.position = P3(76+(sin(time)*12), 18+(sin(time)*12), sin(time))
panda1.hpr = HPR(time, sin(time), 0)

startSphere = sphere(size = .5, texture = "check.JPG")
startSphere.position = P3(7,7,0)

endSphere = sphere(size = .5, texture = "check.JPG")
endSphere.position = P3(73, 27, 0)

def driving(model, p0, h0, speed0):
    print "Driving"
#    text(speed0)
    a1 = hold(0, key("arrow_right",  -1) + keyUp("arrow_right",  0))
    a2 = hold(0, key("arrow_left",  1) + keyUp("arrow_left",  0))
    a3 = hold(0, key("arrow_up",  1) + keyUp("arrow_up",  0))
    a4 = hold(0, key("arrow_down",  -1) + keyUp("arrow_down",  0))
    delta = a1 + a2
    dspeed = a3 + a4
 
    decay = -1.95*model.angle   # Straighten wheels after turning
    model.angle = integral(delta + decay)   # Should be limited
    
    # the force on the vehicle
    forward = (speed0 * 4) + engineForce * integral(dspeed)
    # velocity
    fvelocity = abs(model.velocity)
    # friction on vehicle
    # get friction from track
    pushBack = track.friction(model.position)
    friction = pushBack * frictionForce * fvelocity
    # speed
    speed = integral(forward - friction)
#    text(speed)
    speed1 = choose(speed < -.4, -.4, speed)
    # heading
    h = h0 + integral(speed1 * model.angle)
    model.hpr = HPR(h,0,-model.angle)
    model.velocity = P3C(speed1,h-pi/2,0)
    model.position = p0 + integral(model.velocity)
    #model.when1(abs(model.angle*abs(model.velocity)*abs(model.velocity)) > spinThresh, spinout)
    model.when1(track.inWall(model), wallburn)
    model.react1(key(" "), jump)
    
def driveReset(model, var):
    drive(model, var, resetSpeed = 1)
    
def spinout(model, var):
    print "SPINNIN'"
    p0 = now(model.position)
    hpr0 = now(model.hpr)
    v0 = now(model.velocity)
    model.position = p0 + integral(v0 * (1 - localTime / 3))
    model.hpr = hpr0 + HPR(integral(20 * (1 - localTime / 3)),0,0)
    soundwipeout.play()
    model.when1(track.inWall(model), wallburn)
    # drive away
    model.react1(localTimeIs(3), driveReset)

def chp(hpr):
    return HPR(getH(hpr), -getP(hpr), getR(hpr))


def jump(model, var):
    print "Jumping"
    p0 = now(model.position)
    v0 = now(model.velocity)
    hpr0 = now(model.hpr)
    
    model.velocity = P3(getX(v0), getY(v0), 1.5) + integral(P3(0,0,-1))
    model.position = p0 + integral(model.velocity)
    
    model.hpr = chp(P3toHPR(deriv(model.position, HPRtoP3(hpr0))))
    model.when1(track.inWall(model), wallburn)
    model.when1(getZ(model.position)<0, drive)

def drive(model, var, resetSpeed = 0):
    p0 = now(model.position)
    hpr0 = now(model.hpr)
    v0 = 0 if resetSpeed == 1 else now(model.velocity)
    driving(model, P3(getX(p0), getY(p0), 0), getH(hpr0), abs(v0))

def burning(model, p0, hpr0):
    print "burning"
    
    model.position = p0
    model.hpr = hpr0
    s = fireish(position = p0, duration = 1)

    # reset the model
    model.react1(localTimeIs(1), respawn)

def respawn(m, v):
    driving(car, P3(4,4,0), pi/2, 0)


def resetEndSphere(m,v):
    #car.hpr = HPR(0, 0, 0)
    #car.velocity = P3(0,0,0)
    car.position = P3(70, 23, 0)
    
def resetStartSphere(m,v):
    car.position = P3(4,4,0)
    
# burning reaction
def burn(model, var):
    # preserve state
    p = now(model.position)
    hpr = now(model.hpr)
    # burning!
    play("bad.mp3")
    burning(model, p, hpr)

def wallburn(model, var):
    # preserve state
    p = now(model.position)
    hpr = now(model.hpr)
    # burning!
    carhit.play()
    burning(model, p, hpr)

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
    track.placeObj(coin, size = .1, position = P3(randomRange(5,track.xmax-5),randomRange(5,track.ymax-5),sin(time * 4) / 64 + .05), score = 1, reaction = powerUp, duration = 30, sound = "good.mp3")

# Other diving reactions
#def setSpeed(m, v):
#    s = abs(now(car.velocity))
#    soundmove.setRate(s)

soundmove.play()

#setAlphaScale(0.5)

a = alarm(step = 4)
react(a, generateObj)
car.react(hit(car, endSphere), resetEndSphere)
car.react(hit(car, startSphere), resetStartSphere)
car.react(hit(car, movingFireBall1), wallburn)
car.react(hit(car, movingFireBall2), wallburn)
car.react(hit(car, movingFireBall3), wallburn)
car.react(hit(car, movingFireBall4), wallburn)
car.react(hit(car, movingFireBall5), wallburn)
car.react(hit(car, movingFireBall6), wallburn)
car.react(hit(car, blackHole1), wallburn)
car.react(hit(car, blackHole2), wallburn)
car.react(hit(car, blackHole3), wallburn)
car.react(hit(car, panda1), wallburn)

driving(car, P3(4,4,0), pi/2, 0)
#car.react(dist(car.position, P3(5,5,0))<.5, jump) #When the car hits the panda

start()