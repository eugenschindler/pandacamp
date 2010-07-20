from Panda import *

sphere(texture = "pics/mm.jpg", hpr = HPR(-time, time*.1, 0), size = .5, position = P3(-2, 0, 2))
sphere(texture = "pics/mm.jpg", hpr = HPR(time, time*.1, 0), size = .5, position = P3(2, 0, 2))
sphere(texture = "pics/mm.jpg", hpr = HPR(-time, -time*.1, 0), size = .5, position = P3(-2, 0, -2))
sphere(texture = "pics/mm.jpg", hpr = HPR(time, -time*.1, 0), size = .5, position = P3(2, 0, -2))



group = ["pics/duck1.jpg", "pics/eric1.jpg", "pics/mike1.jpg", "pics/mike2.jpg", "pics/mike3.jpg", "pics/raft1.jpg",
         "pics/raft2.jpg", "pics/raft3.jpg", "pics/raft4.jpg", "pics/raft5.jpg", "pics/raft6.jpg", "pics/raft7.jpg",
         "pics/raft8.jpg", "pics/raft9.jpg", "pics/rock1.jpg", "pics/rock2.jpg", "pics/rock3.jpg", "pics/rock4.jpg",
         "pics/sea1.jpg", "pics/sea2.jpg", "pics/sea3.jpg", "pics/sea4.jpg"]
maxm = ["pics/mm2.jpg", "pics/mm3.jpg", "pics/mm5.jpg", "pics/mm.jpg", ]
world.color= color(.2, .1, 0)
yd = 0
def launchRandom(pic):
    global yd
    p = unitSquare(texture = pic, size = .5, position = P3(0, yd, 0))
    yd = yd + .01
    p.react1(localTimeIs(.1 + .5*random01()), randomB)
    
def moveB(m):
    m.position = m.position.now() + integral(P3(random01()-.5, random01()-.5, random01()-.5))
    m.size = m.size.now()
    m.color = m.color.now()
    m.hpr = m.hpr.now()
    m.react1(localTimeIs(.5 + random01()), randomB)

def changeSizeB(m):
    m.position = m.position.now()
    m.size = m.size.now()+ integral(.4*random01()-.1)
    m.color = m.color.now()
    m.hpr = m.hpr.now()
    m.react1(localTimeIs(.5 + random01()), randomB)
def spinB(m):
    m.position = m.position.now()
    m.size = m.size.now()
    m.color = m.color.now()
    m.hpr = m.hpr.now()+ integral(HPR(random11()*2, 0, 0))
    m.react1(localTimeIs(.5 + random01()), randomB)

def spinB2(m):
    m.position = m.position.now()
    m.size = m.size.now()
    m.color = m.color.now()
    m.hpr = m.hpr.now()+ integral(HPR(0, random11()*2, 0))
    m.react1(localTimeIs(.5 + random01()), randomB)
def randomB(m, v):
    f = randomChoice([moveB, changeSizeB, spinB, spinB2])
    f(m)
def exitMe(m, v):
    m.exit()


def showPhoto(w, p):
    photo, pieces = slicePicture(p, 10, 1)
    photo.position = P3(0, -3, 0)
    photo.size = step(localTime)
    for strip in pieces:
        t = localTime - 3 - getX(strip.location)
        strip.position = P3(smoothStep(t)*5, -smoothStep(t), 0)

c = tags(maxm, alarm(start = 2, step = 4))

react(c, showPhoto )
for p in group:
    launchRandom(p)
start()
