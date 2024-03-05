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

F._figname='Pin_Diagrams-'

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

T = cIc(Ring(24),wheel=Wheel(6,0),loops=1,inside=True,ppl=2000)

ppl=12
id = linspace(0,ppl,ppl)
id *= T.max_path() / id[-1]
W = T.resample(id)

S = SpiroData()
X = SpiroData()
Z = SpiroData()

nk=1
gs=0 
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=250*def_factor

pts_fade = array([],dtype=int)
for j in range(n):
    p = npts
    pts_fade = np.append(pts_fade,[p,p//2,p//2,p//2])

for k in range(nk): 
    
    first = 0

    s = 1 
    asym = 0.0 
    nn = n
    aa = 0 

    npins=1
    for j in range(npins):
        
        ao = 0 
        cr = 0 
        p0 = 0 
        pc = array([cr*cos(2*pi*j/npins+p0),cr*sin(2*pi*j/npins+p0)])
        
        X.add(cIc(Ring(2),wheel=W0).move(pc[0],pc[1]))
        for l in range(n):
            Z.add(cIc(Ring(0.2),wheel=W0).move(W.x[first+l],W.y[first+l]))
            
        S.add(on_frame(W,asym=asym,oangle=pi/2,arc_angle=aa,fb=0,fh=0,first=first,orient=ao,pts=pts_fade,scale=s,
                       n=nn,object=k,polyfunc=pcoords,prot=0,pin_coord=pc,pin_to_frame=False,autoscale=True))
        
F.plot(S,color_scheme='segment',cmap='OrRd',alpha=1,dot_size=.1,no_frame=False)
F.plot(X,color_scheme='red',dot_size=.1,new_fig=False)
F.plot(Z,color_scheme='green',dot_size=.1,new_fig=False)
F.plot(W,color_scheme='blue',dot_size=0.1,new_fig=False)

F.save_fig()

##

S = SpiroData()
X = SpiroData()
Z = SpiroData()

nk=1
gs=0 
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=250*def_factor

pts_fade = array([],dtype=int)
for j in range(n):
    p = npts
    pts_fade = np.append(pts_fade,[p,p//2,p//2])

for k in range(nk): 
    
    first = 0

    s = 1 
    asym = 0.0 
    nn = n
    aa = 0 

    npins=1
    for j in range(npins):
        
        ao = 0 
        cr = 0 
        p0 = 0 
        pc = array([cr*cos(2*pi*j/npins+p0),cr*sin(2*pi*j/npins+p0)])
        
        X.add(cIc(Ring(2),wheel=W0).move(pc[0],pc[1]))
        for l in range(n):
            Z.add(cIc(Ring(0.2),wheel=W0).move(W.x[first+l],W.y[first+l]))
            
        S.add(on_frame(W,asym=asym,oangle=pi/3,arc_angle=aa,fb=0,fh=0,first=first,orient=ao,pts=pts_fade,scale=s,
                       n=nn,object=k,polyfunc=tcoords,prot=0,pin_coord=pc,pin_to_frame=True,autoscale=True))
        
F.plot(S,color_scheme='segment',cmap='OrRd',alpha=1,dot_size=.1,no_frame=False)
F.plot(X,color_scheme='red',dot_size=.1,new_fig=False)
F.plot(Z,color_scheme='green',dot_size=.1,new_fig=False)
F.plot(W,color_scheme='blue',dot_size=0.1,new_fig=False)

F.save_fig()

##

S = SpiroData()
X = SpiroData()
Z = SpiroData()

nk=1
gs=0 
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=250*def_factor

pts_fade = array([],dtype=int)
for j in range(n):
    p = npts
    pts_fade = np.append(pts_fade,[p,p//2,p//2])

for k in range(nk): 
    
    first = 0

    s = 1 
    asym = 0.0 
    nn = n
    aa = 0 

    npins=1
    for j in range(npins):
        
        ao = 0 
        cr = 0 
        p0 = 0 
        pc = array([cr*cos(2*pi*j/npins+p0),cr*sin(2*pi*j/npins+p0)])
        
        X.add(cIc(Ring(2),wheel=W0).move(pc[0],pc[1]))
        for l in range(n):
            Z.add(cIc(Ring(0.2),wheel=W0).move(W.x[first+l],W.y[first+l]))
            
        S.add(on_frame(W,asym=asym,oangle=pi/3,arc_angle=aa,fb=0,fh=0,first=first,orient=ao,pts=pts_fade,scale=s,
                       n=nn,object=k,polyfunc=tcoords,prot=0,pin_coord=pc,pin_to_frame=False,autoscale=True))
        
F.plot(S,color_scheme='segment',cmap='OrRd',alpha=1,dot_size=.1,no_frame=False)
F.plot(X,color_scheme='red',dot_size=.1,new_fig=False)
F.plot(Z,color_scheme='green',dot_size=.1,new_fig=False)
F.plot(W,color_scheme='blue',dot_size=0.1,new_fig=False)

F.save_fig()

##

S = SpiroData()
X = SpiroData()
Z = SpiroData()

nk=1
gs=0 
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=250*def_factor

pts_fade = array([],dtype=int)
for j in range(n):
    p = npts
    pts_fade = np.append(pts_fade,[p,p//2,p//2])

for k in range(nk): 
    
    first = 0

    s = 1 
    asym = 0.0 
    nn = n
    aa = 0 

    npins=3
    for j in range(npins):
        
        ao = 0 
        cr = 10 
        p0 = 0 
        pc = array([cr*cos(2*pi*j/npins+p0),cr*sin(2*pi*j/npins+p0)])
        
        X.add(cIc(Ring(2),wheel=W0).move(pc[0],pc[1]))
        for l in range(n):
            Z.add(cIc(Ring(0.4),wheel=W0).move(W.x[first+l],W.y[first+l]))
            
        S.add(on_frame(W,asym=asym,oangle=pi/3,arc_angle=aa,fb=0,fh=0,first=first,orient=ao,pts=pts_fade,scale=s,
                       n=nn,object=k,polyfunc=tcoords,prot=0,pin_coord=pc,pin_to_frame=False,autoscale=True))
        
F.plot(S,color_scheme='segment',cmap='OrRd',alpha=1,dot_size=.1,no_frame=False)
F.plot(X,color_scheme='red',dot_size=.1,new_fig=False)
F.plot(Z,color_scheme='green',dot_size=.1,new_fig=False)
F.plot(W,color_scheme='blue',dot_size=0.1,new_fig=False)

F.save_fig()

##

S = SpiroData()
X = SpiroData()
Z = SpiroData()

nk=1
gs=0 
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=250*def_factor

pts_fade = array([],dtype=int)
for j in range(n):
    p = npts
    pts_fade = np.append(pts_fade,[p,p//2,p//2,p//2])

for k in range(nk): 
    
    first = 0

    s = 1 
    asym = 0.2
    nn = n
    aa = pi/6 

    npins=1
    for j in range(npins):
        
        ao = 0 
        cr = 0 
        p0 = 0 
        pc = array([cr*cos(2*pi*j/npins+p0),cr*sin(2*pi*j/npins+p0)])
        
        X.add(cIc(Ring(2),wheel=W0).move(pc[0],pc[1]))
        for l in range(n):
            Z.add(cIc(Ring(0.5),wheel=W0).move(W.x[first+l],W.y[first+l]))
            
        S.add(on_frame(W,asym=asym,oangle=pi/4,arc_angle=aa,fb=0,fh=0,first=first,orient=ao,pts=pts_fade,scale=s,
                       n=nn,object=k,polyfunc=pcoords,prot=0,pin_coord=pc,pin_to_frame=False,autoscale=True))
        
F.plot(S,color_scheme='segment',cmap='OrRd',alpha=1,dot_size=.1,no_frame=False)
F.plot(X,color_scheme='red',dot_size=.1,new_fig=False)
F.plot(Z,color_scheme='green',dot_size=.1,new_fig=False)
F.plot(W,color_scheme='blue',dot_size=0.1,new_fig=False)

F.save_fig()

##

S = SpiroData()
X = SpiroData()
Z = SpiroData()

nk=1
gs=0 
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=250*def_factor

pts_fade = array([],dtype=int)
for j in range(n):
    p = npts
    pts_fade = np.append(pts_fade,[p,p//2,p//2,p//2])

for k in range(nk): 
    
    first = 0

    s = 1 
    asym = 0.2
    nn = n
    aa = pi/6 

    npins=3
    for j in range(npins):
        
        ao = 0 
        cr = 40 
        p0 = 0 
        pc = array([cr*cos(2*pi*j/npins+p0),cr*sin(2*pi*j/npins+p0)])
        
        X.add(cIc(Ring(2),wheel=W0).move(pc[0],pc[1]))
        for l in range(n):
            Z.add(cIc(Ring(0.5),wheel=W0).move(W.x[first+l],W.y[first+l]))
            
        S.add(on_frame(W,asym=asym,oangle=pi/4,arc_angle=aa,fb=0,fh=0,first=first,orient=ao,pts=pts_fade,scale=s,
                       n=nn,object=k,polyfunc=pcoords,prot=0,pin_coord=pc,pin_to_frame=False,autoscale=True))
        
F.plot(S,color_scheme='segment',cmap='OrRd',alpha=1,dot_size=.1,no_frame=False)
F.plot(X,color_scheme='red',dot_size=.1,new_fig=False)
F.plot(Z,color_scheme='green',dot_size=.1,new_fig=False)
F.plot(W,color_scheme='blue',dot_size=0.1,new_fig=False)

F.save_fig()

##

S = SpiroData()
X = SpiroData()
Z = SpiroData()

nk=1
gs=0 
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=250*def_factor

pts_fade = array([],dtype=int)
for j in range(n):
    p = npts
    pts_fade = np.append(pts_fade,[p,p//2,p//2,p//2])

for k in range(nk): 
    
    first = 0

    s = 10 
    asym = 0.2
    nn = n
    aa = 0

    npins=3
    for j in range(npins):
        
        ao = 0 
        cr = 40 
        p0 = 0 
        pc = array([cr*cos(2*pi*j/npins+p0),cr*sin(2*pi*j/npins+p0)])
        
        X.add(cIc(Ring(2),wheel=W0).move(pc[0],pc[1]))
        for l in range(n):
            Z.add(cIc(Ring(0.5),wheel=W0).move(W.x[first+l],W.y[first+l]))
            
        S.add(on_frame(W,asym=asym,oangle=pi/4,arc_angle=aa,fb=0,fh=0,first=first,orient=ao,pts=pts_fade,scale=s,
                       n=nn,object=k,polyfunc=pcoords,prot=0,pin_coord=pc,pin_to_frame=False,autoscale=False))
        
F.plot(S,color_scheme='segment',cmap='OrRd',alpha=1,dot_size=.1,no_frame=False)
F.plot(X,color_scheme='red',dot_size=.1,new_fig=False)
F.plot(Z,color_scheme='green',dot_size=.1,new_fig=False)
F.plot(W,color_scheme='blue',dot_size=0.1,new_fig=False)

F.save_fig()

##

S = SpiroData()
X = SpiroData()
Z = SpiroData()

nk=1
gs=0 
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=250*def_factor

pts_fade = array([],dtype=int)
for j in range(n):
    p = npts
    pts_fade = np.append(pts_fade,[p,p//2,p//2,p//2])

for k in range(nk): 
    
    first = 0

    s = 10 
    asym = 0.2
    nn = n
    aa = 0

    npins=3
    for j in range(npins):
        
        ao = 0 
        cr = 40 
        p0 = 0 
        pc = array([cr*cos(2*pi*j/npins+p0),cr*sin(2*pi*j/npins+p0)])
        
        X.add(cIc(Ring(2),wheel=W0).move(pc[0],pc[1]))
        for l in range(n):
            Z.add(cIc(Ring(0.5),wheel=W0).move(W.x[first+l],W.y[first+l]))
            
        S.add(on_frame(W,asym=asym,oangle=pi/4,arc_angle=aa,fb=0,fh=0,first=first,orient=ao,pts=pts_fade,scale=s,
                       n=nn,object=k,polyfunc=pcoords,prot=0,pin_coord=pc,pin_to_frame=True,autoscale=False))
        
F.plot(S,color_scheme='segment',cmap='OrRd',alpha=1,dot_size=.1,no_frame=False)
F.plot(X,color_scheme='red',dot_size=.1,new_fig=False)
F.plot(Z,color_scheme='green',dot_size=.1,new_fig=False)
F.plot(W,color_scheme='blue',dot_size=0.1,new_fig=False)

F.save_fig()

##

S = SpiroData()
X = SpiroData()
Z = SpiroData()

nk=3
gs=1
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=250*def_factor

pts_fade = array([],dtype=int)
for j in range(n):
    p = npts
    pts_fade = np.append(pts_fade,[p,p//2,p//2,p//2])

for k in range(nk): 
    
    first = 0

    s = 1 
    asym = 0.0
    nn = n
    aa = pi/4

    npins=3
    for j in range(npins):
        
        ao = 0 
        cr = 40 
        p0 = 0 
        pc = array([cr*cos(2*pi*j/npins+p0),cr*sin(2*pi*j/npins+p0)])
        
        X.add(cIc(Ring(2),wheel=W0).move(pc[0],pc[1]))
        for l in range(W.n()):
            Z.add(cIc(Ring(0.5),wheel=W0).move(W.x[first+l],W.y[first+l]))
            
        S.add(on_frame(W,asym=asym,oangle=pi/2,arc_angle=aa,fb=0,fh=0,first=first,orient=ao,pts=pts_fade,scale=s,
                       n=nn,object=k,polyfunc=pcoords,prot=0,pin_coord=pc,pin_to_frame=False,autoscale=True))
        
F.plot(S,color_scheme='segment',cmap='OrRd',alpha=1,dot_size=.1,no_frame=False)
F.plot(X,color_scheme='red',dot_size=.1,new_fig=False)
F.plot(Z,color_scheme='green',dot_size=.1,new_fig=False)
F.plot(W,color_scheme='blue',dot_size=0.1,new_fig=False)

F.save_fig()

##

S = SpiroData()
X = SpiroData()
Z = SpiroData()

nk=3
gs=1
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=250*def_factor

pts_fade = array([],dtype=int)
for j in range(n):
    p = npts
    pts_fade = np.append(pts_fade,[p,p//2,p//2,p//2])

for k in range(nk): 
    
    first = 0

    s = 1 
    asym = 0.0
    nn = n
    aa = pi/4

    npins=3
    for j in range(npins):
        
        ao = 0 
        cr = 40 
        p0 = 0 
        pc = array([cr*cos(2*pi*j/npins+p0),cr*sin(2*pi*j/npins+p0)])
        
        X.add(cIc(Ring(2),wheel=W0).move(pc[0],pc[1]))
        for l in range(W.n()):
            Z.add(cIc(Ring(0.5),wheel=W0).move(W.x[first+l],W.y[first+l]))
            
        S.add(on_frame(W,asym=asym,oangle=pi/2,arc_angle=aa,fb=0.3,fh=0,first=first,orient=ao,pts=pts_fade,scale=s,
                       n=nn,object=k,polyfunc=pcoords,prot=0,pin_coord=pc,pin_to_frame=False,autoscale=True))
        
F.plot(S,color_scheme='segment',cmap='OrRd',alpha=1,dot_size=.1,no_frame=False)
F.plot(X,color_scheme='red',dot_size=.1,new_fig=False)
F.plot(Z,color_scheme='green',dot_size=.1,new_fig=False)
F.plot(W,color_scheme='blue',dot_size=0.1,new_fig=False)

F.save_fig()

##

S = SpiroData()
X = SpiroData()
Z = SpiroData()

nk=3
gs=1
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=250*def_factor

pts_fade = array([],dtype=int)
for j in range(n):
    p = npts
    pts_fade = np.append(pts_fade,[p,p//2,p//2,p//2])

for k in range(nk): 
    
    first = 0

    s = 1 
    asym = 0.0
    nn = n
    aa = 0

    npins=3
    for j in range(npins):
        
        ao = linspace(0,pi/2,n)

        cr = 40 
        p0 = 0 
        pc = array([cr*cos(2*pi*j/npins+p0),cr*sin(2*pi*j/npins+p0)])
        
        X.add(cIc(Ring(2),wheel=W0).move(pc[0],pc[1]))
        for l in range(n):
            Z.add(cIc(Ring(0.5),wheel=W0).move(W.x[first+l],W.y[first+l]))
            
        S.add(on_frame(W,asym=asym,oangle=pi/2,arc_angle=aa,fb=0.,fh=0,first=first,orient=ao,pts=pts_fade,scale=s,
                       n=nn,object=k,polyfunc=pcoords,prot=0,pin_coord=pc,pin_to_frame=False,autoscale=True))
        
F.plot(S,color_scheme='segment',cmap='OrRd',alpha=1,dot_size=.1,no_frame=False)
F.plot(X,color_scheme='red',dot_size=.1,new_fig=False)
F.plot(Z,color_scheme='green',dot_size=.1,new_fig=False)
F.plot(W,color_scheme='blue',dot_size=0.1,new_fig=False)

F.save_fig()

##

S = SpiroData()
X = SpiroData()
Z = SpiroData()

nk=3
gs=1
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=250*def_factor

pts_fade = array([],dtype=int)
for j in range(n):
    p = npts
    pts_fade = np.append(pts_fade,[p,p//2,p//2,p//2])

for k in range(nk): 
    
    first = 0

    s = 1 
    asym = 0.0
    nn = n
    aa = 0

    npins=3
    for j in range(npins):
        
        ao = linspace(0,pi/2,n)

        cr = 40 
        p0 = 0 
        pc = array([cr*cos(2*pi*j/npins+p0),cr*sin(2*pi*j/npins+p0)])
        
        X.add(cIc(Ring(2),wheel=W0).move(pc[0],pc[1]))
        for l in range(n):
            Z.add(cIc(Ring(0.5),wheel=W0).move(W.x[first+l],W.y[first+l]))
            
        S.add(on_frame(W,asym=asym,oangle=pi/2,arc_angle=aa,fb=0.,fh=0,first=first,orient=ao,pts=pts_fade,scale=s,
                       n=nn,object=k,polyfunc=pcoords,prot=0,pin_coord=pc,pin_to_frame=True,autoscale=True))
        
F.plot(S,color_scheme='segment',cmap='OrRd',alpha=1,dot_size=.1,no_frame=False)
F.plot(X,color_scheme='red',dot_size=.1,new_fig=False)
F.plot(Z,color_scheme='green',dot_size=.1,new_fig=False)
F.plot(W,color_scheme='blue',dot_size=0.1,new_fig=False)

F.save_fig()

##

S = SpiroData()
X = SpiroData()
Z = SpiroData()

nk=1
gs=0 
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=250*def_factor

pts_fade = array([],dtype=int)
for j in range(n):
    p = npts
    pts_fade = np.append(pts_fade,[p,p,p])

for k in range(nk): 
    
    first = 0

    asym = 0.3 
    nn = n-1
    aa = 0 
    oa = pi/5 

    s=1
    
    npins=2
    for j in range(npins):
        
        cr = 25
        p0 = pi/2
        pc = array([cr*cos(2*pi*j/npins+p0),cr*sin(2*pi*j/npins+p0)])
        
        X.add(cIc(Ring(2),wheel=W0).move(pc[0],pc[1]))
        for l in range(n):
            Z.add(cIc(Ring(0.4),wheel=W0).move(W.x[first+l],W.y[first+l]))
            
        S.add(on_frame(W,asym=asym,oangle=oa,arc_angle=aa,fb=0.,fh=0,first=first,orient=0,pts=pts_fade,scale=s,
                       n=nn,object=k,polyfunc=tcoords,prot=0,
                       pin_coord=pc,pin_to_frame=False,autoscale=True,pinned_vertex=j+1))
        
F.plot(S,color_scheme='segment',cmap='OrRd',alpha=1,dot_size=.1,no_frame=False)

F.plot(X,color_scheme='red',dot_size=.1,new_fig=False)
F.plot(Z,color_scheme='green',dot_size=.1,new_fig=False)
F.plot(W,color_scheme='blue',dot_size=0.1,new_fig=False)

F.save_fig()

##

S = SpiroData()
X = SpiroData()
Z = SpiroData()

nk=1
gs=0 
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=250*def_factor
pts_fade=npts

for k in range(nk): 
    
    first = 0

    asym = 0.1 
    nn = n-1
    aa = 0 
    oa = pi/5 

    s=1
    
    npins=3
    for j in range(npins):
        
        cr = 25
        p0 = pi/2
        pc = array([cr*cos(2*pi*j/npins+p0),cr*sin(2*pi*j/npins+p0)])
        
        X.add(cIc(Ring(2),wheel=W0).move(pc[0],pc[1]))
        for l in range(n):
            Z.add(cIc(Ring(1),wheel=W0).move(W.x[first+l],W.y[first+l]))
            
        S.add(on_frame(W,asym=asym,oangle=oa,arc_angle=aa,fb=0.,fh=0,first=first,orient=0,pts=pts_fade,scale=s,
                       n=nn,object=k,polyfunc=pcoords,prot=0,
                       pin_coord=pc,pin_to_frame=True,autoscale=True,pinned_vertex=j+1))
        
F.plot(S,color_scheme='segment',cmap='OrRd',alpha=1,dot_size=.1,no_frame=False)

F.plot(X,color_scheme='red',dot_size=.1,new_fig=False)
F.plot(Z,color_scheme='green',dot_size=.1,new_fig=False)
F.plot(W,color_scheme='blue',dot_size=0.1,new_fig=False)

F.save_fig()

##

S = SpiroData()
X = SpiroData()
Z = SpiroData()

nk=3
gs=0 
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=250*def_factor
pts_fade=npts

for k in range(nk): 
    
    asym = 0.1 
    nn = 1
    aa = 0 
    oa = pi/5

    s=1
    
    npins=2
    for j in range(npins):
        
        cr = 25
        p0 = pi/2
        pc = array([cr*cos(2*pi*j/npins+p0),cr*sin(2*pi*j/npins+p0)])
        
        first = k + j*W.n()//2
        
        X.add(cIc(Ring(2),wheel=W0).move(pc[0],pc[1]))
        for l in range(W.n()):
            Z.add(cIc(Ring(1),wheel=W0).disp(W.xy(first+l)))
            
        S.add(on_frame(W,asym=asym,oangle=oa,arc_angle=aa,fb=k*0.1,fh=0.0,first=first,orient=0,pts=pts_fade,scale=s,
                       n=nn,object=k,polyfunc=tcoords,prot=0,
                       pin_coord=pc,pin_to_frame=False,autoscale=True,pinned_vertex=j+1))
        
F.plot(S,color_scheme='segment',cmap='OrRd',alpha=1,dot_size=.1,no_frame=False)

F.plot(X,color_scheme='red',dot_size=.1,new_fig=False)
F.plot(Z,color_scheme='green',dot_size=.1,new_fig=False)
F.plot(W,color_scheme='blue',dot_size=0.1,new_fig=False)

F.save_fig()
