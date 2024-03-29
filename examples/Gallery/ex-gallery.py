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
                             orient_follow=1,orient=ao,arc_angle=aa,pts=pts*def_factor))
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
                             asym=asym,orient_follow=1,orient=0,arc_angle=pi/4,pts=200*def_factor))

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
                             asym=asym,orient_follow=1,orient=0,arc_angle=pi/4,pts=npts*def_factor))

    color_sequence=np.full((npts),0)
    for j in range(n):  
        for k in range(2):
            cs.extend(color_sequence*0+i+2*j/n)
            cs.extend(color_sequence*0+i+2*j/n+3)

figure(S,cs,'turbo')

###  (masking -- panels)

e=0.0
R=7
ppl=1000

a=circum(R,semi_minor(R,e))/(2*pi)
T1 = cIe(Ellipse(R,e),wheel=Wheel(a/3,a/3),ppl=ppl,loops=1,inside=True)

skip=2
n=T1.n()//skip//18

d = T1.neighbor_distances()
dmax=max(d)
dmin=min(d)
scale=5
ao=pi/2*(d-dmin)/(dmax-dmin)

pts = [0,500,500]

offset=1 # np.random.randint(T1.n())

S = SpiroData()
n_swoops=12
for i in range(n_swoops):
    first=T1.n()*i//n_swoops
    S.add(triangles_on_frame(T1,skip=skip,scale=scale,oangle=pi/3,n=n-1,orient=ao,
                             first=first,pts=pts*def_factor,orient_follow=1,arc_angle=pi/2,object=i))
    
U = SpiroData()
npanels=3
pwidth=4
pspace=5
pfirst=-(npanels*pspace)/2
for i in range(npanels):
    pstart=pfirst+i*pspace
    U.add(S.select(np.where( (S.x > pstart) & (S.x < pstart+pwidth) )))

figure(U,'cycles','Blues')

###

e=0.5
R=7
ppl=1000

a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/4,a/6),ppl=ppl,loops=1,inside=True).rotate(pi/4)

skip=10
n=T.n()//skip

scale=7
oa=pi/3
ao=0.0
asym=0.3
aa=pi/3
of=1
npts=300
pts=[npts,npts,npts,0]
    
S=pars_on_frame(T,skip=skip,scale=scale,oangle=oa,n=n,asym=asym,orient_follow=1,orient=ao,arc_angle=aa,pts=pts)

a=0.5
my_cmap = plt.cm.turbo(np.arange(plt.cm.turbo.N))
my_cmap[:,0:3] *= a 
my_cmap = ListedColormap(my_cmap)

# F.plot(T,color_scheme='pink',dot_size=5.0)
F.plot(S,color_scheme='cycles',cmap='turbo',alpha=.4,fig_dim=fd,dot_size=0.1,new_fig=True,color_dither=0.0)
F.plot(S.subsample(3).move(0.2,-0.2),color_scheme='cycles',
       cmap=my_cmap,alpha=.1,fig_dim=fd,dot_size=15,new_fig=False,color_dither=0.0,save=True,filename='Feathers.png')

### 5 Multi-colormapped Panels

e=0.0
R=7
ppl=1000

a=circum(R,semi_minor(R,e))/(2*pi)
T1 = cIe(Ellipse(R,e),wheel=Wheel(a/3,a/3),ppl=ppl,loops=1,inside=True)

skip=2
n=T1.n()//skip//18

d = T1.neighbor_distances()
dmax=max(d)
dmin=min(d)
scale=5
ao=pi/2*(d-dmin)/(dmax-dmin)

pts = [0,500,500]

offset=1 # np.random.randint(T1.n())

S = SpiroData()
n_swoops=12
for i in range(n_swoops):
    first=T1.n()*i//n_swoops
    S.add(triangles_on_frame(T1,skip=skip,scale=scale,oangle=pi/3,n=n-1,orient=ao,
                             first=first,pts=pts*def_factor,orient_follow=1,arc_angle=pi/2,object=i))
    
l=10
U = SpiroData()
npanels=5
pwidth=2.8
pspace=3
pfirst=-(npanels*pspace)/2
cmap=['Oranges','Blues','bone','Greens','Reds']
for i in range(npanels):
    pstart=pfirst+i*pspace
    U=S.select(np.where( (S.x > pstart) & (S.x < pstart+pwidth) ))
    
    F.plot(U,cmap=cmap[i],color_scheme='phase',alpha=0.4,dot_size=.1,limits=[-l,l,-l,l],
          new_fig=True if i==0 else False)

F.save_fig(filename='multi-cmap-panels.png')

###  Frame is Spiro on Spiro, with double arcs drawn on frame

S=SpiroData()
T = cIc(Ring(9),wheel=Wheel(3,3),ppl=540/9,loops=1,inside=True)
for i in range(T.n()):
    W = cIc(Ring(9),wheel=Wheel(3,6*i/T.n()),ppl=540/9,loops=1,inside=True)
    S.add(W.disp(T.xy(i)).select(slice(i,None,1)))
X=on_frame(S,scale=10,oangle=2,first=S.n()//2,fh=0,fb=0,n=S.n()//6,
           asym=0,orient_follow=1,orient=0, polyfunc=ngon_coords,
           arc_angle=[-pi/3,pi/4],pts=300)

figure(X,'phase','turbo')

###

n = 300
a = 1.35
b = 0.25
x = np.zeros(n)
y = np.zeros(n)

for k in range(n-1):
    x[k+1] = 1.0 - a*x[k]*x[k] + y[k]
    y[k+1] = b*x[k]

W = SpiroData()
W.set_array(x,y,x*0,linspace(0,n,n),x*0+1,x*0+1,x*0,y*0)

T = on_frame(W.subsample(1),scale=np.linspace(1.0,1.0,n),oangle=3,first=0,n=n-1,
             asym=0.2,orient_follow=0,orient=2*W.neighbor_distances(),polyfunc=nstar_coords,
             arc_angle=-pi/4,pts=np.linspace(150,150,3*n,dtype=int),object=0,prot=0)

figure(T,'time','turbo')

###  Resample heart figure with huge dots

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

SS=S.resample(linspace(0,S.max_path(),ppl*3))
figure(SS,SS.fradii(),cmap='jet',alpha=0.3,dot_size=500)

###

T = cIc(Ring(24),wheel=Wheel(4,8),loops=1,inside=False,ppl=2000)
W = T.copy()
rr = 1.0
dr = np.random.standard_normal(W.n())
dt = np.random.uniform(0,2*pi,W.n())
W.x += rr*dr*cos(dt)
W.y += rr*dr*sin(dt)

S = SpiroData()

nk=1
gs=0
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=150*def_factor

pts_fade = array([],dtype=int)
for j in range(n):
    p = npts//30 + npts - int(npts*cos(12*pi*j)/n)
    pts_fade = np.append(pts_fade,[0,0,p,p])

for k in range(nk): 
    
    first = k*ns + ns//2
    
    ao = 0
    
    s = 1 
    asym = 0.4 
    nn = n
    aa = -pi/9 

    S.add(on_frame(W,skip=[1,1,1,1,1,1,1,1,1,1,10],asym=asym,oangle=2,arc_angle=aa,
                   fb=0.5,fh=-0.5,first=first,orient=ao,pts=pts_fade,scale=s,
                   n=nn,object=k,polyfunc=nstar_coords,prot=0,pin_coord=array([0,0]),pin_to_frame=False))
    
figure(S,'time','gist_heat')
