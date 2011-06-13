from Panda import *

world.color = black
#Use the slicePicture to break up a picture by rows and columns.
(center, r) = slicePicture( "realpanda.jpg", 10, 10,  size = 2)
#Define blast to move pieces in randam directions.
def blast(p, v):
    p.position = p.position.now() + integral(P3(random11()*getX(p.location), random11(), random11()*getZ(p.location)))
    p.hpr = integral(HPR(random01()*.9, random01() * .9, 0))
#Write a for loop to blast each piece of the picture.
for p in r:
    p.react1(localTimeIs(2 + getX(p.location)), blast)
start()