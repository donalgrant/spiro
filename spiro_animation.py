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

F=SpiroFig()
F.text_color='white'

hd = 0

def_factor = (1+4*hd)
save=True

F.set_default_dpi(150*(1+hd))
fd = 10*(1+2*hd) # figure dimensions

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

