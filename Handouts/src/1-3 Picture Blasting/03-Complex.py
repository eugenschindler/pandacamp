from Panda import *

#Use the slicePicture to break up a picture by rows and columns.

(center, r) = slicePicture( "realpanda.jpg", columns = 10,rows = 10,  size = 1)

# Write a for loop to send the pieces in random directions using random11() or
# random01(). The random11() will give a random number between -1 and 1, and the
# random01() gives a random number between 0 and 1. Use both the position  Then add a step to delay
# to breaking up of the peice.
# Note: you don't need the piece.x or piece.y.

for p in r:
    p.position = step(time - 2)* integral(P3(random11(), random11(), random11()))
    p.hpr = step(time - 2) * integral(HPR(random01()*.9, random01() * .9, random11()* .9))


    
start()