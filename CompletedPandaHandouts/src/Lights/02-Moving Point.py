import math
from Panda import *

r2d2(position=P3(0,0,0))


s1 = slider(min=-2*math.pi,max=2*math.pi, init=0)


PLight(position=P3C(s1,s1,5))


start()
