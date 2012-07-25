from Panda import *

pieces = blastPicture("mathcamp.jpg", 5, 5)

for p in pieces:
    lat = -getZ(p.location)
    long = pi*getX(p.location) + time
    p.position = HPRtoP3(HPR(long, lat, 0))*2
    p.hpr = HPR(long, lat, 0)
    p.size = 2

start()
