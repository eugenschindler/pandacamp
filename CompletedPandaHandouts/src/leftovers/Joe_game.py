
from Panda import *

frict = slider(max = 10)

spr = slider(max = 1)

wf = slider(max = 20)

soccerBall(size = .1, position = P3(2,2,0))
panda(size = .2, position = P3(2,2, 0))


forvel = hold(0.0, key("arrow_up", 1) + keyUp("arrow_up", 0))

turnvel = hold(0.0, key("arrow_left", 1) + keyUp("arrow_left", 0) + 
                  key("arrow_right", -1) + keyUp("arrow_right", 0))
                  
heading = integral(turnvel)

runv = P3C(forvel, heading, 0)

def wall_X(x,y):
        return mazeCube(x, y, color(0, random01(),random01()))

#def open_b(x,y):
#        return bunny(position = P3(x+.5,y+.5,0),size=.5)

#def open_j(x,y):
#        return jeep(position = P3(x+.5,y+.5,0),size=.5)

m2 = maze("maze.txt", __name__)

#text(m2.wallHit(.1, ball.position))



#camera.position = P3(5, 5, 20)
h = integral(getX(mouse))
speed = P3C(getY(mouse)+1, -h, 0)


#camera.hpr = HPR(0, -pi/2, 0)

runner = panda(size = .2)

#other cars
q0 = P3(0,0,.5)
p0 = P3(1.2,1.2,-.5)
v0 = P3(0,0,0)

#key commands
v = hold(v0, tag(P3(-1, 0, 0), key("a")) +
             tag(P3(0, -1, 0), key("s")) +
             tag(P3(0, 1, 0), key("w")) +
             tag(P3(1, 0, 0), key("d")) +
             tag(P3(0, 0, 0), key("h")))

    
moveInMaze(runner,m2,p0,runv)

thing = find1InMaze(m2,"b")

thing.hpr = HPR(time,0,0)

#text (runner.position)

runner.hpr = HPR(heading+ pi/2, 0, 0)

#dir = deriv(runner.position)
#hpr = P3toHPR(dir)
#runner.hpr = HPR(getH(hpr), getP(hpr), 0)


w = panda(size = .2, color = blue)
def funcw(x,y):
    return sqrt(x*x + y*y)

def campan (h,d,f):
    setType(h.vel, P3Type)

    springLoc = runner.position# + P3C(d,getH(runner.hpr)+pi/2,0)
    x = getX(springLoc-h.position)
    y = getY(springLoc-h.position)
    springK = spr * (f(x,y))
    spring = springK * (springLoc - h.position)
    friction =  h.vel * -frict
    force =  spring + friction + m2.wallForce(h.position,springLoc)*wf
    h.vel = integral(force) + v0
    h.position = integral(h.vel) + q0
    pdif =runner.position - h.position
    vect = P3toHPR(pdif)
    h.hpr = HPR(getH(vect),0,0)

campan (w, 1, funcw)
camera.position = choose(lbutton, P3((getX(w.position)),(getY(w.position)),0), P3(5, 5, 20))
camera.hpr = choose(lbutton, HPR(getH(w.hpr)+radians(180),getP(w.hpr),0), HPR(0, -pi/2, 0))

start()
