
from Panda import *
m = modelHandle("stageone.egg")
m.texture="duuuuuude!.jpeg.tga"
m.size = 0.3
#pointLight(position=P3(0,-5,0),color = white)
m.hpr=HPR(time*.5,time*.5,time*.5)
fireWorks(position=P3(0,0,2))
r = rectangle( P3(2,0,0), P3(3,0,0), P3(2,0,1),texture = "jack.JPG")
text(("Jack B."), size = 2)

start()