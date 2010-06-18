import math
from Panda import *

panda(position=P3(0,0,0))

lp = sliderP3(min = -10, max =10, label="light")

PLight(position=lp)
sphere(position = lp, size = .2)

start()
