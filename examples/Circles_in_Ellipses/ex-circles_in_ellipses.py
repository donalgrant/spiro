import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from spiro import *
from spiro_string import *
from spiro_ellipse import *

import matplotlib as mpl
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
cmap1 = LinearSegmentedColormap.from_list("RedOrangePink",["Red","Orange","Pink"])
cmap2 = LinearSegmentedColormap.from_list("Pinks",["rebeccapurple","darkmagenta","orchid","pink"])
cmap3 = LinearSegmentedColormap.from_list("DarkGreen",["seagreen","teal","cornflowerblue","mediumblue","indigo"])

S = SpiroData()
F = SpiroFig()

###

r = Ellipse(20,0.8)
w = Wheel(4,3.5)
S.add(circle_in_ellipse(r,W0).rotate(pi/2))
S.add(circle_in_ellipse(r,w,loops=10,inside=True).rotate(pi/2))

for j in range(1):
    S.add(circle_in_ellipse(r,w,loops=10,inside=False).rotate(pi/2))

F.plot(S,save=True)

###

S.reset()
r = Ellipse(20,0.8)
S.add(circle_in_ellipse(r,Wheel(11,6),loops=20,inside=True).rotate(-pi/4))

for j in range(1):
    S.add(circle_in_ellipse(r,Wheel(6,6),loops=30).rotate(-pi/4))

F.plot(S,color_scheme='time',cmap='magma',save=True)

###

S.reset()
r=Ellipse(20,0.95)
for j in range(4):
    S.add(circle_in_ellipse(r,Wheel(12,10),loops=40,inside=True,ppl=10000))

F.plot(S,color_scheme='s-ripples',save=True)

###

S.reset()
S.add(circle_in_ellipse(r,W0))
for j in range(6):
    S.add(circle_in_ellipse(r,Wheel(1.1,5,pi/10*j),loops=4,inside=True).rotate(pi/20*j))

F.plot(S,color_scheme='cycles',save=True)

###

S.reset()

r = Ellipse(20,0.8)
for j in range(20):
    orient=pi/40*j
    S.add(circle_in_ellipse(r,W0).rotate(orient))
    S.add(circle_in_ellipse(r,Wheel(2.1,4,pi/40*j),loops=2,inside=True).rotate(orient))
F.plot(S,color_scheme='cycles',save=True)

###

S.reset()

for j in range(20):
    orient=pi/40*j
    wo = -pi/2 + pi/40*j
    x0 = j/2
    S.add(circle_in_ellipse(r,W0).rotate(orient).move(x0,0))
    S.add(circle_in_ellipse(r,Wheel(2.1,4,wo),loops=3,inside=True).rotate(orient).move(x0,0))
F.plot(S,color_scheme='cycles',cmap='summer',save=True)

###  (K favorite)

S.reset()

ppl=2000
for j in range(20):
    offset=pi/2+pi/40*j
    orient=pi/4
    wo = pi/40*j
    x0 = j
    y0 = 0
    r = Ellipse(20,0.3+j/50,0,offset)
    S.add(circle_in_ellipse(r,Wheel(5,4,wo),loops=3,ppl=ppl,inside=True).rotate(orient).move(x0,y0))

F.plot(S.rotate(pi),color_scheme='cycles',cmap='Greens',save=True)

###

S.reset()

ppl=2000
for j in range(20):
    orient=pi/4+j/20
    wo = pi/40*j
    x0 = j
    y0 = j/2
    r = Ellipse(20,0.3+j/50,0,orient)
    S.add(circle_in_ellipse(r,Wheel(5,8,wo),loops=3,inside=True,
                            ppl=ppl).rotate(orient).move(x0,y0))

F.plot(S.rotate(3*pi/2),color_scheme='cycles',cmap='nipy_spectral',save=True)

###

S.reset()
ppl=1000
for j in range(20):
    orient=pi/4
    wo = pi/40*j
    x0 = j
    y0 = 0
    r = Ellipse(20,0.3+j/50,0,orient)
    S.add(circle_in_ellipse(r,Wheel(5,2,wo),loops=3,inside=True,ppl=ppl).rotate(orient).move(x0,y0))

F.plot(S,color_scheme='cycles',cmap='turbo',save=True)

###

S.reset()
ppl=2000
for j in range(20):
    orient=pi/4 + pi/20 * j
    wo = pi/40*j
    x0 = 0
    y0 = j/2
    r = Ellipse(20,0.5+j/50,0,orient)
    S.add(circle_in_ellipse(r,W0,ppl=ppl).rotate(orient).move(x0,y0))
    S.add(circle_in_ellipse(r,Wheel(5,5,wo),loops=6,inside=True,
                            ppl=ppl).rotate(orient).move(x0,y0))
    
F.plot(S.rotate(-pi/4),color_scheme='time',cmap='terrain',save=True)

###

S.reset()
ppl=2000
for j in range(20):
    orient=pi/4 + pi/20 * j
    wo = pi/40*j
    x0 = 0
    y0 = j/2
    r = Ellipse(20,0.5+j/50,0,orient)
    S.add(circle_in_ellipse(r,Wheel(4,4,wo),loops=6,inside=True,
                            ppl=ppl).rotate(orient).move(x0,y0))

F.plot(S,color_scheme='time',cmap='gist_earth',save=True)

###

S.reset()

for j in range(20):
    orient=pi/4 + pi/20 * j
    wo = pi/40*j
    x0 = 0
    y0 = j/2
    r = Ellipse(30,0.5+j/50,0,orient)
    S.add(circle_in_ellipse(r,W0,loops=1,ppl=ppl).rotate(orient))
    S.add(circle_in_ellipse(r,Wheel(4,5,wo),loops=1.5,inside=True,
                            ppl=ppl).rotate(orient).move(x0,y0))
    
F.plot(S.rotate(-pi/4),color_scheme='cycles',cmap='gist_earth',save=True)

###

S.reset()
ppl=2000
for j in range(20):
    orient=pi/4 + pi/20 * j
    wo = pi/40*j
    x0 = 0
    y0 = j/2
    r = Ellipse(30,0.5+j/50,0,orient)
    S.add(circle_in_ellipse(r,Wheel(4,5,wo),loops=2.5,
                            ppl=ppl).rotate(orient).move(x0,y0))
    S.add(circle_in_ellipse(r,Wheel(20,13,wo),loops=2.5,inside=True,
                            ppl=ppl).rotate(orient).move(x0,y0))
    
F.plot(S,color_scheme='cycles',cmap='ocean',save=True)

###

S.reset()
r.a=20
ppl=2000
for j in range(20):
    orient=pi/4 + pi/80 * j
    x0 = 0
    y0 = j/10
    r = Ellipse(20,0.5+j/50,0,orient)
    for wo in np.linspace(0,20*pi,20):
        S.add(circle_in_ellipse(r,Wheel(2.3,4.5,wo),loops=0.05,
                                ppl=ppl).rotate(orient).move(x0,y0))
        
F.plot(S,color_scheme='cycles',cmap='ocean',save=True)

###

S.reset()
for j in range(10):
    S.add(circle_in_ellipse(Ellipse(20.2,0.85),
                            Wheel(2.6,15,pi/10*j),loops=13))
    
F.plot(S,color_scheme='radial',cmap='turbo',save=True)

###

S.reset()
r = Ellipse(20,0.8)
ppl=2000
for j in range(20):
    offset=pi/2+pi/40*j
    orient=pi/4
    wo = pi/40*j
    x0 = j/2
    y0 = j/2
    r.e = 0.3 + j/50
    r.o = offset
    S.add(circle_in_ellipse(r,Wheel(5,4,wo),loops=3,ppl=ppl,inside=True).rotate(orient).move(x0,y0))
    
F.plot(S.rotate(pi),color_scheme='cycles',cmap=cmap1,save=True)
