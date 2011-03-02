# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="stu885974"
__date__ ="$Mar 2, 2011 3:00:04 PM$"


from Panda import *

x = slider(min = -1, max = 1, init = 0)
text(format("X Velocity: %5.3f", x))

def h(t):
    height = abs(cos(t))
    return P3(integral(x), 0, height)

s = soccerBall(position = h(time), size = .2, color = red)

start()