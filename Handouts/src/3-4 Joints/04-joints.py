from Panda import *

camera.position = P3(0, -10, .5)
world.color = black
ambientLight(color = gray)
directionalLight(color = white, hpr = HPR(2,.5, 0))
t1 = .8
hc1 = control("neck", itimef(at(HPR(0,0,0)) + to(t1,HPR(-.28, .6, 0)))) + \
      control("leftEyeBrow", itimef(at(HPR(1, .4, 0)) + to(t1, HPR(0, .7,0))))
hc2 = control("neck", itimef(at(HPR(.1,.2,0)) + to(t1,HPR(.4, -.2, .1)))) + \
      control("leftEyeBrow", itimef(at(HPR(1, .2, 0)) + to(t1, HPR(0, .4,0))))
lc1 = control("rightHip", itimef(at(HPR(0,0,0)) + to(t1, HPR(0, 1.1,0)))) + \
      control("rightKnee", itimef(at(HPR(0,0,0)) + to(t1, HPR(0, -1.1, 0))))
lc2 = control("rightHip", itimef(at(HPR(0,0,0)) + to(t1, HPR(0, 1.1,0)))) + \
      control("rightKnee", itimef(at(HPR(0,0,0)) + to(t1, HPR(0, -.1, 0))))

s1 = sonic(position = P3(0,0,0))
s2 = sonic(position = P3(-1, 0, 0))
s3 = sonic(position = P3(1,0,0))
s4 = sonic(position = P3(2, 0, 0))
s1.leftEyeBrow = HPR(0,3.14,0)
s1.leftElbow = HPR(-3.14,-0.60,1.92)
s1.leftShoulder = HPR(-0.275579333,-0.771620095,-0.11)
s1.rightElbow = HPR(-0.38,3.14,-1.157)
s1.rightShoulder = HPR(0,3.14,0)

s2.leftEyeBrow = HPR(0,3.14,0)
s2.leftElbow = HPR(-3.14,-0.60,1.92)
s2.leftShoulder = HPR(-0.27,-0.77,-0.11)
s2.rightElbow = HPR(-0.38,3.14,-1.15)
s2.rightShoulder = HPR(0,3.14,0)

s3.leftEyeBrow = HPR(0,3.14,0)
s3.leftElbow = HPR(-3.14,-0.60,1.92)
s3.leftShoulder = HPR(-0.275579333,-0.771620095,-0.11)
s3.rightElbow = HPR(-0.38,3.14,-1.15)
s3.rightShoulder = HPR(0,3.14,0)

s4.leftEyeBrow = HPR(0,3.14,0)
s4.leftElbow = HPR(-3.14,-0.60,1.92)
s4.leftShoulder = HPR(-0.27,-0.771620095,-0.11)
s4.rightElbow = HPR(-0.38,3.14,-1.157)
s4.rightShoulder = HPR(0,3.14,0)

s1.control = hc1 + lc1
s2.control = hc1 + lc2
s3.control = hc2 + lc1
s4.control = hc2 + lc2
start()
