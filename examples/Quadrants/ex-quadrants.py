import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from spiro import *
from spiro_string import *

S = SpiroData()
F = SpiroFig()

w=Wheel(7.3,5.3,0)

S.reset()
w=Wheel(7.3,5.3,0)
for o in linspace(w.m,w.r,10):
    w.m=o
    S.add(spiro_arc(x0=0,y0=0,orient=o,R=15.0,wheel=w,
                    loops=10,spacing=pi/4000,
                    slide = lambda t: 1,
                    start_guard=0,end_guard=0,start_guard_angle=0,end_guard_angle=0,
                    invert=True,reverse=False))
F.plot(S,color_scheme='cycles',cmap='ocean',save=True)

S.reset()
w=Wheel(7.3,5.3,0)
for o in linspace(w.m,w.r,10):
    w.m=o
    S.add(spiro_arc(x0=0,y0=0,orient=o,R=15.0,wheel=w,
                    loops=7,spacing=pi/4000,
                    quadrants=10, qfuzz=100, slide = lambda t: 1,
                    start_guard=0,end_guard=0,start_guard_angle=0,end_guard_angle=0,
                    invert=True,reverse=False))
F.plot(S,color_scheme='cycles',cmap='ocean',subsample=0,dot_size=.1,save=True)

