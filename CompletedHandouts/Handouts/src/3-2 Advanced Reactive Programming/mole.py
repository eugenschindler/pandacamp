from Panda import *

rectangle(P3(-3, 0, -3), P3(3, 0, -3), P3(-3, 0, 3), green)

score = var(0)

text(format("Score: %s", score), color = red, size = 2)

def jump(m):
    m.react1(localTimeIs(1), popup)
    m.score = static(0)
    m.react(leftClick(m), scoreMe)

def scoreMe(m, v):
    score.add(m.score)

def popup(m, v):
    m.score = 1
    m.position = interpolate(localTime, at(m.position.now()) + move(.2, P3(0,-2, 0)) + move(.2, P3(0, 2, 0)))
    m.react1(localTimeIs(.4), hide)

def hide(m, v):
    m.react1(localTimeIs(1), popup)

p = panda(position = P3(0, 1.5, 0))
jump(p)

start()