
from Panda import *

#
#spin1 = HPR(time,0,0)
##spin2 = HPR(-time,0,0)
##spin3 = HPR(0,time,0)
##spin4 = HPR(0,time,0)
#
#panda(position = P3(-1, 0, 0), hpr = spin1)
#panda(position = P3(1, 0, 0), hpr = spin2)
#panda(position = P3(0, 0, 1.5), hpr = spin3)
#panda(position = P3(0, 0, -.5), hpr = spin4)

def stepfn(x):
    choose(time<x, 0, 1)

panda(position = integral(stepfn(3)*P3(1,0,0)))
start()