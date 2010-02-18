#Basically the same as the derivTest.py in the camp/Calculus... directory.
#I don't think we need two.
#~Kendric 5-29-08

# Works

from Panda import *

p = panda()
text(time)  # Show elapsed time
# Maybe start without the sin(time*3)
b = P3C(3, time, sin(time*3))
p.position = b
db = deriv(P3(0,0,0), b)
p.hpr = P3toHPR(db)
# Explain the math in P3toHPR
#p.HPR = P3(getX(hpr)+radians(90), getY(hpr), 0)


start()