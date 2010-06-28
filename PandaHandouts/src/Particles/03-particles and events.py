from Panda import *

#particles can be stopped and started using the .stop() and .start() methods.
#.stop() will stop producing particles, but lets the remaining particles finish
#their path.
#.start() resumes the production of particles.

# Reaction to make an effect stop
def unboom(p, v):
  p.stop()

def boom(p, v):
  effect = intervalRings(position = P3(0,0,0))
  effect.react(localTimeIs(2),unboom) # Wait 2 seconds and stop
  
b = button("boom")
react(b,boom)
# Change the stop to exit - what happens?

# Next, using fireish, use an alarm and tags to define an event that happens
# every second, changing from true to false each time:
# Using alarm and tags, you can
a = tags([True, False], alarm(start = 0, step = 1))

# Use a to start / stop the fire each second.  You'll need a reaction function
# the looks at the value using an if
def startstop(m, v):
    if v:
        m.start()
    else:
        m.stop()
f = fireish(position = P3(-1, 0, 0))
f.react(a, startstop)
# Add a fireish effect that starts and stops with the clock above by
# giving it a reaction.
start()