from Panda import *

x0 = -3
y0 = 0
z0 = 0



# Answer: The correct answer for the bonus in bounce is the absolute value
# function. The absolute value function always returns a positive value.
##path = P3(x0 +time, y0, z0+abs(cos(time)))
#soccerBall(position = path, size = .2, color = green)
#path1 = P3(x0 + time +.5, y0, z0+abs(cos(time+.5)))
#soccerBall(position = path1, size = .2, color = red)
for i in range (5):
    path = P3(x0 +time+i, y0, z0+abs(cos(time+i)))
    soccerBall(position = path, size = .2, color = green)


start()