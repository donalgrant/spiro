import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from spiro import *
from spiro_string import *

S = SpiroData()
F = SpiroFig()

cmaps=cmap_list()
cs = cs_list()

S.reset()
t=False
S = spiro(R=20,wheel=Wheel(1.7,17.8,0),loops=10,orient=0,inside=t,spacing=0.001)
for s in [300]:
    SO = string_offset_pairs(S,offset=s,step=20)
    for csi in cs:
        F.plot(SO,caption=True,new_fig=True,
               color_scheme=csi,cmap='jet')
        F.caption(f'{s} pt offset, inside={t}')
        F.save_fig()

for t in [True,False]:
    S.reset()
    S = spiro(R=20,wheel=Wheel(5.5,4,0),loops=10,orient=0,inside=t,spacing=0.001)
    for s in [200,400,800,1600,3200,6400]:
        SO = string_offset_pairs(S,offset=s,step=20)
        for csi in cs:
            F.plot(SO,caption=True,new_fig=True,
                   color_scheme=csi,cmap=cmaps[F.fig_number % len(cmaps)])
            F.caption(f'{s} pt offset, inside={t}')
            F.save_fig()

