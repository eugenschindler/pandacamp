from Panda import *
# Parcile effects can be controlled just as models are by position, hpr, and size

grassScene()
camera.position = P3(0, -10, 1)
path = P3C(2, time, 0)
path1 = P3C(2, time-.21, 0)

panda(position = path)

likeFountainWater(position = path1)
fireish(position = path1, hpr = HPR (0,5,0))

# Try a different effect.  Add controls for the size and hpr in the effect.
start()