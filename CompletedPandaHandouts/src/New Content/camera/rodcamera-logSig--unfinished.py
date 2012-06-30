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
cam = sphere(size = 0, color = black)

v0 = P3(0,0,0)

# character
#character = panda()
character = truck()

v = hold(v0, key("arrow_left", P3(-3, 0, 0)) +
             key("arrow_down", P3(0, -3, 0)) +
             key("arrow_up", P3(0, 3, 0)) +
             key("arrow_right", P3(3, 0, 0)) +
             key("space", P3(0,0,0)) +
             key("d", P3(6,0,0)))
             
hpr = P3toHPR(v)
character.hpr = HPR(getH(hpr), getP(hpr), 0)

# initial position and velocity
p0 = P3(0,0,0)
v0 = P3(0,0,0)

# key commands
#v = P3(3,0,0)

k = slider(min = 0, max = 1, init = .5)

# set character position and hpr

character.position = integral(v)

#character.position = 



charHPR = P3toHPR(v)

#key("arrow_left", character.hpr())
#vel = integral(character.hpr - cam.hpr )
hprs = getH(character.hpr - cam.hpr)
c = choose(hprs<0,-log(10)+1, log(10)+1)
#vel = integral(HPR(c,0,0))
text(format("differnce %f", c))
#text(vel)


maxv = 3
maxCamDist = 6
minCamDist = 3


#vel = choose(abs(v) > maxv, choose(v<0,-maxv, maxv), v)
#cam_dist = choose(abs(v) > maxv, integral(maxCamDist - minCamDist), integral(minCamDist))

def logSig(vel, termVel, minD, maxD):
    #e = 2.718281
    #self.pvel = vel
    return (maxD-minD)*(1/(1+math.e**((-vel*(termVel/2))+6)))+minD

def getLogSig(vel, termVel, minD, maxD):
    return (lift(lambda v,t,m,M:logSig(v,t,m,M), "logSig", [numType,numType,numType,numType], numType))(vel,termVel,minD,maxD)


def camVel(vel, thresh, initDIST = 0):
    choose(vel > thresh, @@@@@@@@@@@)  #### TODO: FINISH!
    return (lift())


'''
cam.position = integral(maxCamDist - minCamDist)*HPRtoP3(k) + character.position #+ P3(0,0,3)
cam.hpr = P3toHPR(character.position - cam.position) 
h = 1
camera.position = cam.position + P3(0,0,h)
camera.hpr = cam.hpr + HPR(pi,0,0)
'''
text(abs(v))
#cam.position = logSig(3,maxv,minCamDist,maxCamDist) * HPRtoP3(character.hpr) - character.position
cam.position = -getLogSig(abs(v),maxv,minCamDist,maxCamDist) * HPRtoP3(character.hpr) + character.position
cam.hpr = P3toHPR(character.position - cam.position) 
camera.position = cam.position
camera.hpr = cam.hpr + HPR(pi,0,0)
text(camera.position)


#key("arrow_left", character.hpr + P3())


#camera.rod(character, height = 1)

'''
# put camera on rod
# camera distance slider
camDist = slider(label = "camera distance", min = 0, max = 10, init = 3)
# set camera position
cam.position = -camDist*HPRtoP3(character.hpr)+character.position


# camera behavior
# rotation constant slider
rotK = slider(label = "rotation K", min = 0, max = 1, init = 0.5)

vel = integral(character.hpr - cam.hpr)
cam.hpr = vel*rotK
'''

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

#Glow(amount = .2)

start()
