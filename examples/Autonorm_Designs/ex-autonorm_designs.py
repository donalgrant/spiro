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

###

###   coordinate dither -- pointillist / impressionist version of autonorm design 004

R = 50
ppl = 1000
e = 0.0
e_circum=circum(R,semi_minor(R,e))
a = 1/3*e_circum/2/pi
S1 = cIe(ring=Ellipse(R,e),wheel=Wheel(a,1.3*a),
         loops=1,ppl=ppl,inside=True,reverse=True).rotate(pi/7)

S1 = S1.resample(S1.max_path()*frame_sampling(S1.n(),spacing='random',
                                              repeat=10,deramp=True))

f0=S1.n()//24

U=SpiroData()

ns = 1 

n = S1.n()

norm = 0 

lbox = 4*R
nk = 1
for k in range(nk):
    f = k*S1.n()//nk//4
    for i in range(ns):
        T = auto_inorm_frame(S1,first=f0+f+int(S1.n()/20*i/ns),norm_off1=0,norm_off2=norm,
                             intersect_tol=.1,
                             base=0.0,amp=0.4,rate=10,object=i,n=n).rotate(1*pi*i/ns).valid() 
        for j in range(T.n()):
            T.fx[j]=S1.x[j]
            T.fy[j]=S1.y[j]

        U.add(T)

U = U.valid_in_radius(lbox)

n = U.n()

o = 0 
pts = 100 
aa = 0 

nv = 3
v = linspace(0,nv-1,nv,dtype=int)

rp_opts = { 'n': nv*pts, 
            'parm': 9,
            'spacing':  'random', 'repeat': 3, 'deramp': False }

fs = frame_sampling(1,fs_opts=rp_opts)

offset = 0.5
sc = 75

asym = 0.0 + 0.3 * frame_sampling(n,parm=5,spacing='sinusoid',repeat=3,deramp=True,nocum=True)/6 * 0

f0 = 1384
follow = 1

nn = n
    
S = on_frame(U,scale=sc,oangle=pi/2,fb=offset,fh=offset,asym=asym,orient=o,first=f0,
             polyfunc=tcoords,pts=pts,orient_follow=follow,n=nn,vertex_order=None,
             object=1,arc_angle=aa,rp_opts=None)

figure(S,'fcdist3','hot')

###

R = 50
ppl = 1000
e = 0.0
e_circum=circum(R,semi_minor(R,e))
a = 1/3*e_circum/2/pi
S1 = cIe(ring=Ellipse(R,e),wheel=Wheel(a,1.3*a),
         loops=1,ppl=ppl,inside=True,reverse=True).rotate(pi/7)

f0=S1.n()//24

U=SpiroData()

ns = 1 

n = S1.n()

norm = 0 

lbox = 4*R
nk = 1
for k in range(nk):
    f = k*S1.n()//nk//4
    for i in range(ns):
        T = auto_inorm_frame(S1,first=f0+f+int(S1.n()/20*i/ns),norm_off1=0,norm_off2=norm,
                             intersect_tol=.1,
                             base=0.0,amp=0.4,rate=10,object=i,n=n).rotate(1*pi*i/ns).valid() 
        for j in range(T.n()):
            T.fx[j]=S1.x[j]
            T.fy[j]=S1.y[j]

        U.add(T)

U = U.valid_in_radius(lbox)


n = U.n() 

o = 0 
pts = 100
aa = pi/6

nv = 4
v = linspace(0,nv-1,nv,dtype=int)

offset = 0.5
sc = 75

asym = 0.0 

f0 = 0 
follow = 122

nn = n
    
S = on_frame(U,scale=sc,oangle=pi/4,fb=offset,fh=offset,asym=asym,orient=o,first=f0,
             polyfunc=pcoords,pts=pts,orient_follow=follow,n=nn,vertex_order=None,
             object=1,arc_angle=aa,rp_opts=None)

figure(S,'time','bone_r')

###

R = 50
ppl = 1000
e = 0.0
e_circum=circum(R,semi_minor(R,e))
a = 1/4*e_circum/2/pi
S1 = cIe(ring=Ellipse(R,e),wheel=Wheel(a,1.5*a),
         loops=1,ppl=ppl,inside=True,reverse=True).rotate(pi/7)

f0=S1.n()//24

U=SpiroData()

ns = 1 

n = S1.n()

norm = 0

lbox = 4*R
nk = 1
for k in range(nk):
    f = k*S1.n()//nk//4
    for i in range(ns):
        T = auto_inorm_frame(S1,first=f0+f+int(S1.n()/20*i/ns),norm_off1=0,norm_off2=norm,
                             intersect_tol=.1,
                             base=0.0,amp=0.4,rate=10,object=i,n=n).rotate(1*pi*i/ns).valid() 
        for j in range(T.n()):
            T.fx[j]=S1.x[j]
            T.fy[j]=S1.y[j]

        U.add(T)

U = U.valid_in_radius(lbox)

U = U.resample(U.max_path()*frame_sampling(2*ppl,parm=5,spacing='sinusoid',
                                              deramp=True,repeat=30))


n = U.n() # 2*U.n()//5

o = 0 # linspace(0,pi/4,U.n()) # 0
pts = 100 # (2*U.fradii()).astype(int)
aa = pi/6 # -pi/3

nv = 4
v = linspace(0,nv-1,nv,dtype=int)

rp_opts = { 'n': nv*pts, 
            'parm': 8,
            'spacing':  ['sinusoid'], 'repeat': 8, 'deramp': True }

offset = 0.5
sc = 75

asym = 0.0 

f0 = 0 

nn = n//4

for follow in [147]:
    
    S = on_frame(U,scale=sc,oangle=pi/4,fb=offset,fh=offset,asym=asym,orient=o,first=f0,
                 polyfunc=pcoords,pts=pts,orient_follow=follow,n=nn,vertex_order=None,
                 object=1,arc_angle=aa,rp_opts=rp_opts)

figure(S,'time','hot')

###

R = 50
ppl = 1000
e = 0.0
e_circum=circum(R,semi_minor(R,e))
a = 1/5*e_circum/2/pi
S1 = cIe(ring=Ellipse(R,e),wheel=Wheel(a,1.5*a),
         loops=1,ppl=ppl,inside=False,reverse=False).rotate(pi/7)

f0=S1.n()//24

U=SpiroData()

n = S1.n() 

norm = -pi/9

lbox = 4*R

T = auto_inorm_frame(S1,first=f0,norm_off1=0,norm_off2=norm,
                             intersect_tol=.001,
                             base=0.0,amp=0.0,rate=10,n=n).rotate(0).valid() 
for j in range(T.n()):
    T.fx[j]=S1.x[j]
    T.fy[j]=S1.y[j]

U.add(T)

U = U.valid_in_radius(lbox)

UR = U.resample(U.max_path()*frame_sampling(ppl,parm=5,spacing='sinusoid',
                                            deramp=True,repeat=10))

n = UR.n()

o = 0 
pts = 50 
aa = pi 

nv = 16
v = linspace(0,nv-1,nv,dtype=int)

offset = 0.0
sc = 30

asym = 0.9 

f0 = 0 
follow = n//5

nn = n//3

S = SpiroData()

first_plot=True

nplots=1
for i in range(nplots):

    f0=int(i/nplots * nn * 0.7) + 140
    
    S = on_frame(UR,scale=sc,oangle=nv,fb=offset,fh=offset,asym=asym,orient=o,first=f0,
                 polyfunc=ecoords,pts=pts,orient_follow=follow,n=nn,vertex_order=v,
                 object=1,arc_angle=aa,rp_opts=None)

    r = S.radii()
    alpha = (max(r)-r) / max(r) * 0.4
    
    F.plot(S,color_scheme='time',cmap='cmap1', dot_size=0.1,alpha=alpha,limits=None,
           coord_dither=0.0,color_dither=0.0,new_fig=first_plot)

    first_plot=False
    
    S = on_frame(UR,scale=sc,oangle=nv,fb=offset,fh=offset,asym=asym,orient=o,first=f0,
                 polyfunc=ecoords,pts=pts,orient_follow=follow,n=nn,vertex_order=v,
                 object=1,arc_angle=-aa,rp_opts=None)

    
    r = S.radii()
    alpha = (max(r)-r) / max(r) * 0.4
    
    F.plot(S,color_scheme='time',cmap='cmap1', dot_size=0.1,alpha=alpha,limits=None,
           coord_dither=0.0,color_dither=0.0,new_fig=first_plot)

F.save_fig()

###

R = 50
ppl = 1000
e = 0.0
e_circum=circum(R,semi_minor(R,e))
a = 1/5*e_circum/2/pi
S1 = cIe(ring=Ellipse(R,e),wheel=Wheel(a,1.5*a),
         loops=1,ppl=ppl,inside=False,reverse=False).rotate(pi/7)

f0=S1.n()//24

U=SpiroData()

n = S1.n() 

norm = -pi/9

lbox = 4*R

T = auto_inorm_frame(S1,first=f0,norm_off1=0,norm_off2=norm,
                             intersect_tol=.001,
                             base=0.0,amp=0.0,rate=10,n=n).rotate(0).valid() 
for j in range(T.n()):
    T.fx[j]=S1.x[j]
    T.fy[j]=S1.y[j]

U.add(T)

U = U.valid_in_radius(lbox)

UR = U.resample(U.max_path()*frame_sampling(2*ppl,parm=5,spacing='sinusoid',
                                            deramp=True,repeat=10))

n = UR.n() 

oa = 6
nv = oa*2
v = linspace(0,nv-1,nv,dtype=int)

pts = 40 

rp_opts = { 'n': nv*pts, 
            'parm': 8,
            'spacing':  ['sinusoid'], 'repeat': 8, 'deramp': True }

offset = 0.4
sc = 20

f0 = 0 
follow = n//5

nn = n//13

o = linspace(0,pi,nn) # 0
fs = frame_sampling(nn,parm=4,spacing='sinusoid',deramp=True,reverse=True,nocum=True)
fs /= max(fs)

asym = 0.4 * fs + 0.1

aa = -pi/6 

S = SpiroData()

first_plot=True

cs='fcdist3'
cmap='hot'

nplots=7
for i in range(nplots):

    f0=int(i/nplots * n) + 140
    
    S.add(on_frame(UR,scale=sc,oangle=oa,fb=offset,fh=offset,asym=asym,orient=o,first=f0,
                 polyfunc=nstar_coords,pts=pts,orient_follow=follow,n=nn,vertex_order=None,
                 object=1,arc_angle=aa,rp_opts=None))

r = S.fchord_dists(n//3)
alpha = (max(r)-r) / max(r) * 0.3 + 0.1
    
F.plot(S,color_scheme=cs,cmap=cmap, dot_size=0.1,alpha=alpha,limits=None,
       coord_dither=0.0,color_dither=0.1,new_fig=first_plot)

F.save_fig()

###

R = 50
ppl = 1000
a=R/(2*pi)/3
S1 = spiro_eq_triangle(R=R,wheel=Wheel(a,0.6*a),orient=0,loops=1,fold=False,inside=False)

f0=S1.n()//9

U=SpiroData()

n = S1.n() # S1.n()//50

norm = pi/2

lbox = 1.5*R

T = auto_inorm_frame(S1,first=f0,norm_off1=0,norm_off2=norm,
                             intersect_tol=.3,
                             base=0.5,amp=0.5,rate=4,n=n).rotate(0).valid() 
for j in range(T.n()):
    T.fx[j]=S1.x[j]
    T.fy[j]=S1.y[j]

U.add(T)

U = U.valid_in_radius(lbox)

n = U.n()

oa = 2
nv = oa
v = linspace(0,nv-1,nv,dtype=int)

pts = 60 

rp_opts = { 'n': pts, 
            'parm': 2,
            'spacing':  ['linear'], 'repeat': 3, 'deramp': False }

offset = 0.4
sc = 10

f0 = 0 
follow = 1

nn = n//4

o = linspace(0,6*pi,nn)

asym = 0 

aa = pi/3 

S = SpiroData()

first_plot=True

cs='phase'
cmap='turbo'

f0=nn//4
    
T=on_frame(U,scale=sc,oangle=oa,fb=offset,fh=offset,asym=asym,orient=o,first=f0,
           polyfunc=ngon_coords,pts=pts,orient_follow=follow,n=nn,vertex_order=v,
           object=1,arc_angle=aa,rp_opts=rp_opts)

for i in range(3):  S.add(T.rotate(pi/8))

alpha = 0.4

S.rotate(-pi/3)

F.plot(S,color_scheme=cs,cmap=cmap, dot_size=0.1,alpha=alpha,limits=None,
       coord_dither=0.0,color_dither=0.0,new_fig=first_plot)

F.save_fig()

##

n = U.n()

oa = 2
nv = oa
v = linspace(0,nv-1,nv,dtype=int)

pts = 60 

rp_opts = { 'n': pts, 
            'parm': 2,
            'spacing':  ['linear'], 'repeat': 3, 'deramp': False }

offset = 0.4
sc = 10

f0 = 0 
follow = 1

nn = n

o = linspace(0,6*pi,nn) 

asym = 0 

aa = pi/3

S = SpiroData()

first_plot=True

cs='direction' 
cmap='turbo'

nplots=1
for i in range(nplots):

    f0=int(i/nplots * n) + 0
    
    S.add(on_frame(U,scale=sc,oangle=oa,fb=offset,fh=offset,asym=asym,orient=o,first=f0,
                 polyfunc=ngon_coords,pts=pts,orient_follow=follow,n=nn,vertex_order=v,
                 object=1,arc_angle=aa,rp_opts=rp_opts))

alpha = 0.4 
    
F.plot(S,color_scheme=cs,cmap=cmap, dot_size=0.1,alpha=alpha,limits=None,
       coord_dither=0.2,color_dither=0.0,new_fig=first_plot)

F.save_fig()
