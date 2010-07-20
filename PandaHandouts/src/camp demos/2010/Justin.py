from Panda import *
def randomCube(pics):
    pic1 = shuffle(pics)
    return cube(pic1[0], pic1[1], pic1[2], pic1[3], pic1[4], pic1[5])

group = ["pics/duck1.jpg", "pics/eric1.jpg", "pics/mike1.jpg", "pics/mike2.jpg", "pics/mike3.jpg", "pics/raft1.jpg",
         "pics/raft2.jpg", "pics/raft3.jpg", "pics/raft4.jpg", "pics/raft5.jpg", "pics/raft6.jpg", "pics/raft7.jpg",
         "pics/raft8.jpg", "pics/raft9.jpg", "pics/rock1.jpg", "pics/rock2.jpg", "pics/rock3.jpg", "pics/rock4.jpg",
         "pics/sea1.jpg", "pics/sea2.jpg", "pics/sea3.jpg", "pics/sea4.jpg"]
cpics = ["pics/j3.jpg", "pics/j4.jpg", "pics/j5.jpg", "pics/j6.jpg", "pics/j2.jpg", "pics/j.jpg"]
cube1 = randomCube(group)
cube2 = randomCube(group)
cube1.position = P3C(2.5, time, 0)+ P3(0,2,0)
cube2.position = P3C(2.5, time+pi, 0)+ P3(0,2,0)
cube1.hpr = HPR(time, pi/4, 0)
cube2.hpr = HPR(-time, pi/4, 0)
world.color = color(0,0, .3)
c = tags(cpics, alarm(start = 2, step = 3))
def exitMe (m, v):
    m.exit()
def flameMe(m, v):
    f1 = intervalRings(position = P3(0, -2, 0), size = .1, color = yellow)
    f2 = intervalRings(position = P3(0, -2, 0), size = .3, color = white)
    f3 = intervalRings(position = P3(0, -2, 0), size = .5, color = red)
    f1.hpr = HPR(0, pi/2, 0)
    f1.react1(localTimeIs(1), exitMe)
    f2.hpr = HPR(0, pi/2, 0)
    f2.react1(localTimeIs(1.2), exitMe)
    f3.hpr = HPR(0, pi/2, 0)
    f3.react1(localTimeIs(1.4), exitMe)

def flame(m, v):
    s = unitSquare(texture  = v)
    s.position = P3(0, -2, 0)
    s.size = 3*(1-localTime*localTime)
    s.hpr = HPR(localTime, localTime*.2, 0)
    s.react1(localTimeIs(1),exitMe)
    s.react1(localTimeIs(1), flameMe)
react(c, flame)

start()
