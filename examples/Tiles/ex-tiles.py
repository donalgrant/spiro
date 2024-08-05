import sys
sys.path.append('../..')
import argparse

import numpy as np

from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_frame import *
from polygon import *
from partition import *

parser = argparse.ArgumentParser(description="Tile Examples")
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

F._figname='Tile-'

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

### hexagon with arced sids -- three layers

e=0.2
R=40
ppl=400
loops=10
a=R/2.1
U = cIc(Ring(R),wheel=Wheel(a,0.5*a),ppl=ppl,loops=loops,inside=True)
W = U.resample(U.max_path()*frame_sampling(ppl*loops,parm=0.3,reverse=False,
                                           spacing='erf',deramp=True,repeat=10))

tpts=[0,0,0,300]
n=int(0.3*W.n())
offset=0.5

rp_opts = None 

oa = pi/4 
f0 = W.n()
o = linspace(0,pi/2,n-2)

S = on_frame(W,first=f0,n=n-2,scale=70,pts=tpts,
             oangle=oa,asym=0.2,
             orient_follow=W.n()//3,arc_angle=pi/4,fb=offset,fh=offset,
             polyfunc=pcoords,orient=o,rp_opts=rp_opts)

first=True
nv = 6
nc = ngon_coords(nv)*40
cc = SpiroData()
for i in range(nv):
    cc.load(arc_between_pts(array([ nc[i], nc[(i+1) % nv ] ]),-pi/4,50))

SS = S.copy()

j0 = SS.is_contained_in(cc.coords())
S0 = SS.remove(np.where(j0))
S1 = SS.select(np.where(j0))

j1 = S1.is_contained_in(cc.scale(0.5).rotate(pi/6).coords())
S2 = S1.select(np.where(j1))
S1 = S1.remove(np.where(j1))

F.plot(S1,color_scheme='fcdist3',cmap='autumn',alpha=0.4,dot_size=.1)
F.plot(S2.rotate(pi/72),color_scheme='fcdist3',cmap='Wistia',alpha=0.4,dot_size=0.1,new_fig=False)
F.plot(S0.rotate(-pi/72),color_scheme='fcdist3',cmap='pretty_reds',alpha=0.4,dot_size=.1,new_fig=False)

F.save_fig()

###

e=0.2
R=40
ppl=400
loops=10
a=R/2.1
U = cIc(Ring(R),wheel=Wheel(a,0.5*a),ppl=ppl,loops=loops,inside=True)
W = U.resample(U.max_path()*frame_sampling(ppl*loops,parm=0.3,reverse=False,
                                           spacing='erf',deramp=True,repeat=10))

tpts=[0,0,0,300]
n=int(0.3*W.n())
offset=-0.1

rp_opts = None

oa = pi/4 
f0 = W.n()
o = linspace(0,pi/2,n-2)

S = on_frame(W,first=f0,n=n-2,scale=60,pts=tpts,
             oangle=oa,asym=0.2,
             orient_follow=W.n()//3,arc_angle=pi/2,fb=offset,fh=offset,
             polyfunc=pcoords,orient=o,rp_opts=rp_opts)

cc=SpiroData()
for i in range(3):
    cc.add(cIc(Ring(40),wheel=Wheel(10,0.8*a,pi*i/3),ppl=1500,loops=1,inside=False))

j5 = S.is_within(1,cc.coords())

F.plot(S.select(~j5), color_scheme='fwidth',cmap='Wistia',alpha=0.4,dot_size=0.1,new_fig=True)
F.plot(S.select(j5).rotate(pi/36), color_scheme='fwidth',cmap='gist_heat',
       alpha=0.6,dot_size=0.1,color_dither=0.3,new_fig=False)

F.save_fig()

###

R1=20
a = R1/(2*2*pi)
ppl=500
loops=1

U = spiro_nstar(3,R1,0.25,Wheel(a,a),loops=loops,inside=False,fold=True)
#U = spiro_nstar(3,R1,0.0,Wheel(a,a),loops=loops,inside=False,fold=True)

W = U.resample_using( { 'n': ppl*loops, 'parm': 1, 'spacing': ['constant'], 'deramp': False, 'repeat': 5 } )

l=300
n=W.n()
nn=n
subarcs_spacing=[int(0.4*n),int(0.3*n)]
f0=0
tn=ppl*loops
rp_opts = { 'n': l, 'parm': 1, 'spacing': ['erf'], 'deramp': True, 'repeat': 2 }

T=anchored_arcs(W,subarcs_spacing,arc_angle=0, 
                first=f0, n=nn,
                connect_times=True,line_pts=l,interp_phase=False,
                object=arange(nn),rp_opts=rp_opts,close_loop=False)
T.t /= 500

#X = spiro_ngon(3,R1,W0,loops=1).rotate(pi/3).scale(0.7)
X = cIc(Ring(0.6*R1),W0,ppl=ppl).move(1,0)

j = T.is_contained_in(X.coords())

Q1 = T.select(j)
Q2 = T.select(~j)

F.plot(Q1,color_scheme='time',cmap='turbo',alpha=0.4,dot_size=.1,new_fig=True)

Q2.scale(1.03)
r = Q2.radii()
rmax = max(r)

P = partition_tiles(Q2,30,30,0.0,0.0)
for PP in P:
    if PP.n()>0:
        dx = PP.xmid()
        dy = PP.ymid()
        theta = 2*pi*np.random.standard_normal()*(PP.rmid()/rmax)/8
        PP.move(-dx,-dy).rotate(theta).move(dx,dy)
    
Q2 = objectify(P)
r = Q2.radii()
rmax = max(Q2.radii())
r1 = 0.6*rmax

dc = array([ 0 if r[j] < r1 else 3*((r[j]-r1)/(rmax-r1))**5 for j in range(Q2.n()) ])
Q2.dither_coords(dc)

F.plot(Q2,color_scheme='time',cmap='Wistia',alpha=0.4,dot_size=.1,new_fig=False)

F.save_fig()
