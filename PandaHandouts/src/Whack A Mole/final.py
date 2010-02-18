from Panda import *
score = var(0)

def popDown(p, v):
#  p.position = p.position.now()+P3(0,0,-1)
  path = (at(p.position.now()) + to(1, p.position.now()+P3(0,0,-1)))
  p.position = interpolate(localTime, path)
  up = alarm(start = p.waitTime.now(), step = p.waitTime.now())
  p.react1(up, popUp)
  #Somehow, this is neccessary to make it work
  p.__dict__['up'] = False

def popUp(p, v):
#  p.position=p.position.now()+P3(0,0,1)
  path = (at(p.position.now()) + to(1, p.position.now()+P3(0,0,1)))
  p.position = interpolate(localTime, path)
  down = alarm(start = p.upTime.now(), step = p.upTime.now())
  p.react1(down, popDown)
  p.__dict__['up'] = True

def whackMe(p, v):
  loc = mouse.now()
  p2 = p.pos2.now()
  if (abs(p2-loc)<.1) & p.up:
    sound("whip.wav").play()
    score.add(1)

def makeMole(model, pos3, pos2, waitTime, upTime):
  m = model(position=pos3)
  m.pos2 = pos2
  m.waitTime = waitTime
  m.upTime = upTime
  m.react(lbp, whackMe)
  up = alarm(start = waitTime, step = waitTime)
  m.react1(up, popUp)
  m.__dict__['up'] = False

rectPointBL = P3(-5,5,0)
rectPointBR = P3(5,5,0)
rectPointFL = P3(-5,-5,0)

for i in range(0,3):
  for j in range(0,3):
    makeMole(panda, P3(i*3-3,j*3-3,-1), P2(i*.5-.5, j*.5-.5),rand()*5+1, rand()+1.5)
    #sphere(position=P3(i*3-3,j*3-3,0))

rectangle(rectPointBL, rectPointBR, rectPointFL, purple)

text(score)

#def func(p, v):
#  if (abs(getX(mouse.now())- -0.5)< .1) & (abs(getY(mouse.now())-0.5)<.1):
#    text("Got it!")
#  else:
#    text("nope")
#react(lbp, func)

#add light to make things look interesting
#DLight(hpr=HPR(-50,-10,0), color=blue)

#text(mouse)

camera.position=P3(0,-10,15)
camera.hpr=HPR(0,-1,0)

start()