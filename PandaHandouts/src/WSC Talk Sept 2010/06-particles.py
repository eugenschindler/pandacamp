from Panda import *
discoHall(position = P3(0,-6,-3), hpr = HPR(pi/2,0,0), size = .5)

# The "alarm" function generates an event at regular
# intervals - use "start=" and "step=" to control this.
c = alarm(start = 0, step = 2)
pop = sound("laser.wav")


    # Write a function to create a new bear and send it
    # moving right across the screen.  Use "localTime"
    # to create your motion.
def byebye(m, v):
    m.exit()
    pop.play()
fireish(position = P3(5,0,1))
fireish(position = P3(-5,0,1))
fireish(position = P3(5,0,0), hpr = HPR(0,0,pi))
fireish(position = P3(-5,0,0), hpr = HPR(0,0,pi))
warpSpeed(position = P3(5,0,.5), size = .2)
warpSpeed(position = P3(-5,0,.5), size = .2)
def launch(w, x):
  p = panda(position = P3(2*localTime-5,0,0), hpr = HPR(0,-1.5,localTime))
  p.react(localTimeIs(5),byebye)
  p.size = interpolate(localTime, at(0) +to(.5,1) + to(4.5, 1) + to(.5, 0))
camera.position = P3(0,-20,0)

lightlocation = P3C(4, time*3, .25)
lightcolor = green
ambientLight(color = color(.5, .5, 1))
pointLight(color = lightcolor, position = lightlocation)

react(c, launch)

start()