from Panda import *

camera.position = P3(0,-100,0)

#while loops repeat until a condition is met
#this while loop repeats 10 times

count = 0
while(count < 10):
    p = panda(position=P3(2*random.randint(-count, count), 0, 2*random.randint(-count, count)),
        size=count)
    count = count + 1

start()