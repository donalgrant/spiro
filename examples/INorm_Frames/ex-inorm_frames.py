import sys
sys.path.append('../..')
import argparse

from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_frame import *
from polygon import *

from fractions import Fraction

parser = argparse.ArgumentParser(description="Biframe Diagrams Examples")
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

F._figname='Biframe_Diagrams-'

def figure(S,cs,cmap,alpha=0.4,dot_size=0.1,filename=None,color_dither=0.0,new_fig=True):
    if hd:
        if not hasattr(figure,"data_set"):  figure.data_set=0
        S.save(f'figure-{figure.data_set}.pickle')
        figure.data_set+=1

    if filename is None:
        F.plot(S,color_scheme=cs,cmap=cmap,alpha=alpha,fig_dim=fd,dot_size=dot_size,
               save=save,color_dither=color_dither,new_fig=new_fig)
    else:
        F.plot(S,color_scheme=cs,cmap=cmap,alpha=alpha,fig_dim=fd,dot_size=dot_size,
               save=save,filename=filename,color_dither=color_dither,new_fig=new_fig)

###

R = 50
ppl = 3000
a = R*3/4
S1 = cIc(ring=Ring(R),wheel=Wheel(a,a/2.4),loops=3,ppl=ppl,inside=True,reverse=False)
f=S1.n()//8

S=SpiroData()

ns = 10
for i in range(ns):
    S.add(auto_inorm_frame(S1,first=f+i*10,norm_off1=0,base=0.0,amp=0.0,rate=8,norm_off2=0))

figure(S,'length','turbo')

