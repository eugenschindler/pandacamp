from Panda import *
# We've been limited by not being able to observe the old value of something like a position or hpr
# when computing the new value.  Within a reaction function, you can use .now() to get the current
# (constant) value of a signal like position or hpr.

# Let's move a panda up and down from it's current location
over = var(False)
p = panda(size = .5)
# This takes the panda, looks at the current position,
# and starts going up from this position
c = alarm(start = 0, step = .7)
score = var(0)
def goUp(p, v):
    here = p.position.now()
     # What should you set the position to?
    p.position = here + P3(0,0,localTime*2)

def goDown(p, v):
    here = p.position.now()
    # What should you set the position to?
    p.position = here + P3(0,0,-localTime*2)
def goLeft(p, v):
    here = p.position.now()
    # What should you set the position to?
    p.position = here + P3(-localTime*2,0,0)
def goRight(p, v):
    here = p.position.now()
    # What should you set the position to?
    p.position = here + P3(localTime*2,0,0)
# On the left button press, go up
def blowUp(s, v):
    print "Explode!"
    p.exit()
    fireish(position = s.position.now())
    over.set(True)
    text("Game Over!")

def stopBall(m, v):
    m.position = m.position.now()
p.react(key("arrow_up"),goUp)
p.react(key("arrow_down"),goDown)
p.react(key("arrow_left"),goLeft)
p.react(key("arrow_right"),goRight)
def launch(w, x):
    if not over.get():
       s =soccerBall(position = P3(localTime
       -5,0,random01()*10-5),size=.4)
       s.when1(getX(s.position)>3, scoreball)
       s.when1(abs(p.position - s.position) < .6, blowUp)
       s.when1(over, stopBall)
react(c, launch)


# Try adding a print statement to the goUp function so
# you can see where you are when you start to go up
# print "Position is " + p.here
# Make the panda turn right as it goes up and left as it goes down.
def scoreball(m, v):
    global score
    m.exit()
    score.add(1)
def bump(w, x):
   score.add(1)

text(score)





start()