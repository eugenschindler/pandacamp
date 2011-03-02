# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="stu885974"
__date__ ="$Mar 2, 2011 10:36:59 AM$"

from Panda import *




def f(t):
    return P3(sin(t), 0,cos(t))
def g(t):
    return P3(integral(t*.03), 0, sin(t))
def h(t):
    return P3(-integral(t*.03),0, cos(t))

p = panda(position = f(time))
r1 = r2d2(position = g(time))
r2 = r2d2(position = h(time))

start()