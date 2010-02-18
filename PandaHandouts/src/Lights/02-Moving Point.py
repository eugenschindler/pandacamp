from Panda import *

modelHandle(g.pandaPath +"/models/aGUY", position=P3(0,10,2), localOrientation=HPR(3,0,0))

DLight(hpr=HPR(0,0,0))
camera.position = P3(0,-20,3.5)

start()
