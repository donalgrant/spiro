import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from spiro import *
from spiro_string import *
from polygon import *
from diagrams import *
from Ring import *

S = SpiroData()
F = SpiroFig()

trace='copper'
trs='red'

w0 = Wheel(0.01,0.0)   # for tracing paths

###

phi1=pi/4
phi2=pi*3
n=6
orient=0
ring=Ring(radius=20,orient=orient)
wheel=Ellipse(5,0.7,4,phi1,pen_offset=pi/4)
F.plot(eIc(ring,wheel=wheel,loops=1,inside=True),
       no_frame=False,cmap=trace,color_scheme=trs)
for phi in np.linspace(phi1,phi2,n):
    S.reset()
    wheel.o=phi
    S.add(new_elliptical_diagram(ring=ring,wheel=wheel,phi0=pi/4,inside=True))
    F.plot(S, new_fig=False, color_scheme='cycles',alpha = 1.0 if phi==phi1 else 0.1)
F.save_fig(transparent=False)

###

ring=Ring(radius=20,orient=0)
wheel=Ellipse(8,0.7,7,phi1,pen_offset=pi/4)
F.plot(eIc(ring,wheel=wheel,loops=1,inside=False),cmap=trace,color_scheme=trs)
for phi in np.linspace(phi1,phi2,n):
    S.reset()
    wheel.o=phi
    S.add(new_elliptical_diagram(ring=ring,wheel=wheel,
                                  phi0=phi1,inside=False))
    F.plot(S, new_fig=False, alpha = 1.0 if phi==phi1 else 0.1)

F.save_fig(transparent=False)

###

phi1=-pi/4
phi2=2*pi
n=8
ring=Ring(radius=20,orient=pi/4)
wheel=Wheel(5,5,phi1)
F.plot(spiro(ring,wheel,loops=1,inside=True),cmap=trace,color_scheme=trs)
for phi in np.linspace(phi1,phi2,n):
    S.reset()
    wheel.o=phi
    S.add(ring_wheel_diagram(ring=ring,wheel=wheel,phi0=phi1))
    F.plot(S, new_fig=False, alpha = 1.0 if phi==phi1 else 0.1)

F.save_fig(transparent=False)

###

wheel=Wheel(8,7,phi1)
F.plot(spiro(ring,wheel=wheel,loops=1,inside=False),cmap=trace,color_scheme=trs)
for phi in np.linspace(phi1,phi2,n):
    S.reset()
    wheel.o=phi
    S.add(ring_wheel_diagram(ring=ring,wheel=wheel,phi0=phi1,inside=False))
    F.plot(S, new_fig=False, alpha = 1.0 if phi==phi1 else 0.1)

F.save_fig(transparent=False)

###

e=0.7
phi1=0
phi2=2*pi
n=8
ring=Ellipse(major=20,eccen=e,offset=pi/4,pen_offset=phi1)
wheel=Wheel(5,6)
F.plot(cIe(ring,wheel=wheel,inside=True),cmap=trace,color_scheme=trs)
for phi in np.linspace(phi1,phi2,n):
    S.reset()
    wheel.o=phi
    S.add(cIe_diagram(ring=ring,wheel=wheel,phi0=phi1))
    F.plot(S, new_fig=False, alpha = 1.0 if phi==phi1 else 0.1)

F.save_fig(transparent=False)

n=8
wheel=Wheel(8,7)
ring.o=-pi/4
F.plot(cIe(ring,wheel=wheel,inside=False),cmap=trace,color_scheme=trs)
for phi in np.linspace(phi1,phi2,n):
    S.reset()
    wheel.o=phi
    S.add(cIe_diagram(ring=ring,wheel=wheel,phi0=phi1,inside=False))
    F.plot(S, new_fig=False, alpha = 1.0 if phi==phi1 else 0.1)

F.save_fig(transparent=False)

### arc-continuity

S.reset()
r=10
a=1.3
p=2.3
F.plot(cIc(Ring(r),w0),cmap='hsv',color_scheme='time',new_fig=True)
o=0
for i in range(1):
    S.add(cIc(Ring(r),Wheel(a,p,o+pi),loops=0.25,inside=True,reverse=True))
    o=S.pc()
    S.add(rotate(-r,0,S.xc(),S.yc(),pi))
    S.add(cIc(Ring(r),Wheel(a,p,o+pi),loops=0.25).rotate(-pi/2))
    o=S.pc()
    S.add(rotate(0,r,S.xc(),S.yc(),pi))
    
F.plot(S,new_fig=False,cmap='autumn',color_scheme='time')
F.save_fig(transparent=False)

###

S.reset()
r=Ring(9)
F.plot(cIc(r,w0).rotate(-pi/2),
       cmap='hsv',color_scheme='time',new_fig=True)

rot=pi/10
w=Wheel(1.5,1.3)
for i in range(1):
    S.add(cIc(r,w,loops=0.5,inside=False,reverse=False).rotate(-pi/2+rot))
    S.add(cIc(r,w,loops=0.5,inside=False,reverse=True ).rotate(-pi/2+rot))
    S.add(cIc(r,w,loops=0.5,inside=True, reverse=False).rotate(-pi/2+rot))
    S.add(cIc(r,w,loops=0.5,inside=True, reverse=True ).rotate(-pi/2+rot))
    
F.plot(S,new_fig=False,cmap='autumn',color_scheme='time')
F.save_fig(transparent=False)

###

(x1,y1,x2,y2)=(0,0,30,0)
(a,b)=(2,2)
S.reset()
S.add(roll(x1,y1,x2,y2,w0,invert=False))
S.add(roll(x1,y1,x2,y2,Wheel(a,b),invert=False))
o=S.pc()
S.add(rotate(x2,y2,S.xc(),S.yc(),pi))
S.add(roll(x2,y2,x1,y1,Wheel(a,b,o+pi),invert=False))
S.add(rotate(x1,y1,S.xc(),S.yc(),pi))
S.add(roll(x1,y1,x2,y2,Wheel(a,b),invert=True))
o = S.pc()
S.add(rotate(x2,y2,S.xc(),S.yc(),-pi))
S.add(roll(x2,y2,x1,y1,Wheel(a,b,o-pi),invert=True))
S.add(rotate(x1,y1,S.xc(),S.yc(),-pi))
F.plot(S)

F.save_fig(transparent=False)

###  Elliptical Wheels in Elliptical Rings

e=0.4
phi1=0
phi2=2*pi
po=pi/4
o=0
wo=pi/8
n=8
wheel=Ellipse(8,0.7,7,phi1,pen_offset=po)
F.plot(eIc(Ring(20),wheel=wheel,inside=True,loops=1),cmap=trace,color_scheme=trs)
for phi in linspace(phi1,phi2,n):
    wheel.o=phi
    F.plot(new_elliptical_diagram(wheel=wheel,phi0=0,inside=True),new_fig=False,
          alpha=1.0 if phi==phi1 else 0.1)

F.save_fig(transparent=False)

###

e=0.4
phi1=0
phi2=2*pi
po=pi/4
o=0
wo=pi/8
n=8
ring=Ellipse(major=20,eccen=e,offset=o,pen_offset=wo)
wheel=Ellipse(5,0.9,4,phi1,pen_offset=po)
F.plot(eIe(ring=ring,wheel=wheel,inside=False,loops=1),cmap=trace,color_scheme=trs)
for phi in linspace(phi1,phi2,n):
    wheel.o=phi
    F.plot(ee_diagram(ring=ring,wheel=wheel,phi0=0,inside=False),new_fig=False,
          alpha=1.0 if phi==phi1 else 0.1)

F.save_fig(transparent=False)

###

e=0.7
phi1=0
phi2=2*pi
po=pi/4
o=pi/4
wo=pi/3
phi0=0
n=8
ring=Ellipse(major=20,eccen=e,offset=o,pen_offset=wo)
wheel=Ellipse(5,0.8,4,phi1,pen_offset=po)
F.plot(eIe(ring=ring,wheel=wheel,inside=True,loops=1.0),cmap=trace,color_scheme=trs)
phi = linspace(phi1,phi2,n)
for i in range(len(phi)):
    wheel.o=phi[i]
    F.plot(ee_diagram(ring=ring,wheel=wheel,phi0=phi0,inside=True),new_fig=False,
          alpha=1.0 if phi[i]==phi1 else 0.1)

F.save_fig(transparent=False)

###

e=0.7
phi1=0
phi2=2*pi
po=0
o=0
wo=0
phi0=pi/4
n=8
ring=Ellipse(major=20,eccen=e,offset=o,pen_offset=wo)
wheel=Ellipse(5,0.8,4,phi0,pen_offset=po)
F.plot(eIe(ring=ring,wheel=wheel,inside=True,loops=1.0),cmap=trace,color_scheme=trs)
phi = linspace(phi1,phi2,n)
for i in range(len(phi)):
    wheel.o=phi[i]
    F.plot(ee_diagram(ring=ring,wheel=wheel,phi0=phi0,inside=True),new_fig=False,
          alpha=1.0 if phi[i]==phi1 else 0.1)

F.save_fig(transparent=False)

###

phi0=pi/2
phi1=phi0
phi2=2*pi
n=4
w=Ellipse(major=8,eccen=0.7,pen=7,offset=phi0,pen_offset=-pi/2)
r=Ellipse(major=20,eccen=0.5,offset=-pi/3,pen_offset=pi/2)
F.plot(eIe(r,w,inside=True,loops=1),cmap=trace,color_scheme=trs)
phi = linspace(phi1,phi2,n)
for i in range(len(phi)):
    w.o=phi[i]
    F.plot(ee_diagram(r,w,phi0=phi0,inside=True),new_fig=False,
          alpha=1.0 if phi[i]==phi1 else 0.1)

F.save_fig(transparent=False)

###

phi0=pi/2
phi1=phi0
phi2=2*pi
n=4
w=Ellipse(major=8,eccen=0.7,pen=7,offset=phi0,pen_offset=-pi/2)
r=Ellipse(major=20,eccen=0.5,offset=-pi/3,pen_offset=pi/2)
F.plot(eIe(r,w,inside=False,loops=1),cmap=trace,color_scheme=trs)
phi = linspace(phi1,phi2,n)
for i in range(len(phi)):
    w.o=phi[i]
    F.plot(ee_diagram(r,w,phi0=phi0,inside=False),new_fig=False,
          alpha=1.0 if phi[i]==phi1 else 0.1)

F.save_fig(transparent=False)
