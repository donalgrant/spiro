import sys
sys.path.append('../..')
import argparse

import numpy as np

from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_frame import *
from polygon import *

parser = argparse.ArgumentParser(description="Intersecting Normal Examples")
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

F._figname='Intersecting_Normals-'

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

###  Cover with frame superimposed

pplf=5
ppl1=200
ppl2=250
maj=24
ecc=0.4
a = circum(maj,semi_minor(maj,ecc))/(2*pi)/3
T1 = cIe(Ellipse(maj,ecc),wheel=Wheel(a,2*a),loops=1.0,inside=False,ppl=int(ppl1*pplf)).rotate(pi/3)
T2 = cIe(Ellipse(maj,ecc),wheel=Wheel(a,3*a),loops=1.0,inside=False,ppl=int(ppl2*pplf)).move(0,0)

S = SpiroData()

npts=150*def_factor

nk=1
gs=0
n  = np.lcm(T1.n(),T2.n())//(nk+gs)
ns = T2.n()//nk 

nn = n//8

pts = array([ int(npts/4 + 3/4 * (npts-npts*cos(2*pi*j/nn))) for j in range(nn) ])

oa = pi/3
aa = -pi/4

ptf = 0.

seed=755 # np.random.randint(0,1000)
np.random.seed(seed)

start=np.random.randint(0,nn)
offset = int(0.4*ns)

shift = 0.0 

size = 50 

T = SpiroData()

for k in range(nk):
    first1 = k*ns+start
    first2 = k*ns+start+offset
    ao = 2*k*pi/nk +linspace(0,-pi/8,nn)
    asym = linspace(0.0,0.3,nn)

    S.add(frame_pair(T2,T2,skip1=1,skip2=1,first1=first1,first2=first2,n2=nn,
                     scale=size,oangle=oa,fb=shift,fh=shift,asym=asym,orient=ao,polyfunc=tcoords,
                     pts=pts,arc_angle=aa,object=k,prot=0,vertex_order=None,
                     pin_to_frame1=ptf,autoscale=False,pinned_vertex=1,show_side=array([1,1,1]),
                     normal_intersect=True))
    T.add(frame_pair(T2,T2,skip1=1,skip2=1,first1=first1,first2=first2,n2=nn,
                     scale=size,oangle=oa,fb=shift,fh=shift,asym=asym,orient=ao,polyfunc=tcoords,
                     pts=pts,arc_angle=aa,object=k,prot=0,vertex_order=None,
                     pin_to_frame1=ptf,autoscale=False,pinned_vertex=1,show_side=array([1,1,1]),
                     normal_intersect=True,frame_only=True))

F.plot(S,color_scheme='fpolars',cmap='autumn',alpha=0.4,dot_size=0.1) 
F.plot(T,color_scheme='cyan',dot_size=1.0,new_fig=False)
F.save_fig('Intersecting_Normals-Cover.png')

###

pplf=2
ppl1=200
ppl2=250
maj=24
ecc=0.4
a = circum(maj,semi_minor(maj,ecc))/(2*pi)/3
T1 = cIe(Ellipse(maj,ecc),wheel=Wheel(a,2*a),loops=1.0,inside=False,ppl=int(ppl1*pplf)).rotate(pi/3)
T2 = cIe(Ellipse(maj,ecc),wheel=Wheel(a,a),loops=1.0,inside=False,ppl=int(ppl2*pplf)).move(0,0)

S = SpiroData()

npts=100*def_factor

nk=6
gs=0
n  = np.lcm(T1.n(),T2.n())//(nk+gs)
ns = T2.n()//nk 

pts = npts

oa = pi/3
aa = pi/4

ptf = 0. 

start=int(0.0*ns)
offset = int(0.3*ns)

shift = 0.0

size = 30

for k in range(nk):
    first1 = k*ns+start
    first2 = k*ns+start+offset
    ao = linspace(0,-pi,n) 

    S.add(frame_pair(T2,T2,skip1=1,skip2=1,first1=first1,first2=first2,n2=n,
                     scale=size,oangle=oa,fb=shift,fh=shift,asym=0.0,orient=ao,polyfunc=pcoords,
                     pts=pts,arc_angle=aa,object=k,prot=0,vertex_order=None,
                     pin_to_frame1=ptf,autoscale=False,pinned_vertex=1,show_side=array([1,1,1,1]),
                     normal_intersect=True))

lbox=100
figure(S,'time','hot',limits=[-lbox,lbox,-lbox,lbox])

###

pplf=9
ppl1=200
ppl2=250
maj=24
ecc=0.4
a = circum(maj,semi_minor(maj,ecc))/(2*pi)/3
T1 = cIe(Ellipse(maj,ecc),wheel=Wheel(a,2*a),loops=1.0,inside=False,ppl=int(ppl1*pplf)).rotate(pi/3)
T2 = cIe(Ellipse(maj,ecc),wheel=Wheel(a,3*a),loops=1.0,inside=False,ppl=int(ppl2*pplf)).move(0,0)

S = SpiroData()

npts=100*def_factor

nk=18
gs=3
n  = np.lcm(T1.n(),T2.n())//(nk+gs)
ns = T2.n()//nk 

pts = array([ int(npts/4 + 3/4 * (npts-npts*cos(2*pi*j/n))) for j in range(n) ])

oa = pi/3
aa = pi/4

ptf = 0. 

start=int(0.0*ns)
offset = int(0.4*ns)

shift = 0.0 

size = 50 

for k in range(0,nk,6):
    first1 = k*ns+start
    first2 = k*ns+start+offset
    ao = 2*k*pi/nk +linspace(0,-pi/8,n)

    S.add(frame_pair(T2,T2,skip1=1,skip2=1,first1=first1,first2=first2,n2=n,
                     scale=size,oangle=oa,fb=shift,fh=shift,asym=0.0,orient=ao,polyfunc=pcoords,
                     pts=pts,arc_angle=aa,object=k,prot=0,vertex_order=None,
                     pin_to_frame1=ptf,autoscale=False,pinned_vertex=1,show_side=array([1,1,1,1]),
                     normal_intersect=True))

figure(S,'fradii','twilight') 

##

S = SpiroData()

npts=200*def_factor

nk=1
gs=0
n  = np.lcm(T1.n(),T2.n())//(nk+gs)
ns = T2.n()//nk 

pts = array([ int(npts/4 + 3/4 * (npts-npts*cos(2*pi*j/n))) for j in range(n) ])

oa = pi/3
aa = pi/4

ptf = 0. # array([ 0.5+0.6*cos(6*pi*j/n) for j in range(n) ])

seed=466 
np.random.seed(seed)

start=np.random.randint(0,n)
offset = int(0.4*ns)

shift = 0.0 

size = 50 

for k in range(nk):
    first1 = k*ns+start
    first2 = k*ns+start+offset
    ao = 2*k*pi/nk +linspace(0,-pi/8,n)

    S.add(frame_pair(T2,T2,skip1=1,skip2=1,first1=first1,first2=first2,n2=n//10,
                     scale=size,oangle=oa,fb=shift,fh=shift,asym=0.0,orient=ao,polyfunc=pcoords,
                     pts=pts,arc_angle=aa,object=k,prot=0,vertex_order=None,
                     pin_to_frame1=ptf,autoscale=False,pinned_vertex=1,show_side=array([1,1,1,1]),
                     normal_intersect=True))

figure(S,'spacing','gist_heat_r')
