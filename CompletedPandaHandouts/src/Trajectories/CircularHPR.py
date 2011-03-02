# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="stu885974"
__date__ ="$Mar 2, 2011 4:01:32 PM$"

from Panda import *
h = slider(min = 0, max = 2*pi, label = "heading")
p = slider(min = 0, max = 2*pi, label = "pitch")
r = slider(min = 0, max = 2*pi, label = "roll")


boeing707(hpr = HPR(h*.5*time,p*.5*time,r*.5*time), size = 2,position = P3(-0, 0, 0))










start()
