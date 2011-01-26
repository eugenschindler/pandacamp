# works fine 1/25/11 (TIFF)
# Some useful math functions
from Panda import *
#
t = time - 2
# Replace t with some function of t, like floor(t)
p = panda(position = P3(t, 0,0))
# Don't change this one
p2 = panda(position = P3(t, 0,1))
# Replace the time-2 in p with the following:
#   floor (largest integer <= x)
#   ceiling (smallest integer >= x)
#   fraction (x - floor(x))
#   step (0 if x < 0; 1 if x >= 0)
#   sqrt (square root)  ( Avoid sqrt of a - number)
#   t*t

# Try making t a slider instead of time-2


start()