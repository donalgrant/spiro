import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from Ring import *

S = SpiroData()
F = SpiroFig()

F.no_save()

###

S.reset()
cs='time'
c='autumn'
a=9.0
bv=[0.9*a-0.03*a*i for i in range(10)]
for i in range(10):
    S.add(spiro(Ring(2.0),Wheel(a,bv[i]),9,slide=lambda t: 1.5))
F.plot(S,cmap=c,color_scheme=cs,save=True)

###

S.reset()
cs='time'
ring = Ring(100)
F.plot(spiro(ring,Wheel(-30,31),40,
             slide=lambda t: 0.02*sin(t/30)),
       cmap='Blues',color_scheme=cs)
F.plot(spiro(ring,Wheel(30,25), 40,
             slide=lambda t: 1+0.03*cos(t/30)),
       cmap='Reds',color_scheme=cs,new_fig=False)
F.save_fig()

###

S.reset()
cs='time'
ring = Ring(100)
F.plot(spiro(ring,Wheel(-30,31),40,
             slide=lambda t: 0.1*sin(t/10),pts_per_loop=5000),
       cmap='Blues',color_scheme=cs)
F.plot(spiro(ring,Wheel(30,25),40,
             slide=lambda t: 1+0.3*cos(t/10),pts_per_loop=10000),
       cmap='Reds',color_scheme=cs,new_fig=False)
F.save_fig()

###

F.ok_save()

S.reset()
w=Ellipse(8,0.9,11,0,pi/4)
l=20
S.add(elliptical_in_ellipse(wheel=w,slide=lambda t: -0.5,
                            inside=True,loops=l/0.5,pts_per_loop=10000))
S.rotate(pi/3)
F.plot(S,color_scheme='cycles',cmap='autumn')
F.save_fig()

###

S.reset()
w=Ellipse(10,0.9,11,0,pi/4)
l=20
S.add(elliptical_in_ellipse(wheel=w,slide=lambda t: -0.5,
                            inside=True,loops=l/0.5,pts_per_loop=10000))
S.rotate(pi/3)
F.plot(S,color_scheme='l-waves',cmap='autumn',save=True)

###

S.reset()
w=Ellipse(9,0.9,11,0,pi/4)
l=20
S.add(elliptical_in_ellipse(wheel=w,slide=lambda t: -0.5,
                            inside=True,loops=l/0.5,pts_per_loop=10000))
S.rotate(pi/3)
F.plot(S,color_scheme='t-waves',cmap='autumn',save=True)

###

S.reset()
w=Ellipse(9,0.9,17,0,pi/5)
l=20
S.add(elliptical_in_ellipse(wheel=w,slide=lambda t: 0.1,inside=True,loops=l/0.5,pts_per_loop=10000))
S.rotate(pi/3)
F.plot(S,color_scheme='l-waves',cmap='ocean',save=True)

###

S.reset()
w=Ellipse(9,0.9,17,0,pi/5)
l=20
S.add(elliptical_in_ellipse(wheel=w,slide=lambda t: 2.0,
                            inside=True,loops=l/0.5,pts_per_loop=10000))
S.rotate(pi/3)
F.plot(S,color_scheme='s-ripples',cmap='ocean',save=True)

###

S.reset()
w=Ellipse(9,0.3,17,0,pi/5)
l=20
S.add(elliptical_in_ellipse(wheel=w,slide=lambda t: 2.0,
                            inside=True,loops=l/0.5,pts_per_loop=10000))
S.rotate(pi/3)
F.plot(S,color_scheme='cycles',cmap='turbo',save=True)

###

S.reset()
w=Ellipse(9,0.6,17,0,pi/5)
l=20
S.add(elliptical_in_ellipse(wheel=w,slide=lambda t: 2.0,
                            inside=True,loops=l/0.5,pts_per_loop=10000))
S.rotate(pi/3)
F.plot(S,color_scheme='cycles',cmap='jet',save=True)

###

S.reset()
w=Ellipse(9,0.6,17,0,pi/5)
l=40
S.add(elliptical_in_ellipse(wheel=w,slide=lambda t: 1.7,
                            inside=True,loops=l/0.5,pts_per_loop=10000))
S.rotate(pi/3)
F.plot(S,color_scheme='cycles',cmap='inferno',save=True)
