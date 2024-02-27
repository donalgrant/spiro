import sys
sys.path.append('../..')
import argparse

from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_frame import *
from polygon import *

parser = argparse.ArgumentParser(description="Multi-Pinned Polygon Examples")
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

F._figname='Multi-Pinned_Polygons-'

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

T = roll(-50,-50,50,50,wheel=Wheel(5,2))

ppl=200
id = array( [ 1.0+0.5*cos(6*pi*j/ppl) for j in range(0,ppl) ] ).cumsum()
id *= T.max_path() / id[-1]
W = T.resample(id)

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

pts_fade = npts

for k in range(nk): 
    
    first = k*ns
    
    ao = 0 
    
    s = 1 
    asym = 0.3 
    nn = n
    aa = pi/9 

    S.add(on_frame(W,skip=1,asym=asym,oangle=pi/4,arc_angle=aa,fb=0,fh=0.0,first=first,orient=ao,
                   pts=pts_fade,scale=s,
                   n=nn,object=k,polyfunc=pcoords,prot=0,pin_coord=array([-40,40]),pin_to_frame=False))
    S.add(on_frame(W,skip=1,asym=asym,oangle=pi/4,arc_angle=aa,fb=0,fh=0.0,first=first,orient=ao,
                   pts=pts_fade,scale=s,
                   n=nn,object=k,polyfunc=pcoords,prot=0,pin_coord=array([40,-40]),pin_to_frame=False))
    
figure(S,'time','cmap1')


###

T = cIc(Ring(24),wheel=Wheel(6,6),loops=1,inside=False,ppl=2000)

ppl=500
id = linspace(0,ppl,ppl)
id *= T.max_path() / id[-1]
W = T.resample(id)

S = SpiroData()

nk=4
gs=8
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=250*def_factor

pts_fade = npts

for k in range(nk): 
    
    first = k*ns 

    ao = 0 

    s = 20 
    asym = 0.0 
    nn = n-1
    aa = -pi/3 

    for j in range(4):
        
        cr = 40
        pc = array([cr*cos(2*pi*j/4),cr*sin(2*pi*j/4)])
    
        S.add(on_frame(W,asym=asym,oangle=pi/3,arc_angle=aa,fb=0.2,fh=0.2,
                       first=first,orient=ao,pts=pts_fade,scale=s,
                       n=nn,object=k,polyfunc=tcoords,prot=0,pin_coord=pc,pin_to_frame=True,autoscale=False))

figure(S,'time','pretty_reds')

###

T = cIc(Ring(24),wheel=Wheel(6,6),loops=1,inside=True,ppl=2000)

ppl=500
id = linspace(0,ppl,ppl)
id *= T.max_path() / id[-1]
W = T.resample(id)

S = SpiroData()

nk=4
gs=4
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=250*def_factor
pts_fade = npts

for k in range(nk): 
    
    first = k*ns 

    ao = pi/5 

    s = 40
    asym = 0.0 
    nn = n-1
    aa = pi/3 

    npins=4
    for j in range(npins):
        
        cr = 45
        p0 = pi/4
        pc = array([cr*cos(2*pi*j/npins+p0),cr*sin(2*pi*j/npins+p0)])
    
        S.add(on_frame(W,asym=asym,oangle=pi/3,arc_angle=aa,fb=0,fh=0,first=first,orient=ao,pts=pts_fade,scale=s,
                       n=nn,object=k,polyfunc=tcoords,prot=0,pin_coord=pc,pin_to_frame=False,autoscale=False))

figure(S,'direction','hot')

###

T = cIc(Ring(24),wheel=Wheel(6,0),loops=1,inside=True,ppl=2000)

ppl=500
id = linspace(0,ppl,ppl)
id *= T.max_path() / id[-1]
W = T.resample(id)

S = SpiroData()

nk=3
gs=0
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=250*def_factor
pts_fade = npts

for k in range(nk): 
    
    first = k*ns

    ao = 0 

    s = 1 
    asym = 0.0 
    nn = n
    aa = 0 

    npins=3
    for j in range(npins):
        
        cr = 8
        p0 = pi/4
        pc = array([cr*cos(2*pi*j/npins+p0),cr*sin(2*pi*j/npins+p0)])
    
        S.add(on_frame(W,asym=asym,oangle=pi/3,arc_angle=aa,fb=0,fh=0,first=first,orient=ao,pts=pts_fade,scale=s,
                       n=nn,object=k,polyfunc=tcoords,prot=0,pin_coord=pc,pin_to_frame=False,autoscale=True))

figure(S,S.fradii(),'turbo')

###

e=0.6
R=20
ppl=2000
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e,pen_offset=0),wheel=Wheel(a/4,0),ppl=ppl,loops=1,inside=False).rotate(pi/9)

ppl=350
id = linspace(0,ppl,ppl)
id *= T.max_path() / id[-1]
W = T.resample(id)

S = SpiroData()

nk=W.n()//18
gs=W.n()//9
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=150*def_factor
pts_fade = npts

for k in range(nk): 
    
    first = k*ns 

    ao = pi/5 

    s = 5 
    asym = 0 
    nn = n
    aa = 0 

    npins=7
    for j in range(npins):
        
        cr = 35
        p0 = 0 
        pc = array([cr*cos(2*pi*j/npins+p0),cr*sin(2*pi*j/npins+p0)])
    
        S.add(on_frame(W,asym=asym,oangle=pi/2,arc_angle=aa,fb=0,fh=0,first=first,orient=ao,pts=pts_fade,scale=s,
                       n=nn,object=k,polyfunc=tcoords,prot=0,pin_coord=pc,pin_to_frame=True,autoscale=False))


figure(S,'time','twilight')

###

T = spiro_nstar(3,r1=24,r2=0.2,wheel=Wheel(2,0)).rotate(pi/6)

ppl=350
id = linspace(0,ppl,ppl)

id *= T.max_path() / id[-1]
W = T.resample(id)

S = SpiroData()

nk=W.n()//12
gs=0 # W.n()*5//6
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=150*def_factor
pts_fade = npts

for k in range(nk): 
    
    first = k*ns

    ao = 0 

    s = 1 
    asym = 0 
    nn = n
    aa = 0 

    npins=3
    for j in range(npins):
        
        cr = 15
        p0 = 0
        pc = array([cr*cos(2*pi*j/npins+p0),cr*sin(2*pi*j/npins+p0)])
    
        S.add(on_frame(W,asym=asym,oangle=pi/3,arc_angle=aa,fb=0,fh=0,first=first,orient=ao,pts=pts_fade,scale=s,
                       n=nn,object=k,polyfunc=tcoords,prot=0,pin_coord=pc,pin_to_frame=True,autoscale=True))


figure(S,'spacing','pale_pink')

###

T = spiro_nstar(7,r1=24,r2=0.6,wheel=Wheel(1,0)).rotate(pi/6)
ppl=350
id = linspace(0,ppl,ppl)
id *= T.max_path() / id[-1]
W = T.resample(id)

S = SpiroData()

nk=W.n()//7
gs=0 
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=150*def_factor
pts_fade = npts

for k in range(nk): 
    
    first = k*ns 

    ao = 0 

    s = 1 
    asym = 0 
    nn = n
    aa = 0 

    npins=7
    for j in range(npins):
        
        cr = 8
        p0 = 0
        pc = array([cr*cos(2*pi*j/npins+p0),cr*sin(2*pi*j/npins+p0)])
    
        S.add(on_frame(W,asym=asym,oangle=pi/3,arc_angle=aa,fb=0,fh=0,first=first,orient=ao,pts=pts_fade,scale=s,
                       n=nn,object=k,polyfunc=tcoords,prot=0,pin_coord=pc,pin_to_frame=True,autoscale=True))


figure(S,'time','OrRd')

###

T = spiro_ngon(6,wheel=Wheel(2,2)).rotate(pi/6) 

ppl=350
id = linspace(0,ppl,ppl)
id *= T.max_path() / id[-1]
W = T.resample(id)
S = SpiroData()

nk=6
gs=0
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=150*def_factor
pts_fade = linspace(npts,npts//10,n,dtype=int)

for k in range(2): 
    
    first = k*ns

    ao = linspace(0,pi/3,n) 

    s = 100 
    asym = 0 
    nn = n
    aa = 0 

    npins=12
    for j in range(npins):
        
        cr = 50+j*3
        p0 = k*2*pi/nk/12
        pc = array([cr*cos(2*pi*j/npins+p0),cr*sin(2*pi*j/npins+p0)])
            
        S.add(on_frame(W,asym=asym,oangle=4,arc_angle=aa,fb=0,fh=0,first=first,orient=ao,pts=pts_fade,scale=s,
                       n=nn,object=k,polyfunc=ngon_coords,prot=0,pin_coord=pc,pin_to_frame=False,autoscale=False))
        
figure(S,'y-direction','gist_heat')

###

T = integral_ellipticals(1,0.2,0.3,min_pen=1.0,rounds=9,circuits=8)
ppl=360
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

    ao = pi/4+linspace(0,pi/3,n)

    s = 1 
    asym = 0.1 
    nn = n
    aa = pi/6 

    npins=5
    for j in range(npins):
            
        cr = 30 
        p0 = pi/4 
        pc = array([cr*cos(2*pi*j/npins+p0),cr*sin(2*pi*j/npins+p0)])
            
        S.add(on_frame(W,asym=asym,oangle=pi/4,arc_angle=[aa,-aa],fb=0,fh=0,
                       first=first,orient=ao,pts=pts_fade,scale=s,
                       n=nn,object=k,polyfunc=pcoords,prot=0,pin_coord=pc,pin_to_frame=False,autoscale=True))
        
F.plot(S,color_scheme='time',cmap='turbo',alpha=0.4,dot_size=.1,no_frame=False)
figure(S,'t-waves','Wistia')

###

T = integral_ellipticals(1,0.2,0.2,min_pen=0.5,rounds=9,circuits=8)

ppl=360
id = linspace(0,ppl,ppl)
id *= T.max_path() / id[-1]
W = T.resample(id)

S = SpiroData()

nk=W.n()//31
gs=W.n()*1//21
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=150*def_factor
pts_fade = npts

for k in range(nk): 
    
    first = k*ns 

    s = 1 
    asym = 0.0 
    nn = n
    aa = -pi/6 

    npins=11
    for j in range(npins):
        
        ao = -pi*k/nk
        cr = 4 
        p0 = 0 
        pc = array([cr*cos(2*pi*j/npins+p0),cr*sin(2*pi*j/npins+p0)])
            
        S.add(on_frame(W,asym=asym,oangle=pi/5,arc_angle=aa,fb=0.2,fh=0.,first=first,orient=ao,pts=pts_fade,scale=s,
                       n=nn,object=k,polyfunc=pcoords,prot=0,pin_coord=pc,pin_to_frame=False,autoscale=False))

figure(S,'time','autumn')
