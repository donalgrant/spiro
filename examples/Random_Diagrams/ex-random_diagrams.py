import sys
sys.path.append('../..')
import argparse

import numpy as np

from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_frame import *
from polygon import *

parser = argparse.ArgumentParser(description="Random Diagram Examples")
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

F._figname='Random_Diagram-'

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

F = SpiroFig(rows=2,cols=2)

R = 50
ppl = 400
a = 1/3 * R
S1 = cIc(ring=Ring(R),wheel=Wheel(a,1.3*a),
         loops=1,ppl=ppl,inside=True,reverse=False).rotate(pi/7)

S2 = S1.resample(S1.max_path()*frame_sampling(S1.n(),parm=10,spacing='random',
                                              repeat=1,deramp=False))

cmap='turbo'
cs='time'
sc=20
follow=ppl//3
o = np.random.standard_normal(ppl) * pi/50

F.plot(S1,color_scheme='cyan',dot_size=3)
F.plot(S2,color_scheme='cyan',dot_size=3,new_fig=False)
F.plot(on_frame(S1,polyfunc=tcoords,oangle=pi/3,scale=sc,orient_follow=follow,orient=0),
       new_fig=False,color_scheme=cs,cmap=cmap,alpha=0.2)
F.plot(on_frame(S2,polyfunc=tcoords,oangle=pi/3,scale=sc,orient_follow=follow,orient=0),
       new_fig=False,color_scheme=cs,cmap=cmap,alpha=0.2)

F.save_fig(filename='Random_Diagram-01-random_samp_quad.png')

###

F = SpiroFig(rows=3,cols=3)

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

F.plot(on_frame(S1,polyfunc=tcoords,
                oangle=pi/3,
                fb=0,
                fh=0,
                arc_angle=0,
                asym=0,
                scale=sc,
                orient_follow=follow,
                orient=0),
       new_fig=True,color_scheme=cs,cmap=cmap,alpha=0.2,
       caption=f'original')


F.plot(on_frame(S1,polyfunc=tcoords,
                oangle=pi/3,
                fb=0,
                fh=0,
                arc_angle=0,
                asym=0,
                scale=sc,
                orient_follow=follow,
                orient=g * pi/50),
       new_fig=False,color_scheme=cs,cmap=cmap,alpha=0.2,
       caption=f'orient')

F.plot(on_frame(S1,polyfunc=tcoords,
                oangle=pi/3 * (1 + g/16),
                fb=0,
                fh=0,
                arc_angle=0,
                asym=0,
                scale=sc,
                orient_follow=follow,
                orient=0),
       new_fig=False,color_scheme=cs,cmap=cmap,alpha=0.2,
       caption=f'open angle')

F.plot(on_frame(S1,polyfunc=tcoords,
                oangle=pi/3,
                fb=0,
                fh=0,
                arc_angle=0,
                asym=0,
                scale=sc,
                orient_follow=(follow + g * ppl/18).astype(int),
                orient=0),
       new_fig=False,color_scheme=cs,cmap=cmap,alpha=0.2,
       caption=f'orient follow')

F.plot(on_frame(S1,polyfunc=tcoords,
                oangle=pi/3,
                fb=0,
                fh=0,
                arc_angle=0,
                asym=0,
                scale=sc * (1 + g/10),
                orient_follow=follow,
                orient=0),
       new_fig=False,color_scheme=cs,cmap=cmap,alpha=0.2,
       caption=f'scale')

F.plot(on_frame(S1,polyfunc=tcoords,
                asym=g/10,
                fb=0,
                fh=0,
                arc_angle=0,
                oangle=pi/3,
                scale=sc,
                orient_follow=follow,
                orient=0),
       new_fig=False,color_scheme=cs,cmap=cmap,alpha=0.2,
       caption=f'asymmetry')

F.plot(on_frame(S1,polyfunc=tcoords,
                asym=0,
                fb=g/10,
                fh=g/10,
                arc_angle=0,
                oangle=pi/3,
                scale=sc,
                orient_follow=follow,
                orient=0),
       new_fig=False,color_scheme=cs,cmap=cmap,alpha=0.2,
       caption=f'frame offset')

F.plot(on_frame(S1,polyfunc=tcoords,
                asym=0,
                fb=0,
                fh=0,
                arc_angle=pi/6*g,
                oangle=pi/3,
                scale=sc,
                orient_follow=follow,
                orient=0),
       new_fig=False,color_scheme=cs,cmap=cmap,alpha=0.2,
       caption=f'arc angle')

F.plot(on_frame(S1,polyfunc=tcoords,
                oangle=pi/3*(1+g/16),
                asym=g/10,
                fb=g/10,
                fh=g/10,
                arc_angle=pi/6*g,
                scale=sc * (1 + g/10),
                orient_follow=(follow + g*ppl/18).astype(int),
                orient=g*pi/50),
       new_fig=False,color_scheme=cs,cmap=cmap,alpha=0.2,
       caption=f'all')

F.save_fig(filename='Random_Diagram-02-frame_parms.png')

###

F = SpiroFig()

R = 50
ppl = 600
a = 1/3 * R
S1 = cIc(ring=Ring(R),wheel=Wheel(a,1.3*a),
         loops=1,ppl=ppl,inside=True,reverse=False).rotate(pi/7)

cmap='turbo'
cs='time'
sc=20
follow=ppl//3
g = np.random.standard_normal(ppl)
pts=[100,100,100]

amp = frame_sampling(ppl,parm=1000,spacing='geometric',repeat=12,deramp=True,nocum=True,reverse=False)
amp = amp / max(amp)

F.plot(on_frame(S1,polyfunc=tcoords,
                oangle=pi/3,
                fb=0,
                fh=0,
                arc_angle=0,
                asym=0,
                scale=sc,
                orient_follow=follow,
                pts=pts,
                orient= amp * pi/6 * g),
       new_fig=True,color_scheme=cs,cmap=cmap,alpha=0.2)

F.save_fig(filename='Random_Diagram-03-orient_modulation.png')

###  (grid of increasing amplitudes of random orientation)

F = SpiroFig(rows=3,cols=3)
def_factor=1

R = 50
ppl = 600
a = 1/3 * R
S1 = cIc(ring=Ring(R),wheel=Wheel(a,1.3*a),
         loops=1,ppl=ppl,inside=True,reverse=False).rotate(pi/7)

cmap='turbo'
cs='time'
sc=20
follow=ppl//3
g = np.random.standard_normal(ppl)
pts=[100,100,100]

nf = 9

first_plot=True

for i in range(nf):

    amp = i/nf
    
    F.plot(on_frame(S1,polyfunc=tcoords,
                    oangle=pi/3,
                    fb=0,
                    fh=0,
                    arc_angle=0,
                    asym=0,
                    scale=sc,
                    orient_follow=follow,
                    pts=pts,
                    orient= amp * pi/6 * g),
           new_fig=first_plot,color_scheme=cs,cmap=cmap,alpha=0.2,
           caption=f'{round(amp,2)}')
    
    first_plot=False

F.save_fig(filename='Random_Diagram-04-orient_grid.png')

###

F = SpiroFig(rows=2,cols=2)
def_factor=1

R = 50
ppl = 600
a = 1/3 * R
S1 = cIc(ring=Ring(R),wheel=Wheel(a,1.3*a),
         loops=1,ppl=ppl,inside=True,reverse=False).rotate(pi/7)

cmap='turbo'
cs='time'
sc=20
follow=ppl//3
g = np.random.standard_normal(ppl)
pts=100

first_plot=True

alpha=0.1

F.plot(on_frame(S1,polyfunc=tcoords,
                oangle=pi/3,
                fb=0,
                fh=0,
                arc_angle=0,
                asym=0,
                scale=sc,
                orient_follow=follow,
                pts=pts,
                orient=0,
                rp_opts=None),
       new_fig=first_plot,color_scheme=cs,cmap=cmap,alpha=alpha,
       caption='original')
    
first_plot=False

rp_opts = { 'n': 300, 'parm': 100, 'spacing': ['random'], 'repeat': 1 }

F.plot(on_frame(S1,polyfunc=tcoords,
                oangle=pi/3,
                fb=0,
                fh=0,
                arc_angle=0,
                asym=0,
                scale=sc,
                orient_follow=follow,
                pts=pts,
                orient=0,
                rp_opts=rp_opts),
       new_fig=first_plot,color_scheme=cs,cmap=cmap,alpha=alpha,
       caption='each leg')

p = frame_sampling(ppl,parm=100,spacing='sinusoid',repeat=8,reverse=False,deramp=True,nocum=True)
p = p/max(p) * 5

rp_opts = { 'n': 300, 'parm': p, 'spacing': ['random'] }

F.plot(on_frame(S1,polyfunc=tcoords,
                oangle=pi/3,
                fb=0,
                fh=0,
                arc_angle=0,
                asym=0,
                scale=sc,
                orient_follow=follow,
                pts=pts,
                orient=0,
                rp_opts=rp_opts),
       new_fig=first_plot,color_scheme=cs,cmap=cmap,alpha=alpha,
       caption='modulated random legs')

fs = frame_sampling(300,parm=100,spacing='random',repeat=1)  # same for every triangle

F.plot(on_frame(S1,polyfunc=tcoords,
                oangle=pi/3,
                fb=0,
                fh=0,
                arc_angle=0,
                asym=0,
                scale=sc,
                orient_follow=follow,
                pts=pts,
                orient=0,
                rp_opts=fs/max(fs)),
       new_fig=first_plot,color_scheme=cs,cmap=cmap,alpha=alpha,
       caption='consistent random legs')

F.save_fig(filename='Random_Diagram-05-speckle.png')

### random-color-dither

F = SpiroFig(rows=3,cols=3)
def_factor=1
R = 50
ppl = 600
a = 1/3 * R
S1 = cIc(ring=Ring(R),wheel=Wheel(a,1.3*a),
         loops=1,ppl=ppl,inside=True,reverse=False).rotate(pi/7)

S2 = S1.resample(S1.max_path()*frame_sampling(S1.n(),parm=10,spacing='random',
                                              repeat=1,deramp=False))

cmap='turbo'
cs='time'
sc=20
follow=ppl//3
g = np.random.standard_normal(ppl)
pts=100

first_plot=True

amp = linspace(0.0,0.4,9)
for i in range(amp.shape[0]):
    
#    rp_opts = { 'n': 300, 'parm': amp[i], 'spacing': ['random'], 'repeat': 1 }

    F.plot(on_frame(S1,polyfunc=tcoords,
                    oangle=pi/3,
                    fb=0,
                    fh=0,
                    arc_angle=0,
                    asym=0,
                    scale=sc,
                    orient_follow=follow,
                    pts=pts,
                    orient=0,
                    rp_opts=None),
           new_fig=first_plot,color_scheme=cs,cmap=cmap,alpha=0.2,color_dither=amp[i],
           caption=f'{round(amp[i],2)}')
    
    first_plot=False

F.save_fig(filename='Random_Diagram-06-color_dither.png')

###  Add noise to linear sample spacing on triangle legs

F = SpiroFig(rows=2,cols=2)
def_factor=1

R = 50
ppl = 600
a = 1/3 * R
S1 = cIc(ring=Ring(R),wheel=Wheel(a,1.3*a),
         loops=1,ppl=ppl,inside=True,reverse=False).rotate(pi/7)

S2 = S1.resample(S1.max_path()*frame_sampling(S1.n(),parm=10,spacing='random',
                                              repeat=1,deramp=False))

cmap='turbo'
cs='time'
sc=20
follow=ppl//3
g = np.random.standard_normal(ppl)
pts=100

first_plot=True

alpha=0.2

F.plot(on_frame(S1,polyfunc=tcoords,
                oangle=pi/3,
                fb=0,
                fh=0,
                arc_angle=0,
                asym=0,
                scale=sc,
                orient_follow=follow,
                pts=pts,
                orient=0,
                rp_opts=None),
       new_fig=first_plot,color_scheme=cs,cmap=cmap,alpha=alpha,
       caption='original')

first_plot=False

fs2 = frame_sampling(pts*3,spacing='linear',repeat=15,deramp=True,nocum=True)
fs2 += np.random.standard_normal(pts*3)*0

fs = fs2.cumsum()
fs -= fs[0]
fs /= fs[-1]

F.plot(on_frame(S1,polyfunc=tcoords,
                oangle=pi/3,
                fb=0,
                fh=0,
                arc_angle=0,
                asym=0,
                scale=sc,
                orient_follow=follow,
                pts=pts,
                orient=g * pi/3 * 0.0,
                rp_opts=fs),
       new_fig=first_plot,color_scheme=cs,cmap=cmap,alpha=alpha,
       caption='linear ramp leg spacing')


fs = frame_sampling(pts*3,parm=1000,spacing='random',repeat=15,deramp=True)

F.plot(on_frame(S1,polyfunc=tcoords,
                oangle=pi/3,
                fb=0,
                fh=0,
                arc_angle=0,
                asym=0,
                scale=sc,
                orient_follow=follow,
                pts=pts,
                orient=g * pi/3 * 0.0,
                rp_opts=fs),
       new_fig=first_plot,color_scheme=cs,cmap=cmap,alpha=alpha,
       caption='random leg spacing')

S = SpiroData()

for t in range(ppl):
    
    fs2 = frame_sampling(pts*3,spacing='linear',repeat=15,deramp=True,nocum=True)
    fs2 += np.random.standard_normal(pts*3)/2.0

    fs = fs2.cumsum()
    fs -= fs[0]
    fs /= fs[-1]

    S.add(on_frame(S1,polyfunc=tcoords,
                   first=t,
                   n=1,
                   oangle=pi/3,
                   fb=0,
                   fh=0,
                   arc_angle=0,
                   asym=0,
                   scale=sc,
                   orient_follow=follow,
                   pts=pts,
                   orient=g * pi/3 * 0.0,
                   rp_opts=fs))
    
F.plot(S,new_fig=first_plot,color_scheme=cs,cmap=cmap,alpha=alpha,
       caption='noisy linear ramp legs')

F.save_fig(filename='Random_Diagram-07-noisy_legs.png')

###  Composite of noisy linear leg spacing and modulated orientation noise

F = SpiroFig()

R = 50
ppl = 600
a = 1/3 * R
S1 = cIc(ring=Ring(R),wheel=Wheel(a,1.3*a),
         loops=1,ppl=ppl,inside=True,reverse=False).rotate(pi/7)

S2 = S1.resample(S1.max_path()*frame_sampling(S1.n(),parm=10,spacing='random',
                                              repeat=1,deramp=False))

cmap='autumn'
cs='time'
sc=20
follow=ppl//3
g = np.random.standard_normal(ppl)
pts=100

first_plot=True

alpha=0.4

S = SpiroData()

amp = frame_sampling(ppl,parm=1000,spacing='geometric',repeat=12,deramp=True,nocum=True,reverse=False)
amp = amp / max(amp)

for t in range(ppl):
    
    fs2 = frame_sampling(pts*3,spacing='linear',repeat=15,deramp=True,nocum=True)
    fs2 += np.random.standard_normal(pts*3)/2.0

    fs = fs2.cumsum()
    fs -= fs[0]
    fs /= fs[-1]

    S.add(on_frame(S1,polyfunc=tcoords,
                   first=t,
                   n=1,
                   oangle=pi/3,
                   fb=0,
                   fh=0,
                   arc_angle=0,
                   asym=0,
                   scale=sc,
                   orient_follow=follow,
                   pts=pts,
                   orient=g * pi/6 * amp[t],
                   rp_opts=fs))
    
F.plot(S,new_fig=first_plot,color_scheme=cs,cmap=cmap,alpha=alpha,dot_size=0.1)

F.save_fig(filename='Random_Diagram-08-noisy-linear-legs-modulated-noisy-orient.png')

###  Dither the frame positions with gaussian noise

F = SpiroFig(rows=2,cols=2)
def_factor=1

R = 50
ppl = 600
a = 1/3 * R
S1 = cIc(ring=Ring(R),wheel=Wheel(a,1.3*a),
         loops=1,ppl=ppl,inside=True,reverse=False).rotate(pi/7)

cmap='turbo'
cs='time'
sc=20
follow=ppl//3
g = np.random.standard_normal(ppl)
pts=100

first_plot=True

S = SpiroData()

amp = array([0.0, 0.1, 0.3, 1.0])

for t in range(amp.shape[0]):

    W = S1.copy()
    
    dr = np.random.standard_normal(W.n())
    dt = np.random.uniform(0,2*pi,W.n())
    
    W.x += amp[t]*dr*cos(dt)
    W.y += amp[t]*dr*sin(dt)

    S = on_frame(W,polyfunc=tcoords,
                 oangle=pi/3,
                 fb=0,
                 fh=0,
                 arc_angle=0,
                 asym=0,
                 scale=sc,
                 orient_follow=follow,
                 pts=pts,
                 orient=0,
                 rp_opts=None)
    
    F.plot(S,new_fig=first_plot,color_scheme=cs,cmap=cmap,alpha=0.4,dot_size=0.1,caption=f'{amp[t]}')

    first_plot=False

F.save_fig(filename='Random_Diagram-09-frame_coords.png')

###  dither diagram coordinates (triangle legs, with 2D gaussian offsets)

F = SpiroFig(rows=2,cols=2)
def_factor=1

R = 50
ppl = 600
a = 1/3 * R
S1 = cIc(ring=Ring(R),wheel=Wheel(a,1.3*a),
         loops=1,ppl=ppl,inside=True,reverse=False).rotate(pi/7)

cmap='turbo'
cs='time'
sc=20
follow=ppl//3
g = np.random.standard_normal(ppl)
pts=100

first_plot=True

S = SpiroData()

amp = array([0.0, 0.1, 0.3, 1.0])

for t in range(amp.shape[0]):

    S = on_frame(S1,polyfunc=tcoords,
                 oangle=pi/3,
                 fb=0,
                 fh=0,
                 arc_angle=0,
                 asym=0,
                 scale=sc,
                 orient_follow=follow,
                 pts=pts,
                 orient=0,
                 rp_opts=None)

    if first_plot:
            
        dr = np.random.standard_normal(S.n())
        dt = np.random.uniform(0,2*pi,S.n())
    
    S.x += amp[t]*dr*cos(dt)
    S.y += amp[t]*dr*sin(dt)
    
    F.plot(S,new_fig=first_plot,color_scheme=cs,cmap=cmap,alpha=0.4,dot_size=0.1,caption=f'{amp[t]}')

    first_plot=False

F.save_fig(filename='Random_Diagram-10-final_coords.png')

###

F = SpiroFig(rows=1,cols=1)
def_factor=1

R = 50
ppl = 600
a = 1/3 * R
S1 = cIc(ring=Ring(R),wheel=Wheel(a,1.3*a),
         loops=1,ppl=ppl,inside=True,reverse=False).rotate(pi/7)

cmap='plasma'
cs='time'
sc=20
follow=ppl//3
g = np.random.standard_normal(ppl)
pts=100

first_plot=True

S = SpiroData()

amp = array([1.0])

for t in range(amp.shape[0]):

    S = on_frame(S1,polyfunc=tcoords,
                 oangle=pi/3,
                 fb=0,
                 fh=0,
                 arc_angle=0,
                 asym=0,
                 scale=sc,
                 orient_follow=follow,
                 pts=pts,
                 orient=0,
                 rp_opts=None)

    modulate = frame_sampling(S.n(),parm=10,spacing='geometric',repeat=3,deramp=True,reverse=True,nocum=True)
    modulate /= max(modulate)

    print(max(modulate),min(modulate))
    
    if first_plot:
            
        dr = np.random.standard_normal(S.n())
        dt = np.random.uniform(0,2*pi,S.n())
    
    S.x += amp[t]*dr*cos(dt)*modulate
    S.y += amp[t]*dr*sin(dt)*modulate
    
    F.plot(S,new_fig=first_plot,color_scheme=cs,cmap=cmap,alpha=0.4,dot_size=0.1)

    first_plot=False

F.save_fig(filename='Random_Diagram-11-modulated-leg-noise.png')

###

F = SpiroFig(rows=1,cols=1)
def_factor=1

R = 50
ppl = 400
a = 1/3 * R
S1 = cIc(ring=Ring(R),wheel=Wheel(a,1.3*a),
         loops=1,ppl=ppl,inside=True,reverse=False).rotate(pi/7)

cmap='turbo'
cs='y-direction'
sc=20
follow=ppl//3
g = np.random.standard_normal(ppl)
pts=10 + (10 * (g - min(g))).astype(int)

print(min(pts),max(pts))
pts3=array([],dtype=int)
for j in range(ppl):  pts3=np.append(pts3,(pts[j],pts[j],pts[j]))
    
first_plot=True

S = on_frame(S1,polyfunc=tcoords,
             oangle=pi/3,
             fb=0,
             fh=0,
             arc_angle=0,
             asym=0,
             scale=sc,
             orient_follow=follow,
             pts=pts3,
             orient=0,
             rp_opts=None)

F.plot(S,new_fig=first_plot,color_scheme=cs,cmap=cmap,alpha=0.4,dot_size=3)

F.save_fig(filename='Random_Diagram-12-random-density.png')
