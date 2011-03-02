# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="stu885974"
__date__ ="$Mar 2, 2011 3:47:20 PM$"

from Panda import *



def h(t):
    return P3(integral(sin(t)), 0, integral(cos(t)))

linearTravel = 0
for x in range(8):
    
    s1 = soccerBall(position = h(linearTravel+time), size = .2, color = green)
    linearTravel = linearTravel + pi/4

start()