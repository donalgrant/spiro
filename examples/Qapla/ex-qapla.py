import sys
sys.path.append('../..')
import argparse

from SpiroData import *
from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_ellipses import *
from spiro_arcs import *
from spiro_string import *
from spiro_triangles import *
from polygon import *
from Ring import *

parser = argparse.ArgumentParser(description="Hexagon Examples")
parser.add_argument("--full_res", help="use high-definition mode", action="store_true")
args = parser.parse_args()


F=SpiroFig()
F.text_color='white'

if args.full_res:
    hd = 1
else:
    hd = 0

def_factor = (1+4*hd)
save=True

F.set_default_dpi(150*(1+hd))
fd = 10*(1+2*hd) # figure dimensions

F._figname='Hexed-'

def figure(S,cs,cmap,alpha=0.4,dot_size=0.1,filename=None,color_dither=0.0):
    if hd:
        if not hasattr(figure,"data_set"):  figure.data_set=0
        S.save(f'figure-{figure.data_set}.pickle')
        figure.data_set+=1

    if filename is None:
        F.plot(S,color_scheme=cs,cmap=cmap,alpha=alpha,fig_dim=fd,dot_size=dot_size,
               save=save,color_dither=color_dither)
    else:
        F.plot(S,color_scheme=cs,cmap=cmap,alpha=alpha,fig_dim=fd,dot_size=dot_size,
               save=save,filename=filename,color_dither=color_dither)

###

e=0.0
R=4
ppl=900
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/3,a/3),ppl=ppl,loops=1,inside=True).rotate(pi/7)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,2))
S=SpiroData()

nk=3
gs=2
n = W.n()//(nk+gs)
ns = W.n()//nk 

def_factor=1
npts = def_factor*200

for k in range(nk):
    first = k*ns
    asym=0.1
    scale = 4
    pts= npts
    ao = linspace(0,-pi,n)
    shift = 0.0 
    aa = [pi/3,-pi/3]
    
    S.add(on_frame(W,scale=scale,oangle=3,first=first,fh=shift,fb=shift,n=n,
                   asym=asym,orient_follow=1,orient=ao,polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))

figure(S,'time','hot')
