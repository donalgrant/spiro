import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from spiro import *
from spiro_string import *
from diagrams import *

S = SpiroData()
F = SpiroFig()

###

phi1=0
phi2=pi*3
n=6
orient=0
ring=Ring(radius=20,orient=orient)
wheel=Ellipse(5,0.7,4)
F.plot(elliptical_arc_new(R=ring.r,wheel=wheel,loops=1,inside=True,pen_offset=pi/4),
       no_frame=False)
for phi in np.linspace(phi1,phi2,n):
    S.reset()
    wheel.o=phi
    S.add(new_elliptical_diagram(ring=ring,wheel=wheel,
                                  phi0=0,inside=True,orient=0,pen_offset=pi/4))
    F.plot(S, new_fig=False, color_scheme='cycles',alpha = 1.0 if phi==phi1 else 0.1)
F.save_fig()

###

wheel=Ellipse(8,0.7,7,phi1)
F.plot(elliptical_arc_new(R=ring.r,wheel=wheel,loops=1,inside=False,
                          orient=orient,pen_offset=pi/4))
for phi in np.linspace(phi1,phi2,n):
    S.reset()
    wheel.o=phi
    S.add(new_elliptical_diagram(ring=ring,wheel=wheel,
                                  phi0=0,inside=False,orient=0,pen_offset=pi/4))
    F.plot(S, new_fig=False, alpha = 1.0 if phi==phi1 else 0.1)

F.save_fig()

###

phi1=-pi/4
phi2=2*pi
n=8
ring=Ring(radius=20,orient=pi/4)
wheel=Wheel(5,5,phi1)
F.plot(spiro(ring.r,wheel=wheel,loops=1,inside=True,orient=ring.o))
for phi in np.linspace(phi1,phi2,n):
    S.reset()
    wheel.o=phi
    S.add(ring_wheel_diagram(ring=ring,wheel=wheel,phi0=phi1))
    F.plot(S, new_fig=False, alpha = 1.0 if phi==phi1 else 0.1)

F.save_fig()

###

wheel=Wheel(8,7,phi1)
F.plot(spiro(ring.r,wheel=wheel,loops=1,inside=False,orient=ring.o))
for phi in np.linspace(phi1,phi2,n):
    S.reset()
    wheel.o=phi
    S.add(ring_wheel_diagram(ring=ring,wheel=wheel,phi0=phi1,inside=False))
    F.plot(S, new_fig=False, alpha = 1.0 if phi==phi1 else 0.1)

F.save_fig()

###

e=0.7
phi1=0
phi2=2*pi
n=8
ring=Ellipse(major=20,eccen=e,offset=pi/4)
wheel=Wheel(5,6,phi1)
F.plot(wheel_in_ellipse(wheel=wheel,ellipse=ring,invert=True,orient=pi/4))
for phi in np.linspace(phi1,phi2,n):
    S.reset()
    wheel.o=phi
    S.add(ring_ellipse_diagram(ring=ring,wheel=wheel,phi0=phi1,orient=pi/4))
    F.plot(S, new_fig=False, alpha = 1.0 if phi==phi1 else 0.1)

F.save_fig()

n=8
wheel=Wheel(8,7,phi1)
F.plot(wheel_in_ellipse(wheel=wheel,ellipse=ring,invert=False,orient=-pi/4))
for phi in np.linspace(phi1,phi2,n):
    S.reset()
    wheel.o=phi
    S.add(ring_ellipse_diagram(ring=ring,wheel=wheel,phi0=phi1,inside=False,orient=-pi/4))
    F.plot(S, new_fig=False, alpha = 1.0 if phi==phi1 else 0.1)

F.save_fig()
