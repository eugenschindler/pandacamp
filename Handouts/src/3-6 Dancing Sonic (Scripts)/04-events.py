from Panda import *
#This is the contents of the script file
"""
time,sound,create
time,Event,Event
0,sorry,panda
2,whip,sonic
4,evil_laugh,panda
"""

script = loadScript("soundEvents.csv")

def snd(m, v):
    s = sound(v)
    s.play()

def create(m, v):
    if v == "panda":
        panda(position=P3(0, -localTime, 0))
    if v == "sonic":
        sonic(position=P3(-localTime, -localTime, -localTime))
    if v == "tails":
        tails(position=P3 (localTime,-localTime,-localTime))

react(script['sound'], snd)
react(script['create'], create)
start()