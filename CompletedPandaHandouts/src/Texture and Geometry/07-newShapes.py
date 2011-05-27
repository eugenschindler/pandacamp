#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="stu624689"
__date__ ="$Feb 9, 2011 2:18:19 PM$"
from Panda import *

p1 = P3 (0, 0, 0)
p2 = P3 (-2, 0, -2)
p3 = P3 (2, 0, -2)
p4 = P3 (0, -2, -2)

sphere(hpr = HPR(time,0,0), color = blue, texture = "realpanda.jpg" , size = 1, position = P3(0, 0, 1))
t1 = triangle(p1, p2, p3, color = red)
t2 = triangle(p1, p2, p4, color = blue)
t3 = triangle(p1, p4, p3, color = green)
t4 = triangle(p2, p3, p4, color = orange)
t2.reparentTo(t1)
t3.reparentTo(t1)
t4.reparentTo(t1)
sphere(hpr = HPR(time/3,0,0), texture = "redcloud.png", size = -200)
camera.hpr = sliderHPR(label = "camera")
t1.hpr = sliderHPR()
start()