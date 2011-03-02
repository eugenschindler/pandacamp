# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="stu885974"
__date__ ="$Mar 2, 2011 10:36:59 AM$"

from Panda import *


x = slider(min = -1, max = 1, init = 0)
text(format("X Velocity: %5.3f", x))

def f(t):
    return P3(sin(t), 0, cos(t))
def g(t):
    return P3(integral(x), 0, sin(t))
def h(t):
    height = abs(cos(t))
    return P3(integral(x), 0, height)

#p1 = panda(position = f(time))
#p2 = panda(position = g(time))
s1 = soccerBall(position = h(time), size = .2, color = red)
start()