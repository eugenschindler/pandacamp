from Panda import *

rectangle(P3(-1,0,-1), P3(1,0,-1), P3(-1,0,1), texture = "sarah.bmp")
#fragments = blastPicture("sarah.bmp", 5, 5)  # Cut a panda into 25 squares

#for p in fragments:
#    p.position = p.location
#    p.hpr = HPR(time*random01(), 0, 0)
#    p.size = 2

a = photoWheel(["Ulquiorra.jpg", "moon.jpg", "bleach.jpg" , "cat.jpg", "Powerpuff.jpg", "DeathNote.jpg"], size = 1.5)
a.hpr = HPR(time*2, sin(time), 0)
world.color = purple
fireish(position = P3(-1,0,-1), size = .3)
fireish(position = P3(1,0,-1), size = .3)

start()