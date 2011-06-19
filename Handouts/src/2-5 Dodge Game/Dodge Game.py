from Panda import *


m1 = soccerBall(position = P3(0,20,0), color = green)
m1 = soccerBall(position = P3(0,-20,0), color = red)
m1 = soccerBall(position = P3(-20,0,0), color = blue)
m1 = soccerBall(position = P3(20,0,0), color = orange)
m1 = soccerBall(position = P3(0,0,20), color = yellow)
m1 = soccerBall(position = P3(0,0,-20), color = purple)


vel = P3(0,0,0)
pos = P3(0,0,-2.5)

b = blimp(size = .5)
pointForward(b)

s = spaceship(position =pos + integral(vel), hpr = HPR(3.14,0,0),size = .5)


def turnLeft(m, v):
    m.position = P3(3, 0, 2.5) + integral(P3(-1, 0, 0))
    m.when1(getX(m.position) < -3, turnRight)
    
def turnRight(m, v):
    m.position = P3(-3, 0, 2.5) + integral(P3(1, 0, 0))
    m.when1(getX(m.position) > 3, turnLeft)

turnLeft(b, 0)

def keyPress(m,v):
    if (v == 'a'):
        vel.x = -1.5
    if (v == 'd'):
        vel.x = 1.5
    
s.react(key('a','a'),keyPress)
s.react(key('d','d'),keyPress)

def drop(m,v):
    p = panda(position = P3(getX(b.position.now()), 0, getZ(b.position.now())- localTime * (.5 + random01() *2) ),size = .25)
    p.react1(hit(p,s),death)
c = alarm(start = 0,step = 1)
react(c, drop)

def death(m,v):
    explosion(position = m.position.now())
    m.exit()

start()