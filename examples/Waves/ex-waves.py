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
ppl=200
S = integral_ellipticals(10,0.8,0.6,min_pen=0.8,max_pen=0.8,max_po=pi/2).subsample(80)
N=S.n()
Q=SpiroData()
for i in range(1):
    T=SpiroData()
    T.add(centered_arcs(S.subsample(1),5,arc_scale=0.5,line_pts=100))
Q.add(T)
F.plot(Q,cmap='turbo',color_scheme='length',dot_size=0.1,alpha=0.3,save=True)

###

ppl=100
S = cIc(Ring(30),Wheel(25,25),loops=6)
N=S.n()
Q=SpiroData()
for i in range(1):
    T=SpiroData()
    T.add(centered_arcs(S.subsample(5),25,line_pts=100))
Q.add(T)
F.plot(Q,cmap='hsv_r',color_scheme='polar',save=True)

###

ppl=100
S = cIc(Ring(30),Wheel(25,25),loops=6)
N=S.n()
Q=SpiroData()
for i in range(1):
    T=SpiroData()
    T.add(centered_arcs(S.subsample(4),20,angle_offset=pi/4,line_pts=100))
Q.add(T)
F.plot(Q,cmap='autumn',color_scheme='x+y',save=True)

###

ppl=300
r=30
e=0.6
a=circum(r,semi_minor(r,e))/(2*pi)
S = cIe(Ellipse(r,e,0,pi/4),Wheel(a/4,5),loops=1,inside=True,ppl=ppl)
Q=SpiroData()
for i in range(4):
    T=SpiroData()
    T.add(centered_arcs(S,50,arc_scale=.5,line_pts=100,theta_phase=True))
    Q.add(T.rotate(i*pi/8))
F.plot(Q,cmap='turbo',color_scheme='length',save=True)

###

ppl=600
r=30
e=0.6
a=circum(r,semi_minor(r,e))/(2*pi)
S = cIe(Ellipse(r,e,0,pi/4),Wheel(a/4,5),loops=1,inside=True,ppl=ppl)
Q=SpiroData()
for i in range(4):
    T=SpiroData()
    T.add(centered_arcs(S,50,arc_scale=.5,line_pts=100,theta_phase=False))
    Q.add(T.rotate(i*pi/8))
F.plot(Q,cmap='turbo',color_scheme='cycles',save=True)

##

Q=SpiroData()
for i in range(1):
    T=SpiroData()
    T.add(centered_arcs(S.subsample(2),10,arc_scale=5,line_pts=500,theta_phase=False))
    Q.add(T.rotate(i*pi/8))
F.plot(Q,cmap='turbo',color_scheme='length',save=True)

###

S = spiro_nstar(3,30,0.25).rotate(pi/8)
N=S.n()
Q=SpiroData()
for i in range(1):
    T=SpiroData()
    T.add(centered_arcs(S.subsample(10),30,arc_scale=1,line_pts=300,theta_phase=True))
    Q.add(T.rotate(i*pi/8))
F.plot(Q,cmap='Greens',color_scheme='t-waves',save=True)

##

Q=centered_arcs(S.subsample(10),30,arc_scale=0.7,line_pts=300,theta_phase=False)
F.plot(Q,cmap='ocean',color_scheme='t-waves',save=True)

###

S = spiro_nstar(3,30,0.25,Wheel(5.5,5)).rotate(pi/8)
Q=centered_arcs(S.subsample(20),40,arc_scale=1.0,line_pts=300,theta_phase=False)
F.plot(Q,cmap='ocean',color_scheme='cycles',save=True)

###

S = spiro_nstar(3,30,0.25,Wheel(3.5,5),inside=True,loops=1).rotate(pi/8)
Q=centered_arcs(S.subsample(20),10,arc_scale=0.5,line_pts=300,theta_phase=True)
F.plot(Q,cmap='turbo',color_scheme='cycles',save=True)

###

S = spiro_nstar(4,30,0.5,Wheel(3.5,5),inside=True,loops=1).rotate(pi/8)
Q=centered_arcs(S.subsample(20),10,arc_scale=0.4,line_pts=300,theta_phase=True)
F.plot(Q,cmap='turbo',color_scheme='length',save=True)
