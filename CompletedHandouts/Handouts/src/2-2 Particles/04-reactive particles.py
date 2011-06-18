from Panda import *
# The following code makes a ball bounce - don't worry about how.
def bounce(b, v):
  boom(b.position.now())  # When the ball bounces, call boom
  b.velocity = P3(.5,0,3) + integral(P3(0,0,-3))

# This is a stopping reaction
def unboom(p, v):
  p.exit()
# This is what puts the little explosion at the bounce point.
# Try changing this effect to some of the others.
# The position marks the center of the ball so you need to move the effect
# down a little.

def boom(pos):
  effect = likeFountainWater(position = pos+P3(0,0,-.55))
  effect.react(localTimeIs(0.2),unboom)

ball = soccerBall()

#This is all the math associated with the bouncing ball
setType(ball.velocity, P3Type)
ball.velocity = integral(P3(0,0,-3))
ball.position = P3(-3,0,-2) + integral(ball.velocity)
ball.when(getZ(ball.position) < 0, bounce)

start()