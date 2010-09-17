
from Panda import *

panda(position=P3(0,0,0), size = 2)

pl = pointLight(position =
   sliderP3(min = -10, max =10, label="light"))

sphere(position = pl.position, size = .2)

start()