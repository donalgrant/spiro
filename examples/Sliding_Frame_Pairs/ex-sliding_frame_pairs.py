import sys
sys.path.append('../..')
import argparse

import numpy as np

from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_frame import *
from polygon import *

parser = argparse.ArgumentParser(description="Frame Pair A Examples")
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

F._figname='Sliding_Frame_Pairs-'

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

pplf=1.5
ppl1=450
ppl2=550
maj=24
ecc=0.0
a = circum(maj,semi_minor(maj,ecc))/(2*pi)/3
T1 = cIe(Ellipse(maj,ecc),wheel=Wheel(a,a),loops=1.0,inside=True,ppl=int(ppl1*pplf))
T2 = cIe(Ellipse(maj,ecc),wheel=Wheel(a*3/4,a),loops=1.0,inside=True,ppl=int(ppl2*pplf)).move(20,10)

S = SpiroData()

npts=3 

nk=1
gs=0
n  = np.lcm(T1.n(),T2.n())//(nk+gs)
ns = T2.n()//nk 

pts = npts

oa = pi/3
aa = pi/4

ptf = array([ 0.4+0.3*cos(2*pi*j/n) for j in range(n) ])

start=int(0.0*ns)
offset = int(0.0*ns)

shift = 0.0

size = 0.0 

for k in range(0,nk):
    first1 = k*ns+start
    first2 = k*ns+start+offset
    ao = 0 

    S.add(frame_pair(T1,T2,skip1=1,skip2=1,first1=first1,first2=first2,n2=n,
                     scale=size,oangle=oa,fb=shift,fh=shift,asym=0.0,orient=ao,polyfunc=tcoords,
                     pts=pts,arc_angle=aa,object=k,prot=0,vertex_order=None,
                     pin_to_frame1=ptf,autoscale=False,pinned_vertex=1,show_side=array([1,0,0])))

F.plot(S,color_scheme='length',cmap='turbo',alpha=0.4,dot_size=10,
       save=True,filename='sliding_frame_pairs-cover.png')

###

pplf=1.5
ppl1=450
ppl2=550
maj=24
ecc=0.0
a = circum(maj,semi_minor(maj,ecc))/(2*pi)/3
T1 = cIe(Ellipse(maj,ecc),wheel=Wheel(a,a),loops=1.0,inside=True,ppl=int(ppl1*pplf))
T2 = cIe(Ellipse(maj,ecc),wheel=Wheel(a*3/4,a),loops=1.0,inside=True,ppl=int(ppl2*pplf)).move(20,10)

S = SpiroData()

npts=150*def_factor

nk=24
gs=12
n  = np.lcm(T1.n(),T2.n())//(nk+gs)
ns = T2.n()//nk 

pts = linspace(npts//4,npts,n,dtype=int)

oa = pi/3
aa = pi/4

ptf = array([ 0.4+0.3*cos(2*pi*j/n) for j in range(n) ])

start=int(0.0*ns)
offset = int(0.0*ns)

shift = 0.0

size = 5.0 

for k in range(0,nk//2):
    first1 = k*ns+start
    first2 = k*ns+start+offset
    ao = 2*k*pi/nk 

    S.add(frame_pair(T1,T2,skip1=1,skip2=1,first1=first1,first2=first2,n2=n,
                       scale=size,oangle=oa,fb=shift,fh=shift,asym=0.3,orient=ao,polyfunc=tcoords,
                       pts=pts,arc_angle=aa,object=k,prot=0,vertex_order=None,
                       pin_to_frame1=ptf,autoscale=False,pinned_vertex=1,show_side=array([1,1,1])))

figure(S,'object','turbo')

###

pplf=2
ppl1=400
ppl2=500
maj=24
ecc=0.0
a = circum(maj,semi_minor(maj,ecc))/(2*pi)/3
T1 = cIe(Ellipse(maj,ecc),wheel=Wheel(a,a),loops=1.0,inside=True,ppl=int(ppl1*pplf)).rotate(pi/6)
T2 = cIe(Ellipse(maj,ecc),wheel=Wheel(a*3/4,a),loops=1.0,inside=True,ppl=int(ppl2*pplf)).move(20,0)

S = SpiroData()

npts=150*def_factor

nk=4
gs=0
n  = np.lcm(T1.n(),T2.n())//(nk+gs)
ns = T2.n()//nk 

pts = npts

oa = pi/3
aa = pi/4

ptf = array([ 0.5+0.6*cos(6*pi*j/n) for j in range(n) ])

start=int(0.0*ns)
offset = int(0.0*ns)

shift = 0.0 

size = 1.0 

o = 3
for k in range(o,o+1):
    first1 = k*ns+start
    first2 = k*ns+start+offset
    ao = 0 

    S.add(frame_pair(T1,T2,skip1=1,skip2=1,first1=first1,first2=first2,n2=n,
                     scale=size,oangle=oa,fb=shift,fh=shift,asym=0.0,orient=ao,polyfunc=tcoords,
                     pts=pts,arc_angle=aa,object=k,prot=0,vertex_order=None,
                     pin_to_frame1=ptf,autoscale=True,pinned_vertex=1,show_side=array([1,1,1])))


figure(S,'fcdist3','gist_heat_r')

##

S = SpiroData()

npts=250*def_factor

nk=8
gs=0
n  = np.lcm(T1.n(),T2.n())//(nk+gs)
ns = T2.n()//nk 

pts = npts

oa = pi/3
aa = pi/4

ptf = array([ 0.5+0.6*cos(6*pi*j/n) for j in range(n) ])

start=int(0.0*ns)
offset = int(0.5*ns)

shift = 0.0 

size = 10 

o = 2
for k in range(o,o+2):
    first1 = k*ns+start
    first2 = k*ns+start+offset
    ao = linspace(0,pi,n)

    print(k,first1,first2,n)
    S.add(frame_pair(T1,T2,skip1=1,skip2=1,first1=first1,first2=first2,n2=n,
                     scale=size,oangle=oa,fb=shift,fh=shift,asym=0.0,orient=ao,polyfunc=tcoords,
                     pts=pts,arc_angle=aa,object=k,prot=0,vertex_order=None,
                     pin_to_frame1=ptf,autoscale=True,pinned_vertex=1,show_side=array([1,1,0])))

figure(S,'spacing','cmap1')

###

pplf=2.2
ppl1=200
ppl2=300
maj=24
ecc=0.0
a = circum(maj,semi_minor(maj,ecc))/(2*pi)/3
T1 = cIe(Ellipse(maj,ecc),wheel=Wheel(a,a),loops=1.0,inside=True,ppl=int(ppl1*pplf)).rotate(pi/6)
T2 = cIe(Ellipse(maj,ecc),wheel=Wheel(a*3/4,a),loops=1.0,inside=True,ppl=int(ppl2*pplf)).move(20,0)

S = SpiroData()

npts=250*def_factor

nk=6
gs=0
n  = np.lcm(T1.n(),T2.n())//(nk+gs)
ns = T2.n()//nk 

pts = npts

oa = pi/3
aa = pi/4

ptf = array([ 0.5+0.6*cos(6*pi*j/n) for j in range(n) ])

start=int(0.0*ns)
offset = int(0.5*ns)

shift = 0.0 

size = 10 

o = 3
for k in range(o,o+2):
    first1 = k*ns+start
    first2 = k*ns+start+offset
    ao = linspace(0,pi,n)

    print(k,first1,first2,n)
    S.add(frame_pair(T1,T2,skip1=1,skip2=1,first1=first1,first2=first2,n2=n,
                     scale=size,oangle=oa,fb=shift,fh=shift,asym=0.0,orient=ao,polyfunc=tcoords,
                     pts=pts,arc_angle=aa,object=k,prot=0,vertex_order=None,
                     pin_to_frame1=ptf,autoscale=True,pinned_vertex=1,show_side=array([1,1,0])))

figure(S,'spacing','pretty_reds')
