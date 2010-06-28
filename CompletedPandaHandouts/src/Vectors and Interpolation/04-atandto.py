from Panda import *

# There is a simpler way to do the same thing.  An "interpolant" is
# based on two functions: at and to.  at(p) means that the interpolant is
# at location p, to(t, p) indicates a journey taking time t arriving at
# p.  You can add these together using "+".  For example,
#   i = at(p0) + to(2, p1)
# defines an interpolant starting at (1,2,3) and taking 2 units of time
# to reach (3,2,1).
# To use an interpolant, you need to say "interpolate", as in
#   panda(position = interpolate(t, i))

# Write the previous example using an interpolant:

p0 = P3(1,1, 1)
p1 = P3(2, 0, -1)
soccerBall(position = p0, size = .05, color = red)
soccerBall(position = p1, size = .05, color = blue)

t = slider(min = -1, max = 2, init = 0)
text(t)

p = interpolate(t, at(p0) + to(1, p1) + to(1, P3(0,0,0)))  # Add an interpolant here
panda(position = p)

# Add another destination to the interpolant.
start()