import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from Ellipse import *
from spiro import *
from spiro_string import *
from spiro_ellipse import *

S = SpiroData()
F = SpiroFig()

cmaps=cmap_list()
cs = cs_list()

###

S.reset()
for j in range(10):
    S.add(elliptical_arc(x0=-j/5,y0=j/5,orient=0,R=2.0,wheel=Ellipse(6.5,0.8,2,pi/20*j),
                             loops=3,spacing=0.01,inside=False))
F.plot(S,cmap='Dark2',color_scheme='time',dot_size=10,alpha=1.0)

###

for t in [True,False]:
    S.reset()
    S = spiro(R=20,wheel=Wheel(5.5,4,0),loops=10,orient=0,inside=t,spacing=0.001)
    for s in [200,400,800,1600,3200,6400]:
        SO = string_offset_pairs(S,offset=s,step=20)
        for csi in ['radial']:
            for ds in [1,3,5,10,15]:
                F.plot(SO,caption=True,new_fig=True,
                       subsample=25,dot_size=ds,
                       color_scheme=csi,cmap=cmaps[F.fig_number % len(cmaps)])
                F.save_fig()
