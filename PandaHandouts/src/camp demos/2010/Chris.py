from Panda import *
def randomCube(pics):
    pic1 = shuffle(pics)
    return cube(pic1[0], pic1[1], pic1[2], pic1[3], pic1[4], pic1[5])

group = ["pics/duck1.jpg", "pics/eric1.jpg", "pics/mike1.jpg", "pics/mike2.jpg", "pics/mike3.jpg", "pics/raft1.jpg",
         "pics/raft2.jpg", "pics/raft3.jpg", "pics/raft4.jpg", "pics/raft5.jpg", "pics/raft6.jpg", "pics/raft7.jpg",
         "pics/raft8.jpg", "pics/raft9.jpg", "pics/rock1.jpg", "pics/rock2.jpg", "pics/rock3.jpg", "pics/rock4.jpg",
         "pics/sea1.jpg", "pics/sea2.jpg", "pics/sea3.jpg", "pics/sea4.jpg"]
cpics = ["pics/c1.jpg", "pics/c3.jpg", "pics/c4.jpg", "pics/c5.jpg", "pics/c6.jpg", "pics/c7.jpg", "pics/c.jpg"]
cube1 = randomCube(group)
cube2 = randomCube(group)
cube1.position = P3(-1.7, 1, 0)
cube2.position = P3(1.7, 1, 0)
cube1.hpr = HPR(time, pi/4, 0)
cube2.hpr = HPR(-time, pi/4, 0)
world.color = color(0,.3, 0)
c = tags(cpics, alarm(start = 2, step = 2))
def exitMe (m, v):
    m.exit()
def flameMe(m, v):
    f = fireish(position = P3(0, -2, 0))
    f.react1(localTimeIs(1), exitMe)
    
def flame(m, v):
    s = unitSquare(texture  = v)
    s.position = P3(0, -2, 0)
    s.size = 3*(1-localTime*localTime)
    s.react1(localTimeIs(1),exitMe)
    s.react1(localTimeIs(1), flameMe)
react(c, flame)

start()
