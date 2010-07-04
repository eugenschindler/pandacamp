from Panda import *
group = ["pics/duck1.jpg", "pics/eric1.jpg", "pics/mike1.jpg", "pics/mike2.jpg", "pics/mike3.jpg", "pics/raft1.jpg",
         "pics/raft2.jpg", "pics/raft3.jpg", "pics/raft4.jpg", "pics/raft5.jpg", "pics/raft6.jpg", "pics/raft7.jpg",
         "pics/raft8.jpg", "pics/raft9.jpg", "pics/rock1.jpg", "pics/rock2.jpg", "pics/rock3.jpg", "pics/rock4.jpg",
         "pics/sea1.jpg", "pics/sea2.jpg", "pics/sea3.jpg", "pics/sea4.jpg"]
az = ["pics/an1.jpg", "pics/an2.jpg", "pics/an3.jpg"]
world.color = black
(center, r) = slicePicture( "pics/an2.jpg", 4, size = 2)
def blast(p, v):
    p.position = p.position.now() + integral(P3(random11(), 0, random11()))
    p.hpr = integral(HPR(random01()*.9, random01() * .9, 0))
for p in r:
    p.react1(localTimeIs(2 + 3*random01()), blast)
def stage2(p, v):
    (c1, r1) = slicePicture( "pics/an1.jpg", 6, size = 1.5, position = P3(-1.8, 0, 0))
    (c2, r2) = slicePicture( "pics/an3.jpg", 6, size = 1.5, position = P3(1.8, 0, 0))
    c1.hpr = HPR(localTime*.2, 0, 0)
    c2.hpr = HPR(localTime*-0.2, 0, 0)
    for loc, p in r1:
        p.react1(localTimeIs(2 + 3*random01()), blast)
    for loc, p in r2:
        p.react1(localTimeIs(2 + 3*random01()), blast)


react1(timeIs(6), stage2)
unitSquare(texture = "pics/an.jpg", position = itime(at(P3(-10, 0, 0)) + move(7, P3(0,0,0)) + to(3, P3(0, -4, 0))))
start()

