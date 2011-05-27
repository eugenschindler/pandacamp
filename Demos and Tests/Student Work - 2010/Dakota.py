from Panda import *

def randomTetra(pics):
    pic1 = shuffle(pics)
    return tetra(pic1[0], pic1[1], pic1[2], pic1[3], v1 = P3(random11(), random11(), random11()), v2 = P3(random11(), random11(), random11()), v3 = P3(random11(), random11(), random11()), v4 = P3(random11(), random11(), random11()))
group = ["pics/duck1.jpg", "pics/eric1.jpg", "pics/mike1.jpg", "pics/mike2.jpg", "pics/mike3.jpg", "pics/raft1.jpg",
         "pics/raft2.jpg", "pics/raft3.jpg", "pics/raft4.jpg", "pics/raft5.jpg", "pics/raft6.jpg", "pics/raft7.jpg",
         "pics/raft8.jpg", "pics/raft9.jpg", "pics/rock1.jpg", "pics/rock2.jpg", "pics/rock3.jpg", "pics/rock4.jpg",
         "pics/sea1.jpg", "pics/sea2.jpg", "pics/sea3.jpg", "pics/sea4.jpg"]
dak = ["pics/d1.jpg", "pics/d2.jpg", "pics/d3.jpg", "pics/d4.jpg", "pics/d.jpg"]

def randomTet(p):
    r = randomTetra(group)
    r.position = p
    r.size = 1.5
    r.hpr = integral(HPR(random11(), random11(), random11()))
    
for i in range(5):
    for j in range(5):
        randomTet(P3(i-2, random11()*2, j-2))


world.color = itime(at(color(0,.3, 0)) + to(3, color(0, .3, .3)) + to(3, color(.3, 0, 0)) + to(3, color(.3, 0. ,3)))
c = tags(dak, alarm(start = 2, step = 3))
def launchPhoto(m, f):
    f = unitSquare(texture = f)
    f.position = P3(-4 + localTime, -3, 0)
react(c, launchPhoto)
# name.hpr = HPR(time*3, 0, 0)
start()