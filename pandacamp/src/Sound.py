
# This can play sound in an event handler

import direct.directbase.DirectStart
import g
from Types import *

class Sound:
    def __init__(self, filePath, loopCount = 1, volume = 0.5, kill = None):

        self.filePath = g.pandaPath + "/sounds/" + filePath
        self.type = SoundType
        self.volume = volume
        self.loopCount = loopCount
        loader.loadSfx(self.filePath)
        # Need to do argument type checking
        #self.loopCount
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