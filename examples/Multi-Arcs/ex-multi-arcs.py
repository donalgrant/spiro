import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_string import *
from polygon import *
from Ring import *

import matplotlib as mpl
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
cmap1 = LinearSegmentedColormap.from_list("RedOrangePink",["Red","Orange","Pink"])
cmap2 = LinearSegmentedColormap.from_list("Pinks",["rebeccapurple","darkmagenta","orchid","pink"])
cmap3 = LinearSegmentedColormap.from_list("DarkGreen",["seagreen","teal","cornflowerblue","mediumblue","indigo"])

###

F=SpiroFig()
F.text_color='white'

S = SpiroData()

T = cIe(Ellipse(11.5,0.8,0,-pi/5),Wheel(7,5.5),loops=3,ppl=300)

Q = SpiroData()
offsets=[43,86]
Q.add(arcs_from_multi(T,offsets,40,invert=True,line_pts=500,max_strings=200))
Q.add(arcs_from_multi(T,offsets,40,invert=True,line_pts=500,max_strings=200))
Q.add(arcs_from_multi(T,offsets,30,invert=True,line_pts=500,max_strings=200))
F.plot(Q,cmap='ocean',color_scheme='l-waves',save=True)

##

Q = SpiroData()
offsets=[43,86]
for ar in [20,25,30,35,40]:
    Q.add(arcs_from_multi(T,offsets,ar,invert=False,line_pts=500,max_strings=100))
    Q.add(arcs_from_multi(T,offsets,ar,invert=True, line_pts=500,max_strings=100))

F.plot(Q,cmap=cmap2,color_scheme='l-waves',save=True)

###

T = cIe(Ellipse(11.5,0.8,0,-pi/5),Wheel(7,5.5),loops=3,ppl=300).rotate(pi/2)

Q = SpiroData()
offsets=[43,86]
for ar in [28,29,30,31,32]:
    Q.add(arcs_from_multi(T,offsets,ar,invert=True, line_pts=500,max_strings=200))

F.plot(Q,cmap='autumn',color_scheme='time',save=True)

##

Q = SpiroData()
offsets=[118]
for ar in linspace(20,80,10):
    Q.add(arcs_from_multi(T,offsets,ar,invert=False,line_pts=500,max_strings=20))
    Q.add(arcs_from_multi(T,offsets,ar,invert=True, line_pts=500,max_strings=20))

F.plot(Q,cmap='Reds',color_scheme='length',save=True)

###

(w,p)=(0.1,0.5)
T=heart(wheel=Wheel(w,p),loops=2,inside=False,guarded=True).subsample(10)

Q = SpiroData()
offsets=[123]
for ar in linspace(38,53,5):
    Q.add(arcs_from_multi(T,offsets,ar,invert=False,line_pts=500,max_strings=60))
    Q.add(arcs_from_multi(T,offsets,ar,invert=True, line_pts=500,max_strings=60))

F.plot(Q,cmap='Reds',color_scheme='length',save=True)

###

(w,p)=(0.1,0.0)
T=eIe(Ellipse(20,0.8,0,pi/4),Ellipse(1.0,0.5,1.0),loops=1.0,inside=True,ppl=40)
U=eIe(Ellipse(8,0.5,0,-pi/2),Ellipse(1.0,0.5,0.2),loops=1.0,inside=True,ppl=40)

T.add(U)
Q = SpiroData()
Q_offsets=[37]
for ar in linspace(38,53,3):
    Q.add(arcs_from_multi(T,Q_offsets,ar,invert=True, line_pts=200,max_strings=600))

F.plot(Q,cmap='OrRd',color_scheme='time',save=True)

###

(w,p)=(0.1,0.0)
T=spiro_nstar(3,30,0.25,W0,loops=1).subsample(40)

Q = SpiroData()
Q_offsets=[73]
for ar in linspace(38,53,3):
    Q.add(arcs_from_multi(T,Q_offsets,ar,invert=True, line_pts=500,max_strings=60))

F.plot(Q,cmap='turbo',color_scheme='length',save=True)

###

(w,p)=(0.1,0.0)
T=spiro_nstar(4,30,0.35,W0,loops=1).subsample(40)

for o in [73]:
    Q = SpiroData()
    Q_offsets=[o]
    for ar in linspace(38,53,3):
        Q.add(arcs_from_multi(T,Q_offsets,ar,invert=True, line_pts=500,max_strings=120))
    
F.plot(Q,cmap='Reds',color_scheme='length',save=True)

###

T=spiro_nstar(3,40,0.25,W0,loops=1).subsample(30).rotate(pi/6)

Q = SpiroData()
Q_offsets=[75]
for ar in linspace(18,53,6):
    Q.add(arcs_from_multi(T,Q_offsets,ar,invert=True, line_pts=500,max_strings=50, arc_only=True))

F.plot(Q,cmap='ocean',color_scheme='time',save=True)

###

S=SpiroData()
N=201
S.add(cIc(Ring(50),Wheel(8.7,10),inside=True,ppl=N))
T=SpiroData()
for f in range(15):
    T.add(arcs_from_multi(S,array([int(N/2)]),100-f*3,invert=True,line_pts=400,max_strings=12,first=f*5))

F.plot(T,cmap='inferno_r',color_scheme='radial',save=True)

###

S=SpiroData()
N=600
S.add(cIc(Ring(50),Wheel(8.7,10),inside=True,ppl=N))
T=SpiroData()
for f in range(15):
    for invert in [True,False]:
        T.add(arcs_from_multi(S,array([200]),100-(f%5)*6,invert=invert,line_pts=400,
                              max_strings=15,first=f*3)).move(0,0).rotate(0)
        T.add(arcs_from_multi(S,array([200]),100,invert=invert,line_pts=400,
                              max_strings=15,first=f*3)).move(0,0).rotate(0)

F.plot(T,cmap='Blues',color_scheme='length',save=True)
