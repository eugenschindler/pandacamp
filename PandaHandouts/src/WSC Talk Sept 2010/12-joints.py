from Panda import *

camera.position = P3(0, -10, .5)
world.color = black
ambientLight(color = gray)
directionalLight(color = white, hpr = HPR(2,.5, 0))

hc1 = control("neck", itimef(at(HPR(0,0,0)) + to(1,HPR(-.28, .8, 0)))) + \
      control("leftEyeBrow", itimef(at(HPR(1, .4, 0)) + to(1, HPR(0, .7,0))))
hc2 = control("neck", itimef(at(HPR(.1,.2,0)) + to(.6,HPR(.4, -.2, .1)))) + \
      control("leftEyeBrow", itimef(at(HPR(1, .2, 0)) + to(.4, HPR(0, .4,0))))
lc1 = control("rightHip", itimef(at(HPR(0,0,0)) + to(1, HPR(0, 1.1,0)))) + \
      control("rightKnee", itimef(at(HPR(0,0,0)) + to(1, HPR(0, -1.1, 0))))
lc2 = control("rightHip", itimef(at(HPR(0,0,0)) + to(.6, HPR(0, 1.1,0)))) + \
      control("rightKnee", itimef(at(HPR(0,0,0)) + to(.6, HPR(0, -.1, 0))))
s1 = sonic(position = P3(0,0,0), size = 2)
s2 = sonic(position = P3(-1.5, 0, 0), size = 2)
s3 = sonic(position = P3(1.5,0,0), size = 2)
s4 = sonic(position = P3(3, 0, 0), size = 2)
s1.control = hc1 + lc1
s2.control = hc1 + lc2
s3.control = hc2 + lc1
s4.control = hc2 + lc2
start()