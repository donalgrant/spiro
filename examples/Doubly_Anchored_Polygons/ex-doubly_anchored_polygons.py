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

print(npins,nk,gs,n,ns)

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
