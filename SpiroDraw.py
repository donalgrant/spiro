import matplotlib.pyplot as plt
import SpiroData
import numpy as np
from numpy import sin,cos,arctan2,arccos,pi,sqrt,tan,array

class SpiroFig:

    def new_fig(self,**kw_args):
        self._fig = plt.figure(figsize=(10,10))
        self._ax=self._fig.add_subplot(frameon=False)
        self._ax.set(aspect=1,xticks=[],yticks=[])
        self._ax.set_axis_off()
        return self._ax
        
    def __init__(self,ax=None):
        self._ax=ax
        
    def plot(self,sd,cmap='viridis',color_scheme='radial',
             dot_size=0.1,linestyle='',alpha=1.0,
             new_fig=True,smooth=False, caption=True):
        
        if new_fig or not self._ax:  self.new_fig()
        
        match color_scheme:
            case 'radial':    c=sqrt(sd.x**2+sd.y**2)
            case 'cycles':    c=sin(sd.p)
            case 'polar':     c=arctan2(sd.x,sd.y)
            case 'time':      c=sd.t
            case 'length':    c=range(len(sd.p))
            case 'random':    c=np.random.rand(len(sd.x))
            case 'x':         c=sd.x
            case 'y':         c=sd.y
            case 'xy':        c=sd.x*sd.y
            case 'x+y':       c=sd.x+sd.y
            case 'x-y':       c=sd.x-sd.y
            case 'h-waves':   c=sin(sd.x)
            case 'v-waves':   c=sin(sd.y)
            case 'r-waves':   c=sin(sqrt(sd.x**2+sd.y**2))
            case 'ripples':   c=sin((sd.x**2+sd.y**2))
            case 's-ripples': c=sin((sd.x**2+sd.y**2)**(1/4))
            case _:
                c=color_scheme
                cmap=None

        if (smooth):
            self._ax.plot(sd.x,sd.y)
        else:
            self._ax.scatter(sd.x,sd.y,c=c,linestyle=linestyle,s=dot_size,cmap=cmap,alpha=alpha)

        if caption:
            self._fig.text(0.0, 0.05, f'{color_scheme} Color Scheme, {cmap} color map', ha='left')
            self._fig.text(1.0, 0.05, 'David A. Imel 2023', ha='right')

    def caption(self,text):
        self._fig.text(0.4, 0.05, text, ha='left')
        
    def save_fig(self,filename='spiro.png'):  self._fig.savefig(filename,bbox_inches='tight')


