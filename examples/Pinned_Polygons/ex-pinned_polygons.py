import sys
sys.path.append('../..')
import argparse

from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_frame import *
from polygon import *

parser = argparse.ArgumentParser(description="Pinned Polygon Examples")
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

F._figname='Pinned_Polygons-'

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
R=40
ppl=1000
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e,pen_offset=0),wheel=Wheel(a/4,a/5),ppl=ppl,loops=1,inside=True)

ppl=400
id = linspace(0,ppl,ppl) 
id *= T.max_path() / id[-1]
W = T.resample(id)

S = SpiroData()

nk=8
gs=2
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=300*def_factor
pts_fade = array([ npts//3+npts-int(npts*cos(2*pi*j/(3*n))) for j in range(3*n) ]) 

for k in range(nk):
    
    first = k*ns 
    
    ao = 0 
    
    s = linspace(1.0,1.5,n)
    nn = n-1
    aa = pi/6

    S.add(on_frame(W,asym=0,oangle=pi/3,arc_angle=aa,fb=0.5,fh=0.5,first=first,orient=ao,pts=pts_fade,scale=s,
                   n=nn,object=k,polyfunc=tcoords,prot=-pi/12,pin_coord=array([-3,0]),pin_to_frame=1.0))

figure(S,'time','hot')

###

e=0.0
R=40
ppl=1000
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e,pen_offset=0),wheel=Wheel(a/4,a/2),ppl=ppl,loops=1,inside=True).rotate(pi/9)

ppl=400
id = array( [ 1.0+0.5*cos(6*pi*j/ppl) for j in range(0,ppl) ] ).cumsum()
id *= T.max_path() / id[-1]
W = T.resample(id)

S = SpiroData()

nk=3
gs=2
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=300*def_factor
pts_fade = npts

for k in range(nk):
    
    first = k*ns + ns//3
    
    ao = 0
    
    s = 1 
    nn = n-1
    aa = pi/6

    S.add(on_frame(W,asym=0.5,oangle=pi/3,arc_angle=aa,fb=0.4,fh=0,first=first,orient=ao,pts=pts_fade,scale=s,
                   n=nn,object=k,polyfunc=tcoords,prot=0,pin_coord=array([-60,60]),pin_to_frame=0.0))
    
figure(S,S.chord_dists(S.n()//4),'cmap2')

###

T = cIc(Ring(28),wheel=Wheel(4,5),loops=1,inside=True,ppl=2500).subsample(1)
W = T.copy()

S = SpiroData()

nk=7
gs=2
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=300*def_factor
pts_fade = npts

for k in range(1):
    
    first = k*ns 
    
    ao = 0 
    
    s = linspace(1.0,1.3,n)
    nn = n
    aa = -pi/4 

    S.add(on_frame(W,asym=0,oangle=4,arc_angle=aa,fb=-0.,fh=-0.5,first=first,orient=ao,pts=pts_fade,scale=s,
                   n=nn,object=k,polyfunc=ngon_coords,prot=0,pin_coord=array([0,0]),pin_to_frame=0.0))
    
figure(S,S.fpolars(),'turbo')

###

T = cIc(Ring(28),wheel=Wheel(4,7),loops=1,inside=True,ppl=1000).subsample(1)
W = T.copy()

S = SpiroData()

nk=7
gs=28
n = W.n()//(nk+gs)
ns = W.n()//nk

npts=150*def_factor
pts_fade = array([],dtype=int)
for j in range(n):
    p = npts//30 + npts - int(npts*cos(2*pi*j)/n)
    pts_fade = np.append(pts_fade,[p,p,p,p,p,p])
    
for k in range(nk):
    
    first = k*ns 
    
    ao = 0 
    
    s = 1 
    asym = linspace(0.1,0.6,n)
    nn = n
    aa = -pi/6 

    S.add(on_frame(W,asym=asym,oangle=3,arc_angle=aa,fb=-0.5,fh=-0.5,first=first,orient=ao,
                   pts=pts_fade,scale=s,n=nn,object=k,polyfunc=nstar_coords,prot=0,
                   pin_coord=array([-1,0]),pin_to_frame=1.0))
    
figure(S,S.fchord_dists(S.n()//7),'autumn')

###

T = cIc(Ring(24),wheel=Wheel(4,8),loops=1,inside=False,ppl=2000).subsample(1)
W = T.copy()

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
                   n=nn,object=k,polyfunc=nstar_coords,prot=0,pin_coord=array([0,0]),pin_to_frame=0.0))
    
figure(S,'time','gist_heat')

###

T = roll(-50,-50,50,50,wheel=Wheel(5,2))

ppl=200
id = linspace(0,ppl,ppl) 
id *= T.max_path() / id[-1]
W = T.resample(id) 

S = SpiroData()

nk=1
gs=0
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=150*def_factor
pts_fade = npts

for k in range(nk): 
    
    first = k*ns 
    
    ao = linspace(0,pi/2,n) 
    
    s = 1 
    asym = 0.1 
    nn = n
    aa = pi/9 

    S.add(on_frame(W,skip=1,asym=asym,oangle=pi/4,arc_angle=aa,fb=0,fh=0.0,
                   first=first,orient=ao,pts=pts_fade,scale=s,
                   n=nn,object=k,polyfunc=pcoords,prot=0,pin_coord=array([5,0]),pin_to_frame=0.0))

figure(S,'time','OrRd')

###

T = roll(-50,-50,50,50,wheel=Wheel(5,2))

ppl=400
id = linspace(0,ppl,ppl) 
# id = array( [ 1.0+0.5*cos(6*pi*j/ppl) for j in range(0,ppl) ] ).cumsum()
id *= T.max_path() / id[-1]
W = T.resample(id) # .move(60,-60)

S = SpiroData()

nk=25
gs=5
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=300*def_factor

pts_fade = array([],dtype=int)
for j in range(n):
    p = npts//30 + npts - int(npts*cos(2*pi*j)/n)
    pts_fade = np.append(pts_fade,[p,p,p,p,p])

for k in range(nk): 
    
    first = k*ns
    
    ao = linspace(0,pi/8,n) -pi/2*sin(2*pi*k/nk) 
    
    s = 1 
    asym = 0.0 
    nn = n
    aa = pi/9 

    S.add(on_frame(W,asym=asym,oangle=5,arc_angle=aa,fb=0,fh=0.0,first=first,orient=ao,pts=pts_fade,scale=s,
                   n=nn,object=k,polyfunc=ngon_coords,prot=0,pin_coord=array([-70,-75]),pin_to_frame=1.0))
    
figure(S,'length','emerald_woman')

###

T = spiro_cross(wheel=Wheel(1,0.5),inside=True) 

ppl=400
id = linspace(0,ppl,ppl) 
id *= T.max_path() / id[-1]
W = T.resample(id) 

S = SpiroData()

nk=1
gs=0
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=300*def_factor

pts_fade = npts

for k in range(nk): 
    
    first = k*ns
    
    ao = 0 
    
    s = 1 
    asym = 0.0 
    nn = n
    aa = 0 

    S.add(on_frame(W,asym=asym,oangle=pi/3,arc_angle=aa,fb=0,fh=0.0,first=first,orient=ao,pts=pts_fade,scale=s,
                   n=nn,object=k,polyfunc=tcoords,prot=0,pin_coord=array([0,0]),pin_to_frame=1.0))
    
figure(S,'time','turbo')

###

T = spiro_cross(wheel=Wheel(1,0.5),inside=True) 

ppl=1000
id = linspace(0,ppl,ppl) 
id *= T.max_path() / id[-1]
W = T.resample(id)
W = W.select(np.where(W.y<6)) # .move(60,-60)

S = SpiroData()

nk=12
gs=6
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=300*def_factor

pts_fade = array([],dtype=int)
for j in range(n):
    p = npts//30 + npts - int(npts*cos(2*pi*j)/n)
    pts_fade = np.append(pts_fade,[p,p,p])

for k in range(nk): 
    
    first = k*ns 
    
    ao = 0 
    
    s = 1 
    asym = -0.3 
    nn = n
    aa = pi/9 

    S.add(on_frame(W,asym=asym,oangle=pi/5,arc_angle=aa,fb=0.5,fh=0.5,first=first,orient=ao,
                   pts=pts_fade,scale=s,n=nn,object=k,polyfunc=tcoords,prot=0,
                   pin_coord=array([0,7]),pin_to_frame=1.0))

figure(S,S.lengths(),'inferno')

###

T = spiro_cross(wheel=Wheel(1,0.5),inside=True) 

ppl=1000
id = linspace(0,ppl,ppl) 
id *= T.max_path() / id[-1]
W = T.resample(id)

S = SpiroData()

nk=12
gs=4
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=300*def_factor
pts_fade = npts

for k in range(nk): 
    
    first = k*ns 
    
    ao = 0 
    
    s = 1 
    asym = -0.3 
    nn = n
    aa = pi/9 

    S.add(on_frame(W,asym=asym,oangle=pi/5,arc_angle=aa,fb=0.5,fh=0.5,first=first,orient=ao,
                   pts=pts_fade,scale=s,n=nn,object=k,polyfunc=tcoords,prot=0,
                   pin_coord=array([0,7]),pin_to_frame=0.0,autoscale=False))
    
figure(S,S.lengths(),'pretty_reds')

###

T = spiro_cross(wheel=Wheel(2,4),inside=True)  
W=T.copy().subsample(5)

S = SpiroData()

nk=1
gs=2
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=300*def_factor

pts_fade = array([],dtype=int)
for j in range(n):
    p = npts//3 + npts - int(npts*cos(2*pi*j/n))
    pts_fade = np.append(pts_fade,[p,p,p])

for k in range(nk): 
    
    first = k*ns + ns//10
    
    ao = linspace(0,-3*pi,n) 
    
    s = linspace(1.0,2.0,n)
    asym = 0.0 
    nn = n
    aa = pi/3 

    S.add(on_frame(W,asym=asym,oangle=pi/3,arc_angle=aa,fb=-0.5,fh=-0.5,first=first,orient=ao,
                   pts=pts_fade,scale=s,n=nn,object=k,polyfunc=tcoords,prot=0,
                   pin_coord=array([3,0]),pin_to_frame=0.0,autoscale=True))

figure(S,'time','pretty_blues')

###

T = cIc(Ring(24),wheel=Wheel(4,12),loops=1,inside=True,ppl=1500)
W = T.copy()

S = SpiroData()

nk=1
gs=2
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=150*def_factor

pts_fade = array([],dtype=int)
for j in range(n):
    p = npts//3 + npts - int(npts*cos(6*pi*j/n))
    pts_fade = np.append(pts_fade,[p,p,p,p])



ao = array( [ pi/4*sin(2*pi*j/n) for j in range(n) ])

for k in range(nk): 
    
    first = k*ns + ns//7
    
    s = 1 
    asym = 0.4 
    nn = n-1
    aa = pi/4 

    S.add(on_frame(W,asym=asym,oangle=pi/2,arc_angle=aa,fb=-0.5,fh=-0.5,first=first,orient=ao,
                   pts=pts_fade,scale=s,n=nn,object=k,polyfunc=pcoords,prot=0,
                   pin_coord=array([-10,-10]),pin_to_frame=0.0,autoscale=True))
    
figure(S,'cycles','Oranges')

###

T = cIc(Ring(24),wheel=Wheel(6,6),loops=1,inside=False,ppl=2000)
W = T.copy()

S = SpiroData()

nk=12
gs=4
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=250*def_factor
pts_fade = npts

for k in range(nk//3): 
    
    first = 3*k*ns

    ao = array( [ pi/36*sin(2*pi*j/n) for j in range(n) ]) 

    s = 1
    asym = 0.0 
    nn = n-1
    aa = pi

    pc = array([0,0,])
    
    S.add(on_frame(W,asym=asym,oangle=pi/3,arc_angle=aa,fb=-0.5,fh=-0.5,first=first,orient=ao,
                   pts=pts_fade,scale=s,n=nn,object=k,polyfunc=tcoords,prot=0,
                   pin_coord=pc,pin_to_frame=1.0,autoscale=True))

    S.add(on_frame(W,asym=asym,oangle=pi/3,arc_angle=-aa,fb=-0.5,fh=-0.5,first=first,orient=ao,
                   pts=pts_fade,scale=s,n=nn,object=k,polyfunc=tcoords,prot=0,
                   pin_coord=pc,pin_to_frame=1.0,autoscale=True))
    
figure(S,'direction','turbo')
