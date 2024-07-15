import sys
sys.path.append('../..')
import argparse

from SpiroData import *
from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_frame import *
from spiro_arcs import *
from spiro_string import *
from polygon import *
from Ring import *

parser = argparse.ArgumentParser(description="Ellipses Between Frames Examples")
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

F._figname='EBF-'

def figure(S,cs,cmap,alpha=0.4,dot_size=0.1*(1+hd),filename=None,color_dither=0.0):
    transparent=True
    if hd:
        transparent=False
        if not hasattr(figure,"data_set"):  figure.data_set=0
        S.save(f'figure-{figure.data_set}.pickle')
        figure.data_set+=1

    if filename is None:
        F.plot(S,color_scheme=cs,cmap=cmap,alpha=alpha,fig_dim=fd,dot_size=dot_size,
               save=save,color_dither=color_dither,transparent=transparent)
    else:
        F.plot(S,color_scheme=cs,cmap=cmap,alpha=alpha,fig_dim=fd,dot_size=dot_size,
               save=save,filename=filename,color_dither=color_dither,transparent=transparent)

###

R=24
T1 = cIc(Ring(R),wheel=W0,loops=1,inside=True,ppl=2000)
T2 = cIc(Ring(R),wheel=Wheel(R/3,R/3),loops=1,inside=True,ppl=2000)

figure(ellipses_between_frames(T1,T2,4,2,
                              scale_major=1.0,
                              orient_offset=0,
                              off_major=1.0, 
                              off_minor=0.0,
                              eccen=0.95,
                              nfigs=T1.n()//4,
                              pts=1000*def_factor,
                              istart1=0,istart2=0
                               ),'spacing','Reds')

###

R=24
T1 = cIc(Ring(R),wheel=W0,loops=1,inside=True,ppl=4000)
T2 = cIc(Ring(R),wheel=Wheel(R/3,R/3),loops=1,inside=True,ppl=4000)

figure(ellipses_between_frames(T1,T2,2,3,
                              scale_major=1.0,
                              orient_offset=[0,pi/10,pi/5,pi/10],
                              off_major=1.0, 
                              off_minor=0.0,
                              eccen=0.95,
                              nfigs=T1.n()//4,
                              pts=1000*def_factor,
                              istart1=0,istart2=T2.n()//3
                               ),'x-direction',wreath)

###

R1=24
R2=R1*0.6
r=0.01
ppl=2000

T1 = cIc(Ring(R1),wheel=W0,loops=1,inside=True,ppl=ppl)
T2 = cIc(Ring(R2),wheel=Wheel(R2/4,R2/6),loops=1,inside=True,ppl=ppl)

nf=T1.n()//4
figure(ellipses_between_frames(T1,T2,1,8,
                              scale_major=1.0,
                              orient_offset=pi/8, # pi/4, # offsets,
                              off_major=0.9, 
                              off_minor=0.0,
                              eccen=0.95,
                              nfigs=nf,
                              pts=1000*def_factor,
                              istart1=T1.n()//4,istart2=T2.n()*2//5
                               ),'phase','OrRd')

##

nf=T1.n()//2
figure(ellipses_between_frames(T1,T2,1,4,
                              scale_major=1.5,
                              orient_offset=[0,pi/4], # pi/4, # offsets,
                              off_major=[0.8,1.0], 
                              off_minor=0.0,
                              eccen=0.95,
                              nfigs=nf,
                              pts=1000*def_factor,
                              istart1=0,istart2=T2.n()//8
                               ),'length','autumn')

###

R1=24
R2=R1*0.3
r=0.01
ppl=2000

T1 = cIc(Ring(R1),wheel=Wheel(R1/3,R1/6),loops=1,inside=True,ppl=ppl)
T2 = cIc(Ring(R2),wheel=Wheel(R2/3,R2/6),loops=1,inside=True,ppl=ppl).rotate(pi)

nf=T1.n()//2
figure(ellipses_between_frames(T1,T2,1,5,
                              scale_major=[1.0,2.0,3.0],
                              orient_offset=0, # pi/4, # offsets,
                              off_major=0, 
                              off_minor=[2.5,0.5],
                              eccen=linspace(0.7,0.95,nf),
                              nfigs=nf,
                              pts=1000*def_factor,
                              istart1=0,istart2=T2.n()//8
                               ),'length','autumn')

##

nf = T1.n()//3
bias = [ sin(2*pi*i/(nf//3)) for i in range(nf) ]

figure(ellipses_between_frames(T1,T2,3,3,
                              scale_major=1,
                              orient_offset=0, # pi/4, # offsets,
                              off_major=1, 
                              off_minor=0,
                              eccen=linspace(0.7,0.95,nf//3),
                              bias=bias,
                              nfigs=nf,
                              pts=1000*def_factor,
                              istart1=0,istart2=0
                               ),'time','hot')
###

R1=24
R2=R1*1.4
r=0.01
ppl=2000
T1 = cIc(Ring(R1),wheel=Wheel(R1/3,R1/6),loops=1,inside=True,ppl=ppl)
T2 = cIc(Ring(R2),wheel=Wheel(R2/4,R2/6),loops=1,inside=True,ppl=ppl).rotate(pi)

nf = T1.n()//5
bias = [ sin(2*pi*i/(nf//2)) for i in range(nf) ]

figure(ellipses_between_frames(T1,T2,3,3,
                           scale_major=1,
                           orient_offset=0, # pi/4, # offsets,
                           off_major=1, 
                           off_minor=0,
                           eccen=0.98,
                           bias=bias,
                           nfigs=nf,
                           pts=1000*def_factor,
                           istart1=0,istart2=0
                               ),'y-direction','Reds')

###

R1=24
R2=R1*1.4
r=0.01
ppl=2000
T1 = cIc(Ring(R1),wheel=Wheel(R1/4,R1/6),loops=1,inside=True,ppl=ppl)
T2 = cIc(Ring(R2),wheel=Wheel(R2/4,R2/6),loops=1,inside=True,ppl=ppl).rotate(pi)

nf = T1.n()//5

figure(ellipses_between_frames(T1,T2,2,3,
                               scale_major=np.append(linspace(-50,-30,nf//4),linspace(-30,-50,nf//4)), 
                               orient_offset=linspace(0,2*pi,T1.n()), #
                               off_major=1, 
                               off_minor=0,
                               eccen=0.9,
                               bias=0.0,
                               nfigs=nf,
                               pts=1000*def_factor,
                               istart1=0,istart2=0
                               ),'l-waves',cmap1)

###

R1=24
R2=R1*1.4
r=0.01
ppl=2000
T1 = cIc(Ring(R1),wheel=Wheel(R1/4,R1/6),loops=1,inside=True,ppl=ppl)
T2 = cIc(Ring(R2),wheel=Wheel(R2/8,R2/8),loops=1,inside=True,ppl=ppl).rotate(pi)

nf = T1.n()//5-50

figure(ellipses_between_frames(T1,T2,2,3,
                               scale_major=1.0,
                               orient_offset=linspace(0,2*pi,T1.n()), #
                               off_major=0.6, 
                               off_minor=0,
                               eccen=0.9,
                               bias=0.0,
                               nfigs=nf,
                               pts=1000*def_factor,
                               istart1=0,istart2=0
                               ),'spacing','OrRd')
##

nf = T1.n()//6

figure(ellipses_between_frames(T1,T2,2,3,
                               scale_major=1.0,
                               orient_offset=0, 
                               off_major=0.6, 
                               off_minor=0,
                               eccen=0.9,
                               bias=0.0,
                               nfigs=nf,
                               pts=1000*def_factor,
                               istart1=0,istart2=0
                               ),'length',emerald_woman)
##

nf = T1.n()//3

figure(ellipses_between_frames(T1,T2,1,257,
                               scale_major=1.3,
                               orient_offset=pi/4,
                               off_major=0.7, 
                               off_minor=0.4,
                               eccen=0.9,
                               bias=0.7,
                               nfigs=nf,
                               pts=1000*def_factor,
                               istart1=0,istart2=T2.n()//5
                               ),'y-direction','autumn')

###

R1=24
R2=R1*1.5
r=0.01
ppl=2000
T1 = cIc(Ring(R1),wheel=Wheel(R1/4,R1/4),loops=1,inside=False,ppl=ppl*3)
T2 = cIc(Ring(R2),wheel=Wheel(R2/4,R2/6),loops=1,inside=True,ppl=ppl).rotate(pi).subsample(40)

nf = T1.n()//6

figure(ellipses_between_frames(T1,T2,np.append(np.full(15,3),np.full(5,15)),1,
                               scale_major=0.4,
                               orient_offset=0,
                               off_major=1, 
                               off_minor=0,
                               eccen=0.9,
                               bias=0,
                               nfigs=nf,
                               pts=1000*def_factor,
                               istart1=0,istart2=T2.n()//5
                               ),'y-direction','ocean')

###

R1=24
R2=R1*1.5
r=0.01
ppl=2000

T1 = cIc(Ring(R1),wheel=Wheel(R1/4,R1/4),loops=1,inside=False,ppl=ppl*3)
T2 = cIc(Ring(R2),wheel=Wheel(R2/4,R2/6),loops=1,inside=True,ppl=ppl).rotate(pi).subsample(10)

nf = 240
t1_start=116
t2_start=46

figure(ellipses_between_frames(T1,T2.subsample(2),np.append(np.full(15,3),np.full(5,15)),1,
                               scale_major=-30,
                               orient_offset=0,
                               off_major=0.8, 
                               off_minor=0,
                               eccen=0.9,
                               bias=0.5,
                               nfigs=nf,
                               pts=1000*def_factor,
                               istart1=t1_start,istart2=t2_start
                               ),'cycles','autumn')

###

R1=24
R2=R1*1.5
r=0.01
ppl=2000
#a =major_from_circum(2*pi*R1/4,e)
T1 = cIc(Ring(R1),wheel=Wheel(R1/4,R1/4),loops=1,inside=False,ppl=ppl)
T2 = cIc(Ring(R2),wheel=Wheel(R2/4,R2/6),loops=1,inside=True,ppl=ppl).rotate(pi)

nf = 240
t1_start=1703
t2_start=144

figure(ellipses_between_frames(T1,T2.subsample(2),np.append(np.full(15,3),np.full(5,15)),1,
                               scale_major=-30,
                               orient_offset=np.append(np.full(15,pi/4),np.full(5,0.0)),
                               off_major=0.8, 
                               off_minor=0,
                               eccen=0.9,
                               bias=0.5,
                               nfigs=nf,
                               pts=1000*def_factor,
                               istart1=t1_start,istart2=t2_start
                               ),'cycles','hot')

##

nf = 240
t1_start=1769 # np.random.randint(T1.n())
t2_start=409 # np.random.randint(T2.n()//4)

figure(ellipses_between_frames(T1,T2.subsample(2),np.append(np.full(30,3),np.full(10,15)),1,
                               scale_major=-30,
                               orient_offset=np.append(np.full(30,pi/4),np.full(10,0.0)),
                               off_major=0.8, 
                               off_minor=0,
                               eccen=0.9,
                               bias=0.5,
                               nfigs=nf,
                               pts=1000*def_factor,
                               istart1=t1_start,istart2=t2_start
                               ),'cycles',cmap1)
