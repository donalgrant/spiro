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

hd = 0  # high-def

def_factor = (1+4*hd)

F.set_default_dpi(150*(1+hd))
fd = 10*(1+2*hd) # figure dimensions
data_set=0

###

cmaps=['Reds','OrRd','ocean',cmap1,'bone','Wistia','turbo','autumn','Greens','Blues','copper']
css=['length','phase','radial','direction','x-direction','spacing','t-waves','l-waves','cycles','y-direction']
S = SpiroData()
T = cIc(Ring(30),wheel=Wheel(30/7,6),loops=1,inside=True,ppl=2000).subsample(1)
ppl=T.n()
# F.plot(T,no_frame=False)

seed=751 # np.random.randint(0,1000)
np.random.seed(seed)
# print(f'seed={seed}')

for k in range(16):
    ne=ppl//np.random.randint(4,13)
    first=np.random.randint(0,ppl-ne-1)
    flat=np.random.uniform(0.25,0.75)
    eccen=sqrt(2*flat-flat**2)
#    print(f'{k}: flat/eccen={flat}/{eccen}; ne={ne}, first={first}')
    major =[ 16/(T.neighbor_dist(j))**0.1 for j in arange(first,first+ne) ]
    orient=[ -T.direction(j)+pi/7         for j in arange(first,first+ne) ]
    S = ellipses_on_frame(T,major,eccen,orient,1000*def_factor,first=first,n=ne)
    cs = css[np.random.randint(len(css))]
    c = cmaps[np.random.randint(len(cmaps))]

    
    if hd:
        S.save(f'figure-{data_set}.pickle')
        data_set+=1

    F.plot(S,color_scheme=cs,cmap=c,alpha=0.4,fig_dim=fd,save=True)
