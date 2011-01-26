#works fine though not sure what the slider is for 1/25/11 (TIFF)
from Panda import *

# How does drag affect the final velocity?

camera.position=P3(0,-30, 6)
d = slider(min = -1, max = 0, init = 0)
text(format("Drag: %5.3f", d))
def launch(b, p0, v0, a, drag):
    setType(b.velocity, P3Type)
    force = a + b.velocity * drag
    b.velocity = v0 + integral(force)
    b.position = p0 + integral(b.velocity)
    text(b.velocity)


def newBall(m, v):
    launch(panda(), P3(0,0,10), P3(0,0, 5), P3(0,0,-5), 0)
    launch(panda(), P3(1,0,10), P3(0,0, 5), P3(0,0,-5), d)

react(lbp, newBall)

start()
