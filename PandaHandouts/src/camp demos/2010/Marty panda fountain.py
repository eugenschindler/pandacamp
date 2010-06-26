from Panda import *

# Alter the initial position, velocity, and acceleration

camera.position=P3(0,-30, 6)
p=panda

def launch(b, p0, v0, a):
    setType(b.velocity, P3Type)
    b.velocity = v0 + integral(a)
    b.position = p0 + integral(b.velocity)

def newBall(m, v):
    launch(panda(color=Color(randam01, random01 ,0 ())), P3(0,0,10), P3(0,0, 0), P3(0,0,-5))
    launch(panda(color=Color(random, random01,0 ())), P3(0,0,10), P3(4,0, 5), P3(0,0,-5))
    launch(panda(color=Color(random, random01,0 ())), P3(0,0,10), P3(-4,0, 5), P3(0,0,-5))
    launch(panda(color=Color(random, random01,0 ())), P3(0,0,10), P3(2,0, 5), P3(0,0,-5))
    launch(panda(color=Color(random, random01,0 ())), P3(0,0,10), P3(-2,0, 5), P3(0,0,-5))
    launch(panda(color=Color(random, random01,0 ())), P3(0,0,10), P3(1,0, 5), P3(0,0,-5))
    launch(panda(color=Color(random, random01,0 ())), P3(0,0,10), P3(-1,0, 5), P3(0,0,-5))

react(lbp, newBall)
p.color=random01 ()
start()
