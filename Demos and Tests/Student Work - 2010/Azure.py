from Panda import *
def randomCube(pics):
    pic1 = shuffle(pics)
    return cube(pic1[0], pic1[1], pic1[2], pic1[3], pic1[4], pic1[5])
def randomTetra(pics):
    pic1 = shuffle(pics)
    return tetra(pic1[0], pic1[1], pic1[2], pic1[3])
group = ["pics/duck1.jpg", "pics/eric1.jpg", "pics/mike1.jpg", "pics/mike2.jpg", "pics/mike3.jpg", "pics/raft1.jpg",
         "pics/raft2.jpg", "pics/raft3.jpg", "pics/raft4.jpg", "pics/raft5.jpg", "pics/raft6.jpg", "pics/raft7.jpg",
         "pics/raft8.jpg", "pics/raft9.jpg", "pics/rock1.jpg", "pics/rock2.jpg", "pics/rock3.jpg", "pics/rock4.jpg",
         "pics/sea1.jpg", "pics/sea2.jpg", "pics/sea3.jpg", "pics/sea4.jpg"]
az = ["pics/a1.jpg", "pics/a2.jpg", "pics/a3.jpg", "pics/a4.jpg", "pics/a5.jpg", "pics/a6.jpg", "pics/a7.jpg", "pics/a8.jpg"]
cube1 = randomCube(group)
cube1.position =  P3(30, 0, 0)
tet = randomTetra(group)
tet.position =  P3(30, 0, 0)
def newcube(m, v):
    cube1.position = P3C(3, localTime+3, localTime*.2 - 1)
    cube1.hpr = HPR(localTime*.8, localTime*1.3, localTime*1.1)
    cube1.size = 2
react1(timeIs(2), newcube)
w = photoWheel(az, size = 2, position = P3(0, -1, -1+ time*.1))
w.hpr = HPR(time*1.5, .3, 0)
def newtet(m, v):

    tet.position = P3C(2, -localTime+4, 1-localTime*.2)
    tet.hpr = HPR(localTime*.3, localTime*1.2, localTime*.6)
    tet.size = 2
react1(timeIs(4), newtet)
name = unitSquare(texture = "pics/a.jpg", size = 2)
name.position = itime(at(P3(-3, 0, 0)) + to(2, P3(-1, -2, .5 )) + to(3, P3(1, -2.5, 0)) + to(3, P3(0,-3,0)))
# name.hpr = HPR(time*3, 0, 0)
start()