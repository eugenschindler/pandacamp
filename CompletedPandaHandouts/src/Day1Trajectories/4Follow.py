from Panda import *

x0 = -3
y0 = 0
z0 = 0

xv = integral(1)

# Answer: The correct answer for the bonus in bounce is the absolute value
# function. The absolute value function always returns a positive value.
def f(t):
    height = abs(cos(t))
    return P3(x0 + xv, y0, z0 + height)

for x in range(5):
    s1 = soccerBall(position = f(time-x), size = .2, color = green)

start()