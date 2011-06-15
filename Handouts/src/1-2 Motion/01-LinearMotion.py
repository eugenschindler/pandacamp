from Panda import *

p0 = P3(0,0,0)
v = P3(3,0,0)

# The integral function turns a speed into a position relative to time.  For 
# example, if you are in a car traveling 60 mph along a straight road, after one 
# minute you will be at the first mile marker. And so when you get to an hour
# you will be at mile 60.  We use the integral function so the computer will 
# know where to display the panda as time passes.

# Try this: change the numbers in the v to gain a better
# understanding of how it reacts with integral.  Don't forget to try decimals.


pos = p0 + integral(v)

p = panda(position = pos)


start()