from Panda import *
from nickModels import *

sphere (size = -1000,texture="venusmap.jpg")
pl = pointLight(color = color(.5 , 0 , .4 ), position = P3C(4, 10 , .25))
al = ambientLight(color = color(0 , .5 , .4 ))


#saveCamera("nics")
launchCamera("nics")
z = 0
y = 0
for a in range(160):
    x = a % 5
    if x == 0:
        z= z+10
    if z % 40==0 and x ==0:
        z = z%40 
        y = y +10
    p = propeller(size = 3)
    p.position = P3(x*10, y ,z)
    p.hpr = HPR(pi/2,-time*time/2 ,0)


for a in range(80):
    b=bug(size = 10)
    v = integral(P3(randomRange (-7,7),randomRange(-7,7),0))
    b.position = P3(randomRange (-450,450),randomRange(-450,450),randomRange(600,780))+v
    b.hpr = P3toHPR(b.position)
    
for g in range (80):
    b=ghost(size = 10, )
    v = integral(P3(randomRange (-7,7),randomRange(-7,7),0))
    b.position = P3(randomRange (-450,450),randomRange(-450,450),randomRange(400,660))+v
    b.hpr = P3toHPR(b.position)
start()