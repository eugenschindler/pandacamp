from Panda import *
#This is the contents of the script file
"""
time,hpr1,hpr2,create,destroy,parts
time,HPR,HPR,Event,Event,fire
0,3.14 0 0,0 0 0,panda, ,explode
3, , ,panda, ,
4,0 0 0, ,sonic,,explode
6,0 1 0,3.14 0 0,sonic,panda,fire
8,0 0 0,0 0 0,panda,sonic,
"""

script = loadScript("05-AdvEvents.csv")
p = panda(position=P3(0,0,1), hpr = interpolate(time,script['hpr1']))
s = sonic(position=P3(0,0,-1), hpr = interpolate(time,script['hpr2']))
effect = fireish(position=P3(-1,0,-2), size = .1)

def destroy(m, v):
    if v == "panda":
      global p
      p.exit()
    if v == "sonic":
      global s
      s.exit()

def create(m, v):
    if v == "panda":
        global p
        p = panda(position=P3(0,0,1), hpr = interpolate(time,script['hpr1']))
    if v == "sonic":
        global s
        s = sonic(position=P3(0,0,-1), hpr = interpolate(time,script['hpr2']))

def parts(m, v):
    global effect
    effect.stop()
    if v == "fire":
        effect = fireish(position=P3(-1,0,-2), size = .1)
    if v == "explode":
        effect = explosions(position=P3(1,0,-2))

react(script['create'], create)
react(script['destroy'], destroy)
react(script['parts'], parts)

start()