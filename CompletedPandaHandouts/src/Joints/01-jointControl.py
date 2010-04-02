from Panda import *

camera.position = P3(0, -2, .5)
world.color = black
ambientlight(color = gray)
directionallight(color = white, hpr = HPR(2,.5, 0))

h = slider(min = -pi, max = pi, label = "h")
p = slider(min = -pi, max = pi, label = "p")
r = slider(min = -pi, max = pi, label = "r")

#group the three slider values together
hpr = HPR(h, p, r)
hpr1 = HPR(pi*time/10, 0, 1)
hpr2 = HPR(time*1, time, 1)
hpr3 = HPR(time, 0, time)

s = sonic(hpr = HPR(pi,0,0))

# Some models have joints - places where you can alter the model shape.
# sonic has a lot of joints:
#  neck, leftEyeBrow, rightEyeBrow,
#  leftLowerSpike, lowerRightSpike, topSpike, leftMiddleSpike
#  rightMiddleSpike, lowerSpike, jaw, leftShoulder, rightShoulder,
#  leftElbow, rightElbow, leftWrist, rightWrist, leftHip, rightHip
#  leftKnee, rightKnee, leftAnkle, rightAnkle

#sets the model's left knee's hpr to the hpr specified.
s.leftKnee = hpr
s.rightKnee = hpr1
s.leftHip = hpr2
s.neck = hpr3

start()
# Connect the right knee to the negative of this hpr - what happens?  Why?
# Try out a few of the other joints.
