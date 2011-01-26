#INCOMPLETE 1/25/11 TIFF
# This soccerBall can be moved around with the mouse
s = soccerBall(size = .2)
mouseControl(s)
# This panda lives at the origin
p = panda(position = P3(0,0,0))
# Create a vector from the panda to the ball - subtract the panda's position
# from the ball's position
v =
text(v)
# Set the HPR of the panda using P3toHPR
p.hpr =
# Display this HPR so you can see the angles
text(p.hpr)


# Make the ball move side to side and see if the
# panda always looks at it

# Add a second panda and make it also gaze at the ball
# Add motion to the panda and see if the gaze is correct.
start()
