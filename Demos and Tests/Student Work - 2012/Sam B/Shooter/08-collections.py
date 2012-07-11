# Demostrate collisions between objects and make a small avoidence game

from Panda import *
world.color = black
rectangle(P3(-5,2,-4), P3(5,2,-4),P3(-5,2,4),texture="space1.jpg")
missles = collection()
score = var (0)
text (score, size = 2)
# Here's a bunny that moves left / right with the arrows:
b = spaceship(hpr = HPR (0,1.5,3.14),size = .5)
v = hold(P3(0,0,0), key("left-arrow", P3(-2, 0, 0)) + key("right-arrow", P3(2, 0, 0))+key ("down-arrow",P3(0,0,-1))+key("arrow_up", P3(0,0,1))+key ("b", P3(0,0,0)))
b.position = P3(0,0,-2) + integral(v)


def shootBall(m, v):
    blimp(size = .2, position = now(b.position) + integral(P3(0,0,3)), duration = 2, collection = missles,hpr = HPR (0,1.5,0)) 
    
# This is what happens if a panda hits a bunny
def blowUp(m, v):
    m.exit()
    play("evilLaugh.wav")
    resetWorld()
    text("Game Over", position  = P3(0,0,0), size = 7)  
    
       
def destruct(m, pairs):
    for (m, ball) in pairs:
        m.exit()
        ball.exit()
        score.add(1)
        fireish(position = m.position, duration = .05)
        play ("explosion1.wav")
# This sends a random panda from above.  If it hits the bunny, the bunny disappears
def randomPanda(m, v):
    p = boeing707(position = P3(random11()*3, 0, 2-localTime), size = .3, duration = 4.1 ,hpr = HPR (0,-1.5,0))
    b.react(hit(b,p), blowUp)
    b.react(hit(p, missles), destruct)
    

# This sends a new panda down every .8 seconds
react(key(" "), shootBall)

c = alarm(step = 2)
react(c, randomPanda)

# Todo:
#  Limit the number of soccerballs that the bunny can shoot.  Use a reactive variable
#  to represent this.  In shootBall, you can use now() to find out how many shots
#  are left.

start()
