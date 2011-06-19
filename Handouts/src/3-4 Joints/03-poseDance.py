from Panda import *
camera.position = P3(0, -10, .5)
world.color = black
ambientLight(color = gray)
directionalLight(color = white, hpr = HPR(2,.5, 0))

pose = loadPoseFile("pose.csv")

s = sonic(position = P3(0,0,0))
s.control = itimef(at(pose["armsLeft"]) + to(.5,pose["armsRight"]))

s1 = sonic(position = P3(2,0,0))
s1.control = itimef(at(pose["armsForward"]) + to(.5,pose["armsOut"]))

s2 = sonic(position = P3(-2,0,0))
s2.control = itimef(at(pose["egyptian"]) + to(.5,pose["egyptian2"]))
start()
