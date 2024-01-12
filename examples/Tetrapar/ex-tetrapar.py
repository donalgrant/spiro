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
from spiro_triangles import *
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

F._figname='Tetrapar-'

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
ppl=400

a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/3,a/3),ppl=ppl,loops=1,inside=True).rotate(pi/4)

W=T.subsample(5)
scale=5
ao=0
asym=0
aa=pi/3
npts=300
pts=npts*def_factor

fb=[0,0,1,-1]
fh=[1,-1,0,0]

S=SpiroData()
for i in range(len(fb)):
    S.add(pars_on_frame(W,scale=scale,oangle=pi/2,n=W.n(),asym=asym,orient_follow=0,
                    fb=fb[i],fh=fh[i],orient=ao,arc_angle=aa,pts=pts,object=arange(len(fb))))

figure(S,'cycles','turbo')

###

e=0.0
R=4
ppl=400
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/4,a/4),ppl=ppl,loops=1,inside=True).rotate(pi/4)

W=T.subsample(1)
scale=3
ao=0
asym=0

npts=200
pts=npts*def_factor

fb=[0,0,1,-1]
fh=[1,-1,0,0]
aa=[pi/2,pi/2,pi/2,pi/2]

S=SpiroData()

nk=4
gs=4
n = W.n()//(nk+gs)
ns = W.n()//nk
for k in range(nk):
    first = k*ns+W.n()//4
    for i in range(len(fb)):
        S.add(pars_on_frame(W,scale=scale,oangle=pi/2,first=first,n=16,asym=asym,orient_follow=4,
                            fb=fb[i],fh=fh[i],orient=ao,arc_angle=aa[i],pts=pts,object=k))

figure(S,'object','emerald_woman')

###

e=0.0
R=4
ppl=1200
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/8,a/4),ppl=ppl,loops=1,inside=True).rotate(pi/4)

W=T.subsample(1)
scale=3
ao=0
asym=0
npts=200
pts=npts*def_factor

fb=[0,0,1,-1]
fh=[1,-1,0,0]
aa=[pi/2,pi/2,pi/2,pi/2]

S=SpiroData()

nk=4
gs=4
n = W.n()//(nk+gs)
ns = W.n()//nk
for k in range(nk):
    first = k*ns+W.n()//4
    for i in range(len(fb)):
        S.add(pars_on_frame(W,scale=scale,oangle=pi/2,first=first,n=16,asym=asym,orient_follow=4,
                            fb=fb[i],fh=fh[i],orient=ao,arc_angle=aa[i],pts=pts,object=k))

figure(S,'cycles','Reds')

###

e=0.0
R=4
ppl=1200
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/8,a/8),ppl=ppl,loops=1,inside=True).rotate(pi/4)

W=T.subsample(1)
scale=8
ao=0
asym=0

npts=200
pts=npts*def_factor

fb=[0,0,1,-1]
fh=[1,-1,0,0]
aa=[pi/4,pi/4,pi/4,pi/4]

S=SpiroData()

nk=8
gs=64
n = W.n()//(nk+gs)
ns = W.n()//nk
for k in range(nk):
    first = k*ns+W.n()//4
    for i in range(len(fb)):
        S.add(pars_on_frame(W,scale=scale,oangle=pi/2,first=first,n=n,asym=asym,orient_follow=4,
                            fb=fb[i],fh=fh[i],orient=ao,arc_angle=aa[i],pts=pts,object=k))

figure(S,'object','turbo')

###

e=0.0
R=4
ppl=1200
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/8,a/4),ppl=ppl,loops=1,inside=False).rotate(0)

W=T.subsample(1)
scale=8
ao=0
asym=0

npts=200
pts=npts*def_factor

fb=[0,0,1,-1]
fh=[1,-1,0,0]
aa=[pi/4,pi/4,pi/4,pi/4]

S=SpiroData()

nk=6
gs=50
n = W.n()//(nk+gs)
ns = W.n()//nk
for k in range(nk):
    first = k*ns+W.n()//3
    for i in range(len(fb)):
        S.add(pars_on_frame(W,scale=scale,oangle=pi/2,first=first,n=n,asym=asym,orient_follow=4,
                            fb=fb[i],fh=fh[i],orient=ao,arc_angle=aa[i],pts=pts,object=k))

figure(S,'cycles','ocean')

###

e=0.0
R=4
ppl=1200
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/3,a/2),ppl=ppl,loops=1,inside=True).rotate(0)

W=T.subsample(2)
scale=4
ao=0
asym=0

npts=200
pts=npts*def_factor

fb=[0,0,1,-1]
fh=[1,-1,0,0]
aa=[pi/4,pi/4,pi/4,pi/4]

S=SpiroData()

nk=3
gs=15
n = W.n()//(nk+gs)
ns = W.n()//nk
for k in range(nk):
    first = k*ns # +W.n()//3
    for i in range(len(fb)):
        S.add(pars_on_frame(W,scale=scale,oangle=pi/2,first=first,n=n,asym=asym,orient_follow=4,
                            fb=fb[i],fh=fh[i],orient=ao,arc_angle=aa[i],pts=pts,object=k))

figure(S,'time','OrRd')

###

e=0.0
R=4
ppl=1200
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/3,a/2),ppl=ppl,loops=1,inside=True).rotate(0)

W=T.subsample(2)
scale=4
ao=pi/4
asym=0

npts=200
pts=npts*def_factor

fb=[0,0,1,-1]
fh=[1,-1,0,0]
aa=[pi/4,pi/4,pi/4,pi/4]

S=SpiroData()

nk=3
gs=15
n = W.n()//(nk+gs)
ns = W.n()//nk
for k in range(nk):
    first = k*ns # +W.n()//3
    for i in range(len(fb)):
        S.add(pars_on_frame(W,scale=scale,oangle=pi/2,first=first,n=n,asym=asym,orient_follow=-1,
                            fb=fb[i],fh=fh[i],orient=ao,arc_angle=aa[i],pts=pts,object=k))

figure(S,'cycles','Oranges')

###

e=0.0
R=4
ppl=1200
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/2.5,a/2),ppl=ppl,loops=2,inside=True).rotate(pi/4)

W=T.subsample(6)
scale=2

asym=0

npts=200
pts=npts*def_factor

fb=[0,0,1,-1]
fh=[1,-1,0,0]
f=1.75
aa=[pi/f,pi/f,pi/f,pi/f]

S=SpiroData()

nk=5
gs=5
n = W.n()//(nk+gs)
ns = W.n()//nk # + W.n()//4
ao = linspace(0,pi/4,n)
for k in range(nk):
    first = k*ns # +W.n()//3
    pts=np.geomspace(5,200,4*n,dtype=int)
    for i in range(len(fb)):
        S.add(pars_on_frame(W,scale=scale,oangle=pi/2,first=first,n=n,asym=asym,orient_follow=W.n()//15,
                            fb=fb[i],fh=fh[i],orient=ao,arc_angle=aa[i],pts=pts,object=k))

figure(S,'cycles','pale_pink')
