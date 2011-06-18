from Panda import *
sphere(hpr = HPR(time/3,0,0), texture = "redcloud.png", size = -200)
(picture, pieces) = slicePicture( "pandaLogo.jpg", columns = 10, rows = 10, size=2)
picture.hpr = HPR(sin(time)/2,0,0)

for piece in pieces:
    piece.size= step(time-(random01()*2))
    piece.hpr = step(time-6)*HPR(piece.y*time/2, 0,piece.x*time/2)
panda(position= P3(-2,-2,-2), hpr = HPR(pi/4,cos(time)/4,0), texture= "pandaW.jpg", scale = 1.2)
start()