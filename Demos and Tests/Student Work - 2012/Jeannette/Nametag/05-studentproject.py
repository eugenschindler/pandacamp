from Panda import *

world.color = color(sin(time), cos(time*16), cos(time*8.8))
camera.position = P3(0,time/2-10,0)

rectangle(P3(-5,-5,-5), P3(-5,5,5), P3(5,10,-5), color = color(cos(time*2),sin(time*6),cos(time*8)))
rectangle(P3(5,5,5), P3(5,-5,-5), P3(0,10,-5), color = color(sin(time),cos(time),sin(time*10)))

fireWorks(position = P3(0,0,0), size = 5, hpr = HPR(time, time, time))
lightSnow(position = P3(0,0,0))
warpFace(position = P3(0,0,1))

p = panda(color = color(sin(time*4),cos(time*11),sin(time*12)), hpr = HPR(sin(time),time*2,cos(time*7)))
path = at(P3(-2,0,0)) + to(1, P3(-2,0,1.3)) + to(1, P3(2,0,1.3))
p.position = itime(path)

p = panda(color = color(sin(time*4),cos(time*11),sin(time*12)), hpr = HPR(sin(time),time*2,cos(time*7)))
path = at(P3(2,0,0)) + to(1, P3(2,0,-2)) + to(1, P3(-2,0,-2))
p.position = itime(path)

a = photoWheel(["realpanda.jpg", "Rafts.jpg", "realpanda.jpg" , "Rafts.jpg", "realpanda.jpg", "Rafts.jpg"], size = .5)
a.hpr = HPR(time, 0, 0)
a.position = P3(0,0,1.3)

a = photoWheel(["realpanda.jpg", "Rafts.jpg", "realpanda.jpg" , "Rafts.jpg", "realpanda.jpg", "Rafts.jpg"], size = .5)
a.hpr = HPR(time, 0, 0)
a.position = P3(0,0,-2)


fragments = blastPicture("Rafts.jpg", 30, 20)

for p in fragments:
    p.position = p.location
    p.hpr = HPR(cos(time*2), cos(time*4), cos(time*6))
    p.size = .3*cos(time*2)+1


start()