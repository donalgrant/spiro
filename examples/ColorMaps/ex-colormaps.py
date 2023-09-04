import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from spiro import *
from spiro_string import *

S = SpiroData()
F = SpiroFig()

cs = cs_list()

ncols = 5
nrows = len(cs) // ncols
if nrows*ncols < len(cs):  nrows+=1

fig, axes=plt.subplots(nrows,ncols,figsize=(10,10),layout='compressed')
f=[]
for i in range(nrows):
    for j in range(ncols):
        axes[i,j].set(aspect=1,xticks=[], yticks=[])
        axes[i,j].set_axis_off()
        f.append(SpiroFig(axes[i,j]))
        
cm='hsv'

for i in range(len(cs)):
    f[i]._fig=fig  # kludge
    f[i].plot(spiro_steps(R=8.0,wheel=Wheel(4,4),loops=5,n=10),
              new_fig=False,cmap=cm,color_scheme=cs[i],caption=False,no_frame=True)

fig.savefig('color_scheme_chart.png',bbox_inches='tight',transparent=True)

###

