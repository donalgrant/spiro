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

hd = 1  # 1 for high-def

def_factor = (1+4*hd)

F.set_default_dpi(150*(1+hd))
fd = 10*(1+2*hd) # figure dimensions
data_set=0

###


cmaps=['Reds','OrRd','ocean',cmap1,'bone','Wistia','turbo','autumn',
       'Greens','Blues','copper','jet','terrain','YlOrBr','Oranges','inferno']
css=['length','phase','radial','direction','x-direction','spacing','t-waves','l-waves','cycles','y-direction']

###

S = SpiroData()
T = cIc(Ring(30),wheel=Wheel(6,17),loops=1,inside=True,ppl=3000).subsample(1)
ppl=T.n()

seed=257 # np.random.randint(0,1000)
np.random.seed(seed)
# print(f'seed={seed}')

n_figs=len(cmaps)
for k in range(n_figs):
    ne=ppl//12
    first=np.random.randint(0,ppl-ne-2)
    tnd = [ T.direction(j)+pi for j in arange(first,first+ne) ]
    flat_scale = max(tnd)-min(tnd)
    flat=[ 0.2 + 0.6 * (tnd[j]-min(tnd))/flat_scale for j in range(len(tnd)) ]
#    print(min(flat),max(flat))
    eccen_t = [ eccen_from_flat(flat[j]) for j in range(len(flat)) ]
    eccen = [ 0.97 if eccen_t[j]>0.97 else eccen_t[j] for j in range(len(eccen_t)) ]
    major =20
    orient=[ 100*T.neighbor_dist(j) for j in arange(first,first+ne) ]
    S = ellipses_on_frame(T,major,eccen,orient,1000*def_factor,first=first,n=ne)
    cs = css[np.random.randint(len(css))]
    c = cmaps[k % len(cmaps)]

    if hd:
        S.save(f'figure-{data_set}.pickle')
        data_set+=1

    F.plot(S,color_scheme=cs,cmap=c,alpha=0.4,fig_dim=fd,save=True)

### (same as above, but inside=False for frame)

S = SpiroData()
T = cIc(Ring(30),wheel=Wheel(6,17),loops=1,inside=False,ppl=3000).subsample(1)
ppl=T.n()

seed=87 # np.random.randint(0,1000)
np.random.seed(seed)
# print(f'seed={seed}')

n_figs=len(cmaps)
for k in range(n_figs):
    ne=ppl//12
    first=np.random.randint(0,ppl-ne-2)
    tnd = [ T.direction(j)+pi for j in arange(first,first+ne) ]
    flat_scale = max(tnd)-min(tnd)
    flat=[ 0.2 + 0.6 * (tnd[j]-min(tnd))/flat_scale for j in range(len(tnd)) ]
#    print(min(flat),max(flat))
    eccen_t = [ eccen_from_flat(flat[j]) for j in range(len(flat)) ]
    eccen = [ 0.97 if eccen_t[j]>0.97 else eccen_t[j] for j in range(len(eccen_t)) ]
    major =20
    orient=[ 100*T.neighbor_dist(j) for j in arange(first,first+ne) ]
    S = ellipses_on_frame(T,major,eccen,orient,1000*def_factor,first=first,n=ne)
    cs = css[np.random.randint(len(css))]
    c = cmaps[k % len(cmaps)]

    if hd:
        S.save(f'figure-{data_set}.pickle')
        data_set+=1

    F.plot(S,color_scheme=cs,cmap=c,alpha=0.4,fig_dim=fd,save=True)
