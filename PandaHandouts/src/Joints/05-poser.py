from Panda import *


#open the poser.py and create three poses: rightForward(where the right foot is forward 
# and the left one is back), stand(where the feet are together),
# and leftForward(where the left foot is forward and the right one is back.)
#make sure the file has the right name.



r = ralph(position = P3((time/10)-1,0,0), HPR = P3(pi/2,0,0))

#interpolate the poses so that it looks like the model is walking.
m = repeat(at(d["leftForward"])+to(1,d["stand"])+to(1,d["rightForward"])+to(1,d["stand"])+to(1,d["leftForward"]))
s.control = interpolate(time,m)

rectangle(P3(-1,1,0),P3(-1,-1,0), P3(1,1,0), purple)



start()
