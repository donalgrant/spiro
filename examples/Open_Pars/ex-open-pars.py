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
ppl=1000


a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/4,a/6),ppl=ppl,loops=1,inside=True)

skip=2
n=T.n()//skip


scale=15
oa=pi/3
ao=0.0
asym=0
aa=pi/6
of=1
pts=[500,500,500,0]*def_factor
    
S=pars_on_frame(T,skip=skip,scale=scale,oangle=oa,n=n,asym=asym,orient_follow=1,orient=ao,arc_angle=aa,pts=pts)

my_cmap='gist_heat'

F.plot(S,color_scheme='cycles',cmap=my_cmap,alpha=.4,fig_dim=fd,dot_size=0.1,save=False,color_dither=0.0)

figure(S,'cycles','gist_heat')

###

e=0.5
R=7
ppl=1000

a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/3,a/6),ppl=ppl,loops=1,inside=True).rotate(pi/4)

skip=3
n=T.n()//skip

scale=5
oa=pi/3
ao=pi/4
asym=0.4
aa=pi/6
of=1
npts=500
pts=[npts,0,npts,0]*def_factor
    
S=pars_on_frame(T,skip=skip,scale=scale,oangle=oa,n=n,asym=asym,orient_follow=1,orient=ao,arc_angle=aa,pts=pts)

figure(S,'time','turbo')

##

skip=3
n=T.n()//skip

scale=5
oa=pi/3
ao=pi/4
asym=0.4
aa=pi/6
of=1
npts=500
pts=[npts,npts,npts,0]*def_factor
    
S=pars_on_frame(T,skip=skip,scale=scale,oangle=oa,n=n,asym=asym,orient_follow=100,orient=ao,arc_angle=aa,pts=pts)

figure(S,'phase','hot')

##

nr=3
skip=3
n=T.n()//skip//nr

scale=linspace(3,5,nr)
oa=pi/1.5
ao=0
asym=0
aa=[pi/6,pi/2,0,0]
npts=500
pts=[npts,npts,npts,0]*def_factor
    
S=SpiroData()
for i in range(nr):
    S.add(pars_on_frame(T,skip=skip,scale=scale[i],oangle=oa,n=n,asym=asym,orient_follow=10,
                        first=i*T.n()//nr,orient=ao,arc_angle=aa,pts=pts,object=i))

figure(S,'time','ocean')

##

nr=3
skip=3
n=T.n()//skip//nr

scale=linspace(3,5,nr)
oa=pi/1.5
ao=0
asym=0
aa=[pi/6,pi/2,0,0]
npts=400
pts=[npts,0,npts,0]*def_factor
    
S=SpiroData()
for i in range(nr):
    S.add(pars_on_frame(T,skip=skip,scale=scale[i],oangle=oa,n=n,asym=asym,orient_follow=10,
                        first=i*T.n()//nr,orient=ao,arc_angle=aa,pts=pts,object=i))

figure(S,'time','hot')

###

e=0.5
R=7
ppl=1000

a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/6,a/6),ppl=ppl,loops=1,inside=True).rotate(pi/4)

nr=3
skip=3
n=T.n()//skip//nr

scale=linspace(3,5,nr)
oa=pi/1.5
ao=0
asym=0
aa=[pi/6,pi/2,0,0]
npts=500
pts=[npts,npts,npts,0]*def_factor
    
S=SpiroData()
for i in range(nr):
    S.add(pars_on_frame(T,skip=skip,scale=scale[i],oangle=oa,n=n,asym=asym,orient_follow=10,
                        first=i*T.n()//nr,orient=ao,arc_angle=aa,pts=pts,object=i))

figure(S,'time','ocean')

##

nr=3
skip=3
n=T.n()//skip//nr

scale=linspace(3,5,nr)
oa=pi/1.5
ao=0
asym=0
aa=[pi/6,pi/2,0,0]
npts=500
pts=[npts,0,npts,0]*def_factor
    
S=SpiroData()
for i in range(nr):
    S.add(pars_on_frame(T,skip=skip,scale=scale[i],oangle=oa,n=n,asym=asym,orient_follow=10,
                        first=i*T.n()//nr,orient=ao,arc_angle=aa,pts=pts,object=i))

figure(S,'time','hot')

###

e=0.5
R=7
ppl=1000

a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/6,a/3),ppl=ppl,loops=1,inside=True).rotate(pi/4)

nr=3
skip=3
n=T.n()//skip//nr

scale=linspace(2,3,nr)
oa=pi/1.5
ao=0
asym=0.6
aa=[pi/6,pi/2,pi/6,0]
npts=500
pts=[0,npts,npts,npts]*def_factor
    
S=SpiroData()
for i in range(nr):
    S.add(pars_on_frame(T,skip=skip,scale=scale[i],oangle=oa,n=n,asym=asym,orient_follow=10,
                        first=i*T.n()//nr,orient=ao,arc_angle=aa,pts=pts,object=i))

figure(S,S.s+S.o/nr,'pale_pink')

##

nr=3
skip=4
n=T.n()//skip

scale=linspace(2,3,nr)
oa=pi/1.5
ao=0
asym=0.3
aa=[pi/6,pi/2,pi/6,0]
npts=500
pts=[0,npts,npts,npts]*def_factor
    
S=SpiroData()
for i in range(nr):
    S.add(pars_on_frame(T,skip=skip,scale=scale[i],oangle=oa,n=n,asym=asym,orient_follow=i+1,
                        fb=0.5,fh=0.5,first=0,orient=ao,arc_angle=aa,pts=pts,object=i))

figure(S,S.o+S.p,'turbo')

###

e=0.5
R=7
ppl=1000

a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/3,a/4),ppl=ppl,loops=1,inside=True).rotate(pi/4)

nr=6
skip=10
n=T.n()//skip

scale=linspace(5,6,nr)
oa=pi/1.5
ao=linspace(0,-pi/2,n)
asym=0
aa=[pi/2,pi/2,0,0]
npts=500
pts=[npts,npts,0,0]*def_factor
    
S=SpiroData()
for i in range(nr):
    S.add(pars_on_frame(T,skip=skip,scale=scale[i],oangle=oa,n=n,asym=asym,orient_follow=i+1,
                        fb=-0.5,fh=-0.5,first=i*T.n()//nr,orient=ao,arc_angle=aa,pts=pts,object=i))

figure(S,S.t % npts,'Reds')

###

e=0.0
R=7
ppl=1000

a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/2,a),ppl=ppl,loops=1,inside=True).rotate(pi/4)

nr=3
rep=20
gap=40
skip = append([gap],np.full((rep-1),nr))

ng=T.n()//skip.sum()
n = ng*rep

scale=linspace(7,9,rep)
oa=pi/3
ao=linspace(0,pi/4,rep)-pi/3
asym=-0.2
aa=[pi/2,pi/2,-pi/3,0]
npts=500
pts=[npts,npts,0,npts]*def_factor
    
S=pars_on_frame(T,skip=append(np.full((rep-1),nr),[gap]),scale=scale,
                oangle=oa,n=n,asym=asym,orient_follow=1,
                fb=0.1,fh=0.1,first=0,orient=ao,arc_angle=aa,pts=pts,object=arange(n)//len(skip))

figure(S,S.o,'Blues')

###

e=0.0
R=7
ppl=2000

a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/5,a/2),ppl=ppl,loops=1,inside=True).rotate(pi/4)

nr=1
rep=20
gap=80
skip = append([gap],np.full((rep-1),nr))

ng=T.n()//skip.sum()
n = ng*rep

scale=linspace(7,9,rep)
oa=pi/3
ao=pi/4
asym=-0.2
aa=[pi/2,pi/2,-pi/3,0]
npts=500
pts=[0,npts,npts//5,npts]*def_factor
    
S=pars_on_frame(T,skip=append(np.full((rep-1),nr),[gap]),scale=scale,
                oangle=oa,n=n,asym=asym,orient_follow=T.n()//5,
                fb=0.1,fh=0.1,first=0,orient=ao,arc_angle=aa,pts=pts,object=arange(n)//len(skip))

figure(S,'time','pale_pink')
