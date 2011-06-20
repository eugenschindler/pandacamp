from Panda import *

# Use the slicePicture to break up a picture by rows and columns.

(picture, pieces) = slicePicture( "realpanda.jpg", columns = 5, rows = 5, size = 2)

for piece in pieces:
    piece.position = integral(P3(random01(), 0, 0))

# Write a for loop to send the pieces in random directions using random11() or
# random01(). The random11() will give a random number between -1 and 1, and the
# random01() gives a random number between 0 and 1. Use both the position and hpr.
# Then add a step to delay to breaking up of the peice.
# Note: you don't need the piece.x or piece.y.


    
start()