from Panda import *

# Alter the initial position, velocity, and acceleration

camera.position=P3(0,-30, 6)
springLoc = P3(0,0,10)
sprinkK = 1
friction = -.3

def launch(b, p0, v0):
    setType(b.velocity, P3Type)
    force = (b.position - springLoc) * (1- abs(b.position - springLoc)) + b.velocity * friction
    b.velocity = v0 + integral(force)
    b.position = p0 + integral(b.velocity)

def newBall(m, v):
    p = panda()
    launch(p, P3(2,0,5), P3(0,0, 0))

react(lbp, newBall)

start()
