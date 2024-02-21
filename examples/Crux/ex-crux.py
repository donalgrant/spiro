import sys
sys.path.append('../..')
import argparse

from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_frame import *
from polygon import *

parser = argparse.ArgumentParser(description="Crux Examples")
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

F._figname='Crux-'

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

e=0.2
R=40
ppl=1000
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e,pen_offset=pi/4),wheel=Wheel(a*(2/3),a/5),ppl=ppl,loops=2,inside=True).rotate(-pi/6)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,2))

S=SpiroData()

nk=6
gs=9
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts = def_factor*200
npts_fade = linspace(npts,npts//6,n,dtype=int)
pts=np.zeros(0,dtype=int)
for j in range(n):
    nj=npts_fade[j]
    pts=np.append(pts,array([nj,nj,nj,0]))
    
wr = 0.0
hr = 1.0

for k in range(nk):
    first = k*ns + W.n()//18
    
    scale = [ 40/sqrt(W.radius(j)) for j in range(first,first+n) ]

    ao = linspace(0,pi/6,n)
    
    nn = n-1
    of = 1
    aa = pi/3
    
    S.add(on_frame(W,scale=scale,oangle=pi/2,first=first,n=nn,fh=-1,fb=-1,
                   asym=wr,orient_follow=of,orient=ao,polyfunc=pcoords,
                   arc_angle=aa,pts=pts,object=k,prot=-pi/2))
    
    S.add(on_frame(W,scale=scale,oangle=pi/2,first=first,n=nn,fh=-1,fb=0,
                   asym=wr,orient_follow=of,orient=ao,polyfunc=pcoords,
                   arc_angle=aa,pts=pts,object=k,prot=pi))
    
    S.add(on_frame(W,scale=scale,oangle=pi/2,first=first,n=nn,fh=0,fb=0,
                   asym=wr,orient_follow=of,orient=ao,polyfunc=pcoords,
                   arc_angle=aa,pts=pts,object=k,prot=pi/2))
    
    S.add(on_frame(W,scale=scale,oangle=pi/2,first=first,n=nn,fh=0,fb=-1,
                   asym=wr,orient_follow=of,orient=ao,polyfunc=pcoords,
                   arc_angle=aa,pts=pts,object=k,prot=0))
 

figure(S,S.fradii(),'turbo')

###

e=0.6
R=40
ppl=400
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e,pen_offset=pi/4),wheel=Wheel(a/3,0),ppl=ppl,loops=1,inside=True).rotate(pi/5)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,4))

npts=200
S=crosses_on_frame(W,asym=0,top_ratio=1,bottom_ratio=1,scale=10,
                   arc_angle=0,orient_follow=1,n=W.n(),pts=npts)

figure(S,S.fpolars(),'twilight')

###

e=0.0
R=40
ppl=1000
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e,pen_offset=pi/4),wheel=Wheel(a/3,a/2),ppl=ppl,loops=1,inside=True).rotate(pi/5)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,1))

npts=200
pts_fade = array([ 2,3,5,8,13,21,34,55,89,144,144,89,55,34,21,13,8,5,3,2 ])
S=crosses_on_frame(W,asym=0,top_ratio=1,bottom_ratio=1,scale=10,
                   arc_angle=pi/3,orient_follow=1,pts=pts_fade,n=W.n()-1)

figure(S,'time','cmap2')

###

e=0.0
R=40
ppl=600
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e,pen_offset=pi/4),wheel=Wheel(a/3,a/2),ppl=ppl,loops=1,inside=True).rotate(pi/5)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,1))

S = SpiroData()

nk=3
gs=3
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=200*def_factor
pts_fade = linspace(npts,npts//6,n,dtype=int)

for k in range(nk):
    
    first = k*ns + ns//3
    
    scale = 10

    asym=array( [ 0.3*cos(2*pi*j/n) for j in range(n) ])
    tr = 1
    br = 1
    
    ao = 0
    
    nn = n-1
    of = 1
    aa = pi/6

    S.add(crosses_on_frame(W,asym=asym,top_ratio=tr,bottom_ratio=br,scale=scale,arc_angle=aa,
                           first=first,orient_follow=of,orient=ao,pts=pts_fade,n=nn))
    
figure(S,S.fradii(),'autumn_r')

###

e=0.0
R=40
ppl=3000
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e,pen_offset=pi/4),wheel=Wheel(a/3,a/2),ppl=ppl,loops=1,inside=True).rotate(pi/5)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,1))

S = SpiroData()

nk=3
gs=12
n = 150
ns = W.n()//nk 

npts=200*def_factor
pts_fade = array([ 10+npts+int(npts*cos(2*pi*j/n)) for j in range(n) ]) 

for k in range(nk):
    
    first = k*ns + ns//4
    
    scale = linspace(25,35,n)

    asym=0.0 
    tr = 1
    br = linspace(1.0,1.5,n)

    ao = linspace(0,1.5*pi,n) 
    
    nn = n-1
    of = W.n()//6
    aa = pi/2 

    S.add(crosses_on_frame(W,asym=asym,top_ratio=tr,bottom_ratio=br,scale=scale,arc_angle=aa,
                           first=first,orient_follow=of,orient=ao,pts=pts_fade,n=nn))
    
F.plot(S,color_scheme='length',cmap='turbo',alpha=0.4,dot_size=.1,no_frame=False)

figure(S,'cycles','turbo')

###

e=0.0
R=40
ppl=1000
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e,pen_offset=0),wheel=Wheel(a/4,a/5),ppl=ppl,loops=1,inside=True)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,1))

S = SpiroData()

nk=5
gs=2
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=300*def_factor
pts_fade = array([ 10+npts+int(npts*cos(pi+2*pi*j/n)) for j in range(n) ]) 

for k in range(1):
    
    first = k*ns + ns//3
    
    scale = 5

    asym=-0.3
    tr = 0.7 
    br = 1.5 

    ao = linspace(0,pi/3,n)
    
    nn = n-1
    of = W.n()//6
    aa = -pi/4 

    S.add(crosses_on_frame(W,asym=asym,top_ratio=tr,bottom_ratio=br,scale=scale,arc_angle=aa,
                           first=first,orient_follow=of,orient=ao,pts=pts_fade,n=nn))
    
figure(S,'phase','inferno')

###

e=0.0
R=40
ppl=2000
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e,pen_offset=0),wheel=Wheel(a/4,a/5),ppl=ppl,loops=1,inside=True)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,2))

S = SpiroData()

nk=5
gs=2
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=300*def_factor
pts_fade = array([ 10+npts+int(npts*cos(pi+2*pi*j/n)) for j in range(n) ]) 

for k in range(1):
    
    first = k*ns + ns//3
    
    scale = array( [ W.chord_dist(j,W.n()//3) for j in range(first,first+n) ] )

    asym=linspace(-0.3,0,n)
    tr = 0.7
    br = 1.5

    ao = linspace(0,pi/3,n)
    
    nn = n-1
    of = W.n()//6
    aa = -pi/4 

    S.add(crosses_on_frame(W,asym=asym,top_ratio=tr,bottom_ratio=br,scale=scale,arc_angle=aa,
                           first=first,orient_follow=of,orient=ao,pts=pts_fade,n=nn))
    
figure(S,'direction','pretty_blues')

###

e=0.0
R=40
ppl=2000
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e,pen_offset=0),wheel=Wheel(a/4,a/5),ppl=ppl,loops=1,inside=True)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,2))

S = SpiroData()

nk=3
gs=2
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=300*def_factor
pts_fade = array([ 4+npts+int(npts*cos(pi+2*pi*j/n)) for j in range(n) ]) 

for k in range(nk):
    
    first = k*ns + ns//6
    
    scale = array( [ 0.6*W.chord_dist(j,W.n()//2) for j in range(first,first+n) ] )

    asym=linspace(-0.3,0,n)
    tr = 1. 
    br = 1. 

    ao = linspace(0,pi/4,n)
    
    nn = n-1
    of = W.n()//6
    aa = pi/4 

    S.add(crosses_on_frame(W,asym=asym,top_ratio=tr,bottom_ratio=br,scale=scale,arc_angle=aa,
                           first=first,orient_follow=of,orient=ao,pts=pts_fade,n=nn))
    
figure(S,'time','pretty_reds')

###

T = spiro_cross(wheel=W0)

t1=0
tn=T.n()

W=T.select(slice(t1,t1+tn,20))

S = SpiroData()

nk=1
gs=0
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=200*def_factor
pts_fade = npts

for k in range(nk):
    
    first = k*ns + ns//6
    
    scale = array( [ W.chord_dist(j,5*W.n()//12) for j in range(first,first+n) ] )

    asym=0 
    tr = 1.
    br = 1.

    ao = 0 
    
    nn = n-1
    of = 0
    aa = 0

    S.add(crosses_on_frame(W,asym=asym,top_ratio=tr,bottom_ratio=br,scale=scale,arc_angle=aa,
                           first=first,orient_follow=of,orient=ao,pts=pts_fade,n=nn))
    
figure(S,'time','cmap1')

###

T = spiro_cross(wheel=Wheel(1,0.5),inside=True) 

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,20))

S = SpiroData()

nk=6
gs=3
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=300*def_factor
pts_fade = linspace(npts,npts//12,n,dtype=int)

seed = 957
np.random.seed(seed)

for k in range(nk):
    
    first = k*ns + ns//6
    
    scale = array( [ W.chord_dist(j,W.n()//12) for j in range(first,first+n) ] )

    asym=0 
    tr = 1.
    br = 1.

    ao = np.random.standard_normal()*pi/72
    
    nn = n-1
    of = 0 
    aa = 0 

    S.add(crosses_on_frame(W,asym=asym,top_ratio=tr,bottom_ratio=br,scale=scale,arc_angle=aa,
                           first=first,orient_follow=of,orient=ao,pts=pts_fade,n=nn))

figure(S,'time','gist_heat_r')

###

T = spiro_cross(wheel=Wheel(2,3),inside=True)  # pretty frame

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,20))

S = SpiroData()

nk=4
gs=4
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=150*def_factor
pts_fade = linspace(npts,npts//12,n,dtype=int)

for k in range(nk):
    
    first = k*ns
    
    scale = array( [ 1.5*W.chord_dist(j,W.n()//12) for j in range(first,first+n) ] )

    asym=0 
    tr = 1.
    br = 1.

    ao = pi/4 
    
    nn = n-1
    of = W.n()//12
    aa = pi/4 

    S.add(crosses_on_frame(W,asym=asym,top_ratio=tr,bottom_ratio=br,scale=scale,arc_angle=aa,
                           first=first,orient_follow=of,orient=ao,pts=pts_fade,n=nn))

figure(S,S.fradii(),'hot_r')

###

T = spiro_cross(wheel=Wheel(2,3),inside=True)  # pretty frame

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,8))

S = SpiroData()

nk=4
gs=8
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=150*def_factor
pts_fade = linspace(npts,npts//12,n,dtype=int)

np.random.seed(116)

for k in range(nk):
    
    first = k*ns + np.random.randint(ns//2)
    
    scale = array( [ min(10,max(0.5*W.chord_dist(j,W.n()//3),3)) for j in range(first,first+n) ] )

    asym=0 
    tr = 1.
    br = 1.

    ao = pi/4 
    
    nn = n-1
    of = W.n()//3
    aa = pi/4 

    S.add(crosses_on_frame(W,asym=asym,top_ratio=tr,bottom_ratio=br,scale=scale,arc_angle=aa,
                           first=first,orient_follow=of,orient=ao,pts=pts_fade,n=nn))

figure(S,S.fradii(),'pale_pink')

###

T = heart(wheel=Wheel(1,0),inside=False) 

ppl=500
id = linspace(0,T.max_path(),ppl)
W = T.resample(id)

S = SpiroData()

nk=1
gs=0
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=150*def_factor
pts_fade = array([ npts//5+npts-int(npts*sin(2*pi*j/n)) for j in range(n) ]) 

for k in range(nk):
    
    first = k*ns
    
    scale = 5 
    asym=0 
    tr = 1.
    br = 1.

    ao = pi/4
    
    nn = n-1
    of = W.n()//3
    aa = pi/3 

    
    S.add(crosses_on_frame(W,asym=asym,top_ratio=tr,bottom_ratio=br,scale=scale,arc_angle=aa,
                           first=first,orient_follow=of,orient=ao,pts=pts_fade,n=nn))

figure(S,S.fradii(),'jet')
