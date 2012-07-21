from Panda import *

missles = collection()
ship = spaceship(hpr=HPR(pi,0,0), color=teal, size=.38)
score=var(0)
text(format("Score: %i", score), size = 1.5, position = P2(0, .9))

directionalLight(color = color(.8, .8, .8), hpr = HPR(1,-1,0))
ambientLight(color=color(.6,.6,.6,))

sphere(size=-800, texture="spaceimage2.jpeg", hpr = HPR(time/3, 0, 0)) 
xv=hold(0, key("d",1.5)+key("a",-1.5)+keyUp("d",0)+keyUp("a",0))
zv=hold(0, key("s",-1.5)+key("w",1.5)+keyUp("s",0)+keyUp("w",0))
ship.position=P3(integral(xv),0 ,integral(zv))
camera.position=P3(0, -10, 2.5)

def randomEnemy(m, v):
    enemy = spaceship(position = P3(random11()*4, 15-localTime, (random11()*3)+2), size = .38, duration = 17,color=red)
    ship.react(hit(ship,enemy), blowUp)
    ship.react(hit(enemy, missles), destruct)

def destruct(m, pairs):
    for (m, ball) in pairs:
        m.exit()
        ball.exit()
        score.add(1)
        fireish(position = m.position, duration = .8, size=.18)
        
def blowUp(m, v):
    m.exit()
    play("explosion1.wav")
    resetWorld()
    sphere(size=-800, texture="spaceimage2.jpeg", hpr = HPR(time/3, 0, 0)) 
    text("Game Over",position=P2(0,0), size = 4, color = orange)
    text(format("Your score: %i", score),position=P2(0,-.2), size = 3, color = blue)
def shoot(m,v):
    p=now(m.position)+P3(0,1,0)
    sphere(duration=(7),position=p+integral(P3(0,3,0)),size=.05, color=red, collection = missles)
    play("beep")


ship.react(lbp, shoot)

c = alarm(step = .8)
react(c, randomEnemy)


start()