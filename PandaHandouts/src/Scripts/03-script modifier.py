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
script = loadScript("C:\panda\lib\script3.csv")
s = sonic(position=interpolate(time,script['pos']))

#Add an extra column for a panda to walk by
#Add an extra row for the panda to turn half-way past sonic.


start()