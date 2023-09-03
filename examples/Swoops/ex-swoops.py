import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from spiro import *
from swoops import *

S = SpiroData()
F = SpiroFig()

F.plot(swoops(),color_scheme='time',cmap='hot',save=True)

F.plot(swoops(wheel_e=0.8,yscale=20,xscale=20,
              swoop_min=0.03,swoop_mean=0.1,swoop_spread=0.1),
       color_scheme='x-y',cmap='inferno',save=True)

F.plot(swoops(seed=11,ring_e=0.8,xscale=20,yscale=15,
              swoop_min=0.03,swoop_mean=0.1,swoop_spread=0.2),
       color_scheme='x-y',cmap='inferno',save=True)

###

S=SpiroData()

S.add(swoops(n=40,ring_e=0.8,exponential=True,
             xscale=50,yscale=10,swoop_min=0.03,
             swoop_mean=0.1,swoop_spread=0.1))
F.plot(S,color_scheme='x-y',cmap='inferno')
F.plot(S,color_scheme='x-y',cmap='inferno',
       dot_size=100,alpha=0.03,new_fig=False,subsample=100)

S.reset()
S.add(swoops(n=15,wheel_e=0.8,yscale=20,xscale=20,
              swoop_min=0.03,swoop_mean=0.1,swoop_spread=0.1))
F.plot(S,color_scheme='x-y',cmap='inferno',alpha=0.3,new_fig=False)

S.reset()
S.add(swoops(n=10,yscale=30))
F.plot(S,color_scheme='x-y',cmap='inferno',alpha=0.1,new_fig=False)
F.save_fig()
