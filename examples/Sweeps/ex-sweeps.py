import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from spiro import *
from swoops import *

S = SpiroData()
F = SpiroFig()

F.no_save()

###

S.reset()
w=Ellipse(9,0.6,17,0,pi/5)
for i in range(36):
    r=Ellipse(20,0.5,0,0)
    S.add(ellipse_in_ellipse(wheel=w,inside=True,loops=.3))
    S.rotate(pi/128*i)
    S.x+=1
    S.y-=1
    F.plot(S,color_scheme='cycles',cmap='ocean',caption=True,
           new_fig=True if i==0 else False)

F.save_fig()

###

S.reset()
w=Ellipse(9,0.6,17,0,pi/5)
T = SpiroData()
for i in range(100):
    T.reset()
    r=Ellipse(20,0.5,0,0)
    T.add(ellipse_in_ellipse(wheel=w,inside=True,loops=.8))
    T.rotate(pi/128*i)
    S.add(T)
    S.x+=0.5
    S.y-=1

F.plot(S,color_scheme='length',cmap='Reds',save=True)

###

S.reset()
T = SpiroData()
for i in range(40):
    T.reset()
    w=Ellipse(9,0.4,17,pi/80*i,pi/4)
    r=Ellipse(20,0.5,0,0)
    T.add(ellipse_in_ellipse(wheel=w,inside=True,loops=.65))
    S.add(T)

F.plot(S,color_scheme='length',cmap='rainbow',save=True)

###

S.reset()
T = SpiroData()
for i in range(40):
    T.reset()
    w=Ellipse(9,0.4,13,pi/80*i,pi/4)
    r=Ellipse(20,0.7,0,0)
    T.add(ellipse_in_ellipse(wheel=w,inside=True,loops=.65))
    S.add(T)
    S.x-=0.5

F.plot(S,color_scheme='radial',cmap='inferno',save=True)

###

S.reset()
T = SpiroData()
for i in range(40):
    T.reset()
    w=Ellipse(9,0.4,13,pi/80*i,pi/4)
    r=Ellipse(20,0.7,0,0)
    T.add(ellipse_in_ellipse(wheel=w,inside=True,loops=.65))
    T.rotate(pi/128*i)
    S.add(T)
    S.x-=0.5
    S.y+=1   

F.plot(S,color_scheme='radial',cmap='inferno',save=True)

F.plot(S,color_scheme='l-waves',cmap='OrRd',save=True)

###

S.reset()
T = SpiroData()
for i in range(40):
    T.reset()
    w=Ellipse(9,0.4,13,pi/80*i,pi/4)
    r=Ellipse(20,0.7,0,0)
    T.add(ellipse_in_ellipse(wheel=w,inside=True,loops=.55))
    T.rotate(pi/128*i)
    S.add(T)

F.plot(S,color_scheme='t-waves',cmap='summer',save=True)

###

S.reset()
T = SpiroData()
for i in range(30):
    T.reset()
    w=Ellipse(9,0.4,13+i/5,pi/80*i,pi/4)
    r=Ellipse(20,0.7,0,0)
    T.add(ellipse_in_ellipse(wheel=w,inside=False,loops=.55))
    T.rotate(pi/128*i)
    S.add(T)
    S.x+=0.5
    S.y+=0.5  

F.plot(S,color_scheme='t-waves',cmap='summer',save=True)

###

S.reset()
T = SpiroData()
for i in range(30):
    T.reset()
    w=Ellipse(9,0.4,13+i/5,pi/80*i,0)
    r=Ellipse(20+i/6,0.6,pi/2,0)
    T.add(ellipse_in_ellipse(ring=r,wheel=w,inside=True,loops=.75))
    T.rotate(pi/128*i)
    S.add(T)
    S.x+=0.5
    S.y+=0.5   

F.plot(S,color_scheme='t-waves',cmap='bone',save=True)

###

S.reset()
T = SpiroData()
for i in range(30):
    T.reset()
    w=Ellipse(9,0.4,13+i/5,pi/80*i,0)
    r=Ellipse(20+i/6,0.6,pi/2,0)
    T.add(ellipse_in_ellipse(ring=r,wheel=w,inside=True,loops=.75))
    T.rotate(-pi/64*i)
    S.add(T)

F.plot(S,color_scheme='t-waves',cmap='Greens',save=True)

###

S.reset()
T = SpiroData()
for i in range(30):
    T.reset()
    w=Ellipse(9,0.4,13+i/5,pi/80*i,0)
    r=Ellipse(20+i/6,0.6,pi/2,0)
    T.add(ellipse_in_ellipse(ring=r,wheel=w,inside=True,loops=1.5))
    T.rotate(-pi/64*i)
    S.add(T)
    S.x+=0.5

F.plot(S,color_scheme='length',cmap='Set1',save=True)

###

S.reset()
T = SpiroData()
for i in range(30):
    T.reset()
    w=Ellipse(9,0.4,13+i/10,pi/80*i,0)
    r=Ellipse(20+i/6,0.6,pi/2,0)
    T.add(ellipse_in_ellipse(ring=r,wheel=w,inside=True,loops=1.3))
    T.rotate(-pi/64*i)
    S.add(T)

F.plot(S,color_scheme='length',cmap='tab20',save=True)
    
###

S.reset()
T = SpiroData()
for i in range(30):
    T.reset()
    w=Ellipse(9,0.4,13+i/10,pi/80*i,0)
    r=Ellipse(20+i/6,0.3,pi/2,0)
    T.add(ellipse_in_ellipse(ring=r,wheel=w,inside=True,loops=0.75))
    T.rotate(3*pi/2-pi/45*i)
    S.add(T)
    S.x-=0.5

F.plot(S,color_scheme='time',cmap='tab20',save=True)

###

S.reset()
T = SpiroData()
for i in range(70):
    T.reset()
    w=Ellipse(9,0.0,13+i/10,pi/80*i,0)
    r=Ellipse(20+i/6,0.0,pi/2,0)
    T.add(ellipse_in_ellipse(ring=r,wheel=w,inside=True,loops=0.45))
    T.rotate(3*pi/2-pi/45*i)
    S.add(T)
    S.x-=0.5

F.plot(S,color_scheme='l-waves',cmap='YlOrRd',save=True)

###

F.ok_save()

