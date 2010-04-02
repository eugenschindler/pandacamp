from Panda import *

camera.position = P3(0, -2, .5)
world.color = black
ambientlight(color = gray)
directionallight(color = white, hpr = HPR(2,.5, 0))

t = slider(min = 0, max = 1, label = "time")

# Pick three sonic joints  - here there are again:
#  neck, leftEyeBrow, rightEyeBrow,
#  leftLowerSpike, lowerRightSpike, topSpike, leftMiddleSpike
#  rightMiddleSpike, lowerSpike, jaw, leftShoulder, rightShoulder,
#  leftElbow, rightElbow, leftWrist, rightWrist, leftHip, rightHip
#  leftKnee, rightKnee, leftAnkle, rightAnkle
# Pick two HPRs for each joint and put them in below:

hpr1a = HPR(5,0,0)
hpr1b = HPR(-5,0,0)
hpr2a = HPR(0,5,0)
hpr2b = HPR(0,-5,0)
hpr3a = HPR(0,5,0)
hpr3b = HPR(0,-5,0)

# Now we'll interpolate between these two positions for each joint:
hpr1 = interpolate(t, at(hpr1a) + to(1, hpr1b))
hpr2 = interpolate(t, at(hpr2a) + to(1, hpr2b))
hpr3 = interpolate(t, at(hpr3a) + to(1, hpr3b))

s = sonic(hpr = HPR(pi,0,0))
# Fill in the joint names below.
s.Jaw = hpr1
s.leftHip = hpr2
s.topSpike = hpr3

# Add another joint.  You can create an interpolant to attach t to time
# and get sonic to move without a slider
start()
