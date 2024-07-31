import sys
sys.path.append('../..')
import argparse

import numpy as np

from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_frame import *
from polygon import *

parser = argparse.ArgumentParser(description="Glass and Wings Examples")
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

F._figname='Multi_Sweeps-'

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

S = SpiroData()

###

S.reset()
T = SpiroData()
for wo in linspace(0,5*pi,3):
    for i in range(30):
        T.reset()
        m=5+i/2
        w=Ellipse(major=7,  eccen=0.4,pen=m, offset=0, pen_offset=0)
        r=Ellipse(major=20, eccen=0.7,       offset=0, pen_offset=wo)
        T.add(eIe(ring=r,wheel=w,inside=True,loops=0.5))
        S.add(T)

F.plot(S,color_scheme='t-waves',cmap='jet',save=True)

###

S.reset()
T = SpiroData()
for wo in linspace(0,3*pi,5):
    for i in range(12):
        T.reset()
        m=5+i/3
        w=Ellipse(major=3,  eccen=0.4,pen=m, offset=0, pen_offset=0)
        r=Ellipse(major=20, eccen=0.7,       offset=0, pen_offset=wo)
        T.add(eIe(ring=r,wheel=w,inside=True,loops=0.3))
        T.rotate(wo)
        T.x+=i
        S.add(T) 

F.plot(S,color_scheme='length',cmap='jet',save=True)

###

S.reset()
T = SpiroData()
for sweep in range(15):
    wo = np.random.uniform(0,2*pi)
    R = 20 + np.random.uniform(-10,5)
    for i in range(20):
        T.reset()
        m=5+i/3
        w=Ellipse(major=3,  eccen=0.4,pen=4, offset=i*pi/20, pen_offset=0)
        r=Ellipse(major=R, eccen=0.0,       offset=0, pen_offset=wo)
        T.add(eIe(ring=r,wheel=w,inside=True,loops=0.06))
 #       T.rotate(wo)
 #       T.x+=i
        S.add(T)
F.plot(S,color_scheme='length',save=True)

###

S.reset()
T = SpiroData()
for sweep in range(15):
    wo = np.random.uniform(0,2*pi)
    R = 20 + np.random.uniform(-15,5)
    T.reset()
    for i in range(20):
        m=5+i/3
        w=Ellipse(major=3,  eccen=0.4,pen=4, offset=i*pi/20, pen_offset=0)
        r=Ellipse(major=R, eccen=0.0,       offset=0, pen_offset=wo)
        T.add(eIe(ring=r,wheel=w,inside=True,loops=0.1))
    T.x+=np.random.uniform(-R,R)
    T.y+=np.random.uniform(-R,R)
    S.add(T)
F.plot(S,color_scheme='time',save=True)

###

S.reset()
T = SpiroData()
for sweep in range(15):
    wo = np.random.uniform(0,2*pi)
    R = 20 + np.random.uniform(-15,5)
    T.reset()
    for i in range(10):
        m=5+i/3
        w=Ellipse(major=3,  eccen=0.4,pen=4, offset=i*pi/20, pen_offset=0)
        r=Ellipse(major=R, eccen=0.0,       offset=0, pen_offset=wo)
        T.add(eIe(ring=r,wheel=w,inside=False,loops=0.1))
    T.x+=np.random.uniform(-R,R)
    T.y+=np.random.uniform(-R,R)
    S.add(T)

F.plot(S,color_scheme='cycles',save=True)

###

S.reset()
T = SpiroData()
for sweep in range(15):
    wo = np.random.uniform(0,2*pi)
    R = 20 + np.random.uniform(-15,5)
    T.reset()
    for i in range(20):
        m=5+i/3
        w=Ellipse(major=3, eccen=0.3, pen=4, offset=i*pi/20, pen_offset=0)
        r=Ellipse(major=R, eccen=0.0,        offset=0,       pen_offset=wo)
        T.add(eIe(ring=r,wheel=w,inside=True,loops=0.1))
        T.rotate(i/120)
    T.x+=np.random.uniform(-R,R)
    T.y+=np.random.uniform(-R,R)
    S.add(T)
F.plot(S,color_scheme='cycles',cmap='ocean',save=True)

###

S.reset()
T = SpiroData()
for sweep in range(25):
    wo = np.random.uniform(0,2*pi)
    R = 20 + np.random.uniform(-15,5)
    T.reset()
    for i in range(20):
        m=5+i/3
        w=Ellipse(major=3, eccen=0.3, pen=4, offset=i*pi/20, pen_offset=0)
        r=Ellipse(major=R, eccen=0.1,        offset=0,       pen_offset=wo)
        T.add(eIe(ring=r,wheel=w,inside=True,loops=0.1))
        T.rotate(i/240)
    T.x+=np.random.uniform(-R,R)
    T.y+=np.random.uniform(-R,R)
    S.add(T)
F.plot(S,color_scheme='cycles',cmap='terrain',save=True)

###

S.reset()
T = SpiroData()
for sweep in range(25):
    wo = np.random.uniform(0,2*pi)
    R = 20 + np.random.uniform(-15,5)
    T.reset()
    for i in range(20):
        m=5+i/3
        w=Ellipse(major=6, eccen=0.3, pen=4, offset=i*pi/20, pen_offset=0)
        r=Ellipse(major=R, eccen=0.1,        offset=0,       pen_offset=wo)
        T.add(eIe(ring=r,wheel=w,inside=True,loops=0.1))
        T.rotate(i/280)
    T.x+=np.random.uniform(-R,R)
    T.y+=np.random.uniform(-R,R)
    S.add(T)
F.plot(S,color_scheme='t-waves',cmap='ocean',save=True)

###

S.reset()
T = SpiroData()
for sweep in range(25):
    wo = np.random.uniform(0,2*pi)
    R = 20 + np.random.uniform(-15,5)
    T.reset()
    for i in range(20):
        m=5+i/3
        w=Ellipse(major=6, eccen=0.8, pen=4, offset=i*pi/20, pen_offset=0)
        r=Ellipse(major=R, eccen=0.8,        offset=0,       pen_offset=wo)
        T.add(eIe(ring=r,wheel=w,inside=True,loops=0.1))
        T.rotate(i/280)
    T.x+=np.random.uniform(-R,R)
    T.y+=np.random.uniform(-R,R)
    S.add(T)
F.plot(S,color_scheme='rrand',cmap='hsv',save=True)

###

S.reset()
T = SpiroData()
for sweep in range(25):
    wo = np.random.uniform(0,2*pi)
    R = 20 + np.random.uniform(-15,5)
    T.reset()
    for i in range(20):
        m=5+i/3
        w=Ellipse(major=6, eccen=0.8, pen=4, offset=i*pi/20, pen_offset=0)
        r=Ellipse(major=R, eccen=0.8,        offset=0,       pen_offset=wo)
        T.add(eIe(ring=r,wheel=w,inside=True,loops=0.1))
        T.rotate(i/280)
    T.x+=np.random.uniform(-R,R)
    T.y+=np.random.uniform(-R,R)
    S.add(T)
F.plot(S,color_scheme='x+y',cmap='rainbow',save=True)

###

S.reset()
T = SpiroData()
for sweep in range(15):
    wo = np.random.uniform(0,2*pi)
    R = 20 + np.random.uniform(-15,5)
    T.reset()
    for i in range(10):
        m=5+i
        w=Ellipse(major=6, eccen=0.2, pen=m, offset=i*pi/20, pen_offset=pi/4)
        r=Ellipse(major=R, eccen=0.6,        offset=0,       pen_offset=wo)
        T.add(eIe(ring=r,wheel=w,inside=True,loops=0.2))
        T.rotate(i/280)
    T.x+=np.random.uniform(-R,R)
    T.y+=np.random.uniform(-R,R)
    S.add(T)
F.plot(S,color_scheme='length',cmap='rainbow',save=True)

###

e=0.2
R=40
ppl=80
loops=10
a=R/2.1
U = cIc(Ring(R),wheel=Wheel(a,0.5*a),ppl=ppl,loops=loops,inside=True)
W = U.resample(U.max_path()*frame_sampling(ppl*loops,parm=1,reverse=False,
                                           spacing='erf',deramp=True,repeat=30))

tpts=array([0,0,15,0])
n=int(0.03*W.n())
offset=linspace(-0.3,0.5,n-2)

rp_opts = None

seed = np.random.randint(100) # 12
np.random.seed(seed)
oa = pi/7
f0 = 667 

o = pi/6+linspace(0,pi/2,n-2)
asym=linspace(-0.1,0.1,n-2)
SM = SpiroData()
for i in range(6):
    SM.add(on_frame(W,first=f0+i*W.n()//6-W.n()//9,n=n-2,scale=30,pts=tpts,
                    oangle=oa,asym=asym,
                    orient_follow=1,arc_angle=pi/8,fb=offset,fh=offset,
                    polyfunc=pcoords,orient=o,rp_opts=rp_opts,object=arange(n-2,dtype=int)))

first=True

rp_opts = { 'n': 200, 'parm': 1, 'spacing': ['sinusoid'], 'deramp': True, 'repeat': 5 }

nt = tpts.sum()
offset = 0.4

S = SpiroData()
S.add(on_frame(SM,scale=60,pts=[20,0,0],
               oangle=pi/3,asym=0,fh=offset,fb=offset,
               orient_follow=1,arc_angle=pi/3,
               polyfunc=tcoords,orient=0,rp_opts=rp_opts,object=arange(0,nt)))

cmap=modify_colormap('ocean_r',saturation_factor=0.6,brightness_factor=3.0)
F.plot(S,color_scheme='time',cmap=cmap,alpha=0.4,dot_size=0.1,new_fig=first)

F.save_fig()
