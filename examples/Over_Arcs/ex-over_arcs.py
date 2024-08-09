import sys
sys.path.append('../..')
import argparse

import numpy as np

from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_frame import *
from polygon import *
from partition import *

parser = argparse.ArgumentParser(description="Over Arcs Examples")
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

F._figname='Over_Arcs-'

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

###

R1=20
a = R1/2.5
ppl=500
loops=2

U = cIc(Ring(R1),Wheel(a,1.4*a),ppl=ppl,loops=loops)
W = U.resample_using( { 'n': ppl*loops, 'parm': 1, 'spacing': ['constant'], 'deramp': False, 'repeat': 5 } )

l=300
n=W.n()
nn=n//3
f0=0

T = on_frame(W,scale=linspace(20,30,nn),oangle=pi/4,fb=0.0,fh=0.0,asym=0.3,
             orient=linspace(0,4*pi,nn),polyfunc=pcoords,
             pts=l,orient_follow=n//3,arc_angle=pi/6,arc_scale=1.3,arc_offset=0.0,
             n=nn,rp_opts=None)

T.rotate(pi/6)
F.plot(T,color_scheme='fwidth',cmap='jet',alpha=0.4,dot_size=.1,new_fig=True)
F.save_fig(filename='Cover.png')

F.plot(T,color_scheme='fwidth',cmap='grey',alpha=0.4,dot_size=.1,new_fig=True)
F.save_fig()

###

R1=20
a = R1/2.5
ppl=500
loops=2 + 0.5/ppl

U = cIc(Ring(R1),Wheel(a,1.4*a),ppl=ppl,loops=loops)
W = U.resample_using( { 'n': int(ppl*loops), 'parm': 10, 'spacing': ['sinusoid'], 'deramp': True, 'repeat': 5 } )

l=300
n=W.n()
nn=n//3
f0=0
rp_opts = { 'n': l, 'parm': 1, 'spacing': ['constant'], 'deramp': True, 'repeat': 1 }

offsets=[n//5,n//5,n//5,n//5]
scale = array([ 1.0 + 0.3 * sin(10*pi*j/nn) for j in range(nn) ])
T = anchored_arcs(W,offsets,pi/5,scale=scale,arc_offset=0.0, # array([0.3*sin(10*pi*j/nn) for j in range(nn)]),
                  first=0,n=nn,line_pts=300,close_loop=True,
                  interp_phase=True,object=0,connect_times=True,rp_opts=None)

F.plot(T,color_scheme='fwidth',cmap='cyans',alpha=0.4,dot_size=.1,new_fig=True)
F.plot(W,color_scheme='orange',cmap='turbo',dot_size=.5,alpha=0.8,new_fig=False)

F.save_fig()

###

R1=20
a = R1/2.5
ppl=500
loops=0.7

U = cIc(Ring(R1),Wheel(a,1.4*a),ppl=ppl,loops=loops)
W = U.resample_using( { 'n': int(ppl*loops), 'parm': 10, 'spacing': ['sinusoid'], 'deramp': True, 'repeat': 5 } )

l=300
n=W.n()
nn=n
f0=0

offsets=[n//15,n//5,n//15]
scale = array([ 1.0 + 0.3 * sin(10*pi*j/nn) for j in range(nn) ])
T = anchored_arcs(W,offsets,pi/5,scale=scale,arc_offset=0.0, 
                  first=0,n=nn,line_pts=300,close_loop=True,
                  interp_phase=True,object=0,connect_times=True,rp_opts=None)

F.plot(T,color_scheme='dir_off_frm',cmap='hot',alpha=0.4,dot_size=.1,new_fig=True)

F.save_fig()

###

R1=20
a = R1/2.5
ppl=1000
loops=0.5 

U = cIc(Ring(R1),Wheel(a,1.4*a),ppl=ppl,loops=loops)
W = U.resample_using( { 'n': int(ppl*loops), 'parm': 10, 'spacing': ['sinusoid'], 'deramp': True, 'repeat': 5 } )

l=300
n=W.n()
nn=n//3
f0=n

offsets=[n//15,n//5,n//15]
scale = array([ 1.0 + 0.3 * sin(10*pi*j/nn) for j in range(nn) ])
T = anchored_arcs(W,offsets,pi/5,scale=scale,arc_offset=0.0,
                  first=0,n=nn,line_pts=300,close_loop=True,
                  interp_phase=True,object=0,connect_times=True,rp_opts=None)

T.rotate(-pi/7)
F.plot(T,color_scheme='t-waves',cmap='cmap2',alpha=0.4,dot_size=.1,new_fig=True)

F.save_fig()

###

R1=20
a = R1/2.5
ppl=200
loops=2 + 0.5/ppl

U = cIc(Ring(R1),Wheel(a,1.4*a),ppl=ppl,loops=loops)
W = U.resample_using( { 'n': int(ppl*loops), 'parm': 10, 'spacing': ['sinusoid'], 'deramp': True, 'repeat': 5 } )

n=W.n()
nn=n//5
f0=n

S = SpiroData()

n_bundles = 5
for i in range(n_bundles):
    
    offsets=[n//15,n//5,n//15]
    aa = pi/2 * i / n_bundles
    scale = array([ 1.0 + 0.3 * sin(10*pi*j/nn) for j in range(nn) ])
    T = anchored_arcs(W,offsets,aa,scale=scale,arc_offset=0.0,
                      first=0,n=nn,line_pts=300,close_loop=True,
                      interp_phase=True,object=0,connect_times=True,rp_opts=None).rotate(-pi/7)

    S.add(T)
    

F.plot(S,color_scheme='t-waves',cmap='autumn',alpha=0.4,dot_size=.1,new_fig=True)

F.save_fig()

###

R1=20
a = R1/2.5
ppl=30
loops=2 + 0.5/ppl

U = cIc(Ring(R1),Wheel(a,1.4*a),ppl=ppl,loops=loops)
W = U.resample_using( { 'n': int(ppl*loops), 'parm': 10, 'spacing': ['sinusoid'], 'deramp': True, 'repeat': 5 } )

n=W.n()
nn=n//7
f0=np.random.randint(n)
print(f0)

S = SpiroData()

n_bundles = 10
for i in range(n_bundles):

    rp_opts = { 'n': 300, 'parm': 3, 'spacing': ['gaussian'], 'deramp': False, 'repeat': 20 }
    offsets=[n//3]
    aa = pi/4 * i / n_bundles
    scale = 1.3 
    T = anchored_arcs(W,offsets,aa,scale=scale,arc_offset=i/n_bundles * 0.1,
                      first=0,n=nn,line_pts=300,close_loop=False,
                      interp_phase=True,object=0,connect_times=True,rp_opts=rp_opts).rotate(-pi/7)

    S.add(T)
    
T = S.copy()
for i in range(7):
    S.add(T.rotate(pi/9))
    
F.plot(S,color_scheme='t-waves',cmap='peaches',alpha=0.4,dot_size=.1,new_fig=True)

F.save_fig()

###

R1=20
a = R1/(2+1/7)
ppl=50
loops=7*(1 + 0.5/ppl)

U = cIc(Ring(R1),Wheel(a,1*a),ppl=ppl,loops=loops,inside=False)
W = U.resample_using( { 'n': int(ppl*loops), 'parm': 10, 'spacing': ['sinusoid'], 'deramp': True, 'repeat': 5 } ).rotate(-pi/7)

F.plot(W,color_scheme='orange',cmap='turbo',dot_size=1)

n=W.n()
nn=n//5

S = SpiroData()

n_bundles = 12
aa = linspace(-pi/2,pi/2,n_bundles)
for i in range(n_bundles):

    rp_opts = { 'n': 500, 'parm': 3, 'spacing': ['gaussian'], 'deramp': False, 'repeat': 20 }
    offsets=[n//3]
    scale = 1.3 
    arc_offset = linspace(0.5,0.5,nn)
    T = anchored_arcs(W,offsets,aa[i],scale=scale,arc_offset=arc_offset,
                      first=0,n=nn,line_pts=30,close_loop=False,
                      interp_phase=True,object=0,connect_times=True,rp_opts=rp_opts)

    S.add(T)
    

F.plot(S,color_scheme='t-waves',cmap='cyans',alpha=0.4,dot_size=.1,new_fig=True)
F.save_fig()
