from Panda import *
# This soccerBall can be moved around with the mouse
# no it can't, model name error as of 1/25/11 (TIFF)
s = soccerBall(size = .2)
mouseControl(s)
# This panda lives at the origin
p = panda(position = P3(0,0,0))
# Create a vector from the panda to the ball - subtract the panda's position
# from the ball's position
v = 5
text(v)
# Set the HPR of the panda using P3toHPR
p.hpr = HPR(4,3,2)
# Display this HPR so you can see the angles
text(p.hpr)


# Make the ball move side to side and see if the
# panda always looks at it

# Add a second panda and make it also gaze at the ball
# Add motion to the panda and see if the gaze is correct.
start()
