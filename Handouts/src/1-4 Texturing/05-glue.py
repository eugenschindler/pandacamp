from Panda import *
# You can "glue" objects together by using "reparentTo" - when you reparent one model to another,
# moving the first model will move the other.
# This only works with rectangles and triangles - not other models

# Pick any 4 points in space and join then with 4 triangles
# Color each triangle differently
# reparent each triangle to the first

p1 = P3(-1, -1, 0)
p2 = P3(1, -1, 0)
p3 = P3(0, 1, 0)
p4 = P3(0, 0, 1.5)
m = triangle(p1, p2, p3, color = red)
n = triangle(p1, p2, p4, color = blue)
o = triangle(p1, p4, p3, color = green)
p = triangle(p2, p3, p4, texture = "realpanda.jpg", color = white)
n.reparentTo(m)
o.reparentTo(m)
p.reparentTo(m)
m.hpr = sliderHPR()
start()