#works 1/25/11 (TIF)
from Panda import *

#for p in [P3(0,0,0), P3(1,0,0), P3(-1, 0, 0), P3(1,0,1)]:
#    panda(position = p)

for m, p in [(panda, P3(0,0,1)), (chair, P3(-2, 0, 0))]:
    m(position = p)

for x in [1, 3, 6]:
    panda(position = P3(1,0,0) * x * time)
    
start()
