from Panda import *

r = slider(label = "Distance", max = 6)
theta = slider(label = "Angle", max = 2*pi)
z = slider(label = "Height", min = -4, max = 4, init = 0)
text(format("R = %f Theta = %f z = %f", r, theta, z), position = P2(-.4, .9), size = 1.5)
p = P3C(r, theta, z)
text(format("Position = %s", p), position = P2(-.4, .8), size = 1.5)

panda(position = p)


start()