from Panda import *

x0 = -3
y0 = 0
z0 = 0


# To make the ball appear to bounce across the screen we gave the x coordinate
# travel from left to right, and created a height value for the z coordinate
# that isolates between 1 and -1.

# Try this: Change the cosine function to a sine function. Describe the
# difference between the two.

path = P3(x0 +time, y0, z0+cos(time))
soccerBall(position = path, size = .2, color = green)

# Now make another ball and have follow the original ball. Start by Coping the
# path and soccerBall code, then subtrack one from time in the path code.

# Try this: get the ball to lead in front of the original ball.



start()

# Bonus: if you tried to bounce a ball in real life it would never go to a
# height of -1.  Also the ball is not quite bouncing, but looks like a bouy
# rising and falling in the waves.  To correct this attribute there is a
# function we could apply around the cosine so the value returned would never be
# negative. Do you know what that is?