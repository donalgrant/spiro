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

parser = argparse.ArgumentParser(description="Polygon Pieces Examples")
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

F._figname='Polygon_Pieces-'

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

e=0.1
R=40
ppl=1000
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e,pen_offset=pi/4),wheel=Wheel(a/6,a/2),ppl=ppl,loops=1,inside=True)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,1))

S=SpiroData()

nk=9
gs=9
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts = def_factor*200 

for k in range(nk):
    first = k*ns 
    asym= 0 
    scale = 30
    pts = [ npts, npts, 0, npts, npts, 0, npts, 0 ]
    ao = 0 
    aa = 0 
    
    S.add(on_frame(W,scale=scale,oangle=8,first=first,n=n-1,
                   asym=asym,orient_follow=1,orient=ao,polyfunc=ngon_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))
    
figure(S,'segment','turbo')

##

S=SpiroData()

nk=1
gs=0
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts = def_factor*200 

for k in range(nk):
    first = k*ns  # + W.n()//15

    scale = 15 # [ W.radius(j) for j in range(first,first+n) ]

    ao = 0 # pi/(k+1) + linspace(0,pi/((k+1)*nk),n) # [ np.random.standard_normal()*pi/100 for j in range(n) ]  # [ pi/6*sin(2*pi*j/n) for j in range(n) 
    aa = 0 # [pi/4,-pi/8] # linspace(-pi/2,-pi/3,8*n)
    
    S.add(on_frame(W,scale=scale,oangle=5,first=first,n=n-1,
                   asym=0.0,orient_follow=1,orient=ao,polyfunc=ngon_coords,
                   arc_angle=aa,pts=[npts,0],object=k,prot=0))
    
figure(S,'time',pale_pink.reversed())

###

e=0.1
R=40
ppl=1000
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e,pen_offset=pi/4),wheel=Wheel(a/5,a/3),ppl=ppl,loops=1,inside=True)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,3))

S=SpiroData()

nk=5
gs=2
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts = def_factor*200 

for k in range(nk):
    first = k*ns 

    scale = 35 

    ao = 0 
    aa = 0 
    
    S.add(on_frame(W,scale=scale,oangle=5,first=first,n=n-1,
                   asym=0.3,orient_follow=W.n()//3,orient=ao,polyfunc=nstar_coords,
                   arc_angle=pi/3,pts=[npts,0],object=k,prot=0))
    
figure(S,'time','pretty_reds')

###

e=0.4
R=40
ppl=1000
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e,pen_offset=pi/4),wheel=Wheel(a/5,a/2),ppl=ppl,loops=1,inside=False).rotate(pi/5)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,1))

S=SpiroData()

nk=1
gs=4
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts = def_factor*300 
npts_fade = linspace(npts,npts//5,7*n,dtype=int)
pts=np.zeros(0,dtype=int)
for j in range(npts_fade.shape[0]):
    pts=np.append(pts,array([npts_fade[j],int(0)]))
    
for k in range(nk):
    first = k*ns//4

    scale = [ 10*sqrt(W.radius(j)) for j in range(first,first+n) ]

    ao = linspace(0,2*pi,n)
    
    S.add(on_frame(W,scale=scale,oangle=7,first=first,n=n-1,
                   asym=0.6,orient_follow=W.n()//3,orient=ao,polyfunc=nstar_coords,
                   arc_angle=pi/3,pts=pts,object=k))
    
figure(S,'direction','pretty_blues')

##

S=SpiroData()

nk=1
gs=4
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts = def_factor*300 
npts_fade = linspace(npts//3,npts,7*n,dtype=int)
pts=np.zeros(0,dtype=int)
for j in range(npts_fade.shape[0]):
    pts=np.append(pts,array([0,npts_fade[j]]))
    
for k in range(nk):
    first = k*ns

    scale = [ 10*sqrt(W.radius(j)) for j in range(first,first+n) ]

    ao = linspace(0,2*pi,n)
    
    S.add(on_frame(W,scale=scale,oangle=7,first=first,n=n-1,
                   asym=0.1,orient_follow=W.n()//3,orient=ao,polyfunc=nstar_coords,
                   arc_angle=pi,pts=pts,object=k))
    
figure(S,'y-direction','cmap1')

###  First demonstration of "frame-width" for color-scheme

e=0.4
R=40
ppl=1000
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e,pen_offset=pi/4),wheel=Wheel(a/3,a/2),ppl=ppl,loops=1,inside=True).rotate(pi/5)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,1))

S=SpiroData()

nk=1
gs=4
n = W.n()//(nk+gs)
ns = W.n()//nk 

star_points=3
npts = def_factor*300
npts_fade = array([ 2+npts+int(npts*sin(6*pi*j/(n*star_points))) for j in range(n*star_points) ])
pts=np.zeros(0,dtype=int)
for j in range(n*star_points):
    pts=np.append(pts,array([0,npts_fade[j]]))
    
for k in range(nk):
    first = k*ns

    scale = [ 10*sqrt(W.radius(j)) for j in range(first,first+n) ]

    ao = linspace(0,2*pi,n)
    
    S.add(on_frame(W,scale=scale,oangle=star_points,first=first,n=n-1,
                   asym=-0.5,orient_follow=W.n()//3,orient=ao,polyfunc=nstar_coords,
                   arc_angle=pi,pts=pts,object=k))
    S.add(on_frame(W,scale=scale,oangle=star_points,first=first,n=n-1,
                   asym=-0.5,orient_follow=W.n()//3,orient=ao,polyfunc=nstar_coords,
                   arc_angle=-pi,pts=pts,object=k))
    
w = array( [ W.chord_dist(j,j+W.n()//2) for j in range(n-1) ] )
width=np.zeros(0)
for j in range(n-1):
    for k in range(star_points*2):
        width=np.append(width,np.full(pts[j*(star_points*2)+k],w[j]))
        
for j in range(n-1):
    for k in range(star_points*2):
        width=np.append(width,np.full(pts[j*(star_points*2)+k],w[j]))
        
figure(S,width,'pretty_reds')

###

e=0.4
R=40
ppl=1000
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e,pen_offset=pi/4),wheel=Wheel(a/3,a/2),ppl=ppl,loops=1,inside=True).rotate(pi/5)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,2))

S=SpiroData()

nk=3
gs=4
n = W.n()//(nk+gs)
ns = W.n()//nk 

star_points=6
npts = def_factor*300
npts_fade = linspace(npts,npts//6,n*star_points,dtype=int)
pts=np.zeros(0,dtype=int)
for j in range(n*star_points//2):
    nj=npts_fade[j]
    pts=np.append(pts,array([nj,nj,0,0]))
    
for k in range(nk):
    first = k*ns

    scale = 20

    ao = linspace(0,pi/3,n)
    
    S.add(on_frame(W,scale=scale,oangle=star_points,first=first,n=n-1,
                   asym=-0.6,orient_follow=0,orient=ao,polyfunc=nstar_coords,
                   arc_angle=-pi/3,pts=pts,object=k))
    
figure(S,'spacing','turbo')

###

e=0.4
R=40
ppl=1000
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e,pen_offset=pi/4),wheel=Wheel(a/3,a/5),ppl=ppl,loops=1,inside=True).rotate(-pi/5)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,1))

S=SpiroData()

nk=18
gs=0
n = W.n()//(nk+gs)
ns = W.n()//nk 

star_points=2
npts = def_factor*100
npts_fade = array([ 2+npts+int(npts*sin(1*pi*j/(n*star_points))) for j in range(n*star_points) ]) # 

pts=np.zeros(0,dtype=int)
for j in range(n*star_points//2):
    nj=npts_fade[j]
    pts=np.append(pts,array([nj,nj,0,0]))
    
for k in range(nk):
    first = k*ns
    
    scale = [ W.radius(j) for j in range(first,first+n) ]

    ao = -2*pi*k/nk+linspace(0,-pi/8,n)
    
    S.add(on_frame(W,scale=scale,oangle=star_points,first=first,n=n-1,
                   asym=0.8,orient_follow=W.n()//4,orient=ao,polyfunc=nstar_coords,
                   arc_angle=-pi/4,pts=pts,object=k))
    
figure(S,'time','emerald_woman')

###

e=0.2
R=40
ppl=1000
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e,pen_offset=pi/4),wheel=Wheel(a*(10/7),a/4),ppl=ppl,loops=10,inside=True).rotate(-pi/5)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,3))

S=SpiroData()

nk=3
gs=22
n = W.n()//(nk+gs)
ns = W.n()//nk 

star_points=6
npts = def_factor*100
npts_fade = array([ 2+npts+int(npts*sin(1*pi*j/(n*star_points))) for j in range(n*star_points) ]) # 
pts=np.zeros(0,dtype=int)
for j in range(n*star_points//2):
    nj=npts_fade[j]
    pts=np.append(pts,array([nj,nj,0,0]))
    
for k in range(nk):
    first = k*ns 
    
    scale = 15 

    ao = pi/4-pi*k/nk+linspace(0,-pi/4,n)
    
    S.add(on_frame(W,scale=scale,oangle=star_points,first=first,n=n-1,
                   asym=0.4,orient_follow=0,orient=ao,polyfunc=nstar_coords,
                   arc_angle=pi/1.3,pts=pts,object=k))
    
figure(S,'length','inferno')

###

e=0.2
R=40
ppl=1000
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e,pen_offset=pi/4),wheel=Wheel(a*(4/3),a/5),ppl=ppl,loops=4,inside=True).rotate(-pi/5)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,3))

S=SpiroData()

nk=3
gs=6
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts = def_factor*200
npts_fade = linspace(npts,npts//6,n,dtype=int)
pts=np.zeros(0,dtype=int)
for j in range(n):
    nj=npts_fade[j]
    pts=np.append(pts,array([0,0,nj,0]))
    
for k in range(nk):
    first = k*ns 
    
    scale = 5

    ao = pi/4-pi*0/nk+linspace(0,-pi/4,n)
    

    for prot in linspace(-pi/2,pi,4):
        S.add(on_frame(W,scale=scale,oangle=pi/1.5,first=first,n=n-1,fh=0,fb=0,
                       asym=0.2,orient_follow=0,orient=0,polyfunc=pcoords,
                       arc_angle=pi/3,pts=pts,object=k,prot=prot))
    

figure(S,'length','Oranges')

###

e=0.2
R=40
ppl=1000
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e,pen_offset=pi/4),wheel=Wheel(a*(4/3),a/5),ppl=ppl,loops=4,inside=True).rotate(-pi/6)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,2))

S=SpiroData()

nk=1
gs=0
n = 200 
ns = W.n()//nk 

npts = def_factor*100
npts_fade = array([ 50+npts+int(npts*cos(6*pi*j/n)) for j in range(n) ]) 
pts=np.zeros(0,dtype=int)
for j in range(n):
    nj=npts_fade[j]
    pts=np.append(pts,array([nj,0,nj,0]))
    
for k in range(nk):
    first = k*ns 
    
    scale = 3 

    ao = pi/4-pi*1/nk+linspace(0,pi,n)
    
    ip=0
    for prot in linspace(-pi/2,pi,4):
        S.add(on_frame(W,scale=scale,oangle=pi/1.5,first=first,n=n-1,fh=0,fb=0,
                       asym=0.4,orient_follow=1,orient=ao,polyfunc=pcoords,
                       arc_angle=pi/3,pts=pts,object=k*4+ip,prot=prot))
        ip+=1
    

figure(S,'length','autumn')

###

e=0.2
R=40
ppl=1000
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e,pen_offset=pi/4),wheel=Wheel(a*(2/3),a/5),ppl=ppl,loops=2,inside=True).rotate(-pi/6)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,2))

S=SpiroData()

nk=3
gs=3
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts = def_factor*200
npts_fade = linspace(npts,npts//6,n,dtype=int)
pts=np.zeros(0,dtype=int)
for j in range(n):
    nj=npts_fade[j]
    pts=np.append(pts,array([0,0,nj,0]))
    
for k in range(nk):
    first = k*ns
    
    scale = 10 

    ao = pi/2-pi*1/nk+linspace(0,pi,n)
    
    ip=0
    for prot in linspace(0,2*pi*(1-1/7),7):
        S.add(on_frame(W,scale=scale,oangle=pi/1.5,first=first,n=n-1,fh=0,fb=0,
                       asym=0.1,orient_follow=S.n()//3,orient=ao,polyfunc=pcoords,
                       arc_angle=[pi,-pi],pts=pts,object=k*4+ip,prot=prot))
        ip+=1
    

figure(S,'time','pretty_reds')

