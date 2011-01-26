#CSV sonic.csv not found.
#File sonic.csv not found.
#uh oh needs fixing 1/25/11 (TIFF)
from Panda import *


#open the poser.py and create three poses: rightForward(where the right foot is forward 
#open the poser.py and create three poses: rightForward(where the right foot is forward
# and the left one is back), stand(where the feet are together),
# and leftForward(where the left foot is forward and the right one is back.)
#make sure the file has the right name.
d = loadPoseFile('sonic.csv')

r = sonic(position = P3((time/10)-1,0,0), hpr = HPR(pi/2,0,0))


r = ralph(position = P3((time/10)-1,0,0), hpr = HPR(pi/2,0,0))

#interpolate the poses so that it looks like the model is walking.
r.control = itime(forever(at(d["leftFootForward"]) + to(1, d["rightFootForward"]) + to(1,d["leftFootForward"])))
rectangle(P3(-1,1,0),P3(-1,-1,0), P3(1,1,0), purple)

start()
