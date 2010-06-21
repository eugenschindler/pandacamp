from Panda import *
#This is the contents of the script file
"""
time,pose,pos,hpr
time,Pose sonic.csv,P3,HPR
0,default,-3 0 0,1.57 0 0
1,leftFootForward,,1.57 0 0
2,,1.5 0 0,4.71 0 0
3,rightFootForward,
4,default,-3 0 0,
"""
script = loadScript("03-modifyMe.csv")
s = sonic()
p = panda(position=interpolate(time,script['pos']), hpr=interpolate(time,script['hpr']))

#Add an extra column for a panda to walk by
#Add an extra row for the panda to turn half-way past sonic.


start()