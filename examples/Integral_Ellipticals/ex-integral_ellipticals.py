import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from spiro import *
from spiro_string import *
from spiro_ellipse import *

S = SpiroData()
F = SpiroFig()

###

c = cmap_list()
cs = cs_list()

fig_n = 0

for e in [0.1,0.5,0.9]:
    F.plot(integral_ellipticals(10,0.6,e,max_po=0.0),
           color_scheme=cs[fig_n % len(cs)],
           cmap=c[fig_n % len(c)])
    fig_n+=1
    F.save_fig()

###

for e in linspace(0.1,0.9,3):
    F.plot(integral_ellipticals(10,e,0.3,max_po=0.0),
           color_scheme=cs[fig_n % len(cs)],
           cmap=c[fig_n % len(c)])
    fig_n+=1
    F.save_fig()

###

for rounds in [1,3,7]:
    for circuits in [1,2,4,8]:
        F.plot(integral_ellipticals(10,0.7,0.8,max_po=0.0,rounds=rounds,circuits=circuits),
               color_scheme=cs[fig_n % len(cs)],
               cmap=c[fig_n % len(c)])
        fig_n+=1
        F.save_fig()

###

F.plot(integral_ellipticals(10,0.8,0.6,min_pen=0.8,max_pen=0.8,max_po=pi/2),
       color_scheme=cs[fig_n % len(cs)],
       cmap=c[fig_n % len(c)])
fig_n+=1
F.save_fig()

###

F.plot(integral_ellipticals(6,0.8,0.6,min_pen=0.8,max_pen=0.8,max_po=pi/8),
       color_scheme=cs[fig_n % len(cs)],
       cmap=c[fig_n % len(c)])
fig_n+=1
F.save_fig()

###

for rc in array([ [1,2], [3,4], [7,4] ]):
    F.plot(integral_ellipticals(10,0.7,0.8,max_po=0.0,inside=False,
                                rounds=rc[0],circuits=rc[1]),
           color_scheme=cs[fig_n % len(cs)],
           cmap=c[fig_n % len(c)])
    fig_n+=1
    F.save_fig()

###

S.reset()
for i in range(4):
    S.add(integral_ellipticals(2,0.8,0.7,ring_angle=pi/4+i*pi/32,max_po=0.0,
                               min_pen=0.5,max_pen=1.0,
                               rounds=3,circuits=2,inside=True))
F.plot(S,color_scheme=cs[fig_n % len(cs)], cmap=c[fig_n % len(c)],save=True)
fig_n+=1
