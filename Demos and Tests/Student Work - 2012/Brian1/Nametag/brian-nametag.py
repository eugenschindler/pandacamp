from Panda import *

sphere(size = -800, texture = "spaceimage2.jpeg", hpr = HPR(time/3, 0, 0))

c=cube("brianpic1.jpg","brianpic2.jpg","brianpic3.jpg","brianpic1.jpg","brianpic2.jpg","brianpic3.jpg")
c.hpr = HPR(time*2, sin(time), 0)
c.position = P3(0,2,0)
fragments = blastPicture("brianpic3.jpg", 15, 15)
fragments1 = blastPicture("brian-name.jpg", 15, 15)


for p in fragments1:
    path = at(P3(random11()*10,-20,random01()))+move(5, P3(0,0,0)) + to((p.x+p.y*15)/70.0 + 2,p.location + P3(0,8,0))
    p.position = itime(path)
for p in fragments:
    path = at(p.location) + to(2+random01(),p.location) + to(3, P3((p.x-5)*randomRange(12, 22), randomRange(8, 18), randomRange(10, 20)))
    p.position = itime(path)
cp = at(P3(0,-9,0))+to(5, P3(0,3,0))
camera.position=itime(cp)
start()