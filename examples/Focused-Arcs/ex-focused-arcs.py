import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_string import *
from polygon import *
from Ring import *

F=SpiroFig()
F.text_color='white'

F.set_default_dpi(150)

S = SpiroData()

###

N=600
S.add(cIc(Ring(50),Wheel(8.7,10),inside=True,ppl=N))

T=SpiroData()
for first in range(6):
    for offset in range(15):
        Q=SpiroData()
        Q.add(arcs_from_multi(S,array([int(offset*3+N/3)]),100,invert=True,line_pts=400,
                              max_strings=1,first=int(N/6*first*1.3),arc_only=False)).move(0,0).rotate(0)
        Q.t=Q.x*0+first%5
        T.add(Q)

F.plot(T,cmap='jet',color_scheme='time',save=True)
