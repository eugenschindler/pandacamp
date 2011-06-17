from Panda import *

# The integral function turns a speed into a position relative to time.  For 
# example, if you are in a car traveling 60 mph along a straight road, after one 
# minute you will be at the first mile marker. And so when you get to an hour
# you will be at mile 60.  We use the integral function so the computer will 
# know where to display the panda as time passes.

# Try this: change the numbers in the velecity to gain a better
# understanding of how it reacts with integral.  Don't forget to try decimals.

p0 = P3(0,0,0)
velocity = P3(0,0,0)
pos = p0 + integral(velocity)

# The Spin of an object is determind by the head, pitch, and roll or hpr.
# The direction that the object faces can be changed with the number of
# the hpr of s0. To get a object to spin add a number to the hpr of the svelocity.

s0 = HPR(0,0,0)
svelocity = HPR(3,0,0)
spin = s0 + integral(svelocity)

panda(position = pos, hpr = spin)

start()