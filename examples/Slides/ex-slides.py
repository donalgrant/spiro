import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from spiro import *
from spiro_string import *

S = SpiroData()
F = SpiroFig()

###

S.reset()
cs='time'
c='autumn'
a=9.0
bv=[0.9*a-0.03*a*i for i in range(10)]
for i in range(10):
    S.add(spiro(2.0,Wheel(a,bv[i]),9,slide=lambda t: 1.5))
F.plot(S,cmap=c,color_scheme=cs,save=True)

###

S.reset()
cs='time'
ring = 100
F.plot(spiro(ring,Wheel(-30,31),40,
             slide=lambda t: 0.02*sin(t/30),spacing=0.001),
       cmap='Blues',color_scheme=cs,caption=False)
F.plot(spiro(ring,Wheel(30,25), 40,
             slide=lambda t: 1+0.03*cos(t/30),spacing=0.001),
       cmap='Reds',color_scheme=cs,new_fig=False)
F.save_fig()

###

S.reset()
cs='time'
ring = 100
F.plot(spiro(ring,Wheel(-30,31),40,
             slide=lambda t: 0.1*sin(t/10),spacing=0.0001),
       cmap='Blues',color_scheme=cs,caption=False)
F.plot(spiro(ring,Wheel(30,25),40,
             slide=lambda t: 1+0.3*cos(t/10),spacing=0.0001),
       cmap='Reds',color_scheme=cs,new_fig=False)
F.save_fig()
