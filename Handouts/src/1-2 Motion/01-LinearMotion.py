from Panda import *

# The integral function turns a speed into a position relative to time.  For 
# example, if you are in a car traveling 60 mph along a straight road, after one 
# minute you will be at the first mile marker. And so when you get to an hour
# you will be at mile 60.  We use the integral function so the computer will 
# know where to display the panda as time passes.

# Try this: change the numbers in the velecity to gain a better
# understanding of how it reacts with integral.  Don't forget to try decimals.

location = P3(0,0,0)
velocity = P3(0,0,0)
pos = location + integral(velocity)

# The Spin of an object is determind by the head, pitch, and roll or hpr.
# The direction that the object faces can be changed with the number of
# the hpr(note that hpr is in the increment of pi). To get a object to spin add
# a variable of time to the hpr.

spin = HPR(0,0,0)

# The use of step will add delay to the movement. The object will move once time 
# equals zero so if you substract two from time then the object will start 
# moveing in two secends.

# Try this: move the step function in front of spin. What is delayed? Now try
# using sstep instead of step.

panda(position = step(time)*pos, hpr = spin)

start()