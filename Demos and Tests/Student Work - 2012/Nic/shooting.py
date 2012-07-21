from Panda import *


# You attach a reaction to a model by giving the triggering event and the name of the reaction function.  

# exitScene is a built in reaction function

# This tells the panda to exit the scene when the right mouse button is pressed (lbp).

missles = collection()
v = hold(P3(0,0,0), key('a', P3(-2,0,0)) + keyUp('a', P3(0,0,0))+ key('d', P3(2,0,0)) + keyUp('d', P3(0,0,0)))
p = panda(size = .7)
p.position=P3(0,0,-2.5) + integral(v)
world.color = Color(abs(cos(randomRange(-1000,1000))),abs(sin(randomRange(-1000,1000))),abs(cos(randomRange(-1000,1000))))

# This reaction function is used to respond to a mouse click by launching a soccer ball.
# The first parameter is the model that is reacting - the now function is used to find the current
# value of a signal like the position. The soccer ball moves up from the position of the model.

# The value comes from the event that causes the reaction.  lbp doesn't generate a value so we ignore it.
ii = var(0)
def launch(model, value):
    ii.add(1)
    pos = now(model.position)
    c = blue
    if ii.get()% 2 ==0:
        c = red
    soccerBall(position = pos + P3(0,0,1) + integral(P3(0,0,4)), size = .25, color = c, collection = missles)
    fireish(position = pos + P3(0,0,1), duration = 0.5, size = 1-localTime/.5)
p.react(key("space"), launch)


rectangle(P3(-5,4,-4),P3(5,4,-4),P3(-5,4,4),texture = "cute kitty.jpg", hpr = HPR(0,0,time))
def blowUp(m, v):
    m.exit()
    resetWorld()
    rectangle(P3(-5,2,-4),P3(5,2,-4),P3(-5,2,4),texture = "cute kitty.jpg")
    text("Game Over")
def destruct(m, pairs):
    for (m, ball) in pairs:
        m.exit()
        ball.exit()

def randomBunny(m, v):
    b1 = bunny(position = P3(random11()*2, 0, 2-localTime), size = .5, duration = 4.1, color = Color(abs(cos(randomRange(-1000,1000))),abs(sin(randomRange(-1000,1000))),abs(cos(randomRange(-1000,1000)))) )
    p.react(hit(p,b1), blowUp)
    p.react(hit(b1, missles), destruct)


c = alarm(step = .9)
react(c, randomBunny)
# Activities
#   Write a velocity controller that uses the arrow keys to move the panda left and right
#   Make the panda face left or right depending on which way he's going
#   Make the soccer ball come up from the top of the panda instead of the bottom
#   Launch a ball on left mouse or on the space key
#   Change the launch event to generate a color and use this to change the color of the soccer ball
#   Launch a blue ball with the space key and a red one with the left button

# You can create reactions that are not attached to models.  Create a reaction function
# which launches a model into the scene that moves from left to right.
# Launce this model when the space key is pressed.

start()