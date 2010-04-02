from Panda import *
#This is the contents of the script file
"""
time,pose
time,Pose
0,default
1,left_forward
3,right_forward
4,
5,default
"""

script = loadScript("script1.csv")

s = sonic(position = P3(0,0,0), hpr = HPR(pi,0,0))
s.control = interpolate(time,script['pose'])

s2 = sonic(position = P3(-1,0,0), hpr = HPR(pi,0,0))
s2.control = interpolate(time+1,script['pose'])

s3 = sonic(position = P3(1,0,0), hpr = HPR(pi,0,0))
s3.control = interpolate(time-1,script['pose'])
start()