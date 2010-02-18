
import g
from Handle import *
from direct.gui.DirectGui import *
from Time import *
from Types import *
from Text import *

class Slider:
    def __init__(self, size = 1, position = None, min = 0, max = 1, pageSize = None, init = None, name = 'Slider', label = None):
        t = getPType(name)
        if t != stringType:
            argTypeError(self.name, t, stringType, 'name')
        self.name = uniqueName(name)
        if init is None:
            init = min
        if pageSize is None:
            pageSize = (max - min) / 100
        t = getPType(size)
        if t != numType:
            argTypeError(self.name, t, numType, 'size')
        t = getPType(min)
        if t != numType:
            argTypeError(self.name, t, numType, 'min')
        t = getPType(max)
        if t != numType:
            argTypeError(self.name, t, numType, 'max')
        t = getPType(pageSize)
        if t != numType:
            argTypeError(self.name, t, numType, 'pageSize')
        t = getPType(init)
        if t != numType:
            argTypeError(self.name, t, numType, 'init')

        if position is None:
            pos = (.95, 0, g.nextNE2dY)
            g.nextNE2dY = g.nextNE2dY - .1
        else:
            t = getPType(position)
            if t != P2Type:
                argTypeError(self.name, t, P2Type, 'position')
            pos = (position.x, 0, position.y)
        self.slider = DirectSlider(scale = .2*size, pos = pos, range = (min, max), pageSize = pageSize, value = init, command = self.setSlider)
        self.value = SliderValue(self)
        self.svalue = init
        self.reactive = True
        if label is not None:
            text(text = label, position = SP2(pos[0]-.3, pos[2]))

# Doesn't need to be sustained - not reactive
    def set(self, val):
        self.slider['value'] = val

    def setSlider(self):
        self.svalue = self.slider['value']

    def refresh(self):
        pass
    def checkSignals(self, context):
        pass
    def maybeLift(self):
        self.value

def slider(*p, **a):
    res = Slider(*p, **a)
    return res.value
