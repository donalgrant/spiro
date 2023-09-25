import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_string import *
from polygon import *
from Ring import *

F=SpiroFig()
F.text_color='white'

F.set_default_dpi(150)

###

S=SpiroData()
S=cIe(Ellipse(30,0.7,0,pi/2.7),Wheel(8,9),loops=20,inside=True)
N=S.n()

T=SpiroData()
for sub in [90]:
    T.add(arcs_from_multi(S.subsample(sub),array([1]),0,invert=True, line_pts=200,arc_always=True))
    T.add(arcs_from_multi(S.subsample(sub),array([1]),0,invert=False,line_pts=200,arc_always=True))
    
F.plot(T,cmap='ocean',color_scheme='time',save=True)

###

S=cIe(Ellipse(30,0.7,0,pi/2.7),Wheel(8,9),loops=20,inside=False)
N=S.n()
T=SpiroData()
for sub in [N//150]:
    T.add(arcs_from_multi(S.subsample(sub),array([1]),0,invert=True, line_pts=500,arc_always=True))
    T.add(arcs_from_multi(S.subsample(sub),array([1]),0,invert=False,line_pts=500,arc_always=True))
F.plot(T,cmap='Blues',color_scheme='time',save=True)

###

S=cIe(Ellipse(30,0.9,0,pi/3),Wheel(8,7),loops=20,inside=True,ppl=100)
U=cIe(Ellipse(30,0.9,0,pi/3),Wheel(3,3),loops=2,inside=False,ppl=100)
N=S.n()
M=U.n()

T=SpiroData()
np.random.seed(21)
for first in range(0,N-1,30):
    offset = np.random.randint(2,10)
    T.add(arcs_from_multi(S,array([offset]),0,invert=True,
                          line_pts=500,arc_always=True,max_strings=1,first=first))
    T.add(arcs_from_multi(S,array([offset]),0,invert=False,
                          line_pts=500,arc_always=True,max_strings=1,first=first))

Q=SpiroData()
offset=array([M//3])
for j in range(6):
    first = np.random.randint(0,M-1)
    for arc_radius in [30,33,35,38,40]:
        Q.add(arcs_from_multi(U,offset,arc_radius,invert=False, line_pts=500,max_strings=5,first=first))

F.plot(T,cmap='Blues',color_scheme='time')
F.plot(Q,cmap=cmap_from_list(['palegreen','aquamarine','aqua']),color_scheme='time',new_fig=False,alpha=0.2)
F.save_fig()

###

S=cIe(Ellipse(30,0.9,0,pi/3),Wheel(8,7),loops=1,inside=True,ppl=60)
N=S.n()
T=SpiroData()
Q=SpiroData()
for i in range(10):
    T.add(arcs_from_multi(S,array([1]),0,invert=True, line_pts=500,arc_always=True))
    T.add(arcs_from_multi(S,array([1]),0,invert=False,line_pts=500,arc_always=True))
    Q.add(T.rotate(pi/20*i))

F.plot(Q,cmap='summer',color_scheme='time',save=True)

###

S=cIc(Ring(30),Wheel(10,9),loops=1,inside=True,ppl=60)
N=S.n()
Q=SpiroData()
for i in range(12):
    T=SpiroData()
    T.add(arcs_from_multi(S,array([1]),0,invert=True, line_pts=500,arc_always=True))
    T.add(arcs_from_multi(S,array([1]),0,invert=False,line_pts=500,arc_always=True))
    T.t=T.x*0+i*10
    Q.add(T.rotate(pi/18*i))

F.plot(Q,cmap=cmap1,color_scheme='time',save=True)

###

S=eIe(Ellipse(30,0.5,0,pi/4),Ellipse(17,0.5,14,pi/4),loops=0.45,inside=True,ppl=90)
N=S.n()
Q=SpiroData()
for i in range(16):
    T=SpiroData()
    T.add(arcs_from_multi(S,array([1]),0,invert=True, line_pts=500,arc_always=True))
    T.add(arcs_from_multi(S,array([1]),0,invert=False,line_pts=500,arc_always=True))
    T.t=T.x*0+i*10
    Q.add(T.rotate(pi/12*i))
Q.rotate(pi/2)
F.plot(Q,cmap='ocean',color_scheme='x+y',dot_size=0.3,alpha=1)
F.save_fig()
