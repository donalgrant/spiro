import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from Ellipse import *
from spiro_ellipse import *
from spiro import *
from Ring import *

S = SpiroData()
F = SpiroFig()

# made a special colormap for several of these...

import matplotlib as mpl
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
cmap = LinearSegmentedColormap.from_list("RedOrangePink",["Red","Orange","Pink"])

###

S.reset()
for po in np.linspace(0,pi/4,9):
    r = Ring(20+po/5,np.array([po/2,po/2]),pi/7)
    S.add(ellipse_in_circle(r,Ellipse(10,0.4,7.5,pen_offset=po),
                            loops=6,inside=True,pts_per_loop=3000))
    
for po in np.linspace(0,pi/4,9):
    r = Ring(20+po/5,np.array([po*2,po*4]))
    S.add(ellipse_in_circle(r,Ellipse(10,0.4,7.5,pen_offset=po),
                            loops=3,inside=False,pts_per_loop=3000))
    
F.plot(S,color_scheme='cycles',cmap=cmap,dot_size=0.1,save=True)

###

S.reset()
S.add(ellipse_in_circle(Ring(20),Ellipse(3.4,0.9,20,pen_offset=pi/2),
                          loops=5,inside=False,pts_per_loop=10000))
F.plot(S,color_scheme='cycles',cmap=cmap,dot_size=0.1,save=True)

###

S.reset()

for po in np.linspace(0,10,8):
    S.add(ellipse_in_circle(Ring(14,origin=np.array([po/4,-po/2]),orient=pi/30*po),
                            Ellipse(15-po/5,0.7,10+po/30,pen_offset=pi/20*po),
                            loops=10,inside=True,pts_per_loop=2000))
    

for po in np.linspace(0,10,8):
    S.add(ellipse_in_circle(Ring(14,origin=np.array([po/4,-po/2]),orient=pi/30*po),
                            Ellipse(15-po/2,0.7,10+po/30,pen_offset=pi/20*po),
                            loops=5,inside=False,pts_per_loop=2000))
    
F.plot(S,color_scheme='cycles',cmap='autumn',save=True)

###

S.reset()

for a in np.linspace(9,25,2):
    w = Ellipse(a,0.7,1.3*a)
    for i in range(6):
        w.po=pi/24*i
        S.add(ellipse_in_circle(Ring(30),w,loops=5,inside=True,pts_per_loop=3000))
    
F.plot(S,color_scheme='cycles',cmap='ocean',save=True)

###

S.reset()

for a in np.linspace(10,25,4):
    w = Ellipse(a,0.7,1.3*a)
    for i in range(3):
        w.po=pi/24*i
        S.add(ellipse_in_circle(Ring(30),w,loops=5,inside=True,pts_per_loop=3000))

F.plot(S,color_scheme='cycles',cmap='ocean',save=True)

###

S.reset()

for a in np.linspace(5,20,5):
    w = Ellipse(a,0.7,1.3*a)
    for i in range(3):
        S.add(ellipse_in_circle(Ring(30-i*2),w,loops=3,inside=True,pts_per_loop=3000))
    
F.plot(S,color_scheme='cycles',cmap='ocean',save=True)

###

S.reset()

for a in np.linspace(5,20,5):
    w = Ellipse(a,0.7,1.3*a)
    S.add(ellipse_in_circle(Ring(30),w,loops=8,inside=True,pts_per_loop=3000))
    
F.plot(S,color_scheme='radial',cmap='magma',save=True)

###

S.reset()

for po in np.linspace(5,25,6):
    w = Ellipse(po,0.7,7)
    S.add(ellipse_in_circle(Ring(30),w,loops=5,inside=True,pts_per_loop=3000))
    
F.plot(S,color_scheme='radial',cmap='magma',save=True)

###

S.reset()

for po in np.linspace(0,10,5):
    S.add(ellipse_in_circle(Ring(5,orient=pi/7),Ellipse(15,0.9,7+po/5),
                            loops=20,inside=True,pts_per_loop=3000))
    
F.plot(S,color_scheme='radial',cmap='Wistia',save=True)

###

S.reset()

for po in np.linspace(0,pi/4,2):
    S.add(ellipse_in_circle(Ring(5+po/5,origin=np.array([po/2,po/2]),orient=pi/7),
                            Ellipse(15,0.9,7,pen_offset=po),loops=60,inside=True,
                            pts_per_loop=3000))
    
F.plot(S,color_scheme='cycles',cmap='summer',save=True)

###

S.reset()

for po in np.linspace(0,pi/4,9):
    S.add(ellipse_in_circle(Ring(20+po/5,origin=np.array([po/2,po/2]),orient=pi/7),
                            Ellipse(10,0.8,7.5,pen_offset=po),
                            loops=3,inside=True,pts_per_loop=3000))
    
for po in np.linspace(0,pi/4,9):
    S.add(ellipse_in_circle(Ring(20+po/5,origin=np.array([po*2,po*4])),
                            Ellipse(10,0.8,7.5,pen_offset=po),
                            loops=3,inside=False,pts_per_loop=3000))
    
F.plot(S,color_scheme='cycles',cmap=cmap,save=True)

###

S.reset()

for po in np.linspace(0,pi/4,9):
    S.add(ellipse_in_circle(Ring(20+po/5,origin=np.array([po*2,po*4])),
                            Ellipse(10,0.8,7.5,pen_offset=po),
                            loops=12,inside=True,pts_per_loop=3000))

F.plot(S,color_scheme='time',cmap=cmap,save=True)

###

S.reset()

for po in np.linspace(0,pi/4,9):
    S.add(ellipse_in_circle(Ring(20),Ellipse(10,0.6,8,pen_offset=po),
                            loops=5,inside=True))

F.plot(S,color_scheme='polar',cmap='turbo',dot_size=0.5,save=True)

###

S.reset()
r = Ring(20)
S.add(ellipse_in_circle(r,Ellipse(0.01,0.0,0.0),loops=1,inside=True))
S.add(ellipse_in_circle(r,Ellipse(5.2,0.8,5.2),loops=9,inside=False))
S.add(ellipse_in_circle(r,Ellipse(2.2,0.6,2.2),loops=9,inside=True))
F.plot(S,color_scheme='polar',cmap='turbo',dot_size=0.5,save=True)

###

S.reset()
r = Ring(20)
S.add(ellipse_in_circle(r,Ellipse(0.01,0.0,0.0),loops=1,inside=True))
S.add(ellipse_in_circle(r,Ellipse(5.2,0.8,2.4,pen_offset=pi/4),loops=9,inside=False))
S.add(ellipse_in_circle(r,Ellipse(2.2,0.6,1,pen_offset=pi/4),loops=9,inside=True))
F.plot(S,color_scheme='polar',cmap='turbo',dot_size=0.5,save=True)

###

S.reset()
r = Ring(20)
S.add(ellipse_in_circle(r,Ellipse(0.01,0.0,0.0),loops=1,inside=True))
S.add(ellipse_in_circle(r,Ellipse(5.2,0.8,3),loops=10,inside=False,pts_per_loop=3000))
S.add(ellipse_in_circle(r,Ellipse(5.2,0.8,3,S.pc()),loops=10,inside=True,pts_per_loop=3000))
F.plot(S,color_scheme='cycles',cmap='inferno',save=True)

###

S.reset()
r = Ring(20)
S.add(ellipse_in_circle(r,Ellipse(10,0.7,8,0),
                          loops=30,inside=True,pts_per_loop=3000))
for i in range(6):
    r.o=pi/6*i
    S.add(ellipse_in_circle(r,Ellipse(4,0.95,4),
                            loops=4,inside=False,pts_per_loop=20000))
F.plot(S,color_scheme='cycles',save=True,dot_size=0.3)

###

S.reset()
r = Ring(20)
S = SpiroData()
for i in range(4):  
    S.add(ellipse_in_circle(r,Ellipse(40,0.6+i/50,40),
                            loops=10,inside=False))
F.plot(S,color_scheme='time',cmap='inferno',save=True)

###

S.reset()
r = Ring(20)
S.add(circle_in_circle(r,Wheel(0.01,0.0)))
for i in range(6):
    S.add(ellipse_in_circle(r,Ellipse(10,0.3,4,pi/3*i),loops=10, inside=True))
    r1 = r
    r1.o=pi/3*i
    S.add(ellipse_in_circle(r1,Ellipse(3.5,0.1,2,0),loops=4, inside=True))
S.add(ellipse_in_circle(r,Ellipse(3,0.1,4,0),loops=21, inside=False, pts_per_loop=2000))
F.plot(S,save=True,color_scheme='t-waves')

###

S.reset()
r = Ring(2)
for p in range(10):
    S.add(ellipse_in_circle(r,Ellipse(9.5,0.4,5+p/2,0),inside=False))
for csi in ['time','rrand']:
    F.plot(S,cmap='tab20b',color_scheme=csi,save=True)

###

S.reset()
r = Ring(2)
for j in range(10):
    r = Ring(2,np.array([-j/5,j/5]))
    S.add(ellipse_in_circle(r,Ellipse(6.5,0.8,2,pi/20*j),loops=3,inside=False))
F.plot(S,cmap='Dark2',color_scheme='time',save=True)
