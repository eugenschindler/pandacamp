from Panda import *
# Sphere have a lot of predifined textures.  Look in pictures for some
# planets.  Take a photo and add some border space to it so that it won't
# distort too much and put it on a sphere.

sp = sphere(hpr = HPR(time*time,0,0))

sp.setTexture("r2.png")

start()