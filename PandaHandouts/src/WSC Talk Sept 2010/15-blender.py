from Panda import *
world.color = black
laugh = sound("evilLaugh.wav")
camera.position = P3(0, -25, .5)
ambientLight(color = color(.3, .3, .3))
def scareThem(m, v):
    ambientLight(color = white)
    laugh.play()
    fireWorks(position = P3(5,0,0))
    fireWorks(position = P3(-2,0,0))
    fireWorks(position = P3(-3,0,0))
    fireWorks(position = P3(4,0,0))
    fireish(position = P3(4,1,0))
    fireish(position = P3(-2,1,0))
    fireish(position = P3(4,5,0))
    warpSpeed(position = P3(0,10,0))
react1(timeIs(2), scareThem)
s = modelHandle("tiki.egg", texture= "Tiki.jpg", hpr = HPR(time, 0, 0), size = .8)



start()