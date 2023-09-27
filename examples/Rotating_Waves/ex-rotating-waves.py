import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_arcs import *
from polygon import *
from Ring import *

F=SpiroFig()
F.text_color='white'

F.set_default_dpi(150)

###

ppl=100
S = cIc(Ring(30),Wheel(25,25),loops=6)
N=S.n()
Q=SpiroData()
for i in range(1):
    T=SpiroData()
    T.add(rotating_arcs(S.subsample(4),20,rotation_rate=50,line_pts=100))
Q.add(T)
F.plot(Q,cmap='ocean',color_scheme='t-waves',save=True)

##

Q=SpiroData()
for i in range(1):
    T=SpiroData()
    T.add(rotating_arcs(S.subsample(2),40,rotation_rate=50,arc_scale=1/5,line_pts=100))
Q.add(T)
F.plot(Q,cmap='turbo',color_scheme='t-waves',save=True)

##

Q=SpiroData()
for i in range(1):
    T=SpiroData()
    T.add(rotating_arcs(S.subsample(2),40,rotation_rate=800,arc_scale=1/8,line_pts=100))
Q.add(T)
F.plot(Q,cmap='autumn',color_scheme='cycles',save=True)

###

S=SpiroData()
ppl=10
S = cIc(Ring(17),Wheel(11,8),inside=True,loops=17*11,ppl=ppl)
N=S.n()
Q=SpiroData()
for i in range(1):
    T=SpiroData()
    T.add(rotating_arcs(S.subsample(1),15,arc_scale=0.02,rotation_rate=1,line_pts=200))
Q.add(T)
F.plot(Q,cmap=cmap2,color_scheme='cycles',save=True)

## (stunning combination for any cmap / color_scheme!) (do a poster of these!)

ppl=10
S = cIc(Ring(17),Wheel(11,8),inside=True,loops=17*11,ppl=ppl)
Q=SpiroData()
for i in range(1):
    T=SpiroData()
    T.add(rotating_arcs(S.subsample(5),15,arc_scale=0.02,rotation_rate=17*11,line_pts=200))
Q.add(T)
F.plot(Q,cmap='turbo',color_scheme='time',save=True)

##

Q=SpiroData()
for i in range(1):
    T=SpiroData()
    T.add(rotating_arcs(S.subsample(5),25,arc_scale=0.05,rotation_rate=17*9,line_pts=500))
Q.add(T)
F.plot(Q,cmap='Reds',color_scheme='length')

###

ppl=300
S = cIc(Ring(30),Wheel(5,10),inside=True,loops=1,ppl=ppl)
Q=rotating_arcs(S.subsample(1),25,arc_scale=0.4,rotation_rate=1,line_pts=200)
F.plot(Q,cmap='turbo',color_scheme='time',save=True)

##

Q=rotating_arcs(S.subsample(1),25,arc_scale=0.3,rotation_rate=.4,line_pts=200)
F.plot(Q,cmap='turbo',color_scheme='length',save=True)

##

Q=rotating_arcs(S.subsample(1),10,arc_subtended=2*pi,rotation_rate=1,line_pts=400)
F.plot(Q,cmap='turbo',color_scheme='length',save=True)

##

Q=rotating_arcs(S.subsample(1),10,arc_subtended=pi/6,arc_offset_angle=pi/2,rotation_rate=1,line_pts=400)
F.plot(Q,cmap='OrRd',color_scheme='cycles',save=True)
