import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from Ellipse import *
from spiro import *
from spiro_string import *
from spiro_ellipse import *

S = SpiroData()
F = SpiroFig()

cmaps=cmap_list()
cs = cs_list()

###

S.reset()
for j in range(10):
    S.add(elliptical_arc(x0=-j/5,y0=j/5,orient=0,R=2.0,wheel=Ellipse(6.5,0.8,2,pi/20*j),
                             loops=3,spacing=0.01,inside=False))
F.plot(S,cmap='Dark2',color_scheme='time',dot_size=10,alpha=1.0)

###


fig_number=0
cmaps = cmap_list()
csl = cs_list()

s_vals = [200,400,800,1600,3200,6400]
ds_vals = [0.5,1,3,5,7]
ss_vals = [15,30,60]
    
for t in [True,False]:

    S.reset()
    S = spiro(R=20,wheel=Wheel(5.5,4,0),loops=10,orient=0,inside=t,spacing=0.001)
    
    for s in s_vals:
        
        SO = string_offset_pairs(S,offset=s,step=20)
        
        nsubs=len(ds_vals)*(len(ss_vals)+1)+2
        ncols=4
        nrows=nsubs // ncols
        if nsubs % ncols > 0: nrows+=1
        F=SpiroFig(rows=nrows,cols=ncols)
        F.text_color='white'
        
        F.plot(S, color_scheme='radial',cmap='Reds',caption='Original')

        ds=2.5
        for ss in ss_vals:
            cs=csl[fig_number % len(csl)]
            c=cmaps[fig_number % len(cmaps)]
            F.plot(S,new_fig=False,
                   subsample=ss,dot_size=ds,caption=f'O: {ss}/{ds} {cs}/{c}',
                   fontsize=10,
                   color_scheme=cs,cmap=c)
    
            fig_number+=1

            
        F.plot(SO,color_scheme='radial',cmap='Reds',caption=f'String',new_fig=False)
        
        for ds in ds_vals:
            for ss in ss_vals:
                cs=csl[fig_number % len(csl)]
                c=cmaps[fig_number % len(cmaps)]
                F.plot(SO,new_fig=False,
                       subsample=ss,dot_size=ds,caption=f'S: {ss}/{ds} {cs}/{c}',
                       fontsize=10,
                       color_scheme=cs,cmap=c)
    
                fig_number+=1

        F.caption(f'String Subsample {s}')     
        F.save_fig(f'dot-chart-{s}-{t}.png')
