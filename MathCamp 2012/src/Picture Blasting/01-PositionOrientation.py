from Panda import *

# This illustrates the 3-D coordinate system and the HPR of a model
p = panda()
p.position = sliderP3(label = "pos", min = -5, max = 5)
p.hpr = sliderHPR(label="hpr")
text(format("panda position: %s", p.position), size = 1.6, position = P2(-.5, .9))
text(format("panda hpr: %s", p.hpr), size = 1.6, position = P2(-.5, .8))

start()
