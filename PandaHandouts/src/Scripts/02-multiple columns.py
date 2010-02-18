from Panda import *
#This is the contents of the script file
"""
time,pose,pos,orient,color,size
time,Pose C:\pose.csv, P3,HPR,Color,Number
0,right_forward,5 5 5,0 0 0,yellow,1
1, ,1 1 1, , ,4
2,default, 2 2 2,3.14 0 0,black, 1
3, ,-2 -2 -2, ,green,
4,right_forward,-1 -1 -1, ,2
5, ,-5 -5 -5,0 0 0,blue,1
"""
#Other types besides numbers can be used in script files
script = loadScript("C:\panda\lib\script2.csv")
s = sonic(position=interpolate(time,script['pos']), hpr=interpolate(time,script['orient']), size=interpolate(time,script['size']))
s.control = interpolate(time,script['pose'])

s2 = sonic(position=interpolate(time-1,script['pos'])+P3(0,5,0), hpr=interpolate(time-1,script['orient']), size=interpolate(time-1,script['size']))
s2.control = interpolate(time-1,script['pose'])

sphere(color=interpolate(time,script['color']), position=P3(-2,0,2))

start()