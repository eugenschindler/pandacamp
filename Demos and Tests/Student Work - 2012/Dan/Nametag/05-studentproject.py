from Panda import *

# Write your own nametag function
world.color = color (abs(sin(time*.3)),abs(cos(time*.9)),abs(cos(time*.4)))

panda(position = P3 (0,0,0))


p = spaceship()
path = at(P3(0,0,0)) + to(3, P3(2, -3, -3)) + to(3, P3(-1, 5, 3)) + to(3, P3(-4, 4, 2)) + to(3, P3(-3, 4, 3))+ to (3, P3 (-2, 6, 4)) + to (3, P3(4, 6, 3))   # This path takes 3 seconds (why?)

p.position = itime(path)

a = photoWheel(["DannyRaft.jpg", "DannyKyak.jpg", "Dannywhoot.jpg", "Dannyiswrightinghisnamealot.jpg", "Dannyisdanny.jpg", "Dannyhasdannydandan.jpg", "Dannywater.jpg","dannyhasnolife.jpg", "wootywoot.jpg","meow.jpg",]*2)


a.hpr = HPR(time*2, sin(time), 3*12*45)

fireish (position = a.position-P3(0, 0, 3))
start()
 
 