from Panda import *


p1 = panda(position = P3(-2, 0, 0), hpr = HPR(time, 0, time/10))
p2 = panda(position = P3(0, 0, 0), hpr = HPR(time, 0, time/10), texture = "pandaInvert.jpg")
p3 = panda(position = P3(2, 0, 0), hpr = HPR(time, 0, time/10), texture = "pandaW.jpg")


start()