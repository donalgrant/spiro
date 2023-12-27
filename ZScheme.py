import SpiroData
import numpy as np
from numpy import sin,cos,arctan2,arccos,pi,sqrt,tan,array,linspace
import scipy

def cs_list():
    return ['radial','cycles','phase','spacing','direction','x-direction','y-direction',
            'polar','time','length','random',
            'x','xrand','y','yrand','rrand', # 'prand','crand','drand','srand',  # add these?
            'xy','x+y','x-y','h-waves','t-waves','l-waves','v-waves',
            'r-waves','ripples','s-ripples'
            ]

def apply_dither(c,dfactor):
    if dfactor==0: return c
    spread = max(c)-min(c)
    g = np.random.standard_normal(len(c))*spread*dfactor
    return c+g

class ZScheme:
'''  Create a new (Z or Color) coordinate from the other available coordinates.

Calling convention:

   ZS = ZScheme(SpiroData)
   ax.scatter(SpiroData.x,SpiroData.y,ZS.z(scheme,options)

'''
    
    def __init__(self): self.sd = sd

    def z(zs=None,o=None):

        sd=self.sd
        
        if zs is None:  zs='radial'

        if hasattr(zs,"__len__") and len(zs)==sd.n():
            return zs
        else:
            match color_scheme:
                case 'radial':    return sd.radii()
                case 'cycles':    return sin(sd.p)
                case 'phase':     return sd.p
                case 'polar':     return arctan2(sd.x,sd.y)
                case 'x-direction': return cos(scipy.signal.medfilt(sd.directions()))
                case 'y-direction': return sin(scipy.signal.medfilt(sd.directions()))
                case 'direction': return scipy.signal.medfilt(sd.directions())
                case 'spacing':   return scipy.signal.medfilt(sd.neighbor_distances())
                case 'time':      return sd.t
                case 'length':    return linspace(0,sd.x.shape[0],sd.x.shape[0])
                case 'random':    return np.random.rand(len(sd.x)) 
                case 'x':         return sd.x
                case 'xrand':     return sd.x+np.random.normal(0,max(sd.x)/3,sd.n())
                case 'y':         return sd.y
                case 'yrand':     return sd.y+np.random.normal(0,max(sd.y)/3,sd.n())
                case 'rrand':     return r+np.random.normal(0,max(r)/3,sd.n())
                case 'xy':        return sd.x*sd.y
                case 'x+y':       return sd.x+sd.y
                case 'x-y':       return sd.x-sd.y
                case 'h-waves':   return sin(sd.x)
                case 't-waves':   return sin(sd.t/max(sd.t)*4*pi)
                case 'l-waves':   return sin(linspace(0,4*pi,sd.n()))
                case 'v-waves':   return sin(sd.y)
                case 'r-waves':   return sin(sd.radii())
                case 'ripples':   return sin(sd.radii()**2)
                case 's-ripples': return sin(sqrt(sd.radii()))
                case _:
                    return color_scheme
