from Panda import *
# Interpolation is one way of making a function.  You can also use math directly.

# Here's a simple trajectory, expressed as a function of t, in which:
#  The x is t
#  The y coordinate is always 0
#  The z coordinate rises faster and faster with t
def f(t):
    return P3(t, 0, t*t/4)

# Create a soccerball that follows this path (use "time" as your t parameter


# Create a second ball of a different color that follows the same path but
# instead of time use time/2 or time+2 - how does this change things?


# Use a slider to control the time to see these realtionships more easily

start()