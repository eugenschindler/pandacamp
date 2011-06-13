
from Panda import *

m2 = maze("maze.txt", __name__)



def wall_X(x,y):
        return Maze.mazecube(x, y, color(0, random01(),random01()))

def open_b(x,y):
        return bunny(position = P3(x+.5,y+.5,0),size=.5)

def open_j(x,y):
        return jeep(position = P3(x+.5,y+.5,0),size=.5)

def staticCollide(p,s):
    bl = p
    br = p + P3(1,0,0)*s
    tl = p + P3(0,1,0)*s
    tr = p + P3(0,0,1)*s
    rest = ((m2.collide(bl))or(m2.collide(br))or(m2.collide(tl))or(m2.collide(tr)))
    return rest
collide = lift(staticCollide,"Collide",[P3Type,numType],boolType)



#camera.position = P3(5, 5, 20)
h = integral(getX(mouse))
speed = P3C(getY(mouse)+1, -h, 0)


#camera.hpr = HPR(0, -pi/2, 0)

runner = panda(size = .4)

#other cars
q0 = P3(0,0,0)
p0 = P3(1,1,0)
v0 = P3(0,0,0)

#key commands
v = hold(v0, tag(P3(-1, 0, 0), key("a")) +
             tag(P3(0, -1, 0), key("s")) +
             tag(P3(0, 1, 0), key("w")) +
             tag(P3(1, 0, 0), key("d")) +
             tag(P3(0, 0, 0), key("h")))


def bounce(m, v):
    launch(m,m.oldposition.now())

def launch(m,start):
    m.position = start + integral(v)
    m.oldposition = delay(start,m.position)
    m.when1(collide(m.position,m.size),bounce)

text (runner.position)


#p = p0 + integral(v)
dir = deriv(P3(0,0,0), runner.position)
#runner.position =p
launch(runner,p0)
hpr = P3toHPR(dir)
runner.hpr = HPR(getH(hpr), getP(hpr), 0)


w = panda(size = .2, color = blue)
def funcw(x,y):
    return sqrt(x*x + y*y)

def campan (h,j,f):
    setType(h.vel, P3Type)

    springLoc = runner.position
    x = getX(springLoc-h.position)
    y = getY(springLoc-h.position)
    springK = j * (f(x,y))
    spring = springK * (springLoc - h.position)
    friction =  h.vel * -2
    force =  spring + friction
    h.vel = integral(force) + v0
    h.position = integral(h.vel) + q0
    pdif =runner.position - h.position
    vect = P3toHPR(pdif)
    h.hpr = HPR(getH(vect),0,0)

campan (w, .5, funcw)
camera.position = choose(lbutton, P3((getX(w.position)),(getY(w.position)),0), P3(5, 5, 20))
camera.hpr = choose(lbutton, HPR(getH(w.hpr)+radians(180),getP(w.hpr),0), HPR(0, -pi/2, 0))

start()
