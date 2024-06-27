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

###

S1 = cIc(Ring(30),Wheel(6,6),loops=1,ppl=400,inside=True)
S2 = cIc(Ring(25),Wheel(5,5),loops=1,ppl=400,inside=True)

S2 = S2.resample(S2.max_path()*frame_sampling(400,parm=10,spacing='linear',
                                              deramp=False,repeat=50))

nv = 2
v = linspace(0,nv-1,nv,dtype=int)

pts = 200

nn = 400
rp_opts = { 'n': nn, 'parm': 1.0, 'spacing':  ['constant'], 'repeat': 10, 'deramp': True }

S=SpiroData()

nf0=1
for i in range(nf0):
    f0=n//nf0*i 

    S.add(frame_pair(S1,S2,skip1=1,skip2=1,first1=0,first2=S2.n()//6,
               scale=1.0,oangle=pi/3,fb=0.0,fh=0.0,asym=0,orient=0,polyfunc=tcoords, 
               pts=100,n1=1,n2=None,arc_angle=0,object=i,prot=0,vertex_order=None,
               pin_to_frame1=0.0,autoscale=True,pinned_vertex=0,show_side=None,
               normal_intersect=True,norm_off1=0.0,norm_off2=0.0,frame_only=False,intersect_tol=1.0e-1,
               show_line=False,show_intersect=False))

l = [-45,45,-45,45]

figure(S,'time','cmap1',limits=l)

###

ppl=800

S1 = cIc(Ring(30),Wheel(6,6),loops=1,ppl=ppl,inside=True)
S2 = cIc(Ring(25),Wheel(5,5),loops=1,ppl=ppl,inside=True)

S2 = S2.resample(S2.max_path()*frame_sampling(ppl,parm=10,spacing='linear',
                                              deramp=False,repeat=50))

n = S2.n()

nf=n//11

nv = 2
v = linspace(0,nv-1,nv,dtype=int)
nb = S2.n()//11
o = S2.chord_dirs(nb)

pts = 500

aa = pi/3 

offset = 0
S=SpiroData()

nf0=3
for i in range(nf0):
    f0=n//nf0*i 

    S.add(frame_pair(S1,S2,skip1=1,skip2=1,first1=f0,first2=S2.n()//9,
               scale=1.0,oangle=pi/3,fb=0.0,fh=0.0,asym=0,orient=0,polyfunc=tcoords, 
               pts=100,n1=1,n2=nf,arc_angle=aa,object=i,prot=0,vertex_order=None,
               pin_to_frame1=0.0,autoscale=True,pinned_vertex=0,show_side=None,
               normal_intersect=True,norm_off1=0.0,norm_off2=0.0,frame_only=False,intersect_tol=1.0e-1,
               show_line=False,show_intersect=False))

l = [-45,45,-45,45]
figure(S,'time','emerald_woman',limits=l)

###

ppl=800

S1 = cIc(Ring(30),Wheel(6,6),loops=1,ppl=ppl,inside=True)
S2 = cIc(Ring(25),Wheel(5,5),loops=1,ppl=ppl,inside=True)

S2 = S2.resample(S2.max_path()*frame_sampling(ppl,parm=10,spacing='linear',
                                              deramp=False,repeat=50))

n = S2.n()

nf=n

nv = 2
v = linspace(0,nv-1,nv,dtype=int)
nb = S2.n()//11
o = S2.chord_dirs(nb) 

pts = 500

nn = 400
rp_opts = { 'n': nn, 'parm': 10.0, 'spacing':  ['linear'], 'repeat': 10, 'deramp': False }

aa = pi/3 

offset = 0
S=SpiroData()

nf0=1
for i in range(nf0):
    f0=n//nf0*i 

    S.add(frame_pair(S1,S2,skip1=1,skip2=1,first1=f0,first2=S2.n()//9,
               scale=2.0,oangle=pi/3,fb=0.0,fh=0.0,asym=0,orient=0,polyfunc=tcoords, 
               pts=100,n1=1,n2=nf,arc_angle=aa,object=i,prot=0,vertex_order=None,
               pin_to_frame1=0.0,autoscale=True,pinned_vertex=0,show_side=None,
               normal_intersect=True,norm_off1=0.0,norm_off2=0.0,frame_only=False,intersect_tol=1.0e-1,
               show_line=False,show_intersect=False,rp_opts=rp_opts))

ll=60
l = [-ll,ll,-ll,ll]
figure(S,'dist_to_frm','Oranges',limits=l)  # try any color-scheme for this one!

###

ppl=800

S1 = cIc(Ring(30),Wheel(5,6),loops=1,ppl=ppl,inside=True)
S2 = cIc(Ring(24),Wheel(4,5),loops=1,ppl=ppl,inside=True)


S1 = S1.resample(S1.max_path()*frame_sampling(ppl,parm=10,spacing='sinusoid',
                                              deramp=True,repeat=40)).rotate(pi/5)
S2 = S2.resample(S2.max_path()*frame_sampling(ppl,parm=10,spacing='sinusoid',
                                              deramp=False,repeat=40))

n = S2.n()

nf=n//9

nv = 2
v = linspace(0,nv-1,nv,dtype=int)
nb = S2.n()//11
o = S2.chord_dirs(nb)

pts = 500

nn = 600
rp_opts = { 'n': nn, 'parm': 10.0, 'spacing':  ['sinusoid'], 'repeat': 3, 'deramp': True }

aa = pi 

offset = 0
S=SpiroData()

f2 = S2.n()//6
nf0=7
for i in range(nf0):
    f0=0

    T=frame_pair(S1,S2,skip1=1,skip2=1,first1=f0,first2=f2,
               scale=2.0,oangle=pi/4,fb=0.0,fh=0.0,asym=0,orient=0,polyfunc=tcoords, 
               pts=100,n1=1,n2=nf,arc_angle=aa,object=i,prot=0,vertex_order=None,
               pin_to_frame1=0.0,autoscale=True,pinned_vertex=0,show_side=None,
               normal_intersect=True,norm_off1=0.0,norm_off2=0.0,frame_only=False,intersect_tol=1.0e-1,
               show_line=False,show_intersect=False,rp_opts=rp_opts)
    S.add(T.rotate(2*pi/nf0*i))

ll=80
l = [-ll,ll,-ll,ll]

figure(S,'cycles','hot',limits=l)

###

ppl=1200

S1 = cIc(Ring(30),Wheel(5,6),loops=1,ppl=ppl,inside=True)
S2 = cIc(Ring(24),Wheel(4,5),loops=1,ppl=ppl,inside=True)


S1 = S1.resample(S1.max_path()*frame_sampling(ppl,parm=10,spacing='sinusoid',
                                              deramp=True,repeat=40)).rotate(pi/5)
S2 = S2.resample(S2.max_path()*frame_sampling(ppl,parm=10,spacing='sinusoid',
                                              deramp=False,repeat=40))

n = S2.n()

nf=n//9

nv = 2
v = linspace(0,nv-1,nv,dtype=int)
nb = S2.n()//11
o = S2.chord_dirs(nb) 

pts = 400

nn = 600
rp_opts = { 'n': nn, 'parm': 1.0, 'spacing':  ['sinusoid'], 'repeat': 10, 'deramp': True }

aa = pi 

offset = 0
S=SpiroData()

f2 = S2.n()//6
f0=0

T=frame_pair(S1,S2,first1=f0,first2=f2,n1=1,n2=nf,pin_to_frame1=0.5,
             normal_intersect=True,norm_off1=0.0,norm_off2=0.0,
             frame_only=True,intersect_tol=1.0e-1)

fpts=500
T0=T.resample(T.max_path()*
              frame_sampling(fpts,parm=10,spacing='sinusoid',deramp=False,repeat=30))

T1=on_frame(T0,skip=1,scale=20.0,oangle=pi/3,fb=0.5,fh=0.5,asym=0,orient=0,polyfunc=tcoords, 
           pts=pts,first=0,n=T0.n()//5,orient_follow=T0.n()//20,
           arc_angle=0,object=0,prot=0,vertex_order=None,
           pin_coord=None,pin_to_frame=1.0,autoscale=False,pinned_vertex=0,rp_opts=rp_opts)

ni=11
for i in range(ni//3):  S.add(T1.rotate(2*pi/ni))

S.rotate(-pi/2)
ll=50
l = None

figure(S,'time','turbo')

###

ppl=800

S1 = cIc(Ring(30),Wheel(5,6),loops=1,ppl=ppl,inside=True)
S2 = cIc(Ring(24),Wheel(4,5),loops=1,ppl=ppl,inside=True).move(15,0)

S1 = S1.resample(S1.max_path()*frame_sampling(ppl,parm=10,spacing='sinusoid',
                                              deramp=True,repeat=40)).rotate(pi/5)
S2 = S2.resample(S2.max_path()*frame_sampling(ppl,parm=10,spacing='sinusoid',
                                              deramp=False,repeat=40))
n = S2.n()

nf=n//23+10

nv = 2
v = linspace(0,nv-1,nv,dtype=int)

pts = 400

nn = 600
rp_opts = { 'n': nn, 'parm': 10.0, 'spacing':  ['sinusoid'], 'repeat': 10, 'deramp': True }

aa = [pi/40,pi/5,pi/40,pi/5]

offset = 0
S=SpiroData()

f2 = S2.n()//17
f0=0

sc = linspace(1,3,nf)
T=frame_pair(S1,S2,skip1=1,skip2=1,first1=f0,first2=f2,
             scale=sc,oangle=pi/4,fb=offset,fh=offset,asym=0.2,orient=0,polyfunc=pcoords, 
             pts=pts,n1=1,n2=nf,arc_angle=aa,object=0,prot=0,vertex_order=None,
             pin_to_frame1=0.0,autoscale=True,pinned_vertex=0,show_side=None,
             normal_intersect=True,norm_off1=0.0,norm_off2=0,frame_only=False,
             intersect_tol=1.0e-1,rp_opts=rp_opts)

ni=7
dn=2*pi/11
for i in range(ni):  S.add(T.rotate(dn))

S.rotate(-pi/5)

figure(S,'fradii','twilight')
