from Panda import *


world.color = color(sin(time), cos(time*16), cos(time*8.8))

warpSpeed(position = P3(0,10,0))

a = photoWheel(["me.jpg", "raft.jpg", "space1.jpg", "realpanda.jpg"])

a.hpr = HPR(time*2, sin(time), time*3)

a.size = 2+cos(time*2.57)

a.position = P3(0,0,0) + integral (P3(0,2,0))


fragments = blastPicture("space1.jpg", 10,10)
fragments1 = blastPicture("group.jpg", 10,10)
fragments2 = blastPicture("kayak.jpg", 10,10)
fragments3 = blastPicture("raft.jpg", 10,10)



for p in fragments:
    path = at(P3(randomRange(-3,3),0, randomRange(-2,2))) + to(3, p.location + P3(-2,0,2))
    p.position = itime(path)
    
for z in fragments1:
    path2 = at(P3(randomRange(-3,3),0, randomRange(-2,2))) + to(3, z.location + P3(2,0,-2))
    z.position = itime(path2)

for w in fragments2:
    path3 = at(P3(randomRange(-3,3),0, randomRange(-2,2))) + to(3, w.location + P3(-2,0,-2))
    w.position = itime(path3)
    
for t in fragments3:
    path4 = at(P3(randomRange(-3,3),0, randomRange(-2,2))) + to(3, t.location + P3(2,0,2))
    t.position = itime(path4)


start()