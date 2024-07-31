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

parser = argparse.ArgumentParser(description="One-Offs")
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

F._figname='One-Offs-'

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

###  highly asymmetric triangles  (move this to one of the triangles projects?)

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

###  zoom in on a design

S = SpiroData()
e=0.0
R=7
ppl=1000
a=circum(R,semi_minor(R,e))/(2*pi)
T1 = cIe(Ellipse(R,e),wheel=Wheel(a/6,a/5),ppl=ppl,loops=1,inside=True).rotate(pi/4)

pts = [500,500,0]

S = triangles_on_frame(T1,scale=3,oangle=pi/3,pts=pts*def_factor,orient_follow=1)

figure(S,'cycles','hot',limits=[-5,0,4,9])

###  large dots

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

### experiment with color:  color groups of triangles -- modulo on color-scheme

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

###  Feathers:  playing with colormap, alpha, and dot_size

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
       cmap=my_cmap,alpha=.1,fig_dim=fd,dot_size=15,new_fig=False,color_dither=0.0)

F.save_fig()

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

###  chaos frame

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

###  arcs on a frame with random jitter in its coords

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

F.plot(S,color_scheme='fcdist3',cmap='hot', dot_size=0.1,alpha=0.4,coord_dither=2.0,limits=None)

F.save_fig()

###  "disintegration"

e=0.2
R=40
ppl=200
loops=10
a=R/2.1
U = cIc(Ring(R),wheel=Wheel(a,0.6*a),ppl=ppl,loops=loops,inside=True)
W = U.resample(U.max_path()*frame_sampling(ppl*loops,parm=0.3,reverse=False,
                                           spacing='erf',deramp=True,repeat=10))

tpts=[100,200,300]
n=int(0.2*W.n())
offset=0.5

rp_opts = None 

oa = linspace(pi/4,pi/2,n-2)
f0 = W.n()//6
o = linspace(pi/2,pi/2,n-2)

S = on_frame(W,first=f0,n=n-2,scale=70,pts=tpts,
             oangle=oa,asym=0.2,
             orient_follow=1,arc_angle=pi/4,fb=offset,fh=offset,
             polyfunc=tcoords,orient=o,rp_opts=rp_opts)

max_dither=10
exp_dither=6

cd=S.dists_to_coord(array([min(S.x),max(S.y)]))
mcd=max(cd)
x = np.copy(S.x)
y = np.copy(S.y)
dr = np.random.standard_normal(S.n())
dt = np.random.uniform(0,2*pi,S.n())
coord_dither = max_dither*((cd/mcd)**exp_dither)
for j in range(S.n()):
    x[j] += coord_dither[j]*dr[j]*cos(dt[j])
    y[j] += coord_dither[j]*dr[j]*sin(dt[j])
T = S.copy()
T.update_coords(x,y)
F.plot(T,color_scheme='time',cmap='cyans',alpha=0.4,dot_size=0.1)

F.save_fig()

###

e=0.2
R=40
ppl=500
loops=10
a=R/2.1
U = cIc(Ring(R),wheel=Wheel(a,0.5*a),ppl=ppl,loops=loops,inside=True)
W = U 

tpts=[20,20,0,30]
n=int(0.1*W.n())
offset=-0.1

rp_opts = { 'n': 500, 'parm': 2, 'spacing': ['erf'], 'deramp': True, 'repeat': 5 }

oa = pi/4 
f0 = W.n()//3
o = linspace(0,pi/2,n-2)
asym=linspace(-0.1,0.3,n-1)

S = on_frame(W,first=f0,n=n-2,scale=30,pts=tpts,
             oangle=oa,asym=asym,
             orient_follow=W.n()//3,arc_angle=pi/2,fb=offset,fh=offset,
             polyfunc=pcoords,orient=o,rp_opts=rp_opts,object=arange(n-2,dtype=int))

fade = np.full( (ppl), 0.0 )
fade[ppl-ppl//3:ppl] = linspace(0.0,5.0,ppl//3)
sat = np.full( (ppl), 0.0 )
sat[0:ppl//4] = 1.0
sat[ppl//4:ppl-ppl//4] = linspace(1.0,0.0,ppl//2)
sat[ppl-ppl//4:ppl] = 0.0

for cmap in ['prism']:
    first=True
    for i in range(ppl):
        F.plot(S.select(np.where(np.rint(S.o)==i)),color_scheme='time',
               cmap=modify_colormap_saturation(cmap,sat[i]),
               alpha=0.4,dot_size=0.1,new_fig=first,coord_dither=fade[i])
        first=False

F.save_fig()
