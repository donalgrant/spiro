import sys
sys.path.append('../..')
import argparse

import numpy as np

from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_frame import *
from polygon import *

parser = argparse.ArgumentParser(description="Autonorm Design Examples")
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

F._figname='Autonorm_Design-'

def figure(S,cs,cmap,alpha=0.4,dot_size=0.1,filename=None,color_dither=0.0,limits=None):
    if hd:
        if not hasattr(figure,"data_set"):  figure.data_set=0
        S.save(f'figure-{figure.data_set}.pickle')
        figure.data_set+=1

    if filename is None:
        F.plot(S,color_scheme=cs,cmap=cmap,alpha=alpha,fig_dim=fd,dot_size=dot_size,
               save=save,color_dither=color_dither,limits=limits)
    else:
        F.plot(S,color_scheme=cs,cmap=cmap,alpha=alpha,fig_dim=fd,dot_size=dot_size,
               save=save,filename=filename,color_dither=color_dither,limits=limits)

###

R = 50
ppl = 4000
a=R/(2*pi)/1.4
S1 = spiro_eq_triangle(R=R,wheel=Wheel(a,1.6*a),orient=0,loops=5,fold=False,inside=False)

S1 = S1.resample(S1.max_path()*frame_sampling(ppl,parm=4,spacing='sinusoid',
                                              repeat=200,deramp=True))


n = S1.n() 

oa = 2
nv = oa
v = linspace(0,nv-1,nv,dtype=int)

pts = 160 

rp_opts = { 'n': pts, 
            'parm': 5,
            'spacing':  ['sinusoid'], 'repeat': 3, 'deramp': True }

offset = 0.4
sc = S1.radii()/max(S1.radii()) * 30

f0 = 0 # 
follow = 1

nn = n

o = linspace(0,6*pi,nn) 

fs = frame_sampling(nn,parm=4,spacing='linear',deramp=False,reverse=True,nocum=True)
fs /= max(fs)

asym = 0 

aa = pi/3

S = SpiroData()

first_plot=True

cs='direction'
cmap='turbo'

S = on_frame(S1,scale=sc,oangle=oa,fb=offset,fh=offset,asym=asym,orient=o,first=f0,
             polyfunc=ngon_coords,pts=pts,orient_follow=follow,n=nn,vertex_order=v,
             object=1,arc_angle=aa,rp_opts=rp_opts)

r = S.radii() 
alpha = (r /max(r))**2 * 0.3 + 0.1
    
F.plot(S,color_scheme=cs,cmap=cmap, dot_size=0.1,alpha=alpha,limits=None,
       coord_dither=0.0,color_dither=0.0,new_fig=first_plot)

figure(S,'direction','turbo',alpha=alpha)
