from Panda import *

c = alarm(start = 0, step = 1)

score = var(0)
lines = var(10)
camera.position = P3(0, -46, 8)  # Stand back to see the herd of pandas!
Text(score)
# This function puts a line of panda
def tick(m,v):
    score.add(1)

def deletePanda(m, v):
    m.exit()

def deleteLine(m,v):
    score.sub(1)
    lines.sub(1)        
    m.exitVar.set(True)
    m.exit()

def pandaLine(number, place, p,n, v):

    if number > 0:
        if (n== number):

            p1 = panda(position = place, hpr = HPR(p/5,p*1.2,p/2))
            p1.exitVar = static(v)
            p1.react1(leftClick(p1), deleteLine)
 
        else:
 
            p1 = panda(position = place, hpr = HPR(p/5,p,p/2))
            p1.exitVar = static(v)
            p1.when1(v, deletePanda)
        pandaLine(number-1, place + P3(1,0,0), p + .3, n, v)


        
#def pandaLine2(number, place, p):
#    if number > 0:
#        panda(position = place, hpr = HPR(0,p,0))
#        pandaLine(number-1, place + P3(1,0,0.5), p + .3)
#def pandaLine1(number, place, p):
#    if number > 0:
#        panda(position = place, hpr = HPR(0,p,0))
#        pandaLine(number-1, place + P3(1,0,.1), p + .3)
# Make a line of 10 pandas that starts at P3(-4,0,0)
def pandas(pos):
    var1= var(False)
    pandaLine(10, pos, time,randomInt(10)+1, var1)

pandas(P3(-6, 0, 0))
pandas(P3(-6, 0, 2))
pandas(P3(-6, 0, 4))
pandas(P3(-6, 0, 6))
pandas(P3(-6, 0, 8))
pandas(P3(-6, 0, 10))
pandas(P3(-6, 0, 12))
pandas(P3(-6, 0, 14))
pandas(P3(-6, 0, 16))
pandas(P3(-6, 0, 18))

if lines < 1 :
    react(c,tick)
react(lbp,tick)
#pandaLine(10, P3(-6, 0, 2), time,random01())
#pandaLine(10, P3(-6, 0, 4), time,random01())
#pandaLine(10, P3(-6, 0, 6), time,random01())
#pandaLine(10, P3(-6, 0, 8), time,random01())
#pandaLine(10, P3(-6, 0, 10), time,random01())
#pandaLine(10, P3(-6, 0, 12), time,random01())
#pandaLine(10, P3(-6, 0, 14), time,random01())
#pandaLine(10, P3(-6, 0, 16), time,random01())
#pandaLine(10, P3(-6, 0, 18), time,random01())

#pandaLine1(100, P3(-3, 0, 0), time)
#pandaLine2(100, P3(-3, 0, 0), time)

# Can you make a line of 20 pandas?
# Can you put two pandas in a stack at each position?
# Can you have the roll change as well as the position?
# Can you make the line rise?

start()