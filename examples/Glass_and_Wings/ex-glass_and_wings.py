import sys
sys.path.append('../..')
import argparse

import numpy as np

from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_arcs import *
from spiro_frame import *
from polygon import *

parser = argparse.ArgumentParser(description="Glass and Wings Examples")
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

F._figname='Glass_and_Wings-'

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

###  colormap chosen by Cara vote, with 'time', and no rp_opts, though 'spacing' is good with rp_opts

e=0.2
R=40
ppl=300
loops=2
a=R/(1.07*2)
U = cIc(Ring(R),wheel=Wheel(a,0.5*a,pi/6),ppl=ppl,loops=loops,inside=True).rotate(pi/3)
W = U.resample(U.max_path()*frame_sampling(ppl*loops,parm=1.0,
                                           spacing='sinusoid',deramp=True,repeat=15))

tpts=150
n=W.n()
offset=0.5

rp_opts = None # { 'n': 3*tpts, 'spacing': ['sinusoid'], 'deramp': True, 'repeat': 1 }

S = on_frame(W,first=1,n=n-2,scale=50,pts=tpts,
             oangle=linspace(pi/4,pi/2,n-2),asym=0.2,
             orient_follow=1,arc_angle=pi/4,fb=offset,fh=offset,
             polyfunc=pcoords,orient=0,rp_opts=rp_opts)

F.plot(S,color_scheme='time',cmap='twilight',alpha=0.4,dot_size=0.1)

F.save_fig()

###

e=0.2
R=40
ppl=1000
loops=2
a=R/(1.07*2)
U = cIc(Ring(R),wheel=Wheel(a,0.5*a,pi/6),ppl=ppl,loops=loops,inside=True).rotate(pi/3)
W = U.resample(U.max_path()*frame_sampling(ppl*loops,parm=0.3,
                                           spacing='gaussian',deramp=True,repeat=5))

tpts=[100,0,0]
n=W.n()
offset=0.5

rp_opts = { 'n': 3*tpts[0], 'parm': 0.3, 'spacing': ['sinusoid'], 'deramp': False, 'repeat': 30 }

S = on_frame(W,first=1,n=n-2,scale=50,pts=tpts,
             oangle=linspace(pi/4,pi/2,n-2),asym=0.5,
             orient_follow=1,arc_angle=pi/4,fb=offset,fh=offset,
             polyfunc=tcoords,orient=0,rp_opts=rp_opts)

first=True
F.plot(S,color_scheme='time',cmap='pretty_blues',alpha=0.4,dot_size=0.1,new_fig=first)

F.save_fig()

###

e=0.2
R=40
ppl=500
loops=10
a=R/2.1
U = cIc(Ring(R),wheel=Wheel(a,0.5*a),ppl=ppl,loops=loops,inside=True)
W = U 

tpts=[20,20,0,30]
n=int(0.1*W.n())
offset=-0.1

rp_opts = { 'n': 500, 'parm': 2, 'spacing': ['erf'], 'deramp': True, 'repeat': 5 }

oa = pi/4 
f0 = W.n()//3
o = linspace(0,pi/2,n-2)
asym=linspace(-0.1,0.3,n-1)

S = on_frame(W,first=f0,n=n-2,scale=30,pts=tpts,
             oangle=oa,asym=asym,
             orient_follow=W.n()//3,arc_angle=pi/2,fb=offset,fh=offset,
             polyfunc=pcoords,orient=o,rp_opts=rp_opts,object=arange(n-2,dtype=int))

first=True
for i in range(ppl):
    F.plot(S.select(np.where(np.rint(S.o)==i)),color_scheme='time',
           cmap=modify_colormap_saturation('turbo',(1.0-i/ppl)),
           alpha=0.4,dot_size=0.1,new_fig=first)
    first=False

F.save_fig()

###

e=0.2
R=40
ppl=150
loops=10
a=R/2.1

nrings=3
U = integral_ellipticals(nrings,0.4,0.3,ring_angle=0,min_pen=0.8,max_pen=1.0,
                         min_po=0.0,max_po=pi/4,rounds=3,circuits=4,inside=True,ppl=100)

W = U.resample(U.max_path()*frame_sampling(ppl*loops,parm=0.2,reverse=False,
                                          spacing='sinusoid',deramp=True,repeat=5))

F.plot(W,color_scheme='white',cmap='turbo',alpha=0.4,dot_size=1)

tpts=array([150,150,0,0])
n=int(W.n())
offset=0

rp_opts = { 'n': 150, 'parm': 5, 'spacing': ['sinusoid'], 'deramp': True, 'repeat': 5 }

f00 = 0 
oa = pi/2 
asym=0 
S = SpiroData()
objects = np.unique(W.o)
for i in objects:
    T = W.select(np.where(np.rint(W.o)==i))
    n = T.n()
    f0 = f00 + int(i/(nrings*objects.shape[0]) * T.n())
    o = pi/4+linspace(0,pi/8,n)
    S.add(on_frame(T,first=f0,n=n,scale=10,pts=tpts,
                   oangle=oa,asym=asym,
                   orient_follow=1,arc_angle=pi/2,fb=offset,fh=offset,
                   polyfunc=pcoords,orient=o,rp_opts=rp_opts))

cs = 'dist_to_frm'
cmap='Reds'
first=True

F.plot(S,color_scheme=cs,cmap=cmap,alpha=0.4,dot_size=0.1,new_fig=first,coord_dither=0)

F.save_fig()

###

e=0.2
R=40
ppl=50

nrings=6
U = integral_ellipticals(nrings,0.4,0.3,ring_angle=0,min_pen=0.3,max_pen=1.0,
                         min_po=0.0,max_po=pi,rounds=6,circuits=4,inside=True,ppl=ppl)
W=U

tpts=array([15,15,0,0])
n=int(W.n())
offset=0.4 

rp_opts = { 'n': linspace(450,30,n//6,dtype=int), 'parm': 2, 'spacing': ['erf'], 'deramp': True, 'repeat': 3 }

seed = np.random.randint(100) # 6 
np.random.seed(seed)
f00 = 0 
oa = pi/4 

asym=0 
S = SpiroData()
first=True
objects = np.unique(np.rint(W.o))

cs = 'object'
cmap='Oranges'

first=True
for i in [1,2,3,4]:
    T = W.select(np.where(np.rint(W.o)==i))
    n = T.n()
    f0 = f00 
    o = 0 
    S.add(on_frame(T,first=f0,n=n,scale=16,pts=tpts,
                   oangle=oa,asym=asym,
                   orient_follow=T.n()//3,arc_angle=pi/2,fb=offset,fh=offset,
                   polyfunc=pcoords,orient=o,rp_opts=rp_opts,object=i))

first=True
F.plot(S,color_scheme=cs,cmap=cmap,alpha=0.4,dot_size=0.1,new_fig=first,coord_dither=0)

F.save_fig()

###

e=0.2
R=40
ppl=500

re = 0.4
a = circum(R,semi_minor(R,re))
U = cIe(ring=Ellipse(R,re),wheel=Wheel(a/(2*pi)/4,a/4),inside=True,ppl=1000,loops=1)

W = U.resample(U.max_path()*frame_sampling(ppl*1,parm=5,reverse=False,
                                           spacing='erf',deramp=False,repeat=5))

n=W.n()
tn = ppl
l = 500
rp_opts = { 'n': linspace(l,l//20,tn,dtype=int), 'parm': 5, 'spacing': ['linear'], 'deramp': True, 'repeat': 5 }

S = SpiroData()

cs = 'time'
cmap='cyans'

f0=269
subarcs_spacing=[n//9,n//6]
S=closed_subarcs(W,subarcs_spacing,sub_angle=pi/3,invert=True,skip=1,first=f0,n=n//2,
                 connect_times=True,line_pts=l,interp_phase=False,object=arange(n//10),rp_opts=rp_opts)
S.t /= 500
F.plot(S,color_scheme=cs,cmap=cmap,alpha=0.4,dot_size=0.1)

F.save_fig()

###

e=0.2
R=40
ppl=500

re = 0.4
a = circum(R,semi_minor(R,re))
U = cIe(ring=Ellipse(R,re),wheel=Wheel(a/(2*pi)/4,a/4),inside=True,ppl=1000,loops=1)

W = U.resample(U.max_path()*frame_sampling(ppl*1,parm=1,reverse=False,
                                           spacing='sinusoid',deramp=False,repeat=5))
W.dither_coords(0)

n=W.n()
tn = ppl
l = 600
rp_opts = { 'n': linspace(l,30,tn//4,dtype=int), 'parm': 5, 'spacing': ['linear'], 'deramp': True, 'repeat': 5 }

S = SpiroData()

cs = 'time'
cmap='pinks'

f0=32 
subarcs_spacing=[n//8,n//12,n//4]
T=anchored_arcs(W,subarcs_spacing,arc_angle=linspace(-pi/11,-pi/3,n//10),first=f0,n=n//10,
                connect_times=True,line_pts=l,interp_phase=False,
                object=arange(n//10),rp_opts=rp_opts)
T.t /= 500
    
nrots = 3
for i in range(nrots):
    S.add(T.scale(0.95).rotate(pi/4)).move(5,0).subsample((i+1)*3)

F.plot(S,color_scheme=cs,cmap=cmap,alpha=0.4,dot_size=0.1)

F.save_fig()

