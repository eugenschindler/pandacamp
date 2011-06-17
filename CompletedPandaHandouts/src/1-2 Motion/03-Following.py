from Panda import *

# To get pandas to follow each other when the time in the position has to be
# delayed, a delay in velocity or the pandas start in a line.
# A for loop is used to create multiple pandas, i is the panda being made and
# range is the number of pandas being made. The i can be use to delay the pandas
# inside a step so they are following each other. The step will pause until time is
# is 0 and then the next code will continue.

# Try this :
# 1. Use i in the x of p0, what happens?
# 2. Change the p0 back to 0 and use i in the x of velocity, what happen?
# 3. Change the velocity back to 1 and subtrack i from time in the step?

for i in range(2):
    p0 = P3(0,0,0)
    velocity = P3(1,0,0)
    panda(position = p0+integral(step(time)*velocity))

start()