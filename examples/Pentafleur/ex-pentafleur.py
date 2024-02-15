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

F._figname='Pentafleur-'

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
R=7
ppl=200
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/3,a/5),ppl=ppl,loops=1,inside=True).rotate(pi/4)

n=T.n()
first=0

pts = 300
S=SpiroData()
scale=2.5
nr=5
for j in range(nr):
    S.add(pars_on_frame(T,scale=scale,oangle=pi/3,first=0,fh=0,fb=0,n=n,
                        asym=0,orient_follow=n//3,orient=linspace(0,2*pi,1),
                        arc_angle=pi/nr,pts=pts,object=0,prot=-2*j*pi/nr))

figure(S,'cycles','OrRd')

###

e=0.0
R=7
ppl=300

a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/2,a/5),ppl=ppl,loops=1,inside=True).rotate(pi/4)

nk=9
n=T.n()//(3*nk)

S=SpiroData()

nr=5

for k in range(nk):
    first=3*k*n
    oa=linspace(0,pi/6,n)+pi/2
    aa=pi/nr
    pts=200
    scale=1.5*18.0*T.neighbor_distances()
    for j in range(nr):
        S.add(pars_on_frame(T,scale=scale,oangle=pi/3,first=first,fh=0,fb=0,n=n,
                            asym=0,orient_follow=n//3,orient=oa,
                            arc_angle=aa,pts=pts,object=k,prot=-2*j*pi/nr))

cs=linspace(0,S.n(),S.n()) % (n*nr*pts*4)

figure(S,cs,'Oranges')

###

e=0.0
R=7
ppl=9*6*10
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/5,a/4),ppl=ppl,loops=1,inside=True).rotate(pi/4)
nk=5
gs=5
n=T.n()//((gs+1)*nk)
S=SpiroData()
nr=5
for k in range(nk):
    first=(gs+1)*k*n+T.n()//10
    oa=0
    aa=pi/nr
    pts=200
    scale=3
    for j in range(nr):
        S.add(pars_on_frame(T,scale=scale,oangle=pi/3,first=first,fh=0,fb=0,n=n,
                            asym=0,orient_follow=0,orient=oa,
                            arc_angle=aa,pts=pts,object=k,prot=-2*j*pi/nr))

figure(S,'segment','turbo')

###

e=0.0
R=7
ppl=9*6*10
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/10,a/10),ppl=ppl,loops=1,inside=True).rotate(pi/4)
nk=5
gs=5
n=T.n()//((gs+1)*nk)
S=SpiroData()
nr=5
for k in range(nk):
    first=(gs+1)*k*n+T.n()//10
    oa=0
    aa=pi/nr
    pts=200
    scale=3
    for j in range(nr):
        S.add(pars_on_frame(T,scale=scale,oangle=pi/3,first=first,fh=0,fb=0,n=n,
                            asym=0,orient_follow=0,orient=oa,
                            arc_angle=aa,pts=pts,object=k,prot=-2*j*pi/nr))

figure(S,'segment','Wistia')

##

nk=10
gs=1
n=T.n()//((gs+1)*nk)

S=SpiroData()

nr=5

for k in range(nk):
    first=(gs+1)*k*n+T.n()//10
    oa=0 
    aa=pi/nr
    pts=200
    scale=3 
    for j in range(nr):
        S.add(pars_on_frame(T,scale=scale,oangle=pi/3,first=first,fh=0,fb=0,n=n,
                            asym=0,orient_follow=0,orient=oa,
                            arc_angle=aa,pts=pts,object=k,prot=-2*j*pi/nr))

figure(S,'segment','cmap2')

###

e=0.0
R=7
ppl=9*6*10

a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/10,a/3),ppl=ppl,loops=1,inside=False).rotate(pi/4)

nk=5
gs=3
n=T.n()//((gs+1)*nk)

S=SpiroData()

nr=5

for k in range(nk):
    first=(gs+1)*k*n+T.n()//10
    oa=0
    aa=pi/nr
    pts=200
    scale=2 
    for j in range(nr):
        S.add(pars_on_frame(T,scale=scale,oangle=pi/3,first=first,fh=0,fb=0,n=n,
                            asym=0,orient_follow=0,orient=oa,
                            arc_angle=aa,pts=pts,object=k,prot=-2*j*pi/nr))

figure(S,'time','pretty_blues')

###

e=0.0
R=7
ppl=9*6*10

a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/3,a),ppl=ppl,loops=1,inside=False).rotate(pi/4)

nk=2
gs=0
n=T.n()//((gs+1)*nk)

S=SpiroData()

nr=5

for k in range(nk):
    first=(gs+1)*k*n
    oa=0
    aa=pi/nr
    pts=100
    scale=3
    for j in range(nr):
        S.add(pars_on_frame(T,scale=scale,oangle=pi/4,first=first,fh=0,fb=0,n=n-1,
                            asym=0,orient_follow=1,orient=oa,
                            arc_angle=aa,pts=pts,object=k,prot=-2*j*pi/nr))

figure(S,'segment','Reds')

###

e=0.0
R=7
ppl=9*7*10

a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/7,a/1.3),ppl=ppl,loops=1,inside=True).rotate(pi/4)

nk=7
gs=2
n=T.n()//((gs+1)*nk)

S=SpiroData()

nr=5

for k in range(nk):
    first=(gs+1)*k*n
    oa=0
    aa=pi/2
    pts=100
    scale=3
    for j in range(nr):
        S.add(pars_on_frame(T,scale=scale,oangle=pi/3,first=first,fh=0,fb=0,n=n-1,
                            asym=0,orient_follow=-T.n()//3,orient=oa,
                            arc_angle=aa,pts=pts,object=k,prot=-2*j*pi/nr))

figure(S,'segment','copper')

###

e=0.7
R=7
ppl=9*7*10

a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/5,a/1.3),ppl=ppl,loops=1,inside=False).rotate(pi/4)

nk=5
gs=4
n=T.n()//((gs+1)*nk)

S=SpiroData()

nr=5

for k in range(nk):
    first=(gs+1)*k*n+T.n()//12
    oa=0
    aa=[pi/2,0,pi/2,0]
    scale=1.
    for j in range(nr):
        pts=np.geomspace(2,200,4*n,dtype=int)
        S.add(pars_on_frame(T,scale=scale,oangle=pi/3,first=first,fh=0,fb=0,n=n-1,
                            asym=0,orient_follow=1,orient=oa,
                            arc_angle=aa,pts=pts,object=k,prot=-2*j*pi/nr))

figure(S,'cycles','hot')

###  This figure looks great in just about any color map, in cycles, object, and time color-schemes

e=0.7
R=7
ppl=9*15*10

a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/5,a/1.3),ppl=ppl,loops=1,inside=False).rotate(pi/4)

nk=5
gs=4
n=T.n()//((gs+1)*nk)

S=SpiroData()

nr=5

for k in range(nk):
    first=(gs+1)*k*n-T.n()//8
    oa=0 # linspace(0,pi/6,n)
    aa=[pi/2,0,pi/2,0]
    scale=2. # 18.0*T.neighbor_distances()
    for j in range(nr):
        pts = [52 + int(50 * sin(2*pi*i/(4*n))) for i in range(4*n)]
        S.add(pars_on_frame(T,scale=scale,oangle=pi/3,first=first,fh=0,fb=0,n=n-1,
                            asym=0,orient_follow=1,orient=oa,
                            arc_angle=aa,pts=pts,object=k,prot=-2*j*pi/nr))

figure(S,'time','autumn')
