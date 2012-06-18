from Panda import *

# A for loop repeats code with a value that changes at each repetition

# Range counts from 0 to a limit, less 1
for x in range(10):
    panda(position = P3(x-5, 0, 0))

# Or you can put values between brackets
for p in [P3(-1, 0, 1), P3(2, 1.5, -1), P3(0, 2, -1.5)]:
        jeep(position = p)

# Challenges:
#  Rotate each panda differently - use x to set the pitch
#  Make each panda move to the right after x seconds
#  Use nested loops to make a 10 x 10 grid of pandas.  Place a y loop inside the x loop
#  Use pairing to give each jeep an initial HPR and position.  Write (pos, hpr)
#    where the P3's are.  Replace for p by for p, hpr

start()
