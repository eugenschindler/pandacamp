# Vectors and interpolation/10-dance.py
from Panda import *
# Create a "dance" that scripts the position, HPR, and color of a model.
# Create three different interpolants, one for each.  Build the interpolants in
# 6 segments of .5 and repeat each forever.
# The position interpolant should use only "move" - start with an "at" in each
# model so each model can be at a different place.
# Put three (or more!) models in your dance.

colori1 = at(red) + to(.5, blue) + to(.5, green) + to(.5, white)
colori = forever(colori1 + reverse(colori1))

hpri = forever(at(HPR(0,0,0)) + move(.5, HPR(0,.3, 0)) + move(.5, HPR(0, -.3, 0)) + move(.5, HPR(0,0,0)) +
               move(.5, HPR(-.2, 0, 0)) + move(.5, HPR(.2, 0, 0)) + move(.5, HPR(0,0,0)))

posi = forever(move(1, P3(0,0,0)) + move(.5, P3(0,0,1)) + move(1, P3(0,0,0)) + move(.5, P3(0,0,-1)))

t = time*4
panda(position = interpolate(t, at(P3(0,0,0)) + posi), hpr = interpolate(t, hpri), color = interpolate(t, colori))
panda(position = interpolate(t, at(P3(-1,0,0)) + posi), hpr = interpolate(t, hpri), color = interpolate(t+1, colori))
panda(position = interpolate(t, at(P3(1,0,0)) + posi), hpr = interpolate(t, hpri), color = interpolate(t+2, colori))
start()
