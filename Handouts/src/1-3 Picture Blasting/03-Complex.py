from Panda import *

world.color = black
#Use the slicePicture to break up a picture by rows and columns.
(center, r) = slicePicture( "realpanda.jpg", 10, 10,  size = 2)
#Define blast to move pieces in randam directions.
for p in r:
    p = integral(step(time-2)*v)
    p.position = integral(P3(random11()*getX(p.location), random11(), random11()*getZ(p.location)))
    p.hpr = integral(HPR(random01()*.9, random01() * .9, 0))
#Write a for loop to blast each piece of the picture.

    
start()