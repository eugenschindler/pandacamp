from Panda import *

pieces = blastPicture("mathcamp.jpg", 5, 5)

for p in pieces:
    p.position = p.location + P3(sin(time*(p.x+1)), cos(time*(p.x+1)), 0)

start()