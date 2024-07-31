import sys
sys.path.append('../..')
import argparse

import numpy as np

from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_frame import *
from polygon import *
from partition import *

parser = argparse.ArgumentParser(description="Partition Examples")
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

F._figname='Partition-'

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

F.save_fig()

###


R = 50
ppl = 4000
a=R/(2*pi)/1.4
S1 = spiro_eq_triangle(R=R,wheel=Wheel(a,1.6*a),orient=0,loops=5,fold=False,inside=True)

S1 = S1.resample(S1.max_path()*frame_sampling(ppl,parm=4,spacing='sinusoid',
                                              repeat=200,deramp=True))
n = S1.n() 

oa = 2
nv = oa
v = linspace(0,nv-1,nv,dtype=int)

pts = 160 

rp_opts = { 'n': pts, 
            'parm': 5,
            'spacing':  ['sinusoid'], 'repeat': 3, 'deramp': True }

offset = 0.4
sc = S1.radii()/max(S1.radii()) * 30

f0 = 0 # 
follow = 1

nn = n

o = linspace(0,6*pi,nn) 

asym = 0 

aa = pi/3

cs='direction' 
cmap='turbo'

S = on_frame(S1,scale=sc,oangle=oa,fb=offset,fh=offset,asym=asym,orient=o,first=f0,
             polyfunc=ngon_coords,pts=pts,orient_follow=follow,n=nn,vertex_order=v,
             object=1,arc_angle=aa,rp_opts=rp_opts)

ns = 15
SA = []

for i in range(ns):
    r = S.radii()
    mr = max(S.radii())
    S=S.remove(np.where( r < (i+0.25)/ns * mr))
    r = S.radii()
    mr = max(S.radii())
    SA.append(S.select(np.where( r < (i+1)/ns * mr)))

first_plot=True              
for i in range(ns):
    F.plot(SA[i].rotate(i/ns*pi/3),color_scheme=cs,cmap=cmap, dot_size=0.1,alpha=(i+1)/ns * 0.6,limits=None,
           coord_dither=0.0,color_dither=0.0,new_fig=first_plot)
    first_plot=False

F.save_fig()

###  stained glass panels

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
 
cmap = ['Blues','Reds','Greens','Oranges','OrRd']

nx = 10
ny = 10
minx = min(S.x)
miny = min(S.y)
maxx = max(S.x)
maxy = max(S.y)
rangex = maxx-minx
rangey = maxy-miny
k=0
first=True
W = SpiroData()
pad=0.01
for ix in range(nx):
    for iy in range(ny):
        x1 = ix/nx * rangex + minx
        x2 = (ix+1)/nx * rangex + minx
        y1 = iy/ny * rangey + miny
        y2 = (iy+1)/ny * rangey + miny
        j = np.where( (S.x > x1) & (S.x < x2) & (S.y > y1) & (S.y < y2) )
        sd = S.select(j)
        
    
        sd = sd.remove(np.where( (sd.x > x1+(1-pad)*rangex) | (sd.x < x1+pad*rangex) |
                                 (sd.y > y1+(1-pad)*rangey) | (sd.y < y1+pad*rangey) ))
        
        c = np.random.randint(len(cmap))
        F.plot(sd,color_scheme='fradii',cmap=cmap[c],alpha=0.4,dot_size=0.1,
               limits=[minx,maxx,miny,maxy],new_fig=first)
        first=False
        k += 1
        
F.save_fig()

### tiles, with small random orientation changes (and random colors)

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
 
cmap = ['Blues','Reds','Greens','Oranges','OrRd']

nx = 12
ny = 12
minx = min(S.x)
miny = min(S.y)
maxx = max(S.x)
maxy = max(S.y)
rangex = maxx-minx
rangey = maxy-miny
k=0
first=True
W = SpiroData()
pad=0.01
xf = 1.0
for ix in range(nx):
    for iy in range(ny):
        x1 = ix/nx * rangex + minx
        x2 = (ix+1)/nx * rangex + minx
        y1 = iy/ny * rangey + miny
        y2 = (iy+1)/ny * rangey + miny
        j = np.where( (S.x > x1) & (S.x < x2) & (S.y > y1) & (S.y < y2) )
        sd = S.select(j)
        
    
        sd = sd.remove(np.where( (sd.x > x1+(1-pad)*rangex) | (sd.x < x1+pad*rangex) |
                                 (sd.y > y1+(1-pad)*rangey) | (sd.y < y1+pad*rangey) ))

        sd.move(-(x1+x2)/2,-(y1+y2)/2).rotate(2*pi/120*np.random.standard_normal()).move(xf*(x1+x2)/2,xf*(y1+y2)/2)
        
        c = np.random.randint(len(cmap))
        F.plot(sd,color_scheme='fradii',cmap=cmap[c],alpha=0.4,dot_size=0.1,new_fig=first)
        first=False
        k += 1

F.save_fig()

###  partitioned, with coords inverted

e=0.2
R=40
ppl=2000
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
 

nx = 12
ny = 12
minx = min(S.x)
miny = min(S.y)
maxx = max(S.x)
maxy = max(S.y)
rangex = maxx-minx
rangey = maxy-miny
k=0
first=True
W = SpiroData()
pad=0.01
xf = 1.0
for ix in range(nx):
    for iy in range(ny):
        x1 = ix/nx * rangex + minx
        x2 = (ix+1)/nx * rangex + minx
        y1 = iy/ny * rangey + miny
        y2 = (iy+1)/ny * rangey + miny
        j = np.where( (S.x > x1) & (S.x < x2) & (S.y > y1) & (S.y < y2) )
        sd = S.select(j)

        sd = sd.remove(np.where( (sd.x > x1+(1-pad)*rangex) | (sd.x < x1+pad*rangex) |
                                 (sd.y > y1+(1-pad)*rangey) | (sd.y < y1+pad*rangey) ))

        sd.set_objects(np.random.random())

        W.add(sd)
        
S=W.remove(np.where(W.radii()<1.0)).inverted_radii()
rmin=min(S.radii())
rmax=max(S.radii())
F.plot(S,color_scheme='object',cmap='pretty_reds',
       limits=[-0.2,0.2,-0.2,0.2],
       alpha=0.1+0.8*sqrt(S.radii()/rmax),dot_size=0.1+0.3*sqrt(S.radii()/rmax),new_fig=first)

F.save_fig()

### elliptical partitions, rotated in both directions

e=0.2
R=40
ppl=300
a=R/(1.03*2)
U = cIc(Ring(R),wheel=Wheel(a,0.5*a,pi/6),ppl=ppl,loops=2,inside=True)
W = U.resample(U.max_path()*frame_sampling(ppl,spacing='constant'))
F.plot(U,color_scheme='white',cmap='turbo',alpha=0.4,dot_size=1)
F.plot(W.move(2,2),color_scheme='cyan',cmap='turbo',alpha=0.4,dot_size=1,new_fig=False)
T = on_frame(W,orient_follow=1,scale=50,pts=20,oangle=64,polyfunc=ecoords,n=W.n()//2)
F.plot(T,color_scheme='time',cmap='turbo',alpha=0.4,dot_size=.1)

WA = partition_rings(T,n=18,pad=0.0,scalex=0.5)

S = SpiroData()
for i in range(len(WA)):
    isign = 1 if i<len(WA)/2 else -1
    WA[i].rotate(isign*pi/2*i/len(WA))
    S.add(WA[i])

F.plot(S,color_scheme='fcdist3',cmap='Blues',alpha=0.4,dot_size=0.1)
F.save_fig()

###  evolving partition rings

e=0.2
R=40
ppl=40
loops=10
a=R/(1.03*2)
U = cIc(Ring(R),wheel=Wheel(a,0.5*a,pi/6),ppl=ppl,loops=loops,inside=True)
W = U.resample(U.max_path()*frame_sampling(ppl*loops,spacing='constant'))

nv=8
v = linspace(0,nv-1,nv-1,dtype=int)

T = on_frame(W,orient_follow=1,scale=50,pts=100,vertex_order=v,
             oangle=8,arc_angle=pi,polyfunc=ecoords,n=W.n()//2)
T.add(on_frame(W,orient_follow=1,scale=50,pts=100,vertex_order=v,
               oangle=8,arc_angle=-pi,polyfunc=ecoords,n=W.n()//2))

nr=10
S = objectify(partition_rings(T,nr,pad=0.1,
                              scalex=linspace(1.0,0.4,nr),
                              prot=linspace(0,pi/4,nr)))

F.plot(S,color_scheme='width',cmap='hot',alpha=0.4,dot_size=0.1)
F.save_fig()

###

e=0.2
R=40
ppl=40
loops=10
a=R/(1.03*2)
U = cIc(Ring(R),wheel=Wheel(a,0.5*a,pi/6),ppl=ppl,loops=loops,inside=True)
W = U.resample(U.max_path()*frame_sampling(ppl*loops,spacing='constant'))

nv=8
v = linspace(0,nv-1,nv-1,dtype=int)
T = on_frame(W,orient_follow=1,scale=50,pts=100,vertex_order=v,
             oangle=8,arc_angle=pi,polyfunc=ecoords,n=W.n()//2)
T.add(on_frame(W,orient_follow=1,scale=50,pts=100,vertex_order=v,
               oangle=8,arc_angle=-pi,polyfunc=ecoords,n=W.n()//2))

S = SpiroData()
nr=10
WA = partition_rings(T,nr,pad=-0.1,scalex=linspace(1.0,0.4,nr),prot=linspace(0,pi/4,nr))
for j in range(len(WA)):
    r = j+0.5
    na = int(8*r)
    WAA = partition_azimuth(WA[j],na,pad=0.05)
    for Q in WAA: 
        Q.rotate(pi/4)
        Q.set_objects(np.random.random())
        Q.set_segments((j+0.5)/len(WA)*0.6)  # use this for alpha
        S.add(Q)

F.plot(S,color_scheme='phase',cmap='emerald_woman',alpha=S.s,dot_size=0.1)

F.save_fig()

###

e=0.2
R=40
ppl=1000
loops=10
a=R/(1.03*2)
U = cIc(Ring(R),wheel=Wheel(a,0.5*a,pi/6),ppl=ppl,loops=loops,inside=True)
W = U.resample(U.max_path()*frame_sampling(ppl*loops,spacing='constant'))

first=True
S=SpiroData()
nx=15
ny=15
WA = partition_tiles(W,nx,ny)
for i in range(0,len(WA),15):
    F.plot(WA[i],color_scheme='cyan',dot_size=2.0,new_fig=first)
    first=False
    S.add(on_frame(WA[i],first=1,n=WA[i].n()-2,scale=10,pts=100,
                   orient_follow=1,arc_angle=pi/5,
                   polyfunc=tcoords,orient=2*pi*i/len(WA),object=i))

F.plot(S,color_scheme='width',cmap='gist_heat_r',alpha=0.4,dot_size=0.1)

F.save_fig()

###

e=0.2
R=40
ppl=1000
loops=1
a=R/(1.03*2)
U = cIc(Ring(R),wheel=Wheel(a,0.5*a,pi/6),ppl=ppl,loops=loops,inside=True).rotate(pi/3)
W = U.resample(U.max_path()*frame_sampling(ppl*loops,parm=15.0,spacing='sinusoid',deramp=True,repeat=10))

S=SpiroData()
nx=5
tpts=200
WA = partition_panels(W,nx,pad=0.25)
for i in range(0,len(WA)):
    n=WA[i].n()
    offset=0.5 
    if n>10:
        S.add(on_frame(WA[i],first=1,n=n-2,scale=60,pts=tpts,
                       orient_follow=0,arc_angle=pi/3,fb=offset,fh=offset,
                       polyfunc=tcoords,orient=linspace(0,pi/2*i/len(WA),n-2),object=i))

F.plot(S,color_scheme='t-waves',cmap='gist_heat',alpha=0.4,dot_size=0.1)
F.save_fig()

###

e=0.2
R=40
ppl=1000
loops=1
a=R/(1.03*2)
U = cIc(Ring(R),wheel=Wheel(a,0.5*a,pi/6),ppl=ppl,loops=loops,inside=True).rotate(pi/3)
W = U.resample(U.max_path()*frame_sampling(ppl*loops,parm=15.0,spacing='sinusoid',deramp=True,repeat=10))

first=True
S=SpiroData()
nx=5
tpts=200
WA = partition_panels(W,nx,pad=0.25)
for i in range(0,len(WA)):
    F.plot(WA[i],color_scheme='cyan',dot_size=2.0,new_fig=first)
    first=False
    n=WA[i].n()
    offset=0.5 
    if n>10:
        S.add(on_frame(WA[i],first=1,n=n-2,scale=60,pts=tpts,oangle=linspace(pi/4,pi/2,n-2),
                       orient_follow=0,arc_angle=pi/4,fb=offset,fh=offset,
                       polyfunc=pcoords,orient=linspace(0,pi/2*i/len(WA),n-2),object=i))

F.plot(S,color_scheme='direction',cmap='twilight',alpha=0.4,dot_size=0.1)

F.save_fig()

###  shimmers of a thousand tiles

e=0.2
R=40
ppl=300
loops=2
a=R/(1.07*2)
U = cIc(Ring(R),wheel=Wheel(a,0.5*a,pi/6),ppl=ppl,loops=loops,inside=True).rotate(pi/3)
W = U.resample(U.max_path()*frame_sampling(ppl*loops,parm=1.0,
                                           spacing='sinusoid',deramp=True,repeat=15))

F.plot(W,color_scheme='white',cmap='turbo',alpha=0.4,dot_size=1)

tpts=100
n=W.n()
offset=0.5

rp_opts = { 'n': 9*tpts, 'spacing': ['sinusoid'], 'deramp': True, 'repeat': 4 }

S = on_frame(W,first=1,n=n-2,scale=50,pts=tpts,
             oangle=linspace(pi/4,pi/2,n-2),asym=0.2,
             orient_follow=1,arc_angle=pi/4,fb=offset,fh=offset,
             polyfunc=pcoords,orient=0,rp_opts=rp_opts)

ST = partition_rings(S,3,scalex=0.7,prot=pi/4)
QQ = []
for STI in ST[1:]:
    SA = partition_tiles(STI,30,30) 
    for Q in SA:  
        dx=Q.meta['tile-xc']
        dy=Q.meta['tile-yc']
        Q.set_objects(sqrt(dx**2+dy**2)).move(-dx,-dy).rotate(np.random.standard_normal()*pi/4).move(dx,dy)
        QQ=np.append(QQ,Q)
        
SS = objectify(QQ)
F.plot(SS,color_scheme='time',cmap='Oranges',alpha=0.4,dot_size=0.1)
F.plot(ST[0].subsample(2),color_scheme='time',cmap='gist_heat_r',alpha=0.4,dot_size=0.1,new_fig=False)

F.save_fig()

###  exploding tiles

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

oa = pi/4
f0 = W.n()//6
o = linspace(pi/2,pi/2,n-2)

S = on_frame(W,first=f0,n=n-2,scale=70,pts=tpts,
             oangle=oa,asym=0.2,
             orient_follow=1,arc_angle=pi/4,fb=offset,fh=offset,
             polyfunc=tcoords,orient=o,rp_opts=rp_opts)

SS = S.copy()

nn = 4
ST = partition_rings(SS,nn,pad=0.0)
QQ = [ ST[0] ]
QQ1 = ST[1]
r0 = min(QQ1.radii())/2
k=0
for Q in ST[1:]:
    scale = Q.rmid()/r0
    naz = int(nn*scale)
    for X in partition_azimuth(Q,naz,pad=0.0):
        if X.n()>0:
            X.set_objects(k)
            k+=1
            theta = X.azmid()
            dr = Q.rmid()/nn * (1+np.random.standard_normal()/3)
            X.update_coords(X.x + dr*cos(theta),X.y + dr*sin(theta))
            QQ=np.append(QQ,X.rotate(2*pi*np.random.standard_normal()/(3*naz)))

SS = objectify(QQ)

max_dither=20
exp_dither=6

cd = SS.dists_to_coord(array([ 0,0 ]))
mcd=max(cd)
x = np.copy(SS.x)
y = np.copy(SS.y)
dr = np.random.standard_normal(SS.n())
dt = np.random.uniform(0,2*pi,SS.n())
coord_dither = max_dither*((cd/mcd)**exp_dither)
for j in range(SS.n()):
    x[j] += coord_dither[j]*dr[j]*cos(dt[j])
    y[j] += coord_dither[j]*dr[j]*sin(dt[j])

SS.update_coords(x,y)
F.plot(SS,color_scheme='fwidth',cmap='gist_heat',alpha=0.4,dot_size=0.1)

F.save_fig()
