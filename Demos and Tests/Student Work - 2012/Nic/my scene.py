# To change this template, choose Tools | Templates
# and open the template in the editor.
from Panda import*
sphere(size = -1000, color = red)

rectangle(P3(-1000,-1000,-2),P3(1000,-1000,-1), P3(-1000,1000,-1), color = green)
saveCamera("nics scene")
h = 0
for p in range (400):
    velocity = P3(0,-1,0)
    if p % 20==0:
        h = h+5
    panda(position=P3(p, h*10, 0)+integral(velocity))







start()