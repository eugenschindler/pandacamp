
from Panda import *

camera.position = P3(0, -2, .5)
world.color = black
ambientLight(color = gray)
directionalLight(color = white, hpr = HPR(2,.5, 0))

hpr = sliderHPR()

#group the three slider values together

s = sonic()


# Some models have joints - places where you can alter the model shape.
# sonic has a lot of joints:
#  neck, leftEyeBrow, rightEyeBrow,
#  leftLowerSpike, lowerRightSpike, topSpike, leftMiddleSpike
#  rightMiddleSpike, lowerSpike, jaw, leftShoulder, rightShoulder,
#  leftElbow, rightElbow, leftWrist, rightWrist, leftHip, rightHip
#  leftKnee, rightKnee, leftAnkle, rightAnkle

#sets the model's left knee's hpr to the hpr specified.
s.leftEyeBrow = HPR(0,3.141592741,0)
s.leftElbow = HPR(-3.141592741,-0.606272578,1.929047227)
s.leftShoulder = HPR(-0.275579333,-0.771620095,-0.110231653)
s.rightElbow = HPR(-0.385809273,3.141592741,-1.157429338)
s.rightShoulder = HPR(0,3.141592741,0)

s.neck = hpr




start()
# Connect the right knee to the negative of this hpr - what happens?  Why?
# Try out a few of the other joints.
