from Panda import *

# 
world.color = black
warpSpeed(position = P3(0,2,0), color = white)
marti = ["pics/m.jpg", "pics/m1.jpg", "pics/m2.jpg", "pics/m5.jpg", "pics/m6.jpg", "pics/m7.jpg", "pics/m8.jpg", "pics/m9.jpg", "pics/m10.jpg" ]
angle = 2*pi/len(marti)
pw1 = photoWheel(marti, size = 2, position = P3(.5, 0, -0.5))
pos1 = at(HPR(-pi/2+angle/2,0,0)) + forever(move(1, HPR(angle, 0, 0)) + move(1, HPR(0,0,0)))
pw1.hpr = interpolate(integral(floor(time*.1)+1), pos1)
m1 = list(marti)
m1.reverse()
pw2 = photoWheel(m1, size = 1, position = P3(.5, 0, -1.8))
pos2 = at(HPR(-pi/2+angle/2,0,0)) + forever(move(1, HPR(-angle, 0, 0)) + move(1, HPR(0,0,0)))
pw2.hpr = interpolate(integral(floor(time*.1)+1), pos2)
group = ["pics/duck1.jpg", "pics/eric1.jpg", "pics/mike1.jpg", "pics/mike2.jpg", "pics/mike3.jpg", "pics/raft1.jpg",
         "pics/raft2.jpg", "pics/raft3.jpg", "pics/raft4.jpg", "pics/raft5.jpg", "pics/raft6.jpg", "pics/raft7.jpg",
         "pics/raft8.jpg", "pics/raft9.jpg", "pics/rock1.jpg", "pics/rock2.jpg", "pics/rock3.jpg", "pics/rock4.jpg",
         "pics/sea1.jpg", "pics/sea2.jpg", "pics/sea3.jpg", "pics/sea4.jpg"]
def path(t):
    return P3(-2.3, 2*sin(t), 2*cos(t))
i = 0
l = len(group)
for p in group:
    pic = unitSquare(size = .45, texture = p)
    pic.position = path(time + i*2*pi/l)
    i = i + 1
start()
