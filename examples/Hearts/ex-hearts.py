import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from spiro import *
from polygon import *

S = SpiroData()
F = SpiroFig()

###

S.reset()

(w,p)=(2.1,1.5)
F.plot(heart(wheel=Wheel(w,p),loops=20,inside=True,guarded=True),save=True)
F.plot(heart(wheel=Wheel(w,p),loops=40,inside=False,guarded=True),save=True)

###

(w,p)=(2.1,1.5)
F.plot(heart(wheel=Wheel(w,p),loops=10,inside=True,fold=True))
F.plot(heart(wheel=Wheel(w,p),loops=10,inside=False,fold=True),new_fig=False,save=True)

###

(w,p)=(1.7,3.6)
F.plot(heart(wheel=Wheel(w,p),loops=10,inside=True,guarded=False))
F.plot(heart(wheel=Wheel(w,p),loops=10,inside=False,guarded=False),new_fig=False,save=True)
F.plot(heart(wheel=Wheel(w,p),loops=10,inside=True,guarded=True),save=True)

###

fig, ax=plt.subplots(figsize=(10,10))
ax.set(aspect=1)
F.ax=ax
(w,p)=(1.0,5)
F._fig=fig  # kludge
F.plot(heart(wheel=Wheel(0.001,0),loops=1,inside=False,guarded=False),
       cmap='inferno',color_scheme='radial',new_fig=False)
F.plot(heart(wheel=Wheel(w,p),loops=1,inside=False,guarded=True),
       cmap='inferno',color_scheme='radial',new_fig=False)
F.plot(heart(wheel=Wheel(w,p),loops=1,inside=True,guarded=True),
       cmap='inferno',color_scheme='radial',new_fig=False)
F.plot(heart(wheel=Wheel(2*w,p),loops=1,inside=True,guarded=True),
       cmap='inferno',color_scheme='radial',new_fig=False)
F.save_fig()

###

(wheel,pen)=(2.2,1.0)
c="inferno"
cs="radial"
pen_inc=0.5
for j in range(5):
    F.plot(heart(wheel=Wheel(w,pen+j*pen_inc),loops=10,inside=False),cmap=c,color_scheme=cs,
           new_fig = True if j==0 else False)

w=1.5
pen=w*1.1
pen_inc=0.5
for j in range(1):
    F.plot(heart(wheel=Wheel(w,pen+j*pen_inc),loops=22,inside=True,guarded=True),
           cmap=c,color_scheme=cs,new_fig=False)

F.save_fig()

###

(w,p)=(2.2,1.0)
c="inferno"
cs="radial"
pen_inc=0.5
for j in range(5):
    F.plot(heart(wheel=Wheel(w,pen+j*pen_inc),loops=5,fold=True,inside=False),cmap=c,color_scheme=cs,
          new_fig = True if j==0 else False)

w=1.5
pen=w*1.1
pen_inc=0.5
for j in range(1):
    F.plot(heart(wheel=Wheel(w,pen+j*pen_inc),loops=11,fold=True,
                 inside=True,guarded=True),cmap=c,color_scheme=cs,new_fig=False)

F.save_fig()

###

(w,p)=(2.2,1.0)
c="inferno"
cs="radial"
pen_inc=0.5
for j in range(5):
    F.plot(heart(width=40,depth=10,wheel=Wheel(w,pen+j*pen_inc),
                 loops=5,fold=False,inside=False),cmap=c,color_scheme=cs,
           new_fig = True if j==0 else False)

w=1.5
pen=w*1.1
pen_inc=0.5
for j in range(1):
    F.plot(heart(width=50,depth=10,wheel=Wheel(w,pen+j*pen_inc),
                 loops=11,fold=False,inside=True,guarded=True),
           cmap=c,color_scheme=cs,new_fig=False)

F.save_fig()

###

S = SpiroData()

offset=0
c="inferno"
cs="radial"
w=2.2
pen=1
pen_inc=0.5
depth=-3
for j in range(5):
    for i in range(10):
        S.add(roll(20,depth,0,20,wheel=Wheel(w,pen+j*pen_inc,offset)))
        S.add(rotate(0,20,S.xc(),S.yc(),pi))
        S.add(spiro_arc(10,20,-pi/2,10,wheel=Wheel(w,pen+j*pen_inc,S.pc()),loops=0.5))
        S.add(rotate(20,20,S.xc(),S.yc(),pi/2))
        S.add(spiro_arc(30,20,-pi/2,10,wheel=Wheel(w,pen+j*pen_inc,S.pc()),loops=0.5))
        S.add(rotate(40,20,S.xc(),S.yc(),pi))
        S.add(roll(40,20,20,depth,wheel=Wheel(w,pen+j*pen_inc,S.pc())))
        S.add(rotate(20,depth,S.xc(),S.yc(),pi/2))
        offset=S.pc()
        
offset=0
c="inferno"
cs="radial"
w=1.5
pen=w*1.1
pen_inc=0.5
depth=-3
for j in range(1):
    for i in range(22):
        S.add(roll(20,depth,0,20,wheel=Wheel(w,pen+j*pen_inc,offset),invert=True))
        S.add(spiro_arc(10,20,-pi/2,10,wheel=Wheel(w,pen+j*pen_inc,S.pc()),loops=0.5,invert=True))
        S.add(spiro_arc(30,20,-pi/2,10,wheel=Wheel(w,pen+j*pen_inc,S.pc()),loops=0.5,invert=True))
        S.add(roll(40,20,20,depth,wheel=Wheel(w,pen+j*pen_inc,S.pc()),invert=True))
        offset=S.pc()
    
F.plot(S,cmap=c,color_scheme=cs,save=True)
