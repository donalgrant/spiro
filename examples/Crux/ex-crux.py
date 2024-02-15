import sys
sys.path.append('../..')
import argparse

from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_frame import *

parser = argparse.ArgumentParser(description="Crux Examples")
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

F._figname='Crux-'

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
 

figure(S,S.fradii(),'turbo')

