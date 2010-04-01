from Panda import *

script = loadScript("script6.csv")

#This dictionary can then be accessed using the names on the top line of the csv file (Sonic and Sonic2, in this case)

#create a sonic model and set the control to the interpolate of time and the dictionary entry.


s1 = sonic(position=P3(-.5,0,-1), hpr=HPR(pi,0,0),size=itime(script["size"]))
s2 = sonic(position=P3(1,0,-1), hpr=itime(script["hpr"]),size=itime(script["size"]))

s1.control = interpolate(time, script['Sonic'])

s2.control = interpolate(time, script['Sonic2'])

chicken = sound("chickenDance.wav")
chicken.play()

#camera.position = interpolate(time,script["cameraPos"])

def die(p,v):
    p.stop()

def fire(p, v):
    fireish(position=P3(2,0,v)).react1(localTimeIs(.05),die)

react(tags([-1.5,-.5,.5,1.5],script["explode"]),fire)

text(time)
#DLight(hpr=HPR(0,0,0), color=interpolate(time,script['move1']))
#
#m = monster()
#y = slider()
#w = color(y,0,0)
#x = explosion(position=P3(0,0,0), startColor=green, endColor=w)

start()