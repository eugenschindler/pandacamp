from Panda import *



def h(t):
    return P3(integral(sin(t)), 0, integral(cos(t)))

linearTravel = 0
for x in range(8):

    s1 = soccerBall(position = h(linearTravel+time), size = .2, color = green)
    linearTravel = linearTravel + pi/4

start()
#Accelleration-integarate time
#Hpr-making a constant, and joint motion (two objects spining side by side)
#delayed motion, using functions