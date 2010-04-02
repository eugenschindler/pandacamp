
from Panda import *
text("Use a s w d h to move")
grassScene()

#sonic
runner = sonic()

#constants
v0 = P3(0,0,0)

#movement commands
v = hold(v0, tag(P3(-3, 0, 0), key("a")) +
             tag(P3(0, -3, 0), key("s")) +
             tag(P3(0, 3, 0), key("w")) +
             tag(P3(3, 0, 0), key("d")) +
             tag(P3(0, 0, 0), key("h")))


#sonic vars
p =integral(v)
runner.position = p
hpr = P3toHPR(v)
runner.hpr = P3toHPR(v)





#camera position
camera.position = runner.position + P3 (0,-2,0)
camera.hpr = HPR(0, 3*pi/2,0)





start()