import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_ellipses import *
from spiro_arcs import *
from spiro_string import *
from polygon import *
from Ring import *

F=SpiroFig()
F.text_color='white'

hd = 0  # 1 for high-def

def_factor = (1+4*hd)
save=True

F.set_default_dpi(150*(1+hd))
fd = 10*(1+2*hd) # figure dimensions
data_set=0

###

R=24
T1 = cIc(Ring(R),wheel=W0,loops=1,inside=True,ppl=2000).subsample(1)
T2 = cIc(Ring(R),wheel=Wheel(R/3,R/3),loops=1,inside=True,ppl=2000).subsample(1)

cs = 'spacing'
my_cmap = 'Reds'

S=SpiroData()

S.add(ellipses_between_frames(T1,T2,4,2,
                              scale_major=1.0,
                              orient_offset=0,
                              off_major=1.0, 
                              off_minor=0.0,
                              eccen=0.95,
                              nfigs=T1.n()//4,
                              pts=1000*def_factor,
                              istart1=0,istart2=0
                           ))

if hd:
    S.save(f'figure-{data_set}.pickle')
    data_set+=1
    
F.plot(S,color_scheme=cs,cmap=my_cmap,alpha=0.4,fig_dim=fd,dot_size=0.1,save=save)
