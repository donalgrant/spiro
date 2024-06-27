import sys
sys.path.append('../..')
import argparse

from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_frame import *
from polygon import *

from fractions import Fraction

parser = argparse.ArgumentParser(description="IE Arcs Examples")
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

F._figname='IE_Arcs-'

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
S1 = integral_ellipticals(1,0.7,0.5,min_pen=1.3,rounds=2,circuits=1,ppl=1500)
S2 = S1.copy()
n = S2.n()

nv = 2
v = linspace(0,nv-1,nv,dtype=int)
o = linspace(0,8*pi,n)

pts = 30 

nn = 200 
rp_opts = { 'n': nn, 'parm':  4, 'spacing':  ['sinusoid'], 'repeat': 4, 'deramp': True }

aa = pi/4
f0=0

S=on_frame(S2,scale=10,oangle=nv,fb=0.5,fh=0.5,orient=o,
           polyfunc=ngon_coords,pts=pts,first=f0,n=n,orient_follow=1,
           arc_angle=aa,object=0,vertex_order=v,
           pin_coord=None,pin_to_frame=0.0,autoscale=False,pinned_vertex=0,
           rp_opts=rp_opts)

figure(S,'fcdist3','magma')

###

S1 = integral_ellipticals(1,0.5,0.5,min_pen=1.3,rounds=3,circuits=1,ppl=1500)
S2 = S1.resample(S1.max_path()*frame_sampling(1500,parm=2,spacing='constant',
                                              deramp=True,repeat=1))
S2.rotate(-pi/2)
#S2 = S1.copy()
F.plot(S1,color_scheme='cyan',dot_size=0.5,alpha=0.4)
F.plot(S2,color_scheme='white',dot_size=0.5,new_fig=True,alpha=0.4)

n = S2.n()

nv = 2
v = linspace(0,nv-1,nv,dtype=int)
o = linspace(0,8*pi,n)

pts = 30 

nn = 200 
rp_opts = { 'n': nn, 'parm':
            frame_sampling(n,parm=10,spacing='linear',deramp=True,nocum=True),
            'spacing':  ['sinusoid'], 'repeat': 4, 'deramp': True }

aa = pi/4
f0=0 

S=on_frame(S2,scale=10,oangle=nv,fb=0.5,fh=0.5,orient=o,
           polyfunc=ngon_coords,pts=pts,first=f0,n=n,orient_follow=1,
           arc_angle=aa,object=0,vertex_order=v,
           pin_coord=None,pin_to_frame=0.0,autoscale=False,pinned_vertex=0,
           rp_opts=rp_opts)

F.plot(S,color_scheme='fcdist3',cmap='magma',dot_size=.1,alpha=0.4)
figure(S,'l-waves','gist_heat_r')

###

S1 = integral_ellipticals(1,0.5,0.5,min_pen=0.6,rounds=3,circuits=2,ppl=1500)
S2 = S1.resample(S1.max_path()*frame_sampling(1500,parm=2,spacing='constant',
                                              deramp=True,repeat=1))
S2 = S1.copy()
S2.rotate(-pi/2)

n = S2.n()

nv = 2
v = linspace(0,nv-1,nv,dtype=int)
o = linspace(0,-6*pi,n)

pts = 30

nn = 200
rp_opts = { 'n': nn, 'parm':  
           0.1*frame_sampling(n,parm=10,spacing='linear',deramp=True,repeat=1,nocum=True),
           'spacing':  ['sinusoid'], 'repeat': 10, 'deramp': False }

aa = pi/4 
f0=0 

S=on_frame(S2,scale=10,oangle=nv,fb=0.5,fh=0.5,orient=o,
           polyfunc=ngon_coords,pts=pts,first=f0,n=n,orient_follow=0,
           arc_angle=aa,object=0,vertex_order=v,
           pin_coord=None,pin_to_frame=0.0,autoscale=False,pinned_vertex=0,
           rp_opts=rp_opts)

figure(S,'fcdist3','turbo')

###  any colormap works for this one...

S1 = integral_ellipticals(1,0.5,0.5,min_pen=1.5,rounds=3,circuits=2,ppl=2000,inside=False)
S2 = S1.resample(S1.max_path()*frame_sampling(2000,parm=2,spacing='constant',
                                              deramp=True,repeat=1))
S2.rotate(-pi/2)
n = S2.n()

nv = 2
v = linspace(0,nv-1,nv,dtype=int)
o = linspace(0,12*pi,n)

pts = 100

aa = pi/4 
f0=S2.n()//20

S=on_frame(S2,scale=30,oangle=nv,fb=0.5,fh=0.5,orient=o,
           polyfunc=ngon_coords,pts=pts,first=f0,n=n//2,orient_follow=n//3,
           arc_angle=aa,object=0,vertex_order=None,
           pin_coord=None,pin_to_frame=0.0,autoscale=False,pinned_vertex=0)

F.plot(S,color_scheme='fcdist3',cmap='turbo',dot_size=.1,alpha=0.4)
figure(S,'direction','pretty_blues')

###

S1 = integral_ellipticals(1,0.5,0.8,min_pen=1.5,rounds=7,circuits=5,ppl=2000,inside=True)
S2 = S1.resample(S1.max_path()*frame_sampling(3000,parm=2,spacing='sinusoid',
                                              deramp=True,repeat=50))
n = S2.n()

nf=n//21

nv = 2
v = linspace(0,nv-1,nv,dtype=int)
o = linspace(0,4*pi,nf)

pts = 400

aa = [-pi/2,pi/3] 

offset = linspace(0.25,-0.5,nf)
S=SpiroData()

nf0=5
for i in range(nf0):
    f0=n//nf0*i 

    S.add(on_frame(S2,scale=25,oangle=nv,fb=offset,fh=offset,orient=o,
          polyfunc=ngon_coords,pts=pts,first=f0,n=nf,orient_follow=1,
          arc_angle=aa,object=0,vertex_order=v,
          pin_coord=None,pin_to_frame=0.0,autoscale=False,pinned_vertex=0))

figure(S,'width','hot')

###

S1 = integral_ellipticals(1,0.9,0.1,min_pen=1.5,rounds=1,circuits=1,ppl=2000,inside=True)
S2 = S1.resample(S1.max_path()*frame_sampling(1000,parm=2,spacing='constant',
                                              deramp=False,repeat=1))
n = S2.n()

nf=n

nv = 2
v = linspace(0,nv-1,nv,dtype=int)
o = linspace(0,-2*pi,nf)

pts = 200

aa = pi/4

offset = 0 
S=SpiroData()

nf0=1
for i in range(nf0):
    f0=n//nf0*i 

    S.add(on_frame(S2,scale=20,oangle=nv,fb=offset,fh=offset,orient=o,
          polyfunc=ngon_coords,pts=pts,first=f0,n=nf,orient_follow=n//6,
          arc_angle=aa,object=0,vertex_order=v,
          pin_coord=None,pin_to_frame=0.0,autoscale=False,pinned_vertex=0))

figure(S,'time','autumn')

###

S1 = integral_ellipticals(1,0.9,0.1,min_pen=1.5,rounds=1,circuits=1,ppl=2000,inside=True)
S2 = S1.resample(S1.max_path()*frame_sampling(1500,parm=2,spacing='constant',
                                              deramp=False,repeat=1))
n = S2.n()//7

nf=n

nv = 2
v = linspace(0,nv-1,nv,dtype=int)
o = pi/3+S2.chord_dirs(S2.n()//3)

pts = 300

aa = pi/4

offset = 0

S=SpiroData()

dists = S2.chord_dists(S2.n()//5)

nf0=3
for i in range(nf0):
    f0=n//nf0*i 

    S.add(on_frame(S2,scale=dists,oangle=nv,fb=offset,fh=offset,orient=o,
          polyfunc=ngon_coords,pts=pts,first=f0,n=nf,orient_follow=0,
          arc_angle=aa,object=i,vertex_order=v,
          pin_coord=None,pin_to_frame=0.0,autoscale=False,pinned_vertex=0))

figure(S,'time','turbo')

###

S1 = integral_ellipticals(1,0.2,0.5,min_pen=0.5,rounds=3,circuits=2,ppl=2000,inside=True)
S2 = S1.resample(S1.max_path()*frame_sampling(1000,parm=2,spacing='constant',
                                              deramp=False,repeat=1))
n = S2.n()

nf=n

nv = 2
v = linspace(0,nv-1,nv,dtype=int)
o = pi/3+S2.chord_dirs(S2.n()//3) 

pts = 200

aa = pi/3

offset = -0.2 
S=SpiroData()

dists = S2.chord_dists(S2.n()//5)

nf0=1
for i in range(nf0):
    f0=n//nf0*i 

    S.add(on_frame(S2,scale=np.roll(dists,f0),oangle=nv,
                   fb=offset,fh=offset,orient=np.roll(o,f0),
                   polyfunc=ngon_coords,pts=pts,first=f0,n=nf-1,orient_follow=0,
                   arc_angle=aa,object=i,vertex_order=v,
                   pin_coord=None,pin_to_frame=0.0,autoscale=False,pinned_vertex=0))

figure(S,'time','gist_heat_r')

###

S1 = integral_ellipticals(1,0.2,0.5,min_pen=0.5,rounds=3,circuits=2,ppl=2000,inside=True)
S2 = S1.resample(S1.max_path()*frame_sampling(800,parm=2,spacing='constant',
                                              deramp=False,repeat=1))
n = S2.n()

nf=n//3

nv = 2
v = linspace(0,nv-1,nv,dtype=int)
nb = S2.n()//7
o = pi/2.5+S2.chord_dirs(nb) 

pts = 200

aa = pi/3 

offset = -0.0 
S=SpiroData()

dists = S2.chord_dists(nb)

nf0=3
for i in range(nf0):
    f0=n//nf0*i 

    S.add(on_frame(S2,scale=np.roll(dists,f0),oangle=nv,
                   fb=offset,fh=offset,orient=np.roll(o,f0),
                   polyfunc=ngon_coords,pts=pts,first=f0,n=nf-1,orient_follow=0,
                   arc_angle=aa,object=i,vertex_order=v,
                   pin_coord=None,pin_to_frame=0.0,autoscale=False,pinned_vertex=0))

figure(S,'y-direction','cmap1')

###

S1 = integral_ellipticals(1,0.2,0.5,min_pen=2.5,rounds=15,circuits=2,ppl=2000,inside=True)
S2 = S1.resample(S1.max_path()*frame_sampling(3000,parm=2,spacing='constant',
                                              deramp=False,repeat=1))

n = S2.n()

nf=n//7

nv = 2
v = linspace(0,nv-1,nv,dtype=int)
nb = S2.n()//7

o = linspace(0,12*pi,nf)

pts = 200

aa = pi/3 

offset = -0.0
S=SpiroData()

dists = 8 

nf0=3
for i in range(nf0):
    f0=n//nf0*i 

    S.add(on_frame(S2,scale=dists,oangle=nv,
                   fb=offset,fh=offset,orient=o,
                   polyfunc=ngon_coords,pts=pts,first=f0,n=nf-1,orient_follow=0,
                   arc_angle=aa,object=i,vertex_order=v,
                   pin_coord=None,pin_to_frame=0.0,autoscale=False,pinned_vertex=0))

figure(S,'time','pretty_reds')

###

S1 = integral_ellipticals(1,0.2,0.5,min_pen=2.5,rounds=15,circuits=2,ppl=2000,inside=False)
S2 = S1.resample(S1.max_path()*frame_sampling(3000,parm=10,spacing='linear',
                                              deramp=False,repeat=100))
n = S2.n()

nf=n//11

nv = 2
v = linspace(0,nv-1,nv,dtype=int)
nb = S2.n()//11
o = S2.chord_dirs(nb)

pts = 200

aa = pi/3 

offset = -0.0
S=SpiroData()

dists = S2.chord_dists(nb)

nf0=3
for i in range(nf0):
    f0=n//nf0*i 

    S.add(on_frame(S2,scale=np.roll(dists,f0),oangle=nv,
                   fb=offset,fh=offset,orient=np.roll(o,f0),
                   polyfunc=ngon_coords,pts=pts,first=f0,n=nf-1,orient_follow=0,
                   arc_angle=aa,object=i,vertex_order=None,
                   pin_coord=None,pin_to_frame=0.0,autoscale=False,pinned_vertex=0)) 

S.rotate(pi/4)
figure(S,'direction','turbo')
