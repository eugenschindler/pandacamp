# Lights/05-lighting.py

# Add lighting to this scene to make the gorilla army look more sinister
from Panda import *

for x in range(20):
    for y in range(20):
        gorilla(position = P3(3*(x-10), 3*(y-10), 0))

sphere(size = -100, texture = "nebula.png")

t = time/5
camera.position = P3C(20, t, .4)
camera.hpr = HPR(t, 0, 0)
ambientLight(color = color(.3, 0, 0))
directionalLight(color = color(.3, .3, .3), hpr = HPR(time*2, time/2, 0))
pointLight(color = white, position = P3C(20, t*3, 2))
start()