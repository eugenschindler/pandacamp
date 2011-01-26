#works as of 1/25/11 (TIFF)
from Panda import *

p = panda()
text(time)  # Show elapsed time
# Maybe start without the sin(time*3)
b = P3C(3, time, sin(time*3))
p.position = b
# db = deriv(P3(0,0,0), b)
# p.hpr = P3toHPR(db)



start()
