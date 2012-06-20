from Panda import *

# Demonstrate color interpolation, HPR interpolation, cycling, and reversing

# You can interpolate colors as well as points in space.
# Create an interpolant that goes between three different colors and set the
# background color of the world using this - interpolate at the current time.

colori = at(red) + to(.4, white) + to(.2, cyan)

world.color = interpolate(time, colori)
# Things you can do with interpolants:
#  reverse(i): go backwards
#  repeat(n, i): repeat n times
#  forever(i): repeat forever


p = at(P3(0,0,0)) + move(.5, P3(1, 0, 0)) + move(.5, P3(0, 0, 1)) + move(.5, P3(-1, 0, 0)) + move(.5, P3(0, 0, -1))


panda(position = interpolate(time, p))
start()