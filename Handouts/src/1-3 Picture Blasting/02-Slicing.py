from Panda import *
(center, pieces) = slicePicture( "realpanda.jpg", columns = 10,  size = 2)
center.hpr = HPR(time,0,0)
for piece in pieces:
    piece.position = P3((time*piece.x*.2),0,0)
start()