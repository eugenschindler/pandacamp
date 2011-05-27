from Panda import *
s = modelHandle("demonskull.egg")
s.position = P3(0,3,1)
s.size = 0.5
s.color = green

s.texture = "pandas.jpg"
#lp = sliderP3(min = -10, max =10, label="light")
#text(lp)
s.hpr = HPR(sin(time)/2,2.09, 0)
#s.hpr = sliderHPR()
pointLight(position=P3(0,0,0), color = green)
warpSpeed(position = P3(0,0,-1))
#ambientLight(color = color(5 , 0 , 0 ))
world.color = black

likeFountainWater(position = P3(0,0,-3))
likeFountainWater(position = P3(-2,0,-3))
likeFountainWater(position = P3(2,0,-3))
#likeFountainWater(position = P3(-4,0,-3))
#likeFountainWater(position = P3(4,0,-3))
#likeFountainWater(position = P3(-3,0,-3))
#likeFountainWater(position = P3(3,0,-3))
#likeFountainWater(position = P3(-1,0,-3))
#likeFountainWater(position = P3(1,0,-3))
m = sound("evilLaugh.wav")
#text(s.hpr)
text("Green is epic!!")
c = alarm(start = 0, step = 7)
#rectangle(P3(10,0,0), P3(10,0,0), P3(0,0,10),hpr = HPR(0,90,0), texture = "realpanda.jpg")

def launch(w, x):
    p = bunny(position = P3(0, -localTime*5,-2.4), texture = "pandas.jpg", hpr = HPR(0,0,0))
    p2 = bunny(position = P3(-2, -localTime*5, -2.4), texture = "pandas.jpg", hpr = HPR(0,0,0))
    p3 = bunny(position = P3(2, -localTime*5, -2.4), texture = "pandas.jpg", hpr = HPR(0,0,0))
    p4 = bunny(position = P3(4, -localTime*5,-2.4), texture = "pandas.jpg", hpr = HPR(0,0,0))
    p5 = bunny(position = P3(-4, -localTime*5, -2.4), texture = "pandas.jpg", hpr = HPR(0,0,0))
    m.play()


react(c, launch)

camera.position = P3(0,-13,0)

start()
