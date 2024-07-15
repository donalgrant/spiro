import sys
sys.path.append('../..')
import argparse

import numpy as np

from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_frame import *
from polygon import *

parser = argparse.ArgumentParser(description="Partition Examples")
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

F._figname='Partition-'

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

###  (masking -- panels)

e=0.0
R=7
ppl=1000

a=circum(R,semi_minor(R,e))/(2*pi)
T1 = cIe(Ellipse(R,e),wheel=Wheel(a/3,a/3),ppl=ppl,loops=1,inside=True)

skip=2
n=T1.n()//skip//18

d = T1.neighbor_distances()
dmax=max(d)
dmin=min(d)
scale=5
ao=pi/2*(d-dmin)/(dmax-dmin)

pts = [0,500,500]

offset=1 # np.random.randint(T1.n())

S = SpiroData()
n_swoops=12
for i in range(n_swoops):
    first=T1.n()*i//n_swoops
    S.add(triangles_on_frame(T1,skip=skip,scale=scale,oangle=pi/3,n=n-1,orient=ao,
                             first=first,pts=pts*def_factor,orient_follow=1,arc_angle=pi/2,object=i))
    
U = SpiroData()
npanels=3
pwidth=4
pspace=5
pfirst=-(npanels*pspace)/2
for i in range(npanels):
    pstart=pfirst+i*pspace
    U.add(S.select(np.where( (S.x > pstart) & (S.x < pstart+pwidth) )))

figure(U,'cycles','Blues')

### 5 Multi-colormapped Panels

e=0.0
R=7
ppl=1000

a=circum(R,semi_minor(R,e))/(2*pi)
T1 = cIe(Ellipse(R,e),wheel=Wheel(a/3,a/3),ppl=ppl,loops=1,inside=True)

skip=2
n=T1.n()//skip//18

d = T1.neighbor_distances()
dmax=max(d)
dmin=min(d)
scale=5
ao=pi/2*(d-dmin)/(dmax-dmin)

pts = [0,500,500]

offset=1 # np.random.randint(T1.n())

S = SpiroData()
n_swoops=12
for i in range(n_swoops):
    first=T1.n()*i//n_swoops
    S.add(triangles_on_frame(T1,skip=skip,scale=scale,oangle=pi/3,n=n-1,orient=ao,
                             first=first,pts=pts*def_factor,orient_follow=1,arc_angle=pi/2,object=i))
    
l=10
U = SpiroData()
npanels=5
pwidth=2.8
pspace=3
pfirst=-(npanels*pspace)/2
cmap=['Oranges','Blues','bone','Greens','Reds']
for i in range(npanels):
    pstart=pfirst+i*pspace
    U=S.select(np.where( (S.x > pstart) & (S.x < pstart+pwidth) ))
    
    F.plot(U,cmap=cmap[i],color_scheme='phase',alpha=0.4,dot_size=.1,limits=[-l,l,-l,l],
          new_fig=True if i==0 else False)

F.save_fig()

###


R = 50
ppl = 4000
a=R/(2*pi)/1.4
S1 = spiro_eq_triangle(R=R,wheel=Wheel(a,1.6*a),orient=0,loops=5,fold=False,inside=True)

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

asym = 0 

aa = pi/3

cs='direction' 
cmap='turbo'

S = on_frame(S1,scale=sc,oangle=oa,fb=offset,fh=offset,asym=asym,orient=o,first=f0,
             polyfunc=ngon_coords,pts=pts,orient_follow=follow,n=nn,vertex_order=v,
             object=1,arc_angle=aa,rp_opts=rp_opts)

ns = 15
SA = []

for i in range(ns):
    r = S.radii()
    mr = max(S.radii())
    S=S.remove(np.where( r < (i+0.25)/ns * mr))
    r = S.radii()
    mr = max(S.radii())
    SA.append(S.select(np.where( r < (i+1)/ns * mr)))

first_plot=True              
for i in range(ns):
    F.plot(SA[i].rotate(i/ns*pi/3),color_scheme=cs,cmap=cmap, dot_size=0.1,alpha=(i+1)/ns * 0.6,limits=None,
           coord_dither=0.0,color_dither=0.0,new_fig=first_plot)
    first_plot=False

F.save_fig()
