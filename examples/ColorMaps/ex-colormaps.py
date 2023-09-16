import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from spiro import *
from spiro_string import *
from Ring import *

###

T = spiro_string(cIc(Ring(10),Wheel(4,3.5),loops=50,
                                  ppl=1283),subsample=500)
print(T.n())
nsubs=len(cmap_list())
ncols=6
nrows=nsubs//ncols
G = SpiroFig(rows=nrows,cols=ncols)
G.text_color='white'
if nsubs % ncols > 0:  nrows += 1
for cs in cs_list():
    first=True
    for color_map in cmap_list():
        G.plot(T,color_scheme=cs,cmap=color_map,caption=color_map,
               new_fig=True if first else False)
        first=False
    G.caption(cs)
    G.save_fig()

###

cs = cs_list()

nsubs=len(cs)
ncols=5
nrows=nsubs//ncols
if nsubs % ncols > 0:  nrows += 1

S = spiro_steps(Ring(8.0),wheel=Wheel(4,4),loops=5,n=10)
F = SpiroFig(rows=nrows,cols=ncols)

F.text_color='white'
first=True
for color_scheme in cs:
    F.plot(S,color_scheme=color_scheme,cmap='hsv',caption=color_scheme,
           new_fig=True if first else False)
    first=False

F.save_fig('color_scheme_chart.png')
