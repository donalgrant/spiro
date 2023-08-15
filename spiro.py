import matplotlib.pyplot as plt
import numpy as np
from numpy import sin,cos,arctan2,pi,sqrt,tan,array
import math

class SpiroData:
    
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.x = np.array([])
        self.y = np.array([])
        self.p = np.array([])

    def add(self, sd):
        self.x = np.append(self.x,sd.x)
        self.y = np.append(self.y,sd.y)
        self.p = np.append(self.p,sd.p)

    def xc(self):  return self.x[-1] 
    def yc(self):  return self.y[-1] 
    def pc(self):  return self.p[-1]
    
class SpiroFig:

    def new_fig(self,**kw_args):
        fig, self._ax=plt.subplots(figsize=(10,10))
        self._ax.set(aspect=1,xticks=[],yticks=[])
        return self._ax
        
    def __init__(self,ax=None):
        self._ax=ax
        
    def plot(self,sd,cmap='viridis',color_scheme='radial',new_fig=True):
        
        if new_fig or not self._ax:  self.new_fig()
        
        dot_size=0.1
        linestyle=''

        match color_scheme:
            case 'radial':    c=sqrt(sd.x**2+sd.y**2)
            case 'cycles':    c=sin(sd.p)
            case 'polar':     c=arctan2(sd.x,sd.y)
            case 'time':      c=range(len(sd.p))
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
            case _:           c=[ 0 for i in range(len(sd.x))]
    
        self._ax.scatter(sd.x,sd.y,c=c,linestyle=linestyle,s=dot_size,cmap=cmap)

    def save_fig(self,filename='spiro.png'):  plt.savefig(filename,bbox_inches='tight')

def spiro(R=10.0,a=4.0,b=3.5,loops=5,offset=0,spacing=pi/4000):
    sd = SpiroData()
    t=np.linspace(0.0,loops*2*pi,int(loops/spacing))
    sd.x=(R-a)*sin(t)-b*sin(t*R/a+offset)
    sd.y=(R-a)*cos(t)+b*cos(t*R/a+offset)
    sd.p=t*R/a+offset    
    return sd

def spiro_arc(x0=0,y0=0,orient=0,R=10.0,a=4.0,b=3.5,
              loops=1,offset=0,spacing=pi/4000,invert=False,reverse=False):  
    '''roll on the outside (inside if invert=True) of an arc
    centered on x0, y0, with radius, starting at orientation of
    orient radians cw from the vertical.  Arc has length loops * 2pi
    Direction of motion can be reversed by setting reverse=True
    '''
    iv = -1 if invert else 1
    sd = SpiroData()
    t=np.linspace(0.0,2*pi*loops*R/a,int(loops/spacing)) # roll distance
    if reverse: t=-1*t
    sd.x=x0+(R+iv*a)*sin(t*a/R+orient) +iv*b*sin(t+offset)
    # should orient come into the argument of the sin?
    sd.y=y0+(R+iv*a)*cos(t*a/R+orient) + b*cos(t+offset)
    sd.p=t+offset 
    
    return sd

def spiro_steps(R=10,a=4,b=3.5,loops=1,n=10,offset=pi/10,spacing=pi/2000):
    sd = SpiroData()
    for i in range(n): sd.add(spiro(R,a,b,loops,offset=offset*i,spacing=spacing)) 
    return sd

def roll(x1,y1,x2,y2,a,b,offset=0,guard=0,invert=False):
    '''roll in straight line from (x1,y1) to (x2,y2)
    using wheel of diameter a and pen position b.
    offset is the start angle off the vertical for the pen, in radians.
    invert keyword controls sense of wheel location:  default
    is above and/or to the right.  invert=True is the opposite.
    '''
    R=sqrt((x2-x1)**2+(y2-y1)**2) - 2*guard # roll distance
    A=arctan2(y2-y1,x2-x1)                  # roll angle
    t=np.linspace(0,R/a,1000)               # angle through which the wheel rolls

    iv = -1 if invert else 1

    xs=x1-iv*a*sin(A)+guard*cos(A)
    ys=y1+iv*a*cos(A)+guard*sin(A)

    sd = SpiroData()
    sd.x = xs+a*t*cos(A) +iv*b*sin(t+offset)
    sd.y = ys+a*t*sin(A) +   b*cos(t+offset)  # consistent with spiro
    sd.p = t+offset
    
    return sd

def rotate(x0,y0,xr,yr,angle):
    '''rotate the coordinate (xr,yr) about the
    origin (x0,y0) by angle
    '''
    t=np.linspace(0.0,np.abs(angle),int(500*np.abs(angle)/pi))
    r=sqrt((xr-x0)**2+(yr-y0)**2)
    phi=arctan2(xr-x0,yr-y0)
    
    if (angle<0): t*=-1

    sd = SpiroData()
    
    sd.x = x0+r*sin(t+phi)
    sd.y = y0+r*cos(t+phi)
    sd.p = t+phi
        
    return sd

def rot_2D(angle_rads):
    return array([ [cos(angle_rads), -sin(angle_rads) ],
                   [sin(angle_rads), cos(angle_rads)  ] ])

def rot_coords(angle_rads,coords):
    cc = np.empty((coords.shape[0],2))
    for i in range(cc.shape[0]):
        cc[i] = np.matmul(rot_2D(angle_rads),coords[i])

    return cc

def spiro_line(R=60,a=12,b=7.2,orient=0,loops=60,n=1,fold=False):

    cc = rot_coords(orient,array([ [-R/2,0], [R/2,0] ]))

    # evenually, calculate rotation angles around each corner
    rot_angle=pi
    if (fold): rot_angle = rot_angle - 2*pi

    sd = SpiroData()
    
    offset=0
    
    for i in range(loops):
        
        for c in range(cc.shape[0]):
        
            cn=(c+1) % cc.shape[0]
            
            sd.add(roll(cc[c,0],cc[c,1],cc[cn,0],cc[cn,1],a,b,offset))  # cycloids roll
            offset=sd.pc()
        
            sd.add(rotate(cc[cn,0],cc[cn,1],sd.xc(),sd.yc(),rot_angle)) # roll over upper right
            offset+=rot_angle
        
    return sd

def spiro_eq_triangle(R=60,a=12,b=7.2,orient=0,loops=60,n=1,fold=False,inside=False):
    
    rot_angle=2.0*pi/3.0
    if (fold): rot_angle = rot_angle - 2*pi

    ytop = R*sin(pi/3.0)
    cc = rot_coords(orient,array([ [-R/2,-ytop/3], [0,2*ytop/3], [R/2,-ytop/3] ]))
    
    bump = a/(np.tan(np.pi/6)) if inside else 0
    
    offset=0

    sd = SpiroData()
    
    for i in range(loops):
        
        for c in range(cc.shape[0]):
        
            cn=(c+1) % cc.shape[0]
            
            sd.add(roll(cc[c,0],cc[c,1],cc[cn,0],cc[cn,1],a,b,offset,guard=bump,invert=inside)) 
            offset=sd.pc()
        
            if not inside:
                sd.add(rotate(cc[cn,0],cc[cn,1],sd.xc(),sd.yc(),rot_angle)) # roll over upper right
                offset+=rot_angle
        
        
    return sd

def spiro_square(R=60,a=12,b=7.2,orient=0,loops=60,scatter=False,mono=False,fold=False,inside=False):

    bump = a if inside else 0

    cc = rot_coords(orient,array([ [-R/2,R/2], [R/2,R/2], [R/2,-R/2], [-R/2,-R/2] ]))

    # evenually, calculate rotation angles around each corner
    
    rot_angle=pi/2.0
    if (fold): rot_angle = rot_angle - 2*pi
    
    offset=0

    sd = SpiroData()
    
    for i in range(loops):
        
        for c in range(cc.shape[0]):
        
            cn=(c+1) % cc.shape[0]
            
            sd.add(roll(cc[c,0],cc[c,1],cc[cn,0],cc[cn,1],a,b,offset,guard=bump,invert=inside)) 
            offset=sd.pc()
        
            if not inside:
                sd.add(rotate(cc[cn,0],cc[cn,1],sd.xc(),sd.yc(),rot_angle)) # roll over upper right
                offset+=rot_angle
    
    return sd

def heart(x0=0,y0=0,width=40,depth=25,wheel=2.2,pen=1.0,loops=1,offset=0.0,invert=False):

    sd = SpiroData()
    
    sd.add(roll(x0,y0-depth,x0-width/2,y0,wheel,pen,offset=offset))
    sd.add(rotate(x0-width/2,y0,sd.xc(),sd.yc(),pi))
    sd.add(spiro_arc(x0-width/4,y0,-pi/2,width/4,wheel,pen,loops=0.5,offset=sd.pc()))
    sd.add(rotate(x0-width/2,y0,sd.xc(),sd.yc(),pi/2))
    sd.add(spiro_arc(x0+width/4,y0,-pi/2,10,wheel,pen,loops=0.5,offset=sd.pc()))
    sd.add(rotate(x0+width/2,y0,sd.xc(),sd.yc(),pi))
    sd.add(roll(x0+width,y0,x0,y0-depth,wheel,pen,offset=sd.pc()))
    sd.add(rotate(x0,y0-depth,sd.xc(),sd.yc(),pi/2))
    offset=sd.pc()

    return sd

