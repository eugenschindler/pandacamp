# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="stu885974"
__date__ ="$Mar 2, 2011 3:17:02 PM$"

from Panda import *



def h(t):
    return P3(t-2, 0, abs(cos(t*2)))

for x in range(5):
    s1 = soccerBall(position = h(time-x), size = .2, color = green)

start()