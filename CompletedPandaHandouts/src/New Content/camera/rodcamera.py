# rodcamera.py
#
# This is a proportional camera controller
# The camera is fixed on a rod
# The rate of change of the heading of the camera is
# proportional to the difference the headings
#

import math
from Panda import *

# create the scene
grassScene()

# camera
#cam = panda(size = .2, color = red)

# character
#character = panda()
character = truck()

# initial position and velocity
p0 = P3(0,0,0)
v0 = P3(0,0,0)

# key commands
v = hold(v0, key("arrow_left", P3(-3, 0, 0)) +
             key("arrow_down", P3(0, -3, 0)) +
             key("arrow_up", P3(0, 3, 0)) +
             key("arrow_right", P3(3, 0, 0)) +
             key("space", P3(0, 0, 0)))

# set character position and hpr
character.position = p0 + integral(v)
charHPR = P3toHPR(v)
character.hpr = HPR(getH(charHPR), getP(charHPR), 0)


#camera.rod(character)

# put camera on rod
# camera distance slider
camDist = slider(label = "camera distance", min = 0, max = 10, init = 3)
# set camera position
cam.position = -camDist*HPRtoP3(character.hpr)+character.position


# camera behavior
# rotation constant slider
rotK = slider(label = "rotation K", min = 0, max = 1, init = 0.5)

vel = integral(character.hpr - cam.hpr)
cam.hpr = vel*rotK+HPR(pi,0,0)

'''# heading difference
diffH = getH(character.hpr) - getH(cam.hpr) - pi # subtrack pi to tell which way to rotate
text(diffH)

def limit(a,b):
    if b>a:
        return a
    else:
        return b

rotLim = 1
#cam.hpr = HPR(diffH*rotK,0,0)'''

# camera perspective
#camera.position = choose(lbutton, P3((getX(cam.position)),(getY(cam.position)),1), P3 (0,0,35)) # place the camera above the scene
#camera.hpr = choose(lbutton, HPR(getH(cam.hpr)+radians(180),getP(cam.hpr),0), HPR(0, 3*pi/2,0)) # looking down

start()
