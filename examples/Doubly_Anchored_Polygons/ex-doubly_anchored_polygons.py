import sys
sys.path.append('../..')
import argparse

from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_frame import *
from polygon import *

parser = argparse.ArgumentParser(description="Doubly-Anchored Polygon Examples")
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

F._figname='Doubly_Anchored_Polygons-'

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

T = cIc(Ring(24),wheel=Wheel(6,3),loops=1,inside=True,ppl=2000)

ppl=360
id = linspace(0,ppl,ppl)
id *= T.max_path() / id[-1]
W = T.resample(id)

S = SpiroData()

nk=1
gs=0 
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts=250*def_factor
pts_fade = linspace(npts,npts//8,n,dtype=int)


for k in range(nk): 
    
    first = 0 

    asym = linspace(-0.2,0.2,n) 
    nn = n-1
    aa = 0 
    oa = linspace(pi/9,pi/2,n)

    s=1
    
    npins=3
    for j in range(npins):
        
        cr =25
        p0 = 0 
        pc = array([cr*cos(2*pi*j/npins+p0),cr*sin(2*pi*j/npins+p0)])
        
        S.add(on_frame(W,asym=asym,oangle=oa,arc_angle=aa,fb=0.,fh=0,first=first,orient=0,pts=pts_fade,scale=s,
                       n=nn,object=k,polyfunc=tcoords,prot=0,
                       pin_coord=pc,pin_to_frame=True,autoscale=True,pinned_vertex=2))
        
figure(S,'time','turbo')

###

T = cIc(Ring(24),wheel=Wheel(6,7),loops=1,inside=True,ppl=2000)

ppl=720
id = linspace(0,ppl,ppl)
id *= T.max_path() / id[-1]
W = T.resample(id).rotate(pi/7)

S = SpiroData()

npins=2
nk=3
gs=1
n = W.n()//(nk+gs)//npins
ns = W.n()//nk 

npts=300*def_factor

pts_fade = array([],dtype=int)
for j in range(n):
    p = npts//5 + 2*npts//3 * j // n
    pts_fade = np.append(pts_fade,[p,p,p,p])

for k in range(nk): 
    
    asym = 0 
    nn = n-1
    aa = pi/6
    oa = pi/4 

    s=1
    
    for j in range(npins):
        
        cr =5
        p0 = pi/2 
        pc = array([cr*cos(2*pi*j/npins+p0),cr*sin(2*pi*j/npins+p0)])
        
        first = k*ns + j*W.n()//npins
        ao = 0
        
        S.add(on_frame(W,asym=asym,oangle=oa,arc_angle=aa,fb=0,fh=0,first=first,orient=ao,pts=pts_fade,scale=s,
                       n=nn,object=k,polyfunc=pcoords,prot=0,
                       pin_coord=pc,pin_to_frame=True,autoscale=True,pinned_vertex=2))
        
figure(S,S.fradii(),'autumn')

###

T = cIc(Ring(24),wheel=Wheel(6,7),loops=1,inside=True,ppl=720)
W = T.rotate(pi/7)

S = SpiroData()

npins=2
nk=1
gs=0
n = W.n()//(nk+gs)//npins
ns = W.n()//nk 

npts=150*def_factor

pts_fade = array([],dtype=int)
for j in range(n):
    p = npts//3 + 2*npts//3 * j // n
    pts_fade = np.append(pts_fade,[p,p,p,p])

for k in range(nk): 
    
    asym = 0
    nn = n-1
    aa = pi/2
    oa = pi/4

    s=1
    
    for j in range(npins):
        
        cr = 10
        p0 = 0
        pc = array([cr*cos(2*pi*j/npins+p0),cr*sin(2*pi*j/npins+p0)])
        
        first = k*ns + j*W.n()//npins
        ao = pi*j/npins/2
        
        S.add(on_frame(W,asym=asym,oangle=oa,arc_angle=aa,fb=0.2,fh=0.2,first=first,orient=ao,pts=pts_fade,scale=s,
                       n=nn,object=k,polyfunc=pcoords,prot=0,
                       pin_coord=pc,pin_to_frame=False,autoscale=True,pinned_vertex=2))
        
figure(S,'direction','turbo')

###

T = cIe(Ellipse(24,0.3),wheel=Wheel(4,4),loops=0.4,inside=True,ppl=1500)
W = T.rotate(pi/7)

S = SpiroData()

npins=2
nk=1
gs=0
n = W.n()//(nk+gs)//npins
ns = W.n()//nk 

npts=250*def_factor

pts_fade = array([],dtype=int)
for j in range(n):
    p = npts//10 + 9*npts//10 * j // n
    pts_fade = np.append(pts_fade,[p,p,p])

pc = array([ [0,0], [-25,10] ])

for k in range(nk): 
    
    asym = linspace(0,0.1,n) 
    nn = n-1
    aa = pi/2
    oa = linspace(pi/4,pi/3,n)

    s=1
    
    for j in range(npins):
        
        cr = 0
        p0 = 0
        first = k*ns + j*W.n()//npins
        ao = pi*j/npins/2 + linspace(0,pi,n)
        
        S.add(on_frame(W,asym=asym,oangle=oa,arc_angle=aa,fb=0.2,fh=0.2,first=first,orient=ao,pts=pts_fade,scale=s,
                       n=nn,object=k,polyfunc=tcoords,prot=0,
                       pin_coord=pc[1-j],pin_to_frame=True,autoscale=True,pinned_vertex=1))
        
figure(S,'spacing','pretty_reds')

###

T = roll(-50,20,50,20,wheel=Wheel(25,15))

ppl=250
id = frame_sampling(ppl,parm=5,spacing='sinusoid',deramp=True,reverse=False,repeat=4)
mp = T.max_path()
W = T.resample(id*mp)

S = SpiroData()

npins=4
nk=1
gs=0
n = W.n()//(nk+gs)//(npins//2)
ns = W.n()//nk 

npts=250*def_factor
pts_fade = npts

pc = array([ [-30,0], [-10,0], [10,0], [30,0] ])

for k in range(nk): 
    
    asym = 0 
    aa = pi/4
    oa = pi/3

    s=1
    
    for j in range(npins):
        
        cr = 0
        p0 = 0
        first = k*ns + j*W.n()//npins
    
        nn = min(n-1,W.n()-first)

        ao = linspace(0,-pi/6,nn) 
        
        offset=linspace(0,0.5,nn)
        S.add(on_frame(W,asym=asym,oangle=oa,arc_angle=aa,fb=offset,fh=offset,
                       first=first,orient=ao,pts=pts_fade,scale=s,
                       n=nn,object=k,polyfunc=pcoords,prot=0,
                       pin_coord=pc[j],pin_to_frame=False,autoscale=True,pinned_vertex=2))
        
figure(S,'spacing','inferno')

###

T = roll(-50,20,50,20,wheel=Wheel(25,15))

ppl=1000

id = frame_sampling(ppl,parm=6,spacing='sinusoid',deramp=True,reverse=False,repeat=10)
mp = T.max_path()

W = T.resample(id*mp)

S = SpiroData()

npins=2
nk=1
gs=0
n = W.n()//(nk+gs)//npins//2
ns = W.n()//nk 

npts=250*def_factor

pts_fade = array([],dtype=int)
for j in range(n):
    p = npts//5 + npts - int(npts*cos(2*pi*j/n))
    pts_fade = np.append(pts_fade,[p,p,p,p])

center=W.n()//2
offset=-W.n()//20
gap = W.n()//10

pinc = array([ center-offset, center+offset ])

pc = array([ W.xy(pinc[0]), W.xy(pinc[1]) ])

firsts = array([ pinc[0]-n-gap, pinc[1]+gap ])

for k in range(nk): 
    
    asym = 0 
    aa = pi/4
    oa = pi/3

    s=1
    
    for j in range(npins):
        
        cr = 0
        p0 = 0
        first = firsts[j]
    
        nn = min(n-1,W.n()-first)

        max_ao = -pi/2
        
        ao = linspace(max_ao,0,nn) if j>0 else linspace(0,max_ao,nn)
        
        offset=linspace(0.3,0,nn) if j>0 else linspace(0,0.3,nn)
        
        S.add(on_frame(W,asym=asym,oangle=oa,arc_angle=aa,fb=offset,fh=offset,
                       first=first,orient=ao,pts=pts_fade,scale=s,
                       n=nn,object=k,polyfunc=pcoords,prot=0,
                       pin_coord=pc[j],pin_to_frame=False,autoscale=True,pinned_vertex=2))
        
figure(S,'fwidth','emerald_woman')

###

T = cIe(Ellipse(24,0.3),wheel=Wheel(4,4),loops=1.0,inside=True,ppl=1000)

ppl=1000
id = frame_sampling(ppl,parm=12,spacing='sinusoid',deramp=True,reverse=False,repeat=4)
mp = T.max_path()

W = T.resample(id*mp)

S = SpiroData()

npins=2
nk=1
gs=0
n = W.n()//(nk+gs)//npins//2
ns = W.n()//nk 

npts=250*def_factor

pts_fade = array([],dtype=int)
for j in range(n):
    p = npts//3 + npts - int(npts*cos(2*pi*j/n))
    pts_fade = np.append(pts_fade,[p,p,p,p])

offset=W.n()//npins//2
gap = W.n()//10

pinc = np.zeros(npins,dtype=int)
firsts = np.zeros(npins,dtype=int)
pc   = np.full((npins,2),0)

for i in range(npins):
    pinc[i]=(i+1)*W.n()//(npins+1) + offset
    pc[i]  = W.xy(pinc[i])
    firsts[i] = pinc[i]-n-gap
    
for k in range(nk): 
    
    asym = 0 
    aa = pi/4
    oa = pi/3 

    s=1
    
    for j in range(npins):
        
        cr = 0
        p0 = 0

        first = firsts[j]
    
        nn = min(n-1,W.n()-first)

        max_ao = -2*pi
        
        ao = linspace(0,max_ao,n)
        
        offset= 0 
        
        S.add(on_frame(W,asym=asym,oangle=oa,arc_angle=aa,fb=offset,fh=offset,
                       first=first,orient=ao,pts=pts_fade,scale=s,
                       n=nn,object=k,polyfunc=pcoords,prot=0,
                       pin_coord=pc[j],pin_to_frame=False,autoscale=True,pinned_vertex=1))

figure(S,'time','gist_heat')

###

maj=24
ecc=0.3
a = circum(maj,semi_minor(maj,ecc))/(2*pi)/6
T = cIe(Ellipse(maj,ecc),wheel=Wheel(a,a),loops=1.0,inside=True,ppl=2000)

ppl=2000

id = frame_sampling(ppl,parm=0,spacing='sinusoid',deramp=True,reverse=False,repeat=1)
mp = T.max_path()

W = T.resample(id*mp)

S = SpiroData()

npins=6
nk=1
gs=0
n = W.n()//(nk+gs)//npins//3
ns = W.n()//nk 

npts=250*def_factor

pts_fade = array([],dtype=int)
for j in range(n):
    p = npts//3 + npts - int(npts*cos(2*pi*j/n))
    pts_fade = np.append(pts_fade,[p,p,p,p])

offset=W.n()//npins//2
gap = W.n()//5

pinc = np.zeros(npins,dtype=int)
firsts = np.zeros(npins,dtype=int)
pc   = np.full((npins,2),0)

for i in range(npins):
    pinc[i]=i*W.n()//(npins+1) + offset
    pc[i]  = W.xy(pinc[i])
    firsts[i] = pinc[i]+n
    
for k in range(nk): 
    
    asym = 0
    aa = pi/4
    oa = pi/3 

    s=1
    
    for j in range(npins):
        
        cr = 0
        p0 = 0

        first = firsts[j]
    
        nn = n-4

        max_ao = -pi
        
        ao = linspace(0,max_ao,n)
        
        offset= 0.3 
        
        S.add(on_frame(W,asym=asym,oangle=oa,arc_angle=aa,fb=offset,fh=offset,
                       first=first,orient=ao,pts=pts_fade,scale=s,
                       n=nn,object=k,polyfunc=pcoords,prot=0,
                       pin_coord=pc[j],pin_to_frame=True,autoscale=True,pinned_vertex=j))
        
figure(S,'time','cmap1')

##

S = SpiroData()

npins=1
nk=1
gs=0
n = W.n()//(nk+gs)//npins//6
ns = W.n()//nk 

npts=250*def_factor

pts_fade = array([],dtype=int)
for j in range(n):
    p = npts//3 + npts - int(npts*cos(2*pi*j/n))
    pts_fade = np.append(pts_fade,[p,p,p,p])

gap = W.n()//11
offset=W.n()//npins//2 + gap

pinc = np.zeros(npins,dtype=int)
firsts = np.zeros(npins,dtype=int)
pc   = np.full((npins,2),0)

for i in range(npins):
    pinc[i]=i*W.n()//(npins+1) + offset
    pc[i]  = W.xy(pinc[i])
    firsts[i] = pinc[i]+n
    
for k in range(nk): 
    
    asym = linspace(0,0.1,n) 
    aa = pi/4
    oa = pi/3 

    s=1
    
    for j in range(npins):
        
        cr = 0
        p0 = 0

        first = firsts[j]+4*k*n
    
        nn = n-1

        max_ao = -pi*2
        
        ao = linspace(0,max_ao,n)
        
        offset= 0.5
        
        S.add(on_frame(W,asym=asym,oangle=oa,arc_angle=aa,fb=offset,fh=offset,
                       first=first,orient=ao,pts=pts_fade,scale=s,
                       n=nn,object=k,polyfunc=pcoords,prot=0,
                       pin_coord=pc[j],pin_to_frame=True,autoscale=True,pinned_vertex=k+3))
        
figure(S,'fpolars','hot')

###

maj=24
ecc=0.3
a = circum(maj,semi_minor(maj,ecc))/(2*pi)/6
T = cIe(Ellipse(maj,ecc),wheel=Wheel(a,2*a),loops=1.0,inside=True,ppl=2000)

ppl=1000

id = frame_sampling(ppl,parm=0,spacing='sinusoid',deramp=True,reverse=False,repeat=1)
mp = T.max_path()

W = T.resample(id*mp)

S = SpiroData()

npins=1
nk=1
gs=0
n = W.n()//(nk+gs)//npins * 2 // 3 
ns = W.n()//nk 

npts=250*def_factor

pts_fade = array([],dtype=int)
for j in range(n):
    p = npts//3 + npts - int(npts*cos(2*pi*j/n))
    pts_fade = np.append(pts_fade,[p,p,p,p])

gap = W.n()//11
offset=W.n()//npins//2 + gap

pinc = np.zeros(npins,dtype=int)
firsts = np.zeros(npins,dtype=int)
pc   = np.full((npins,2),0)

for i in range(npins):
    pinc[i]=i*W.n()//(npins+1) + offset
    pc[i]  = W.xy(pinc[i])
    firsts[i] = pinc[i]+n
    
for k in range(nk): 
    
    asym = linspace(0,0.1,n) 
    aa = pi/4
    oa = pi/3 

    s=1
    
    for j in range(npins):
        
        cr = 0
        p0 = 0

        first = firsts[j]+3*k*n
    
        nn = n-1

        max_ao = -pi*2
        
        ao = linspace(0,max_ao,n)
        
        offset= 0.5
        
        S.add(on_frame(W,asym=asym,oangle=oa,arc_angle=aa,fb=offset,fh=offset,
                       first=first,orient=ao,pts=pts_fade,scale=s,
                       n=nn,object=k,polyfunc=pcoords,prot=0,
                       pin_coord=pc[j],pin_to_frame=True,autoscale=True,pinned_vertex=2))
        
figure(S,'y-direction','pretty_reds')

###

maj=24
ecc=0.3
a = circum(maj,semi_minor(maj,ecc))/(2*pi)/6
T = cIe(Ellipse(maj,ecc),wheel=Wheel(a,2*a),loops=1.0,inside=True,ppl=2000)

ppl=2000

id = frame_sampling(ppl,parm=0,spacing='sinusoid',deramp=True,reverse=False,repeat=1)
mp = T.max_path()

W = T.resample(id*mp)

S = SpiroData()

npins=1
nk=1
gs=0
n = W.n()//(nk+gs)//npins // 3 
ns = W.n()//nk 

npts=250*def_factor

pts_fade = array([],dtype=int)
for j in range(n):
    p = npts//3 + npts - int(npts*cos(2*pi*j/n))
    pts_fade = np.append(pts_fade,[p,p,p,p])

gap = W.n()//11
offset=W.n()//npins//2 + gap

pinc = np.zeros(npins,dtype=int)
firsts = np.zeros(npins,dtype=int)
pc   = np.full((npins,2),0)

for i in range(npins):
    pinc[i]=i*W.n()//(npins+1) + offset
    pc[i]  = W.xy(pinc[i])
    firsts[i] = pinc[i]+n
    
for k in range(nk): 
    
    asym = linspace(0,0.1,n) 
    aa = pi/4
    oa = pi/3 

    s=1
    
    for j in range(npins):
        
        cr = 0
        p0 = 0

        first = firsts[j]+3*k*n
    
        nn = n-1

        max_ao = -pi*2
        
        ao = linspace(0,max_ao,n)
        
        offset= 0.5
        
        S.add(on_frame(W,asym=asym,oangle=oa,arc_angle=aa,fb=offset,fh=offset,
                       first=first,orient=ao,pts=pts_fade,scale=s,
                       n=nn,object=k,polyfunc=pcoords,prot=0,
                       pin_coord=pc[j],pin_to_frame=True,autoscale=True,pinned_vertex=2))
        
figure(S,'y-direction','pretty_blues')

###

maj=24
ecc=0.0
a = circum(maj,semi_minor(maj,ecc))/(2*pi)/3
T = cIe(Ellipse(maj,ecc),wheel=Wheel(a,a),loops=1.0,inside=True,ppl=2000)

ppl=1500

id = frame_sampling(ppl,parm=0,spacing='sinusoid',deramp=True,reverse=False,repeat=1)
mp = T.max_path()

W = T.resample(id*mp)

S = SpiroData()

npins=1
nk=18
gs=9
n = W.n()//(nk+gs)//npins
ns = W.n()//nk 

npts=250*def_factor

pc = array([ 0, 0 ])

for k in range(nk): 
    
    asym = 0.2
    aa = pi/4
    oa = pi/3 

    s=linspace(0.7,1.2,n)
    
    cr = 0
    p0 = 0

    first = k*ns

    nn = n-1

    max_ao = pi/9 
        
    ao = linspace(-max_ao,max_ao,n)
        
    offset= 0.1 
        
    S.add(on_frame(W,asym=asym,oangle=oa,arc_angle=aa,fb=offset,fh=offset,
                   first=first,orient=ao,pts=[npts,0,0,npts],scale=s,
                   n=nn,object=k,polyfunc=pcoords,prot=0,
                   pin_coord=pc,pin_to_frame=True,autoscale=True,pinned_vertex=1))
        
figure(S,'time','hot')

###

maj=24
ecc=0.0
a = circum(maj,semi_minor(maj,ecc))/(2*pi)/7
T = cIe(Ellipse(maj,ecc),wheel=Wheel(a,a),loops=1.0,inside=True,ppl=2000)

ppl=1500

id = frame_sampling(ppl,parm=0,spacing='sinusoid',deramp=True,reverse=False,repeat=1)
mp = T.max_path()

W = T.resample(id*mp)

S = SpiroData()

npins=1
nk=14
gs=7
n = W.n()//(nk+gs)//npins
ns = W.n()//nk 

npts=350*def_factor

pc = array([ 0, 0 ])

for k in range(nk): 
    
    asym = 0.2 
    aa = pi/4
    oa = pi/3 

    s=linspace(0.7,1.,n)
    
    cr = 0
    p0 = 0

    first = k*ns

    fpts = ( (k+nk//7) % (nk//2) ) / (nk//2)
    fpts = (1.0-cos(6*pi*k/nk))/2
    pts = int(npts/5 + 4*npts/5 * fpts)

    nn = n-1

    max_ao = pi/7 
        
    ao = linspace(-max_ao,0,n)
        
    offset= 0.1
        
    for pv in range(3):
        S.add(on_frame(W,asym=asym,oangle=oa,arc_angle=aa,fb=offset,fh=offset,
                       first=first,orient=ao,pts=[pts,0,0,0],scale=s,
                       n=nn,object=pv,polyfunc=pcoords,prot=0,
                       pin_coord=pc,pin_to_frame=True,autoscale=True,pinned_vertex=pv+1))
        
figure(S,'fradii','pale_pink')

##

S = SpiroData()

npins=1
nk=14
gs=0
n = W.n()//(nk+gs)//npins
ns = W.n()//nk

npts=350*def_factor

for k in range(nk//5): 
    
    asym = 0.2 
    aa = -pi/2
    oa = pi/7 

    s=linspace(0.7,1.,n)
    
    cr = 0
    p0 = 0

    first = k*ns

    fpts = ( (k+nk//7) % (nk//2) ) / (nk//2)
    fpts = (1.0-cos(6*pi*k/nk))/2
    pts = int(npts/5 + 4*npts/5 * fpts)

    nn = n-1

    max_ao = pi/7 
        
    ao = linspace(-max_ao,0,n)
        
    offset= 0.1
        
    for pv in range(3):
        S.add(on_frame(W,asym=asym,oangle=oa,arc_angle=aa,fb=offset,fh=offset,
                       first=first,orient=ao,pts=[pts,0,0,0],scale=s,
                       n=nn,object=pv,polyfunc=pcoords,prot=0,
                       pin_coord=pc,pin_to_frame=True,autoscale=True,pinned_vertex=pv+1))
        
figure(S,'length','autumn')
