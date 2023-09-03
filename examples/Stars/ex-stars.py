import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from spiro import *
from polygon import *

S = SpiroData()
F = SpiroFig()

###

F.plot(spiro_nstar(6,r2=0.6,wheel=Wheel(3,3),
                   loops=10,fold=False,inside=True),
       color_scheme='time',cmap='Purples')
F.plot(spiro_nstar(6,r2=0.6,wheel=Wheel(5,4),
                   loops=10,inside=False,fold=False),
       color_scheme='time',cmap='autumn',new_fig=False)

F.save_fig()

###

F.plot(spiro_nstar(12,r2=0.5,wheel=Wheel(3.6,3),
                   loops=10,fold=False,inside=True),
       color_scheme='time',cmap='Purples')
F.plot(spiro_nstar(6,r2=0.5,wheel=Wheel(7,6),
                   loops=20,inside=False,fold=False,orient=pi/6),
       color_scheme='time',cmap='autumn',new_fig=False)

F.save_fig()

###

F.plot(spiro_nstar(4,r2=0.3,wheel=Wheel(3.2,3),
                   loops=10,fold=True,inside=True),
       color_scheme='time',cmap='Purples')
F.plot(spiro_nstar(8,r2=0.6,wheel=Wheel(5,4),
                   loops=10,inside=False,fold=False),
       color_scheme='time',cmap='autumn',new_fig=False)

F.save_fig()
