#works just fine 1/25/11 (TIFF)
from Panda import *

# Alter the initial position, velocity, and acceleration

camera.position=P3(0,-30, 6)


def launch(b, p0, v0, a):
    setType(b.velocity, P3Type)
    b.velocity = v0 + integral(a)
    b.position = p0 + integral(b.velocity)

def newBall(m, v):
    launch(panda(), P3(0,0,10), P3(0,0, 5), P3(0,0,-5))

react(lbp, newBall)

start()
