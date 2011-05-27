from Panda import *

def randomTetra(pics):
    pic1 = shuffle(pics)
    return tetra(pic1[0], pic1[1], pic1[2], pic1[3], v1 = P3(random11(), random11(), random11()), v2 = P3(random11(), random11(), random11()), v3 = P3(random11(), random11(), random11()), v4 = P3(random11(), random11(), random11()))
group = ["pics/duck1.jpg", "pics/eric1.jpg", "pics/mike1.jpg", "pics/mike2.jpg", "pics/mike3.jpg", "pics/raft1.jpg",
         "pics/raft2.jpg", "pics/raft3.jpg", "pics/raft4.jpg", "pics/raft5.jpg", "pics/raft6.jpg", "pics/raft7.jpg",
         "pics/raft8.jpg", "pics/raft9.jpg", "pics/rock1.jpg", "pics/rock2.jpg", "pics/rock3.jpg", "pics/rock4.jpg",
         "pics/sea1.jpg", "pics/sea2.jpg", "pics/sea3.jpg", "pics/sea4.jpg"]
harry = ["pics/h1.jpg", "pics/h2.jpg", "pics/h3.jpg", "pics/h4.jpg", "pics/h5.jpg", "pics/h6.jpg", "pics/h.jpg"]





c = tags(shuffle(group), alarm(start = 0, step = 3))
def launchPhoto(m, f):
    f = unitSquare(texture = f, size = 3)
    f.position = P3(-8 + localTime*2, 2, 0)
react(c, launchPhoto)

def blowUp(m, r):
    m.exit()

def foreground(m, v):
  (center, r) = slicePicture( v, 4, 4, size = 2)
  for square in r:
      square.react1(localTimeIs(1.5+random01()), blowUp)
c1 = tags(harry, alarm(start = 2, step = 3))
react(c1, foreground)

start()
