from Panda import *

# During a reaction, you can query a model to see what the value is "right now" of a signal.

p = panda(position = P3(time, 0, 0))
def fireBunny(m, v):
    b = bunny(position = m.position.now() + integral(P3(0,0,1)))
    
p.react(lbp, fireBunny)


start()