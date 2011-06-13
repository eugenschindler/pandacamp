from Panda import *
(center, r) = slicePicture( "realpanda.jpg", 10, 1,  size = 2)
i=0
center.hpr = HPR(time,0,0)
for p in r:
    p.position = P3((time*i*.2),0,0)
    i=i+1
start()