import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from spiro import *
from polygon import *

S = SpiroData()
F = SpiroFig()

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
