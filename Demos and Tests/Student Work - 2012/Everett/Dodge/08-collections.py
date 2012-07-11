# Demostrate collisions between objects and make a small avoidence game

from Panda import *
score = var(0)
text(score, color = blue)
rectangle(P3(-4,1,-3),P3(4,1,-3),P3(-4,1,3),texture="snow.png")
missles = collection()
ammo=var(10)
#text("ammunition: " ,position = P3(1,0,1),color=red)
# Here's a bunny that moves left / right with the arrows:
ralph1 = ralph()
v = hold(P3(0,0,0), key("left-arrow", P3(-1, 0, 0)) + key("right-arrow", P3(1, 0, 0))+happen(getX(ralph1.position) > 3.5, P3(-1, 0, 0)) +
      happen(getX(ralph1.position) < -3.5, P3(1, 0, 0)))
ralph1.position = P3(0,0,-2) + integral(v)

def shootBall(m, v):
    ammo.add(-1)
    boeing707(size = .2, position = now(ralph1.position) + P3(0, 0, 1) + integral(P3(0,0,3)),
              duration = 2, collection = missles, hpr = HPR(0, pi/2, localTime*8))
    
# This is what happens if a panda hits a bunny
def blowUp(m, v):
    
    play("evilLaugh.wav")
    resetWorld()
    rectangle(P3(-4,1,-3),P3(4,1,-3),P3(-4,1,3),texture="sad face.jpg")
    text("You lost. Get more ammo next time!!!",size=2, position = P3(0,0,0),color=Color(.7,.3,0))

       
def destruct(m, pairs):
    for (m, ball) in pairs:
       # r2d2(size = .5, position = now(m.position) + integral(P3(0,0,-3)), duration = 2, collection = missles2)

        m.exit()
        ball.exit()
        score.add(1)
        play("explosion1.wav")
        if now(score) == 199:
            play("ChickenDanceCUT.wav")
            resetWorld()
            rectangle(P3(-4,1,-3),P3(4,1,-3),P3(-4,1,3),texture="face.jpeg")
            text("You win. Play again!!!",size=4, position = P3(0,0,0),color=Color(.7,.3,0))

# This sends a random panda from above.  If it hits the bunny, the bunny disappears
def randomPanda(m, v):
    p = panda(position = P3(random11()*3, 0, 2-localTime), size = .3, duration = 4.7   )
    p.react(hit(ralph1
    ,p), blowUp)

    ralph1.react(hit(p, missles), destruct)
# This sends a new panda down every .8 seconds
react(key(" "), shootBall)

    

c = alarm(step = 2)
react(c, randomPanda)


    #text(format("Score " %score), position = P3(0,0,-10) )
# Todo:
#  Limit the number of soccerballs that the bunny can shoot.  Use a reactive variable
#  to represent this.  In shootBall, you can use now() to find out how many shots
#  are left.

start()
