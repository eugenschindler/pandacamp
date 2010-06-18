from Panda import *

#Particle effects are created much like Models.
#Simply call the function with the name of the particle effect
world.color = black
#intervalRings(position = P3(0,0,0))
#likeFountainWater(position = P3(0,0,0))
#shakenSparkles(position = P3(0,0,0), color=yellow, endColor=blue)
#warpSpeed(position = P3(0,10,0))
#heavySnow(position = P3(0,0,0))
#lightSnow(position = P3(0,0,0))
#p = explosion(position = P3(0,0,0))
#fw = fireWork(position = P3(0,0,0))
#ex = explosion(position = P3(-1,0,0) )

f = fireish(position = P3(0,0,1), texture="myfire.png")
def shutup(m, v):
    m.stop()
f.react1(localTimeIs(1), shutup)


# Run each of these and see what they do

start()
