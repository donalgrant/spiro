import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from spiro import *
from spiro_string import *
from polygon import *

S = SpiroData()
F = SpiroFig()

###

F.plot(spiro_cross())
F.plot(spiro_cross(wheel=Wheel(5,3.5),loops=10,fold=False), new_fig=False)
F.plot(spiro_cross(wheel=Wheel(3,2.8),loops=10,fold=False,inside=True), new_fig=False)

F.save_fig()

###

F.plot(spiro_cross(width=71,height=97,base=0.6,fwidth=0.25,fheight=0.15,
                   wheel=Wheel(5,3.5),loops=10,fold=False), 
       new_fig=True, cmap="Purples",color_scheme='time')
F.plot(spiro_cross(width=71,height=97,base=0.6,fwidth=0.25,fheight=0.15,
                   wheel=Wheel(4,2.8),loops=10,fold=True,inside=True), 
       new_fig=False, cmap="Reds", color_scheme='time')

F.save_fig()

###

for o in range(10):
    F.plot(spiro_cross(wheel=Wheel(2,5.5,pi/30*o),loops=2,fold=False),
           new_fig=True if o==0 else False)

F.save_fig()

###

for o in range(10):
    F.plot(spiro_cross(wheel=Wheel(2,5.5+o/4,pi/30*o),loops=2,fold=False),
           new_fig=True if o==0 else False)

F.save_fig()
