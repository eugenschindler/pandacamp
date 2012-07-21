from Panda import *
from BrianModels import *
# This is a scene with three moving pandas:

#camera.position = P3(0, -16, 0)
#camera.hpr = HPR(0, 0, 0)
world.color = black
r = rectangle(P3(0,0,0), P3(1,0,0), P3(0,0,1), texture = "brian-name.jpg")
r.hpr = HPR(pi, 0, 0)
r.position = P3(2, 0, -3)
r.size = 5
#three pandas rotating on H P and R respectively
for x in range(11):
    bslug(position = P3(-1.5, x+10, 0), hpr = HPR(pi/2, 0, 0),size=.5)
    bslug(position = P3(1.5, x+10, 0), hpr = HPR(-pi/2, 0, 0),size=.5)

slug(position = P3(0, 28, 0), size = 4)

sphere(size=-800, texture="spaceimage2.jpeg")

directionalLight(color = color(.8, .4, .4), hpr = HPR(1,1,0))
ambientLight(color=color(.6,.6,.6,))
c = alarm(step = .5)
def flame(m, v):
    s = randomInt(10)
    fireish(position = P3(-1.2, 10.81+s, .1), hpr = HPR(0, pi/2, 0), size = .2, duration = .3)
    s2 = randomInt(10)
    fireish(position = P3(1.2, 10.81+s, .1), hpr = HPR(0, -pi/2, 0), size = .2, duration = .3)
react(c, flame)
#saveCamera("test")
launchCamera("test")

start()
