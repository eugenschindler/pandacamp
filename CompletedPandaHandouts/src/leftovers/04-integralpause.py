from Panda import *

text("Use s to stop, d to resume")
sig = hold(10,key('s', 0)+key('d', 10)+key('a', -10))
p = panda(position = P3(0, 10, 3-0.3*integral(sig)))


start()