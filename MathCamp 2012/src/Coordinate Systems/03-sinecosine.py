from Panda import *

# This demonstrates the sine and cosine functions

amplitude = slider(label = "amp", max = 4, init = 1)
delta = slider(label = "delta", max = 2*pi, init = 0)
freq = slider(label = "freq", max = 10, init = 1)
text(format("Amp = %f Delta = %f freq = %f", amplitude, delta, freq), position = P2(-.5, .9), size = 1.5)

def launcher(f, deltaT):
    c = alarm(step = deltaT)
    react(c, lambda m, v: f(localTime, v))

def wave(t, v):
    panda(size = .2, position = P3(t-3, 0, amplitude*sin(freq*t+delta)))
    bunny(size = .2, position = P3(t-3, 0, sin(t)))

launcher(wave, .1)
start()
