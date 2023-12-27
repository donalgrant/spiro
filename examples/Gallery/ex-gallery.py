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

def figure(S,cs,cmap,alpha=0.4,dot_size=0.1,filename=None,limits=None,color_dither=0.0,no_frame=True):
    if hd:
        if not hasattr(figure,"data_set"):  figure.data_set=0
        S.save(f'figure-{figure.data_set}.pickle')
        figure.data_set+=1

    if filename is None:
        F.plot(S,color_scheme=cs,cmap=cmap,alpha=alpha,fig_dim=fd,dot_size=dot_size,save=save,
               limits=limits,color_dither=0.0,no_frame=no_frame)
    else:
        F.plot(S,color_scheme=cs,cmap=cmap,alpha=alpha,fig_dim=fd,dot_size=dot_size,
               save=save,filename=filename,limits=limits,color_dither=0.0,no_frame=no_frame)

###

e=0.7
R=7
ppl=1000
a=circum(R,semi_minor(R,e))/(2*pi)
T1 = cIe(Ellipse(R,e),wheel=Wheel(a/4+0.001,a/5),ppl=ppl,loops=30,inside=True).rotate(pi/4).subsample(51)

arc_angle_t=[pi/6,pi/8,pi/6]
pts = [500,0,500]

S = triangles_on_frame(T1,scale=3,oangle=pi/4,pts=pts*def_factor,
                       asym=0.8,orient_follow=1,orient=pi/4,
                       arc_angle=arc_angle_t)

figure(S,'cycles','pretty_blues')

###

S = SpiroData()
e=0.0
R=7
ppl=1000
a=circum(R,semi_minor(R,e))/(2*pi)
T1 = cIe(Ellipse(R,e),wheel=Wheel(a/6,a/5),ppl=ppl,loops=1,inside=True).rotate(pi/4)

pts = [500,500,0]

S = triangles_on_frame(T1,scale=3,oangle=pi/3,pts=pts*def_factor,orient_follow=1)

figure(S,'cycles','hot',limits=[-5,0,4,9])

###

e=0.0
R=7
ppl=1000

a=circum(R,semi_minor(R,e))/(2*pi)
T1 = cIe(Ellipse(R,e),wheel=Wheel(a/4,a/6),ppl=ppl,loops=1,inside=True)


skip=10
n=T1.n()//skip

ao = linspace(0,pi/9,n)

pts=[]
for j in range(n):  pts.extend([0,7+int(5*sin(6*pi*j/n+pi/3)),0])

my_cmap=emerald_woman

S = triangles_on_frame(T1,skip=skip,scale=5,oangle=pi/3,n=n-1,
                       pts=pts*def_factor,asym=0.5,orient_follow=1,orient=ao,
                       arc_angle=pi/5)

figure(S,'cycles','turbo',dot_size=10,alpha=1)

###

S.reset()

# move this one to a new project:  Stacked Polygons

e=0.0
R=7
ppl=1000

a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/4,a/6),ppl=ppl,loops=1,inside=True)

skip=4
n=30

scale=5
oa=pi/3
ao=0.0
asym=0
aa=pi/3
of=1
pts=[200,200,200]
    
for i in range(15):
    S.add(triangles_on_frame(T,skip=skip,scale=scale,oangle=oa,n=n,fh=0,fb=0,asym=asym,
                             orient_follow=1,orient=ao,arc_angle=aa,pts=pts))
    S.p+=0.1
    scale *= 0.95

figure(S,'cycles','turbo')

### experiment with color:  color groups of triangles

e=0.0
R=7
ppl=1000

a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/3,a/2),ppl=ppl,loops=1,inside=True)

skip=1
n=50

oa=pi/3
ao=0.0
asym=0
of=1

nr=15

theta = linspace(0,2*pi,nr)
aa = linspace(0,pi/2,nr)
lmax = append(linspace(25,3,nr//2),linspace(3,25,nr//2))
rr = np.random.poisson(3,nr)+2.0
scale = rr

S=SpiroData()

for i in range(nr):
    
    first=i*T.n()//nr
    S.add(triangles_on_frame(T,first=first,skip=skip,scale=scale[i],n=n,fh=0,fb=0,
                             asym=asym,orient_follow=1,orient=0,arc_angle=pi/4,pts=200))

cmap='turbo'
cs=np.mod(linspace(0,S.n(),S.n()),200)
figure(S,cs,cmap)

## experiment with color:  overlapping groups of parallelograms

skip=1
n=120

oa=pi/3
ao=0.0
asym=0
of=1

nr=5

theta = linspace(0,2*pi,nr)
aa = linspace(0,pi/2,nr)
lmax = append(linspace(25,3,nr//2),linspace(3,25,nr//2))
rr = np.random.poisson(3,nr)+2.0
scale = rr  

cs=[]

S=SpiroData()

for i in range(nr):
    
    npts=int(30*scale[i])
    first=i*T.n()//nr
    S.add(pars_on_frame(T,first=first,skip=skip,scale=scale[i],n=n,fh=0,fb=0,
                             asym=asym,orient_follow=1,orient=0,arc_angle=pi/4,pts=npts))

    color_sequence=np.full((npts),0)
    for j in range(n):  
        for k in range(2):
            cs.extend(color_sequence*0+i+2*j/n)
            cs.extend(color_sequence*0+i+2*j/n+3)

figure(S,cs,'turbo')
