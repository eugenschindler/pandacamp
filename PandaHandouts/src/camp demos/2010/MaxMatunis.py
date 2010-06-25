from Panda import *
sphere(hpr = HPR(time/3,0,0), texture = "redcloud.png", size = -200)
c = alarm(start = 0, step = 3)
camera.position = P3C(20, time, 0)  # Stand back to see the herd of pandas!
camera.hpr=HPR(time+pi/2,0,0)
gravity = P3(0,0,-5)
pointLight(position=P3(5,0,3))
pointLight(position=P3(-5,0,3))
ambientLight(color = color(.3, .3, .3))
s = sound("beep.wav")
def putOut(m, x):
    m.exit()
def deleteMe(m, x):
    f1 = fireish(position = P3(0,0,0), size = 1.5, texture="fire1.png")
    f1.hpr = HPR(0, pi/2, 0)
    f1.react1(localTimeIs(1), putOut)
    p=bunny(size=1,hpr=HPR(pi/2,0,0))
    p.position=P3(localTime,0,-.25)
    s.play()
    m.exit()


def pandaLine(number, place,p):
    if number > 0:
        panda(position = P3 (0,0,0),hpr=HPR(0,p,time*2),size=2)
        pandaLine(number-1,place+P3(1,0,0),p+.2)

def newpanda(m, v):
    p=panda(size=.5)
    p.position=P3(localTime-6,0,-.25)
    p.hpr=HPR(pi/2,0,0)
    p.when1(getX(p.position) > 0, deleteMe)
react(c, newpanda)


pandaLine(100,P3(-3,0,0),time)

start()