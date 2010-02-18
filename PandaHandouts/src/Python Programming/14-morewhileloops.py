from Panda import *

count = 0

while(count < 5):
    p = panda(position = P3(cos(count), 0, sin(count)), color = blue)
    count = count + 1

while(count < 10):
    p = panda(position = P3(cos(count), 0, sin(count)), color = green)
    count = count + 1

while(count < 15):
    p = panda(position = P3(cos(count), 0, sin(count)), color = red)
    count = count + 1

while(count < 20):
    p = panda(position = P3(cos(count), 0, sin(count)), color = yellow)
    count = count + 1

start()