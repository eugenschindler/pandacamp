from Panda import *
camera.position = P3(0, -2, .5)
world.color = black
ambientlight(color = gray)
directionallight(color = white, hpr = HPR(2,.5, 0))

t = .5*cos(time*2)+.5

# Pick three sonic joints  - here there are again:
#  neck, leftEyeBrow, rightEyeBrow,
#  leftLowerSpike, lowerRightSpike, topSpike, leftMiddleSpike
#  rightMiddleSpike, lowerSpike, jaw, leftShoulder, rightShoulder,
#  leftElbow, rightElbow, leftWrist, rightWrist, leftHip, rightHip
#  leftKnee, rightKnee, leftAnkle, rightAnkle
# Pick two HPRs for each joint and put them in below:

hpr1a = HPR(0,0,2)
hpr1b = HPR(0,0,0)
hpr2a = HPR(0,pi/2,-1)
hpr2b = HPR(0,3.1*pi/2,1)
hpr3a = HPR(3,0,0)
hpr3b = HPR(0,0,4)

# Now we'll interpolate between these two positions for each joint:
hpr1 = interpolate(t, at(hpr1a) + to(1, hpr1b))
hpr2 = interpolate(t, at(hpr2a) + to(1, hpr2b))
hpr3 = interpolate(t, at(hpr3a) + to(1, hpr3b))

r=ralph(position = (P3(-.3,0,0)))
r1 = ralph(position = (P3(.3,0,0)))
# Fill in the joint names below.
r.jaw = hpr1
r.neck = hpr2
r.leftWrist=hpr3

r1.jaw = -hpr1
r1.neck = -hpr2
r1.leftWrist=-hpr3
#fireish
def unboom(r, v):
    r.stop()
def boom(x, pos):
    effect = shakenSparkles(position = P3(pos,0,0)+P3(0,0,1))
    effect.react1(localTimeIs(.2),unboom)
a = alarm(start = 0, step = pi/2)
react(tags([-.5, .5], a),boom)
# Add another joint.  You can create an interpolant to attach t to time
# and get sonic to move without a slider
start()
