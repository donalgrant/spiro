import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from Ellipse import *
from spiro_ellipse import *
from spiro import *

S = SpiroData()
F = SpiroFig()

# made a special colormap for several of these...

import matplotlib as mpl
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
cmap = LinearSegmentedColormap.from_list("RedOrangePink",["Red","Orange","Pink"])

###

S.reset()
for po in np.linspace(0,pi/4,9):
    S.add(elliptical_arc_new(x0=po/2,y0=po/2,R=20+po/5,
                              wheel=Ellipse(10,0.4,7.5),orient=pi/7,
                              loops=6,inside=True,pen_offset=po,spacing=0.0003))
    
for po in np.linspace(0,pi/4,9):
    S.add(elliptical_arc_new(x0=po*2,y0=po*4,R=20+po/5,
                              wheel=Ellipse(10,0.4,7.5),loops=3,inside=False,
                              pen_offset=po,spacing=0.0003))
    
F.plot(S,color_scheme='cycles',cmap=cmap,dot_size=0.1,save=True)

###

S.reset()
S.add(elliptical_arc_new(x0=0,y0=0,R=20,
                          wheel=Ellipse(3.4,0.9,20),orient=0,
                          loops=5,inside=False,pen_offset=pi/2,spacing=0.0001))
F.plot(S,color_scheme='cycles',cmap=cmap,dot_size=0.1,save=True)

###

S.reset()

for po in np.linspace(0,10,8):
    S.add(elliptical_arc_new(x0=po/4,y0=-po/2,R=14,wheel=Ellipse(15-po/5,0.7,10+po/30),
                              orient=pi/30*po,loops=10,inside=True,
                              pen_offset=pi/20*po,spacing=0.0005))
    

for po in np.linspace(0,10,8):
    S.add(elliptical_arc_new(x0=po/4,y0=-po/2,R=14,wheel=Ellipse(15-po/2,0.7,10+po/30),
                              orient=pi/30*po,loops=5,inside=False,
                              pen_offset=pi/20*po,spacing=0.0005))
    
F.plot(S,color_scheme='cycles',cmap='autumn',save=True)

###

S.reset()

for a in np.linspace(9,25,2):
    w = Ellipse(a,0.7,1.3*a)
    for i in range(6):
        S.add(elliptical_arc_new(x0=0,y0=0,R=30,wheel=w,orient=0,
                                  loops=5,inside=True,pen_offset=pi/24*i,spacing=0.0003))
    
F.plot(S,color_scheme='cycles',cmap='ocean',save=True)

###

S.reset()

for a in np.linspace(10,25,4):
    w = Ellipse(a,0.7,1.3*a)
    for i in range(3):
        S.add(elliptical_arc_new(x0=0,y0=0,R=30,wheel=w,orient=0,
                                  loops=5,inside=True,pen_offset=pi/24*i,spacing=0.0003))

F.plot(S,color_scheme='cycles',cmap='ocean',save=True)

###

S.reset()

for a in np.linspace(5,20,5):
    w = Ellipse(a,0.7,1.3*a)
    for i in range(3):
        S.add(elliptical_arc_new(x0=0,y0=0,R=30-i*2,wheel=w,orient=0,
                                  loops=3,inside=True,pen_offset=0,spacing=0.0003))
    
F.plot(S,color_scheme='cycles',cmap='ocean',save=True)

###

S.reset()

for a in np.linspace(5,20,5):
    w = Ellipse(a,0.7,1.3*a)
    S.add(elliptical_arc_new(x0=0,y0=0,R=30,wheel=w,orient=0,
                              loops=8,inside=True,pen_offset=0,spacing=0.0003))
    
F.plot(S,color_scheme='radial',cmap='magma',save=True)

###

S.reset()

for po in np.linspace(5,25,6):
    w = Ellipse(po,0.7,7)
    S.add(elliptical_arc_new(x0=0,y0=0,R=30,wheel=w,orient=0,
                              loops=5,inside=True,pen_offset=0,spacing=0.0003))
    
F.plot(S,color_scheme='radial',cmap='magma',save=True)

###

S.reset()

for po in np.linspace(0,10,5):
    S.add(elliptical_arc_new(x0=0,y0=0,R=5,wheel=Ellipse(15,0.9,7+po/5),
                              orient=pi/7,loops=20,inside=True,pen_offset=0,spacing=0.0003))
    
F.plot(S,color_scheme='radial',cmap='Wistia',save=True)

###

S.reset()

for po in np.linspace(0,pi/4,2):
    S.add(elliptical_arc_new(x0=po/2,y0=po/2,R=5+po/5,wheel=Ellipse(15,0.9,7),
                              orient=pi/7,loops=60,inside=True,pen_offset=po,spacing=0.0003))
    
F.plot(S,color_scheme='cycles',cmap='summer',save=True)

###

S.reset()

for po in np.linspace(0,pi/4,9):
    S.add(elliptical_arc_new(x0=po/2,y0=po/2,R=20+po/5,wheel=Ellipse(10,0.8,7.5),
                              orient=pi/7,loops=3,inside=True,pen_offset=po,spacing=0.0003))
    
for po in np.linspace(0,pi/4,9):
    S.add(elliptical_arc_new(x0=po*2,y0=po*4,R=20+po/5,wheel=Ellipse(10,0.8,7.5),
                              loops=3,inside=False,pen_offset=po,spacing=0.0003))
    
F.plot(S,color_scheme='cycles',cmap=cmap,save=True)

###

S.reset()

for po in np.linspace(0,pi/4,9):
    S.add(elliptical_arc_new(x0=po*2,y0=po*4,R=20+po/5,wheel=Ellipse(10,0.8,7.5),
                              loops=12,inside=True,pen_offset=po,spacing=0.0003))

F.plot(S,color_scheme='time',cmap=cmap,save=True)

###

S.reset()

for po in np.linspace(0,pi/4,9):
    S.add(elliptical_arc_new(R=20,wheel=Ellipse(10,0.6,8),loops=5,inside=True,pen_offset=po))

F.plot(S,color_scheme='polar',cmap='turbo',dot_size=0.5,save=True)

###

S.reset()
S.add(elliptical_arc_new(R=20,wheel=Ellipse(0.01,0.0,0.0),loops=1,inside=True))
S.add(elliptical_arc_new(R=20,wheel=Ellipse(5.2,0.8,5.2),loops=9,inside=False))
S.add(elliptical_arc_new(R=20,wheel=Ellipse(2.2,0.6,2.2),loops=9,inside=True))
F.plot(S,color_scheme='polar',cmap='turbo',dot_size=0.5,save=True)

###

S.reset()
S.add(elliptical_arc_new(R=20,wheel=Ellipse(0.01,0.0,0.0),loops=1,inside=True))
S.add(elliptical_arc_new(R=20,wheel=Ellipse(5.2,0.8,2.4),loops=9,inside=False,pen_offset=pi/4))
S.add(elliptical_arc_new(R=20,wheel=Ellipse(2.2,0.6,1),loops=9,inside=True,pen_offset=pi/4))
F.plot(S,color_scheme='polar',cmap='turbo',dot_size=0.5,save=True)

###

S.reset()
S.add(elliptical_arc_new(R=20,wheel=Ellipse(0.01,0.0,0.0),loops=1,inside=True))
S.add(elliptical_arc_new(R=20,wheel=Ellipse(5.2,0.8,3),loops=10,inside=False,spacing=0.0003))
S.add(elliptical_arc_new(R=20,wheel=Ellipse(5.2,0.8,3,S.pc()),loops=10,inside=True,spacing=0.0003))
F.plot(S,color_scheme='cycles',cmap='inferno',save=True)

###

S.reset()
S.add(elliptical_arc_new(R=20,wheel=Ellipse(10,0.7,8,0),
                          loops=30,inside=True,spacing=0.0003))
for i in range(6):  
    S.add(elliptical_arc_new(R=20,wheel=Ellipse(4,0.95,4),
                              orient=pi/6*i,loops=4,inside=False,spacing=0.00005))
F.plot(S,color_scheme='cycles',save=True,dot_size=0.3)

###

S.reset()
S = SpiroData()
for i in range(4):  
    S.add(elliptical_arc_new(R=20,wheel=Ellipse(40,0.6+i/50,40),
                              orient=0,loops=10,inside=False))
F.plot(S,color_scheme='time',cmap='inferno',save=True)

###

S.reset()
S.add(spiro_arc(R=20,wheel=Wheel(0.01,0.0)))
for i in range(6):
    S.add(elliptical_arc_new(R=20,wheel=Ellipse(10,0.3,4,pi/3*i),loops=10, inside=True))
    S.add(elliptical_arc_new(R=20,wheel=Ellipse(3.5,0.1,2,0),
                                             orient=pi/3*i,loops=4, inside=True))
S.add(elliptical_arc_new(R=20,wheel=Ellipse(3,0.1,4,0),loops=21, inside=False, spacing=0.0005))
F.plot(S,save=True,color_scheme='t-waves')

###

S.reset()
for p in range(10):
    S.add(elliptical_arc_new(x0=0,y0=0,orient=0,R=2.0,wheel=Ellipse(9.5,0.4,5+p/2,0),
                              loops=10,spacing=pi/4000,inside=False))
for csi in ['time','rrand']:
    F.plot(S,cmap='tab20b',color_scheme=csi,save=True)

###

S.reset()
for j in range(10):
    S.add(elliptical_arc_new(x0=-j/5,y0=j/5,orient=0,R=2.0,wheel=Ellipse(6.5,0.8,2,pi/20*j),
                              loops=3,spacing=pi/4000,inside=False))
F.plot(S,cmap='Dark2',color_scheme='time')
