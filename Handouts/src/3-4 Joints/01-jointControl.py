from Panda import *

camera.position = P3(0, -2, .5)
world.color = black
ambientLight(color = gray)
directionalLight(color = white, hpr = HPR(2,.5, 0))

h = slider(min = 0, max = pi, label = "h")
p = slider(min = 0, max = pi, label = "p")
r = slider(min = 0, max = pi, label = "r")

#group the three slider values together
hpr = HPR(h, p, r)
hpr1 = HPR(0, 0, 0)
hpr2 = HPR(0, 0, 0)
hpr3 = HPR(0, 0, 0)

s = sonic(hpr = HPR(0,0,0))


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


h1 = slider(min = -3, max = pi, label = "h1")
p1 = slider(min = -3, max = pi, label = "p1")
r1 = slider(min = -3, max = pi, label = "r1")

hpr = HPR(h1, p1, r1)
hpr1 = HPR(0, 0, 0)
hpr2 = HPR(0, 0, 0)
hpr3 = HPR(0, 0, 0)

s.rightShoulder = hpr
s.rightElbow= hpr1
h = s.rightWrist
h=hpr2

start()
# Connect the right knee to the negative of this hpr - what happens?  Why?
# Try out a few of the other joints.
