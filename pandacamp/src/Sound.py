
# This can play sound in an event handler

import direct.directbase.DirectStart
import g
from direct.actor import Actor
from Time import *
from Signal import *
from Numerics import *
from Types import *
from Switchers import *
from Handle import *


class Sound:
    def __init__(self, filePath, loopCount = 1, volume = 0.5, kill = None):

        self.filePath = getSoundFile(filePath)
        self.type = SoundType
        self.volume = volume
        self.loopCount = loopCount

        #Why are we loading it twice? -Michael Reed s10
        # loader.loadSfx(self.filePath)
        # Need to do argument type checking
        #self.loopCount
        print self.filePath
        self.sound = loader.loadSfx(self.filePath)
        self.sound.setVolume(self.volume)
    def __str__(self):
        "Sound: " + self.filePath
    def play(self):
        if self.loopCount != 1:
            self.sound.setLoop(True)
            self.sound.setLoopCount(self.loopCount)
        self.sound.play()
        return self.sound

def sound(*p, **k):
    return Sound(*p, **k)


def getSoundFile(file):
    f = Filename.expandFrom(file)
    if (f.exists()):
        return f
    f = g.pandaPath + "/sounds/" + file
    if (Filename.expandFrom(f).exists()):
        print "Loaded from library:" + f
        return f
    print "Sound " + file + " not found."
    return Filename.expandFrom(g.pandaPath + "/sounds/duck.wav")
