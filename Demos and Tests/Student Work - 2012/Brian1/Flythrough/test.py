from Panda import *
from BrianModels import *

b1 = bslug()
b1.position = P3(-2, 0, 1)
b1.hpr = HPR(time, 0 ,0)

b2 = bslug()
b2.position = P3(0,0,1)
b2.hpr = HPR(0, cos(time), 0)

b3 = bslug()
b3.position = P3(2,0,1)
b3.hpr = HPR(0, 0, time)

t1 = slug()
t1.position = P3(-2, 0, -1)
t1.hpr = HPR(-time, 0 ,0)

t2 = slug()
t2.position = P3(0,0,-1)
t2.hpr = HPR(0, -cos(time), 0)

t3 = slug()
t3.position = P3(2,0,-1)
t3.hpr = HPR(0, 0, -time)

PLColor = sliderColor(label="DL Color")

dlh = slider(max = 10, min = 0, label="DL heading")
dlp = slider(max = 10, min = 0, label="DL pitch")

dl = directionalLight(color = PLColor, hpr = HPR(dlh,dlp,0) )

start()
