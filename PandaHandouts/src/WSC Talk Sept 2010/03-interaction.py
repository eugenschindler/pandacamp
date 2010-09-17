from Panda import *
# Interaction

p = panda(position = P3(0, 0, 0),
    size = slider(min = 1, max = 4, init = 2),
    hpr = sliderHPR())

text(p.size)

start()
