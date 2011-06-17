from Panda import *

world.color = black

al = ambientLight(color = orange)

gorilla(position = P3(0,15,-2),hpr = HPR(0,0,(.1 * sin(time*100))),size = 5)

bunny(position = P3(-2,0,-2),hpr = HPR(2.8,0,(.1 * sin(time*100))),size = 2)
bunny(position = P3(-.5,0,-2),hpr = HPR(3,0,(.1 * sin(time*100))),size = 2)
bunny(position = P3(.5,0,-2),hpr = HPR(0,0,(.1 * sin(time*100))),size = 2)
bunny(position = P3(0,15,-2),hpr = HPR(0,0,(.1 * sin(time*100))),size = 2)

f1 = fireish(position = P3(-4,10,-1), size = 2)
f2 = fireish(position = P3(4,10,-1), size = 2)
f3 = fireish(position = P3(0,18,0), size = 4)

pl1 = pointLight(color = red, position = P3(-4, 10 , -.25))
pl2 = pointLight(color = red, position = P3(4, 10 , -.25))

start()