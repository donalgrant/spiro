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

import imageio.v2 as imageio
import glob

parser = argparse.ArgumentParser(description="3D Animation Examples")
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

filename='animate-figure-3d.png'

###

def fade_in(S,cs='time',cmap='turbo',nframes=10,ll=None):

    if ll is None:
        zmax=max(S.radii())
        zmin = -zmax
        zscale = zmax-zmin

        ll = 0.95 * zmax
        
    ds = 0.2

    images=[]
    
    a_max = 0.95

    filename='rot3D-temp.png'
    
    nframes=10
    for i in range(nframes):
        alpha=i/nframes*a_max
        F.plot(S,color_scheme=cs,cmap=cmap,alpha=alpha,dot_size=ds,save=True,
               limits=[-ll,ll,-ll,ll],transparent=False,filename=filename)

        images.append(imageio.imread(filename))

    return images

    
def rot3D_plot(S,coords,cs='time',cmap='turbo',n_rot_frames=24,n_transition=10,ll=None):

    zmax=max(S.radii())
    zmin = -zmax
    zscale = zmax-zmin

    if ll is None:
        ll = 0.95 * zmax

    print(f'll is {ll}')
    
    ds = 0.2

    a_max = 0.95

    images=[]
    
    filename='rot3D-temp.png'
    
    # now long second fade to depth cue on original

    xyz=rotY(coords,0)
    z = xyz[:,2]
    a = np.minimum(np.full(S.n(),a_max),np.maximum(np.zeros(S.n()),a_max * (z-zmin)/zscale))

    for i in range(n_transition):
        alpha = a*(i/n_transition) + a_max*(n_transition-i)/n_transition
        F.plot(S,color_scheme=cs,cmap=cmap,alpha=alpha,dot_size=ds,save=True,
               limits=[-ll,ll,-ll,ll],transparent=False,filename=filename)

        images.append(imageio.imread(filename))

    for theta in linspace(0,2*pi,n_rot_frames):

        xyz=rotY(rotZ(coords,-theta),theta)
        x = xyz[:,0]
        y = xyz[:,1]
        z = xyz[:,2]

        SR=S.copy()
        
        a = np.minimum(np.full(SR.n(),a_max),np.maximum(np.zeros(SR.n()),a_max * (z-zmin)/zscale))

        print(100*theta/(2*pi),min(z),max(z),min(a),max(a))
    
        U = SpiroData()
        F.plot(U.set_array(x,y,SR.p,SR.t,SR.o,SR.s),
               color_scheme=cs,cmap=cmap,alpha=a,dot_size=ds,
               transparent=False,save=True,filename=filename,
               limits=[-ll,ll,-ll,ll])

        images.append(imageio.imread(filename))
    
    for theta in linspace(0,2*pi,n_rot_frames):
        
        xyz=rotY(rotZ(coords,theta),theta)
        x = xyz[:,0]
        y = xyz[:,1]
        z = xyz[:,2]
    
        SR=S.copy()
        
        a = np.minimum(np.full(SR.n(),a_max),np.maximum(np.zeros(SR.n()),a_max * (z-zmin)/zscale))
    
        print(100*theta/(2*pi),min(z),max(z),min(a),max(a))
        
        U = SpiroData()
        F.plot(U.set_array(x,y,SR.p,SR.t,SR.o,SR.s),
               color_scheme=cs,cmap=cmap,alpha=a,dot_size=ds,
               transparent=False,save=True,filename=filename,
               limits=[-ll,ll,-ll,ll])
    
        images.append(imageio.imread(filename))
    
    # now one second fade out of depth cue 
    
    xyz=rotY(coords,0)
    z = xyz[:,2]

    a = np.minimum(np.full(S.n(),a_max),np.maximum(np.zeros(S.n()),a_max * (z-zmin)/zscale))
    
    for i in range(n_transition):
        alpha = a_max*(i/n_transition) + a*(n_transition-i)/n_transition
        F.plot(S,color_scheme=cs,cmap=cmap,alpha=alpha,dot_size=ds,save=True,
               limits=[-ll,ll,-ll,ll],transparent=False,filename=filename)
    
        images.append(imageio.imread(filename))
    
    return images

###

R = 50
ppl = 400
a = 1/3 * R
S1 = cIc(ring=Ring(R),wheel=Wheel(a,1.3*a),
         loops=1,ppl=ppl,inside=True,reverse=False).rotate(pi/7)

cmap='turbo'
cs='time'
sc=20
follow=ppl//3
g = np.random.standard_normal(ppl)


S=on_frame(S1,polyfunc=tcoords, oangle=pi/3, fb=0, fh=0, arc_angle=0,
           asym=0, scale=sc, orient_follow=follow, orient=0)

n1 = 10
n2 = 96
ll = 100

fade_in = fade_in(S,cs,cmap,n1,ll)
images=[]

images.extend(fade_in)

xscale=max(S.x)-min(S.x)
images.extend(rot3D_plot(S,S.xyt(scale=xscale),cs,cmap,n2,n1,ll))
images.extend(rot3D_plot(S,S.xyp(scale=xscale),cs,cmap,n2,n1,ll))
images.extend(rot3D_plot(S,S.xyl(scale=xscale),cs,cmap,n2,n1,ll))
images.extend(rot3D_plot(S,S.xyf(scale=xscale),cs,cmap,n2,n1,ll))
images.extend(rot3D_plot(S,S.xys(scale=xscale),cs,cmap,n2,n1,ll))

images.extend(np.flip(fade_in,axis=0))

imageio.mimsave("3D-rotate-01.gif", images, duration=0.1, loop=0)

###

e=0.0
R=7
ppl=1000

a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/4,a/6),ppl=ppl,loops=1,inside=True)

skip=3
n=120

scale=5
oa=pi/3
ao=0.0
asym=0
aa=pi/3
of=1
pts=[200,0,200]

S = SpiroData()

nr=6
for i in range(nr):
    first=i*T.n()//nr
    S.add(triangles_on_frame(T,first=first,skip=skip,scale=scale,oangle=oa,n=n,fh=0,fb=0,
                             asym=asym,orient_follow=1,orient=ao,arc_angle=aa,pts=pts))

my_cmap='turbo'

xscale=max(S.x)-min(S.x)

images=[]

for theta in linspace(0,2*pi,96):
    
    xyz=rotY(S.xyp(scale=xscale),theta)
    x = xyz[:,0]
    y = xyz[:,1]
    z = xyz[:,2]

    U = SpiroData()
    F.plot(U.set_array(x,y,S.p,S.t,S.o,S.s),
           color_scheme='cycles',cmap=my_cmap,alpha=.4,fig_dim=fd,dot_size=0.1,save=True,
           limits=[-15,15,-15,15],transparent=False,filename=filename)

    images.append(imageio.imread(filename))
    
for theta in linspace(0,2*pi,96):
    
    xyz=rotX(S.xyp(scale=xscale),theta)
    x = xyz[:,0]
    y = xyz[:,1]
    z = xyz[:,2]

    U = SpiroData()
    F.plot(U.set_array(x,y,S.p,S.t,S.o,S.s),
           color_scheme='cycles',cmap=my_cmap,alpha=.4,fig_dim=fd,dot_size=0.1,save=True,
           limits=[-15,15,-15,15],transparent=False,filename=filename)

    images.append(imageio.imread(filename))

    
imageio.mimsave("animate_rot-triangle_sets-p.gif", images, duration=0.1, loop=0)

###

# demonstration of rotating, zooming in, and showing the spirograph frame, while evolving

e=0.0
R=7
ppl=1000
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/3,a/2.5),ppl=ppl,loops=1,inside=True)

my_cmap='turbo'
cs = 'cycles'

skip=1
n=40

scale=3
oa=pi/3
ao=0.0
asym=0
of=1
pts=[200,0,200]

nr=120

theta = linspace(0,2*pi,nr)
aa = linspace(0,pi/2,nr)
lmax = append(linspace(25,3,nr//2),linspace(3,25,nr//2))

images=[]

for i in range(nr):
    if i%10==0:  print(i)
    
    first=i*T.n()//nr
    S=triangles_on_frame(T,first=first,skip=skip,scale=scale,oangle=oa,n=n,fh=0,fb=0,
                         asym=asym,orient_follow=1,orient=ao,arc_angle=aa[i],pts=pts)

    xscale=max(S.x)-min(S.x)

    xyz=rotY(S.xyl(scale=xscale/4),theta[i])
    x = xyz[:,0]
    y = xyz[:,1]
    z = xyz[:,2]

    U = SpiroData()

    l=lmax[i]
    ds = 62.5/(l*l)
    
    F.plot(U.set_array(x,y,S.p,S.t,S.o,S.s),color_scheme=cs,cmap=my_cmap,alpha=.4,fig_dim=fd,dot_size=ds,save=False,
           limits=[-l,l,-l,l],transparent=False,filename=filename)

    images.append(imageio.imread(filename))
    
    v = rotY(T.xyl(scale=1.0),theta[i])
    x = v[:,0]
    y = v[:,1]
    z = v[:,2]

    U = SpiroData()

    F.plot(U.set_array(x,y,T.p,T.t,S.o,S.s),
           color_scheme=cs,cmap='pale_pink',alpha=.2,fig_dim=fd,dot_size=ds*10,save=True,
           limits=[-l,l,-l,l],transparent=False,new_fig=False,filename=filename)

    images.append(imageio.imread(filename))
    
imageio.mimsave("animate_evolve-zoom-w-frame.gif", images, duration=0.2, loop=0)
