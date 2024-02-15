import sys
sys.path.append('../..')
import argparse

from SpiroData import *
from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_ellipses import *
from spiro_arcs import *
from spiro_string import *
from spiro_frame import *
from polygon import *
from Ring import *

parser = argparse.ArgumentParser(description="Parallelogram Examples")
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

F._figname='Pentastra-'

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
ppl=1200
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/2.5,a/2),ppl=ppl,loops=2,inside=True).rotate(pi/4)

W=T.subsample(6)

aa=0

S=SpiroData()

nk=5
gs=5
n = W.n()//(nk+gs)
ns = W.n()//nk 
scale = linspace(4,5,n)
ao = linspace(pi/5,pi/3,n)
for k in range(nk):
    first = k*ns +W.n()//5
    pts=200*def_factor
    S.add(on_frame(W,scale=scale,oangle=5,first=first,fh=0,fb=0,n=n,
                   asym=0.5,orient_follow=0,orient=ao, polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))

figure(S,'spacing','Blues')

###

e=0.0
R=4
ppl=1200
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/2.5,a/2),ppl=ppl,loops=2,inside=True).rotate(pi/4)

W=T.subsample(6)

aa=pi/2

S=SpiroData()

nk=5
gs=10
n = W.n()//(nk+gs)
ns = W.n()//nk # + W.n()//4
scale = linspace(2,5,n)
ao = linspace(pi/5,pi/3,n)
for k in range(nk):
    first = k*ns +W.n()//5
    pts=array([ 102 + int(100*sin(2*pi*j/(10*n))) for j in range(10*n) ])*def_factor
    S.add(on_frame(W,scale=scale,oangle=5,first=first,fh=0,fb=0,n=n,
                   asym=0.5,orient_follow=0,orient=ao, polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))

figure(S,'time','pretty_reds')

###

e=0.0
R=4
ppl=1200
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/1.5,a/2),ppl=ppl,loops=2,inside=True).rotate(pi/4)

W=T.subsample(6)

aa=-pi/4

S=SpiroData()

nk=6
gs=5
n = W.n()//(nk+gs)
ns = W.n()//nk 
scale = linspace(5,5,n)
ao = linspace(pi/6,pi/3,n)
for k in range(nk):
    first = k*ns +W.n()//5
    pts=array([ 152 + int(100*sin(2*pi*j/(10*n))) for j in range(10*n) ])*def_factor
    S.add(on_frame(W,scale=scale,oangle=5,first=first,fh=0,fb=0,n=n-1,
                   asym=1.0,orient_follow=0,orient=ao, polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))

figure(S,'cycles','turbo')

figure(S,'segment','hsv')  # cover for project

###

e=0.0
R=4
ppl=1200
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/1.5,a/2),ppl=ppl,loops=2,inside=False).rotate(pi/4)
W=T.subsample(3)

npts=200

aa=-pi/4

S=SpiroData()

nk=3
gs=6
n = W.n()//(nk+gs)
ns = W.n()//nk
scale = linspace(4,8,n)
ao = linspace(pi/6,pi/3,n)
for k in range(nk):
    first = k*ns+W.n()//5
    pts=npts*def_factor
    S.add(on_frame(W,scale=scale,oangle=5,first=first,fh=0,fb=0,n=n-1,
                   asym=0.4,orient_follow=0,orient=ao, polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))

figure(S,'t-waves','jet')

###

e=0.0
R=4
ppl=1200
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/5,a/5),ppl=ppl,loops=1,inside=True).rotate(pi/4)

W=T.subsample(3)

aa=[0,0]

S=SpiroData()

nk=1
gs=0
n = W.n()//(nk+gs)
ns = W.n()//nk # + W.n()//4
scale = linspace(5,5,n)
ao = 0 # linspace(pi/6,pi/3,n)
for k in range(nk):
    first = k*ns+W.n()//5
    pts=array([ 55 + int(50*sin(2*pi*j/(10*n))) for j in range(10*n) ])*def_factor
    S.add(on_frame(W,scale=scale,oangle=5,first=first,fh=0,fb=0,n=n,
                   asym=0.5,orient_follow=W.n()//(W.n()-1),orient=ao, polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))

figure(S,'segment','Oranges')

###

e=0.0
R=4
ppl=1200
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/5,a/5),ppl=ppl,loops=1,inside=True).rotate(pi/4)

W=T.subsample(3)

aa=[pi,pi]

S=SpiroData()

nk=5
gs=10
n = W.n()//(nk+gs)
ns = W.n()//nk 
scale = 4
ao = 0 
for k in range(nk):
    first = k*ns 
    pts=array([ 150 + int(50*sin(2*pi*j/(10*n))) for j in range(10*n) ])*def_factor
    S.add(on_frame(W,scale=scale,oangle=5,first=first,fh=0,fb=0,n=n,
                   asym=0.5,orient_follow=W.n()//(W.n()-1),orient=ao, polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))

figure(S,'segment','OrRd')


###

e=0.0
R=4
ppl=1200
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/5,a/3),ppl=ppl,loops=1,inside=False).rotate(pi/4)

W=T.subsample(2)

aa=[-pi,-pi]

S=SpiroData()

nk=15
gs=25
n = W.n()//(nk+gs)
ns = W.n()//nk # + W.n()//4
scale = 4 # linspace(5,5,n)
ao = 0 # linspace(pi/6,pi/3,n)
for k in range(nk):
    first = k*ns # +W.n()//5
    scale = [ 20/W.radius(j) for j in range(first,first+n) ]
    pts=array([ 150 + int(50*sin(0*pi*j/(10*n))) for j in range(10*n) ])*def_factor
    S.add(on_frame(W,scale=scale,oangle=5,first=first,fh=0,fb=0,n=n,
                   asym=0.5,orient_follow=W.n()//3,orient=ao, polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))

figure(S,'segment','hot')

##

W=T.subsample(2)

aa=[-pi,-pi]

S=SpiroData()

nk=15
gs=25
n = W.n()//(nk+gs)
ns = W.n()//nk

ao = 0
for k in range(nk):
    first = k*ns
    scale = [ 20/W.radius(j) for j in range(first,first+n) ]
    pts=array([ 150 + int(50*sin(0*pi*j/(10*n))) for j in range(10*n) ])*def_factor
    S.add(on_frame(W,scale=scale,oangle=5,first=first,fh=0,fb=0,n=n,
                   asym=0.8,orient_follow=W.n()//3,orient=ao, polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))

figure(S,'spacing','pretty_reds')


###

e=0.0
R=4
ppl=1200
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/2,a/1.5),ppl=ppl,loops=1,inside=True).rotate(pi/4)

W=T.subsample(3)

aa=[-pi/3,-pi/3]

S=SpiroData()

nk=1
gs=0
n = W.n()//(nk+gs)
ns = W.n()//nk 

ao = linspace(0,pi,n)
for k in range(nk):
    first = k*ns +W.n()//5
    scale = 10 
    pts= 100*def_factor
    S.add(on_frame(W.rotate(0*k*pi/5),scale=scale,oangle=5,first=first,fh=0,fb=0,n=n,
                   asym=0.3,orient_follow=0,orient=ao, polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))

figure(S,'cycles','Blues')

###

e=0.0
R=4
ppl=1200
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/3,a/1),ppl=ppl,loops=1,inside=True).rotate(pi/4)

W=T.subsample(2)

aa=[pi/3,pi/3]

S=SpiroData()

nk=3
gs=1
n = W.n()//(nk+gs)
ns = W.n()//nk 

ao = linspace(0,pi/2,n)
for k in range(nk):
    first = k*ns +W.n()//5
    scale = 4
    pts= 150*def_factor
    S.add(on_frame(W.rotate(0*k*pi/5),scale=scale,oangle=5,first=first,fh=0,fb=0,n=n,
                   asym=0.3,orient_follow=W.n()//3,orient=ao, polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))

figure(S,'direction','hot')

##

W=T.subsample(2)

aa=[pi/3,pi/3]

S=SpiroData()

nk=3
gs=5
n = W.n()//(nk+gs)
ns = W.n()//nk 
scale = 3
ao = linspace(0,1.5*pi,n)
for k in range(nk):
    first = k*ns +W.n()//5
    asym=linspace(0.2,1.0,n)
    scale = 4
    pts= 150 * def_factor
    S.add(on_frame(W.rotate(0*k*pi/5),scale=scale,oangle=5,first=first,fh=0,fb=0,n=n,
                   asym=asym,orient_follow=W.n()//5,orient=ao, polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))

figure(S,'direction','pretty_reds')

###

e=0.0
R=4
ppl=2400
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/5,a/1),ppl=ppl,loops=1,inside=False).rotate(pi/4)

W=T.subsample(1)

aa=[pi/3,pi/3]

S=SpiroData()

nk=5
gs=25
n = W.n()//(nk+gs)
ns = W.n()//nk 
ao = linspace(0,-0.8*pi,n)

for k in range(nk):
    first = k*ns +W.n()//5
    asym=linspace(0.2,0.8,n)
    scale = 3
    pts= 150*def_factor
    S.add(on_frame(W.rotate(0*k*pi/5),scale=scale,oangle=5,first=first,fh=0,fb=0,n=n,
                   asym=asym,orient_follow=W.n()//5,orient=ao, polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))

figure(S,'cycles','gist_heat') # confirm color-scheme

##

W=T.subsample(1)

aa=[pi/3,pi/3]

S=SpiroData()

nk=5
gs=35
n = W.n()//(nk+gs)
ns = W.n()//nk 
ao = linspace(0,-0.5*pi,n)

for k in range(nk):
    first = k*ns +W.n()//15
    asym=linspace(0.2,0.8,n)
    scale = 3
    pts= 150*def_factor
    S.add(on_frame(W.rotate(0*k*pi/5),scale=scale,oangle=5,first=first,fh=0,fb=0,n=n,
                   asym=asym,orient_follow=W.n()//15,orient=ao, polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))

figure(S,'cycles','OrRd')

##

W=T.subsample(1)

aa=[pi/3,pi/3]

S=SpiroData()

nk=5
gs=35
n = W.n()//(nk+gs)
ns = W.n()//nk 
ao = linspace(0,-0.5*pi,n)

for k in range(nk):
    first = k*ns +W.n()//15
    asym=linspace(0.2,0.8,n)
    scale =  [ 5/W.radius(j) for j in range(first,first+n) ]
    pts= 150*def_factor
    S.add(on_frame(W.rotate(0*k*pi/5),scale=scale,oangle=5,first=first,fh=0,fb=0,n=n,
                   asym=asym,orient_follow=W.n()//15,orient=ao, polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))

figure(S,'segment','gist_heat')

##

t1=T.n()//4
tn=T.n()//5
W=T.select(slice(t1,t1+tn,1))

aa=[-pi/4,-pi/4]

S=SpiroData()

nk=2
gs=1
n = W.n()//(nk+gs)
ns = W.n()//nk 
ao = [ pi/6*sin(2*pi*j/n) for j in range(n) ]
pts = def_factor*array([ 105 + int(100*cos(pi*j/n)) for j in range(n) ])
for k in range(nk):
    first = k*ns 
    asym=0.4 
    scale =  5 
    S.add(on_frame(W.rotate(0*k*pi/5),scale=scale,oangle=5,first=first,fh=0,fb=0,n=n,
                   asym=asym,orient_follow=0,orient=ao, polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))

figure(S,'time','emerald_woman')

##

t1=T.n()//4
tn=T.n()//5
W=T.select(slice(t1,t1+tn,1))

aa=linspace(pi/2,-pi/2,20)

S=SpiroData()

nk=2
gs=1
n = W.n()//(nk+gs)
ns = W.n()//nk 
ao = 0 
pts = def_factor*array([ 105 + int(100*cos(pi*j/n)) for j in range(n) ])
for k in range(nk):
    first = k*ns 
    asym=0.4 
    scale =  5 
    S.add(on_frame(W.rotate(0*k*pi/5),scale=scale,oangle=5,first=first,fh=0,fb=0,n=n,
                   asym=asym,orient_follow=1,orient=ao, polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))

figure(S,'length','turbo')
