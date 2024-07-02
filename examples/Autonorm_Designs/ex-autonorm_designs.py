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
ppl = 250
e = 0.0
e_circum=circum(R,semi_minor(R,e))
a = 1/3*e_circum/2/pi
S1 = cIe(ring=Ellipse(R,e),wheel=Wheel(a,1.3*a),loops=1,ppl=ppl,inside=True,reverse=False).rotate(0)

f0=S1.n()//11

U=SpiroData()

ns = 60

n = S1.n()//50

norm = array([ pi/9*sin(2*pi*j/n) for j in range(n) ])

lbox = 1*R
nk = 1
for k in range(nk):
    f = k*S1.n()//nk//4
    for i in range(ns):
        T = auto_inorm_frame(S1,first=f0+f+int(S1.n()/20*i/ns),norm_off1=0,norm_off2=norm,
                             intersect_tol=0.001,
                             base=0.0,amp=0.6,rate=10,object=i,n=n).rotate(1*pi*i/ns).valid() 
        for j in range(T.n()):
            T.fx[j]=S1.x[j]
            T.fy[j]=S1.y[j]

        U.add(T)

U = U.valid_in_radius(lbox)

o = 0
pts = 20
aa = pi/8

rp_opts = { 'n': 600, 
            'parm': frame_sampling(U.n(),parm=10, 
                                   spacing='sinusoid', repeat=1,deramp=True, nocum=True),
            'spacing':  ['sinusoid'], 'repeat': 30, 'deramp': False }

sc = 30
S = on_frame(U,scale=sc,oangle=pi/4,fb=0.5,fh=0.5,asym=0.1,orient=o,
             polyfunc=pcoords,pts=pts,orient_follow=1,n=U.n()-1,
             arc_angle=aa,rp_opts=rp_opts)

figure(S,'cycles','gist_heat_r')

###

R = 50
ppl = 1000
e = 0.0
e_circum=circum(R,semi_minor(R,e))
a = 1/4*e_circum/2/pi
S1 = cIe(ring=Ellipse(R,e),wheel=Wheel(a,1.3*a),loops=1,ppl=ppl,inside=True,reverse=False).rotate(0)

f0=S1.n()//11

U=SpiroData()

ns = 1

n = S1.n()

norm = pi/6 

lbox = 2*R
nk = 1
for k in range(nk):
    f = k*S1.n()//nk//4
    for i in range(ns):
        T = auto_inorm_frame(S1,first=f0+f+int(S1.n()/20*i/ns),norm_off1=0,norm_off2=norm,
                             intersect_tol=.2,
                             base=0.0,amp=0.0,rate=10,object=i,n=n).rotate(1*pi*i/ns).valid() 
        for j in range(T.n()):
            T.fx[j]=S1.x[j]
            T.fy[j]=S1.y[j]

        U.add(T)

U = U.valid_in_radius(lbox)

o = linspace(0,pi/4,U.n()) 
pts = (2*U.fradii()).astype(int)
aa = pi/8

rp_opts = { 'n': 800, 
            'parm': frame_sampling(U.n(),parm=10, 
                                   spacing='sinusoid', repeat=1,deramp=True, nocum=True),
            'spacing':  ['sinusoid'], 'repeat': 30, 'deramp': False }

sc = 30
n = 2*U.n()//3-1
S = on_frame(U,scale=sc,oangle=pi/3,fb=0.5,fh=0.5,asym=0.0,orient=o,
             polyfunc=tcoords,pts=pts,orient_follow=1,n=n,
             arc_angle=aa,rp_opts=None)

figure(S,'time','inferno_r')

###

R = 50
ppl = 1000
e = 0.0
e_circum=circum(R,semi_minor(R,e))
a = 1/5*e_circum/2/pi
S1 = cIe(ring=Ellipse(R,e),wheel=Wheel(a,2.3*a),
         loops=1,ppl=ppl,inside=True,reverse=True).rotate(pi/7)

f0=S1.n()//11

U=SpiroData()

ns = 1 

n = S1.n() 

norm = array([ pi/6 + pi/12*sin(2*pi*j/n) for j in range(n) ])

lbox = 3*R
nk = 1
for k in range(nk):
    f = k*S1.n()//nk//4
    for i in range(ns):
        T = auto_inorm_frame(S1,first=f0+f+int(S1.n()/20*i/ns),norm_off1=0,norm_off2=norm,
                             intersect_tol=.2,
                             base=0.0,amp=0.0,rate=10,object=i,n=n).rotate(1*pi*i/ns).valid() 
        for j in range(T.n()):
            T.fx[j]=S1.x[j]
            T.fy[j]=S1.y[j]

        U.add(T)

U = U.valid_in_radius(lbox)

U = U.resample(U.max_path()*frame_sampling(ppl,parm=7,spacing='sinusoid',
                                              deramp=True,repeat=20))

o = 0 
pts = 8
aa = 0 

nv = 50
v = linspace(0,nv-1,nv,dtype=int)

rp_opts = { 'n': nv*pts, 
            'parm': 1.0,
            'spacing':  ['sinusoid'], 'repeat': 10, 'deramp': True }

offset = 0.5
sc = 40
n = U.n()-2 

asym = frame_sampling(n,parm=5,spacing='sinusoid',repeat=5,deramp=True,nocum=True)/6 * 0.8

S = on_frame(U,scale=sc,oangle=nv,fb=offset,fh=offset,asym=asym,orient=o,first=1,
             polyfunc=ecoords,pts=pts,orient_follow=1,n=n,vertex_order=v,
             arc_angle=aa,rp_opts=rp_opts)

figure(S,'direction','turbo')

###

R = 50
ppl = 1000
e = 0.0
e_circum=circum(R,semi_minor(R,e))
a = 1/5*e_circum/2/pi
S1 = cIe(ring=Ellipse(R,e),wheel=Wheel(a,2.3*a),
         loops=1,ppl=ppl,inside=True,reverse=True).rotate(pi/7)

f0=S1.n()//11

U=SpiroData()

ns = 1 

n = S1.n() 

norm = array([ pi/6 + pi/12*sin(2*pi*j/n) for j in range(n) ])

lbox = 3*R
nk = 1
for k in range(nk):
    f = k*S1.n()//nk//4
    for i in range(ns):
        T = auto_inorm_frame(S1,first=f0+f+int(S1.n()/20*i/ns),norm_off1=0,norm_off2=norm,
                             intersect_tol=.2,
                             base=0.0,amp=0.0,rate=10,object=i,n=n).rotate(1*pi*i/ns).valid() 
        for j in range(T.n()):
            T.fx[j]=S1.x[j]
            T.fy[j]=S1.y[j]

        U.add(T)

U = U.valid_in_radius(lbox)

U = U.resample(U.max_path()*frame_sampling(2*ppl,parm=9,spacing='sinusoid',
                                              deramp=True,repeat=30))

n = 2*U.n()//5

o = 0 
pts = 100 
aa = -pi/3

nv = 3
v = linspace(0,nv-1,nv,dtype=int)

rp_opts = { 'n': nv*pts, 
            'parm': 9.0,
            'spacing':  ['sinusoid'], 'repeat': 5, 'deramp': False }

offset = 0.5
sc = 15

asym = 0.8 + frame_sampling(n,parm=5,spacing='sinusoid',repeat=5,deramp=True,nocum=True)/6 * 0

f0 = 1386 
S = on_frame(U,scale=sc,oangle=pi/2,fb=offset,fh=offset,asym=asym,orient=o,first=f0,
             polyfunc=tcoords,pts=pts,orient_follow=1,n=n,vertex_order=[1,2],
             object=1,arc_angle=aa,rp_opts=rp_opts)

S.add(on_frame(U,scale=sc,oangle=pi/2,fb=offset,fh=offset,asym=asym,orient=o,first=f0,
             polyfunc=tcoords,pts=pts//5,orient_follow=1,n=n,vertex_order=[0,1],
             object=1,arc_angle=0,rp_opts=None))

figure(S,S.o+sin(S.t/max(S.t)*2*pi),'Wistia')
