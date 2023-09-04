import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from spiro import *
from spiro_string import *

S = SpiroData()
F = SpiroFig()

###

S.add(wheel_in_ellipse(0,0,wheel=Wheel(0.01,0.0),ellipse=Ellipse(20,0.8,0,pi/2),
                       loops=1,orient=pi/2))
S.add(wheel_in_ellipse(0,0,wheel=Wheel(4,3.5),ellipse=Ellipse(20,0.8,0,pi/2),
                       loops=10,invert=True,orient=pi/2))
for j in range(1):
    S.add(wheel_in_ellipse(0,0,wheel=Wheel(4,3.5),ellipse=Ellipse(20,0.8,0,pi/2+pi/20*j),
                           loops=10,invert=False,orient=pi/2))
F.plot(S,save=True)

###

S.reset()
S.add(wheel_in_ellipse(0,0,wheel=Wheel(11,6),ellipse=Ellipse(20,0.8,0,pi/2),
                       loops=20,invert=True,orient=-pi/4))
for j in range(1):
    S.add(wheel_in_ellipse(0,0,wheel=Wheel(6,6),ellipse=Ellipse(20,0.8,0,pi/2+pi/20*j),
                           loops=30,invert=False,orient=-pi/4))
F.plot(S,color_scheme='time',cmap='magma',save=True)

###

S.reset()
for j in range(4):
    S.add(wheel_in_ellipse(0,0,wheel=Wheel(4,3.5),ellipse=Ellipse(20,0.8,0,pi/2+pi/40*j),
                           loops=10,invert=False,orient=pi/2))
F.plot(S,save=True)

###

S.reset()
for j in range(4):
    S.add(wheel_in_ellipse(0,0,wheel=Wheel(12,10),ellipse=Ellipse(20,0.95,0,pi/2+pi/40*j),
                           loops=10,invert=True))

F.plot(S,color_scheme='s-ripples',save=True)

###

S.reset()
S.add(wheel_in_ellipse(0,0,wheel=Wheel(0.01,0.0),ellipse=Ellipse(20,0.95,0,pi/2),
                       loops=1,invert=False))
for j in range(6):
    S.add(wheel_in_ellipse(0,0,wheel=Wheel(1.1,5,pi/10*j),ellipse=Ellipse(20,0.95,0,pi/2+pi/40*j),
                           loops=4,invert=True,orient=pi/20*j))

F.plot(S,color_scheme='cycles',save=True)

###

S.reset()
e = 0.8
for j in range(20):
    offset=0 # pi/2+pi/40*j
    orient=pi/40*j
    S.add(wheel_in_ellipse(0,0,wheel=Wheel(0.01,0.0),
                           ellipse=Ellipse(20,e,0,offset),
                           loops=1,invert=False,orient=orient))
    S.add(wheel_in_ellipse(0,0,wheel=Wheel(2.1,4,pi/40*j),
                           ellipse=Ellipse(20,e,0,offset),
                           loops=2,invert=True,orient=orient))
F.plot(S,color_scheme='cycles',save=True)

###

S.reset()
e = 0.8
for j in range(20):
    offset=0 # pi/2+pi/40*j
    orient=pi/40*j
    wo = -pi/2 + pi/40*j
    x0 = j/2
    S.add(wheel_in_ellipse(x0,0,wheel=Wheel(0.01,0.0),
                           ellipse=Ellipse(20,e,0,offset),
                           loops=1,invert=False,orient=orient))
    S.add(wheel_in_ellipse(x0,0,wheel=Wheel(2.1,4,wo),
                           ellipse=Ellipse(20,e,0,offset),
                           loops=3,invert=True,orient=orient))
F.plot(S,color_scheme='cycles',cmap='summer',save=True)

###  (K favorite)

S.reset()
ppl=2000
for j in range(20):
    offset=0 # pi/2+pi/40*j
    orient=pi/4
    wo = pi/40*j
    x0 = j
    e = 0.3 + j/50
    S.add(wheel_in_ellipse(x0,0,wheel=Wheel(5,4,wo),
                           ellipse=Ellipse(20,e,0,offset),
                           pts_per_loop=ppl,
                           loops=3,invert=True,orient=orient))
F.plot(S,color_scheme='cycles',cmap='Greens')
F.save_fig(dpi=100)

###

S.reset()
ppl=2000
for j in range(20):
    offset=0 # pi/2+pi/40*j
    orient=pi/4
    wo = pi/40*j
    x0 = j
    e = 0.3 + j/50
    S.add(wheel_in_ellipse(x0,0,wheel=Wheel(5,8,wo),
                           ellipse=Ellipse(20,e,0,offset),
                           pts_per_loop=ppl,
                           loops=3,invert=True,orient=orient))
    
F.plot(S,color_scheme='cycles',cmap='nipy_spectral',save=True)

###

S.reset()
ppl=2000
for j in range(20):
    offset=0 # pi/2+pi/40*j
    orient=pi/4
    wo = pi/40*j
    x0 = j
    e = 0.3 + j/50
    S.add(wheel_in_ellipse(x0,0,wheel=Wheel(5,2,wo),
                           ellipse=Ellipse(20,e,0,offset),
                           pts_per_loop=ppl,
                           loops=3,invert=True,orient=orient))

for c in ['ocean','turbo']:
    F.plot(S,color_scheme='cycles',cmap=c,save=True)

###

S.reset()
ppl=2000
for j in range(20):
    offset=0 # pi/2+pi/40*j
    orient=pi/4 + pi/20 * j
    wo = pi/40*j
    x0 = 0
    y0 = j/2
    e = 0.5 + j/50
    S.add(wheel_in_ellipse(x0,y0,wheel=Wheel(0.01,0.0),
                           ellipse=Ellipse(20,e,0,offset),
                           pts_per_loop=ppl,
                           loops=1,invert=False,orient=orient))
    S.add(wheel_in_ellipse(x0,y0,wheel=Wheel(5,5,wo),
                           ellipse=Ellipse(20,e,0,offset),
                           pts_per_loop=ppl,
                           loops=6,invert=True,orient=orient))
    
F.plot(S,color_scheme='time',cmap='terrain',save=True)

###

S.reset()
ppl=2000
for j in range(20):
    offset=0 # pi/2+pi/40*j
    orient=pi/4 + pi/20 * j
    wo = pi/40*j
    x0 = 0
    y0 = j/2
    e = 0.5 + j/50
    S.add(wheel_in_ellipse(x0,y0,wheel=Wheel(4,4,wo),
                           ellipse=Ellipse(20,e,0,offset),
                           pts_per_loop=ppl,
                           loops=6,invert=True,orient=orient))
F.plot(S,color_scheme='time',cmap='gist_earth',save=True)

###

S.reset()
ppl=2000
for j in range(20):
    offset=0 # pi/2+pi/40*j
    orient=pi/4 + pi/20 * j
    wo = pi/40*j
    x0 = 0
    y0 = j/2
    e = 0.5 + j/50
    S.add(wheel_in_ellipse(x0,y0,wheel=Wheel(0.01,0.0),
                           ellipse=Ellipse(20,e,0,offset),
                           pts_per_loop=ppl,
                           loops=1,invert=False,orient=orient))
    S.add(wheel_in_ellipse(x0,y0,wheel=Wheel(4,5,wo),
                            ellipse=Ellipse(30,e,0,offset),
                            pts_per_loop=ppl,
                            loops=2,invert=True,orient=orient))
    
F.plot(S,color_scheme='cycles',cmap='gist_earth',save=True)

###

S.reset()
ppl=2000
for j in range(20):
    offset=0 # pi/2+pi/40*j
    orient=pi/4 + pi/20 * j
    wo = pi/40*j
    x0 = 0
    y0 = j/2
    e = 0.5 + j/50
    S.add(wheel_in_ellipse(x0,y0,wheel=Wheel(4,5,wo),
                           ellipse=Ellipse(30,e,0,offset),
                           pts_per_loop=ppl,
                           loops=2.5,invert=False,orient=orient))
    S.add(wheel_in_ellipse(x0,y0,wheel=Wheel(20,13,wo),
                           ellipse=Ellipse(30,e,0,offset),
                           pts_per_loop=ppl,
                           loops=2.5,invert=True,orient=orient))
    
F.plot(S,color_scheme='cycles',cmap='ocean',save=True)

###

S.reset()
ppl=2000
for j in range(20):
    offset=0 # pi/2+pi/40*j
    orient=pi/4 + pi/80 * j
    woo = j/50
    x0 = 0
    y0 = j/10
    e = 0.5 + j/50
    for wo in np.linspace(0,20*pi,20):
        S.add(wheel_in_ellipse(x0,y0,wheel=Wheel(2.3,4.5,wo),
                               ellipse=Ellipse(20,e,0,offset),
                               pts_per_loop=ppl,
                               loops=.05,invert=False,orient=orient))
        
F.plot(S,color_scheme='cycles',cmap='ocean',save=True)

###

S.reset()
for j in range(10):
    S.add(wheel_in_ellipse(0,0,wheel=Wheel(2.6,15,pi/10*j),
                           ellipse=Ellipse(20.2,0.85,0,pi/2+pi/40*j),
                           loops=4,invert=False))
    
F.plot(S,color_scheme='radial',cmap='turbo',save=True)
