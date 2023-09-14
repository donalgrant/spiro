import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from spiro import *
from spiro_string import *
from Ring import *

S = SpiroData()
F = SpiroFig()

###

F.plot(spiro_steps(Ring(10.0),Wheel(3,1),1.0,40,7),
       color_scheme='v-waves',new_fig=False)
F.plot(spiro(Ring(10.0),Wheel(9,4),40),
       color_scheme='h-waves',new_fig=False)
F.plot(spiro(Ring(10.0),Wheel(9,1.1),40),
       color_scheme='ripples',new_fig=False)
F.save_fig()

###

S.reset()
w = Wheel(5.5,5.3,0)
S.add(circle_in_circle(Ring(20),w,loops=1/5,inside=True,pts_per_loop=2000))
for i in range(100): 
    w.o=S.pc()
    S.add(circle_in_circle(Ring(20),w,loops=1/5,
                           inside=True,pts_per_loop=2000).rotate(2*pi/5*(i+1)))
F.plot(S,save=True)

###

F.plot(spiro_steps(Ring(10.0),Wheel(-6.0,9.0),1.4,10,offset=pi/40),new_fig=True,save=True)

###

F.plot(spiro_steps(Ring(2.0),Wheel(9.0,0.9*9.0),4,8,pi/100),new_fig=True,save=True)

###

S.reset()
a=9.0
bv=[0.7*a-0.03*a*i for i in range(10)]
for i in range(10):
    S.add(spiro(Ring(17.0),Wheel(a,bv[i]),9))
for cs in ['cycles','radial','time','length','r-waves','s-ripples','l-waves']:
    F.plot(S,color_scheme=cs,save=True)
F.plot(S,color_scheme='polar',cmap='hsv',save=True)

###

S.reset()
a=9.0
nc=10
bv=[-0.7*a-0.03*a*i for i in range(nc)]
for i in range(nc):
    S.add(spiro(Ring(17),Wheel(a,bv[i]),9))
for cs in ['length']:
    F.plot(S,color_scheme=cs,save=True)
