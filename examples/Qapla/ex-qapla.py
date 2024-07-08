import sys
sys.path.append('../..')
import argparse

from SpiroData import *
from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_arcs import *
from spiro_string import *
from spiro_frame import *
from polygon import *
from Ring import *

parser = argparse.ArgumentParser(description="Klingon Symbol Examples")
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

F._figname='Qapla-'

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

e=0.0
R=4
ppl=900
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/3,a/3),ppl=ppl,loops=1,inside=True).rotate(pi/7)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,2))
S=SpiroData()

nk=3
gs=2
n = W.n()//(nk+gs)
ns = W.n()//nk 

def_factor=1
npts = def_factor*200

for k in range(nk):
    first = k*ns
    asym=0.1
    scale = 4
    pts= npts
    ao = linspace(0,-pi,n)
    shift = 0.0 
    aa = [pi/3,-pi/3]
    
    S.add(on_frame(W,scale=scale,oangle=3,first=first,fh=shift,fb=shift,n=n,
                   asym=asym,orient_follow=1,orient=ao,polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))

figure(S,'time','hot')

##

S=SpiroData()

nk=12
gs=6
n = W.n()//(nk+gs)
ns = W.n()//nk 

def_factor=1
npts = def_factor*200 

aaj = linspace(-pi/3,-pi/3,n)
aa = array([])
for j in range(n):
    aa = np.append(aa,[-aaj[j],aaj[j]])
    
for k in range(nk):
    first = k*ns 
    asym= 0.1
    scale = 4 
    pts= npts 

    ao = 0
    shift = 0.0 
    
    S.add(on_frame(W,scale=scale,oangle=3,first=first,fh=shift,fb=shift,n=n,
                   asym=asym,orient_follow=W.n()//3,orient=ao,polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))

figure(S,'time','pretty_reds')

###

e=0.0
R=4
ppl=900
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/6,a/6),ppl=ppl,loops=1,inside=True).rotate(pi/7)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,2))

S=SpiroData()

nk=6
gs=2
n = W.n()//(nk+gs)
ns = W.n()//nk 

def_factor=1
npts = def_factor*200

aaj = linspace(-pi/3,-pi/3,n)
aa = array([])
for j in range(n):
    for k in range(3):
        aa = np.append(aa,[-aaj[j],aaj[j]])
    
for k in range(nk):
    first = k*ns
    asym= 0.1
    scale = 5 
    pts= npts 
    ao = linspace(-pi/6,pi/6,n)
    shift = 0.0 
    
    S.add(on_frame(W,scale=scale,oangle=3,first=first,fh=shift,fb=shift,n=n,
                   asym=asym,orient_follow=0,orient=ao,polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))

figure(S,'time','inferno')

###

e=0.0
R=4
ppl=900
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/6,a/2),ppl=ppl,loops=1,inside=True).rotate(pi/7)

t1=0
tn=T.n()

W=T.select(slice(t1,t1+tn,1))

S=SpiroData()

nk=12
gs=6
n = W.n()//(nk+gs)
ns = W.n()//nk 

def_factor=1
npts = def_factor*200

aaj = linspace(pi/3,pi/3,n)
aa = array([])
for j in range(n):
    for k in range(3):
        aa = np.append(aa,[-aaj[j],aaj[j]])
        aa = np.append(aa,[-aaj[j],aaj[j]])
        aa = np.append(aa,[-aaj[j],aaj[j]])
    
for k in range(nk):
    first = k*ns  + W.n()//12
    asym= 0.1
    scale = 5 
    pts= linspace(npts//5,npts,6*n,dtype=int) 
    ao = pi/3 
    shift = 0.0
    
    S.add(on_frame(W,scale=scale,oangle=3,first=first,fh=shift,fb=shift,n=n,
                   asym=asym,orient_follow=1,orient=ao,polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))

figure(S,'direction','cmap2')

###

e=0.0
R=4
ppl=900
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/3,a/4),ppl=ppl,loops=1,inside=True).rotate(pi/5)

t1=0
tn=T.n()

W=T.select(slice(t1,t1+tn,1))

S=SpiroData()

nk=9
gs=1
n = W.n()//(nk+gs)
ns = W.n()//nk 

def_factor=1
npts = def_factor*200

aaj = linspace(pi/3,pi/3,n)
aa = array([])
for j in range(n):
    for k in range(3):
        aa = np.append(aa,[-aaj[j],aaj[j]])
        aa = np.append(aa,[-aaj[j],aaj[j]])
        aa = np.append(aa,[-aaj[j],aaj[j]])
    
for k in range(nk):
    first = k*ns
    asym= 0.1
    scale = 3 
    pts= linspace(npts//5,npts,6*n,dtype=int) 
    ao = linspace(-pi/4,pi/4,n)
    shift = 0.0
    
    S.add(on_frame(W,scale=scale,oangle=3,first=first,fh=shift,fb=shift,n=n,
                   asym=asym,orient_follow=W.n()//3,orient=ao,polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))
    
figure(S,'cycles','Oranges')

###

e=0.2
R=4
ppl=900
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e,pen_offset=pi/4),wheel=Wheel(a/3.5,a/4),ppl=ppl,loops=2,inside=True).rotate(pi/3)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,3))

S=SpiroData()

nk=15
gs=9
n = W.n()//(nk+gs)
ns = W.n()//nk 

def_factor=1
npts = def_factor*200 


aaj = linspace(-pi/3,pi/3,n)
aa = array([])
for j in range(n):
    for k in range(3):
        aa = np.append(aa,[-aaj[j],aaj[j]])
        aa = np.append(aa,[-aaj[j],aaj[j]])
        aa = np.append(aa,[-aaj[j],aaj[j]])
    
for k in range(nk):
    first = k*ns
    asym= 0.1
    scale = 2 
    pts= npts 
    ao = linspace(0,pi/10,n) 
    shift = 0.0 
    
    S.add(on_frame(W,scale=scale,oangle=3,first=first,fh=shift,fb=shift,n=n,
                   asym=asym,orient_follow=W.n()//5,orient=ao,polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))
    
figure(S,'time','cmap1')

###

e=0.2
R=4
ppl=900
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e,pen_offset=pi/4),wheel=Wheel(a/6,a/20),ppl=ppl,loops=1,inside=False).rotate(pi/3)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,3))

S=SpiroData()

nk=3
gs=1
n = W.n()//(nk+gs)
ns = W.n()//nk 

def_factor=1
npts = def_factor*200 

for k in range(nk):
    first = k*ns 
    asym= [ 0.1+0.2*(pi+W.direction(j))/(2*pi) for j in range(first,first+n) ]
    scale = 2.5 
    pts= npts
    ao = linspace(0,2*pi/nk,n) 
    shift = 0.0
    aa = [-pi/3,pi/3]
    
    S.add(on_frame(W,scale=scale,oangle=3,first=first,fh=shift,fb=shift,n=n,
                   asym=asym,orient_follow=0,orient=ao,polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))
    
figure(S,'cycles','emerald_woman')

###

e=0.2
R=4
ppl=900
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e,pen_offset=pi/4),wheel=Wheel(a/6,a/20),ppl=ppl,loops=1,inside=True).rotate(pi/3)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,3))

S=SpiroData()

nk=12
gs=6
n = W.n()//(nk+gs)
ns = W.n()//nk 

def_factor=1
npts = def_factor*200

for k in range(nk):
    first = k*ns
    asym= [ 0.1+0.2*(pi+W.direction(j))/(2*pi) for j in range(first,first+n) ]
    scale = 2.5 
    pts= npts 
    ao = pi/3 
    shift = 0.0
    aa = [-pi/3,pi/3] 
    
    S.add(on_frame(W,scale=scale,oangle=3,first=first,fh=shift,fb=shift,n=n,
                   asym=asym,orient_follow=1,orient=ao,polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))
    
figure(S,'spacing','turbo')

###

T = cIc(Ring(30),wheel=Wheel(6,17),loops=1,inside=False,ppl=3000).subsample(1)
ppl=T.n()

seed=492
np.random.seed(seed)

tn=ppl//12
t1=np.random.randint(0,ppl-tn-2)
W=T.select(slice(t1,t1+tn,1))

S=SpiroData()

tnd = [ W.direction(j)+pi for j in range(W.n()) ]
flat_scale = max(tnd)-min(tnd)
flat=[ pi/3 * (tnd[j]-min(tnd))/flat_scale for j in range(len(tnd)) ]
aa = array([])
for j in range(len(flat)):
    for l in range(3):
        aa = np.append(aa,[-flat[j],flat[j]])
        aa = np.append(aa,[-flat[j],flat[j]])
        aa = np.append(aa,[-flat[j],flat[j]])
scale = W.radii()/2 
ao=[ 50*W.neighbor_dist(j) for j in range(W.n()) ]
S = on_frame(W,scale=scale,oangle=3,asym=0.1,orient_follow=0,orient=ao,n=W.n()-1,
             polyfunc=nstar_coords,arc_angle=aa,pts=200)

figure(S,'direction','pretty_blues')

###

T = cIc(Ring(30),wheel=Wheel(6,17),loops=1,inside=True,ppl=3000).subsample(1)
ppl=T.n()

seed=218
np.random.seed(seed)

tn=ppl//12
t1=np.random.randint(0,ppl-tn-2)
W=T.select(slice(t1,t1+tn,1))

S=SpiroData()

tnd = [ W.direction(j)+pi for j in range(W.n()) ]
flat_scale = max(tnd)-min(tnd)
flat=[ pi/3 * (tnd[j]-min(tnd))/flat_scale for j in range(len(tnd)) ]
aa = array([])
for j in range(len(flat)):
    for l in range(3):
        aa = np.append(aa,[-flat[j],flat[j]])
        aa = np.append(aa,[-flat[j],flat[j]])
        aa = np.append(aa,[-flat[j],flat[j]])
scale = 5*sqrt(W.radii())
ao=[ pi/4 + 30*W.neighbor_dist(j) for j in range(W.n()) ]
S = on_frame(W,scale=scale,oangle=3,asym=0.1,orient_follow=1,orient=ao,n=W.n()-1,
             polyfunc=nstar_coords,arc_angle=aa,pts=200)

figure(S,'direction','pale_pink')
