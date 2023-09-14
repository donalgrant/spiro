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
    S.add(circle_in_circle(Ring(15),w,loops=10,inside=True).rotate(o))

F.plot(S,color_scheme='cycles',cmap='ocean',save=True)

S.reset()
w=Wheel(7.3,5.3,0)
for o in linspace(w.m,w.r,10):
    w.m=o
    S.add(circle_in_circle(Ring(15),w,loops=7,inside=True,quadrants=10, qfuzz=100).rotate(o))

F.plot(S,color_scheme='cycles',cmap='ocean',subsample=0,dot_size=.1,save=True)

