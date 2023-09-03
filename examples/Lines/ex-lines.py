import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from spiro import *
from polygon import *

S = SpiroData()
F = SpiroFig()

###

F.plot(spiro_line(50,Wheel(5,4),orient=0,loops=4,fold=False),
       new_fig=True,color_scheme='time')
F.plot(spiro_line(50,Wheel(5,4),orient=0,loops=4,fold=False),
       new_fig=False,color_scheme='time',alpha=0.1,subsample=5,dot_size=50)
F.save_fig()

###

o=0
w=Wheel(3,2)
coords=array([ [-20,10], [20,10] ])
F.plot(spiro_polygon(coords, Wheel(0.01,0), o, 1, fold=True, inside=False))
F.plot(spiro_polygon(coords, w, o, 10, fold=False, inside=False),new_fig=False)
coords=array([ [-20,-10], [20,-10] ])
F.plot(spiro_polygon(coords, Wheel(0.01,0), o, 1, fold=True, inside=False),new_fig=False)
F.plot(spiro_polygon(coords, w, o, 10, fold=True, inside=False),new_fig=False)

F.save_fig()

###

F.plot(spiro_line(50,Wheel(5,4),orient=pi/4,loops=4,fold=True),save=True)

###

F.plot(spiro_line_orig(50,Wheel(5,4),orient=0,loops=1,fold=True,invert=True),
       color_scheme='time',save=True)

c='viridis'
cs='radial'
F.plot(spiro_line(50,Wheel(5,4),orient=0,loops=4,fold=True),
       cmap=c,color_scheme=cs)
for o in range(10):
    F.plot(spiro_line(50,Wheel(5,4),orient=2*pi/10*o,loops=4,fold=True),
           new_fig=False,cmap=c,color_scheme=cs)
F.save_fig()

###

F.plot(spiro_line(62,Wheel(-20,15.0),loops=10,fold=False),save=True)
