from Panda import *

# Alter the initial position, velocity, and acceleration


camera.position=P3(0,-30, 6)
gravity = P3(0,0,-5)
def col(t):
    return interpolate(t, forever(at(red) + to(.5, purple) + to(.5, blue) + to(.5, green) + to(.5, yellow) + to(.5, orange) + to(.5, red)))

def launch(b, p0, v0):
    setType(b.velocity, P3Type)
    b.velocity = v0 + integral(gravity)
    b.position = p0 + integral(b.velocity)

def bounceFloor(m, v):
    v = m.velocity.now()
    p = m.position.now()
    v1 = P3(getX(v), getY(v), -getZ(v)*.9)
    launch(m, p, v1)

def bounceRight(m, v):
    v = m.velocity.now()
    p = m.position.now()
    v1 = P3(-getX(v), getY(v), getZ(v))
    launch(m, p, v1)

def bounceLeft(m, v):
    v = m.velocity.now()
    p = m.position.now()
    v1 = P3(-getX(v), getY(v), getZ(v))
    launch(m, p, v1)

def newBall(m, v):
    p = panda(size = 2)
    launch(p, P3(0,0,10), P3(5, 0, 5))
    p.when((getZ(p.position) < 0) & (getZ(p.velocity) < 0), bounceFloor)
    p.when((getX(p.position) > 10) & (getX(p.velocity) > 0 ), bounceRight)
    p.when((getX(p.position) < -10) & (getX(p.velocity) < 0 ), bounceRight)
    p.color = col(localTime/2)

a = alarm(start = 1, step = .4)

react(a, newBall)



def launchs(b, p0, v0):
    setType(b.velocity, P3Type)
    b.velocity = v0 + integral(gravity)
    b.position = p0 + integral(b.velocity)

def bounceFloors(m, v):
    v = m.velocity.now()
    ps = m.position.now()
    v1 = P3(getX(v), getY(v), -getZ(v)*.9)
    launch(m, ps, v1)

def bounceRights(m, v):
    v = m.velocity.now()
    ps = m.position.now()
    v1 = P3(-getX(v), getY(v), getZ(v))
    launch(m, ps, v1)

def bounceLefts(m, v):
    v = m.velocity.now()
    ps = m.position.now()
    v1 = P3(-getX(v), getY(v), getZ(v))
    launch(m, ps, v1)

def newBalls(m, v):
    ps = panda(size = 2)
    launchs(ps, P3(0,0,10), P3(-5, 0, 5))
    ps.when((getZ(ps.position) < 0) & (getZ(ps.velocity) < 0), bounceFloors)
    ps.when((getX(ps.position) > 10) & (getX(ps.velocity) > 0 ), bounceRights)
    ps.when((getX(ps.position) < -10) & (getX(ps.velocity) < 0 ), bounceRights)
    ps.color = col(localTime/2)
    
a = alarm(start = 1, step = .4)


react(a, newBalls)

world.color= black
ambientLight.color = (90,90,90)

start()
