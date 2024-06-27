import sys
sys.path.append('../..')
import argparse

from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_frame import *
from polygon import *

from fractions import Fraction

parser = argparse.ArgumentParser(description="IE Ellipses Examples")
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

F._figname='IE_Ellipses-'

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

S1 = integral_ellipticals(6,0.7,0.8,max_po=0.0,rounds=5,circuits=3,ppl=1000)
S2 = S1.resample(S1.max_path()*frame_sampling(3000,parm=1,spacing='constant'))

f0=0
pts=400
S=ellipses_on_frame(S2,15,0.5,S2.directions(),pts,first=f0,n=None,object=0)

figure(S,'fcdirs3','gist_heat_r')

###

S1 = integral_ellipticals(1,0.7,0.8,max_po=0.0,rounds=5,circuits=5,ppl=1000)
S2 = S1.resample(S1.max_path()*frame_sampling(1000,parm=1,spacing='constant'))

f0=S2.n()//3
n = S2.n()//3

pts = array([ 100*int(10*abs(S2.direction(j))) for j in range(n) ])
S=ellipses_on_frame(S2,2*abs(S2.directions()),0.9,S2.directions(),pts=pts,first=f0,n=n,object=0)

figure(S,'direction','plasma')

###

S1 = integral_ellipticals(1,0.0,0.4,max_po=0.0,rounds=2,circuits=5,ppl=1000)
S2 = S1.resample(S1.max_path()*frame_sampling(1000,parm=1,spacing='constant'))

f0=S2.n()//10
n = S2.n()//4

pts = 50 

S=on_frame(S2,skip=[6,2,2,2,2,2],scale=linspace(100,80,n),oangle=96,fb=0.5,fh=0.5,asym=0.9,orient=0,
           polyfunc=ecoords,pts=pts,first=f0,n=n,orient_follow=1,
           arc_angle=0,object=0,
           pin_coord=None,pin_to_frame=0.0,autoscale=False,pinned_vertex=0)

figure(S,'y-direction','turbo')

###

S1 = integral_ellipticals(1,0.0,0.4,max_po=0.0,rounds=2,circuits=5,ppl=200)
f0= S1.n()//5 # S2.n()//10
n = S1.n()//5 # S2.n()//4

pts = 300

S=on_frame(S1,skip=[6,1,1,1,1,1],scale=linspace(100,80,n),oangle=8,fb=0.5,fh=0.5,asym=0.9,orient=0,
           polyfunc=ecoords,pts=pts,first=f0,n=n,orient_follow=1,
           arc_angle=pi,object=0,
           pin_coord=None,pin_to_frame=0.0,autoscale=False,pinned_vertex=0)
S.add(on_frame(S1,skip=[6,1,1,1,1,1],scale=linspace(100,80,n),oangle=8,fb=0.5,fh=0.5,asym=0.9,orient=0,
           polyfunc=ecoords,pts=pts,first=f0,n=n,orient_follow=1,
           arc_angle=-pi,object=0,
           pin_coord=None,pin_to_frame=0.0,autoscale=False,pinned_vertex=0))

figure(S,'flengths','Oranges')

###

S1 = integral_ellipticals(1,0.6,0.4,min_pen=3.0,rounds=7,circuits=1,ppl=500)
S2 = S1.resample(S1.max_path()*frame_sampling(500,parm=1,spacing='constant'))

f0= 0 
n = S2.n() 

pts = 1

nv = 480
v = linspace(0,nv-1,nv,dtype=int)

S=on_frame(S2,scale=linspace(100,80,n),oangle=nv,fb=0.5,fh=0.5,asym=0.9,orient=0,
           polyfunc=ecoords,pts=pts,first=f0,n=n,orient_follow=S2.n()//3,
           arc_angle=0,object=0,vertex_order=v,
           pin_coord=None,pin_to_frame=0.0,autoscale=False,pinned_vertex=0)

figure(S,'time','twilight')

###

S1 = integral_ellipticals(1,0.6,0.4,min_pen=3.0,rounds=7,circuits=1,ppl=500)
S2 = S1.resample(S1.max_path()*frame_sampling(1500,parm=4,repeat=14,deramp=True,spacing='linear'))

n = S2.n()//4
pts = 1

nv = 480
v = linspace(0,nv-1,nv,dtype=int)
o = 0

nf0 = 8
f0=184
S=on_frame(S2,scale=linspace(20,18,n),oangle=nv,fb=0,fh=0,asym=0.9,orient=o,
           polyfunc=ecoords,pts=pts,first=f0,n=n,orient_follow=S2.n()//3,
           arc_angle=0,object=0,vertex_order=v,
           pin_coord=None,pin_to_frame=0.0,autoscale=False,pinned_vertex=0)

figure(S,'cdist3','gist_heat')

###

S1 = integral_ellipticals(1,0.6,0.4,min_pen=3.0,rounds=7,circuits=2,ppl=500)
S2 = S1.resample(S1.max_path()*frame_sampling(2500,parm=4,repeat=14,deramp=True,spacing='linear'))

n = S2.n()//16
pts = 1

nv = 240
v = linspace(0,nv-1,nv,dtype=int)
o = 0

S = SpiroData()

nf0 = 9
for f0 in linspace(0,S2.n()//2,nf0,dtype=int):

    S.add(on_frame(S2,scale=20,oangle=nv,fb=0,fh=0,asym=0.9,orient=o,
                   polyfunc=ecoords,pts=pts,first=f0,n=n,orient_follow=S2.n()//3,
                   arc_angle=0,object=0,vertex_order=v,
                   pin_coord=None,pin_to_frame=0.0,autoscale=False,pinned_vertex=0))

figure(S,'time','hot')

###

S1 = integral_ellipticals(1,0.6,0.4,min_pen=3.0,rounds=7,circuits=2,ppl=500)
S2 = S1.resample(S1.max_path()*frame_sampling(10000,repeat=100,deramp=True,spacing='fibonacci'))

n = S2.n()

nv = 500
v = linspace(0,nv-1,nv,dtype=int)
o = 0

pts = 1

S = SpiroData()

nf0 = 1
for f0 in linspace(0,S2.n()//2,nf0,dtype=int):

    S.add(on_frame(S2,scale=10,oangle=nv,fb=0,fh=0,asym=0.9,orient=o,
                   polyfunc=ecoords,pts=pts,first=f0,n=n,orient_follow=S2.n()//3,
                   arc_angle=0,object=0,vertex_order=v,
                   pin_coord=None,pin_to_frame=0.0,autoscale=False,pinned_vertex=0))

figure(S,'time','pretty_blues')

###

S1 = integral_ellipticals(1,0.6,0.4,min_pen=1.0,rounds=7,circuits=2,ppl=500)
S2 = S1.resample(S1.max_path()*frame_sampling(2500,spacing='constant'))

n = S2.n()

nv = 600
v = linspace(0,nv-1,nv,dtype=int)
o = 0

pts = 1

rp_opts = { 'n': 1000, 'parm':  4, 'spacing':  ['fibonacci'], 'repeat': 10,
            'reverse': False, 'nocum': False, 'deramp': True }

S = SpiroData()

nf0 = 1
for f0 in linspace(0,S2.n(),nf0,dtype=int):

    S.add(on_frame(S2,scale=15,oangle=nv,fb=0.5,fh=0.5,asym=0.9,orient=o,
                   polyfunc=ecoords,pts=pts,first=f0,n=n,orient_follow=S2.n()//3,
                   arc_angle=0,object=0,vertex_order=v,
                   pin_coord=None,pin_to_frame=0.0,autoscale=False,pinned_vertex=0,
                   rp_opts=rp_opts))

figure(S,'time','hot_r')

###

S1 = integral_ellipticals(1,0.6,0.4,min_pen=0.6,rounds=7,circuits=2,ppl=500)
S2 = S1.resample(S1.max_path()*frame_sampling(2000,parm=2,spacing='sinusoid',deramp=True,repeat=40))

n = S2.n()

nv = 60
v = linspace(0,nv-1,nv,dtype=int)
o = pi/3

pts = 1

rp_opts = { 'n': 500, 'parm':  2, 'spacing':  ['sinusoid'], 'repeat': 10,
            'reverse': False, 'nocum': False, 'deramp': True }

S = SpiroData()

nf0 = 1
for f0 in linspace(0,S2.n(),nf0,dtype=int):
    
    S.add(on_frame(S2,scale=7,oangle=nv,fb=0.5,fh=0.5,asym=0.9,orient=o,
                   polyfunc=ecoords,pts=pts,first=f0,n=n,orient_follow=S2.n()//3,
                   arc_angle=0,object=0,vertex_order=v,
                   pin_coord=None,pin_to_frame=0.0,autoscale=False,pinned_vertex=0,
                   rp_opts=rp_opts))

figure(S,'fwidth','turbo')

###

S1 = integral_ellipticals(1,0.7,0.5,min_pen=1.3,rounds=3,circuits=1,ppl=500)
S2 = S1.resample(S1.max_path()*frame_sampling(2000,parm=2,spacing='fibonacci',
                                              deramp=True,repeat=100))

n = S2.n()

nv = 60
v = linspace(0,nv-1,nv,dtype=int)
o = 0 

pts = 500//nv

rp_opts = { 'n': 500, 'parm':  2, 'spacing':  ['fibonacci'], 'repeat': 25,
            'reverse': False, 'nocum': False, 'deramp': True, 'zero':  True }

S = SpiroData()

nf0 = 1
for f0 in linspace(0,S2.n(),nf0,dtype=int):

    S.add(on_frame(S2,scale=8,oangle=nv,fb=0.5,fh=0.5,asym=0.9,orient=o,
                   polyfunc=ecoords,pts=pts,first=f0,n=n,orient_follow=10, # S2.n()//3,
                   arc_angle=0,object=0,vertex_order=v,
                   pin_coord=None,pin_to_frame=0.0,autoscale=False,pinned_vertex=0,
                   rp_opts=rp_opts))

figure(S,'dist_to_frm','inferno_r')

###

S1 = integral_ellipticals(1,0.7,0.5,min_pen=1.3,rounds=5,circuits=1,ppl=1000)
S2 = S1.copy()

n = S2.n()

nv = 60
v = linspace(0,nv-1,nv,dtype=int)
o = 0

pts = 600//nv

S = SpiroData()

nf0 = 1
for f0 in linspace(0,S2.n(),nf0,dtype=int):

    S.add(on_frame(S2,scale=8,oangle=nv,fb=0.5,fh=0.5,asym=0.9,orient=o,
                   polyfunc=ecoords,pts=pts,first=f0,n=n,orient_follow=10,
                   arc_angle=0,object=0,vertex_order=v,
                   pin_coord=None,pin_to_frame=0.0,autoscale=False,pinned_vertex=0)) 

figure(S,'segment','pale_pink')

###

S1 = integral_ellipticals(1,0.7,0.5,min_pen=1.3,rounds=5,circuits=1,ppl=3000)
S2 = S1.copy()
n = S2.n()

nv = 100
v = linspace(0,nv-1,nv,dtype=int)
o = linspace(0,19*pi,n)

pts = 1000//nv

rp_opts = { 'n': 1000, 'parm':  1, 'spacing':  ['linear'], 'repeat': 25, 'deramp': True }

f0=S2.n()//10
S=on_frame(S2,scale=8,oangle=nv,fb=0.5,fh=0.5,asym=0.9,orient=o,
           polyfunc=ecoords,pts=pts,first=f0,n=n//4,orient_follow=1000,
           arc_angle=0,object=0,vertex_order=v,
           pin_coord=None,pin_to_frame=0.0,autoscale=False,pinned_vertex=0,
           rp_opts=rp_opts)

figure(S,'fradii','gist_heat')

###

S1 = integral_ellipticals(1,0.7,0.5,min_pen=1.3,rounds=8,circuits=1,ppl=1000)
S2 = S1.copy()

n = S2.n()

nv = 10
v = linspace(0,nv-1,nv,dtype=int)
o = 0 

pts = 10 

nn = 200
rp_opts = { 'n': nn, 'parm':  linspace(1,50,n), 'spacing':  ['sinusoid'], 'repeat': 4, 'deramp': True }

f0=0 

S=on_frame(S2,scale=8,oangle=nv,fb=0.5,fh=0.5,asym=0.9,orient=o,
           polyfunc=ecoords,pts=pts,first=f0,n=n,orient_follow=n//4,
           arc_angle=-pi/4,object=0,vertex_order=v,
           pin_coord=None,pin_to_frame=0.0,autoscale=False,pinned_vertex=0,
           rp_opts=rp_opts)

figure(S,'fradii','cmap1')

###

S1 = integral_ellipticals(1,0.7,0.5,min_pen=1.3,rounds=2,circuits=1,ppl=1500)
S2 = S1.copy()

n = S2.n()

nv = 4
v = linspace(0,nv-1,nv,dtype=int)
o = 0 

pts = 100

nn = 40 

aa = linspace(-pi/2,pi/2,nv*n)
f0=0 

S=on_frame(S2,scale=30,oangle=nv,fb=0.5,fh=0.5,asym=0.9,orient=o, 
           polyfunc=ecoords,pts=pts,first=f0,n=n,orient_follow=1,
           arc_angle=aa,object=0,vertex_order=v,
           pin_coord=None,pin_to_frame=0.0,autoscale=False,pinned_vertex=0) 

figure(S,'fradii','turbo')

###

S1 = integral_ellipticals(1,0.7,0.5,min_pen=1.3,rounds=2,circuits=1,ppl=2000)
S2 = S1.copy()

n = S2.n()

nv = 4
v = linspace(0,nv-1,nv,dtype=int)
o = linspace(0,4*pi,n)

pts = 100

nn = 40 

aa = linspace(-pi/2,pi/2,nv*n)
f0=0 

S=on_frame(S2,scale=30,oangle=nv,fb=0.5,fh=0.5,asym=0.9,orient=o, 
           polyfunc=ecoords,pts=pts,first=f0,n=n,orient_follow=1,
           arc_angle=aa,object=0,vertex_order=v,
           pin_coord=None,pin_to_frame=0.0,autoscale=False,pinned_vertex=0) 

figure(S,'fradii','twilight')
