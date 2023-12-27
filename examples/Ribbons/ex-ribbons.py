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

ppl=2000
e=0.8
r=circum(4,semi_minor(4,e))/(2*pi)
T = eIc(Ring(6*r),Ellipse(4,e,12),inside=True,loops=1.0,ppl=ppl)
F.plot(ribbon(T,30,pi/8,4,0,trim=True),cmap='tab20b',color_scheme='cycles',save=True)

###

Q = ribbon(spiro_nstar(5,15,0.25,fold=False).subsample(10).rotate(-pi/10),3,pi/8,5,0,trim=True)
F.plot(Q,cmap='RdBu',color_scheme='cycles',save=True)

###  (make a multi-color poster of this one)

Q=SpiroData()
for i in range(8):
    Q.add(ribbon(cIc(Ring(30),W0).subsample(4),20,pi/8,1,0).move(30,0).rotate(i*pi/4))
F.plot(Q,cmap=cmap1,color_scheme='t-waves',save=True)

###

Q = SpiroData()
for i in range(6):
    Q.add(ribbon(cIc(Ring(30),W0).subsample(4),20,pi/8,3,0).move(30,0).rotate(i*pi/3))

F.plot(Q,cmap='viridis',color_scheme='t-waves',save=True)

###

ppl=1500
e=0.5
wheel_r=5
eps=0.3
rf=4
r=major_from_circum(2*pi*wheel_r*rf,e)
T = cIe(Ellipse(r*(1+eps),e),Wheel(wheel_r,wheel_r*2),inside=True,loops=4.0,ppl=ppl).rotate(pi/4)
Q = ribbon(T.subsample(2),4,pi/8,8,0,trim=True)
F.plot(Q,cmap=cmap2,color_scheme='length',save=True)

##

Q = SpiroData()
for i in range(1):
    Q.add(ribbon(T.subsample(2),4,pi/8,64,0,trim=True))
F.plot(Q,cmap=cmap2,color_scheme='length',save=True)

###

ppl=200
e=0.5
wheel_r=5
eps=0.5
rf=4
r=major_from_circum(2*pi*wheel_r*rf,e)
T = cIe(Ellipse(r*(1+eps),e),Wheel(wheel_r,wheel_r*3),inside=True,loops=1.0,ppl=ppl).rotate(pi/4)
W = ribbon(T,6,pi/8,0,0,pts=20, trim=True)
Q = ribbon(W,3,pi/8,0,0,pts=20,trim=True)
F.plot(Q,cmap='turbo',color_scheme='cycles',save=True)

##

W = ribbon(T.subsample(2),10,pi/8,0,0,pts=60, trim=True)
Q = ribbon(W,2,pi/8,100,0,pts=20,trim=True)
F.plot(Q,cmap='summer',color_scheme='time',save=True)

##
ppl=200
e=0.5
wheel_r=5
eps=0.5
rf=4
r=major_from_circum(2*pi*wheel_r*rf,e)
T = cIe(Ellipse(r*(1+eps),e),Wheel(wheel_r,wheel_r*0.8),inside=True,loops=1.0,ppl=ppl).rotate(pi/4)
W = ribbon(T.subsample(2),10,pi/8,2,0,pts=60, trim=True)
Q = ribbon(W,2,pi/8,100,0,pts=20,trim=True)
F.plot(Q,cmap='autumn',color_scheme='cycles',save=True)

###

S = SpiroData()
T = SpiroData()
for i in range(20):
    T.reset()
    w=Ellipse(9,0.4,13,pi/40*i,pi/4)
    r=Ellipse(20,0.7,0,0)
    T.add(ribbon(eIe(wheel=w,inside=True,loops=.55).subsample(15),5,pi/8,0,pts=50,trim=True))
    T.rotate(pi/64*i)
    S.add(T)

cmap_b=cmap_from_list(['mediumblue','blue','cornflowerblue','deepskyblue'])
F.plot(S,cmap_b),color_scheme='time',save=True)

###

S.reset()
T = SpiroData()
for i in range(20):
    T.reset()
    w=Ellipse(9,0.4,13,pi/40*i,pi/4)
    r=Ellipse(20,0.7,0,0)
    T.add(ribbon(eIe(wheel=w,inside=True,loops=.55).subsample(15),5,pi/8,4,pi/2,pts=50,trim=True))
    T.rotate(pi/64*i)
    S.add(T)

F.plot(S,'OrRd',color_scheme='time',save=True)

###

seed=3
np.random.seed(seed)
S.reset()
T = SpiroData()
for sweep in range(15):
    wo = np.random.uniform(0,2*pi)
    R = 20 + np.random.uniform(-10,5)
    for i in range(20):
        T.reset()
        m=5+i/3
        w=Ellipse(major=3,  eccen=0.4,pen=4, offset=i*pi/20, pen_offset=0)
        r=Ellipse(major=R, eccen=0.0,       offset=0, pen_offset=wo)
        T.add(ribbon(eIe(ring=r,wheel=w,inside=True,loops=0.06).subsample(5),1,pi/8,1,pts=10,trim=True))
        S.add(T)

F.plot(S,'tab20b',color_scheme='l-waves',save=True)

###

T=cIc(Ring(30),Wheel(25,15),loops=5,inside=True)
osc = 10
tw = 5
samp=5
subs=array([ 0.001 + pi * sin(2*pi*j*osc/(T.n()//samp)) for j in range(T.n()//samp)])
Q=ribbon(T.subsample(samp),7,subs,tw,0)
F.plot(Q,cmap='Wistia',color_scheme='t-waves',color_dither=0.15,save=True)

###

a=13
e=0.3
c=circum(a,semi_minor(a,e))
T=eIc(Ring(c*(7/3)/(2*pi)),Ellipse(13,0.3,17),loops=3,inside=True)
osc = 10
tw = 0
samp=2
subs=array([ 0.001 + pi * sin(2*pi*j*osc/(T.n()//samp)) for j in range(T.n()//samp)])
Q=ribbon(T.subsample(samp),40,subs,tw,pi/2,trim=True)
F.plot(Q,cmap='ocean',color_scheme='time',alpha=0.4,save=True)

###

a=13
e=0.3
c=circum(a,semi_minor(a,e))
T=eIc(Ring(c*(7/3)/(2*pi)),Ellipse(13,0.3,20),loops=3,inside=False)

osc = 10
tw = 0
samp=1
subs=array([ 0.001 + pi * sin(2*pi*j*osc/(T.n()//samp)) for j in range(T.n()//samp)])
Q=ribbon(T.subsample(samp).inverted_radii(),.1,subs,tw,pi/2,trim=True)
F.plot(Q,cmap='autumn',color_scheme='cycles',alpha=0.4,save=True)
