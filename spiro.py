import matplotlib.pyplot as plt
import numpy as np
from numpy import sin,cos,arctan2,arccos,pi,sqrt,tan,array
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

def spiro(R=10,a=4.0,b=3.5,loops=5,offset=0,spacing=pi/4000,slide=1.0):
    return spiro_arc(0,0,0,R,a,b,loops,
                     slide=slide,offset=offset,spacing=spacing,invert=True,reverse=False)

def spiro_arc(x0=0,y0=0,orient=0,R=10.0,a=4.0,b=3.5,
              loops=1,offset=0,spacing=pi/4000,
              slide=1.0,start_guard=0,end_guard=0,start_guard_angle=0,end_guard_angle=0,
              invert=False,reverse=False):  
    '''roll on the outside (inside if invert=True) of an arc
    centered on x0, y0, with radius, starting at orientation of
    orient radians cw from the vertical.  Arc has length loops * 2pi
    Direction of motion can be reversed by setting reverse=True
    '''
    iv = -1 if invert else 1
    sd = SpiroData()

    # work out guard effects:  change in arc-length
    if start_guard_angle==0:  start_guard_angle = start_guard/(R+iv*a)
    if end_guard_angle==0:    end_guard_angle   = end_guard/(R+iv*a)

    t=np.linspace(0.0,(2*pi*R/a)*loops-(start_guard_angle+end_guard_angle)*R/a,int(loops/spacing))

    # work out start_guard and end_guard effects in invert and reverse situations

    if invert: t *= -1
    if reverse: t=-1*t

    guard_offset_angle=start_guard_angle
#    guard_offset_angle=end_guard_angle if False else start_guard_angle  # work this out later
    
    sd.x=x0+(R+iv*a)*sin(slide*iv*t*a/R+orient+guard_offset_angle) + b*sin(t+offset)
    sd.y=y0+(R+iv*a)*cos(slide*iv*t*a/R+orient+guard_offset_angle) + b*cos(t+offset)
    sd.p=t+offset 
    
    return sd

def spiro_steps(R=10,a=4,b=3.5,loops=1,n=10,offset=pi/10,spacing=pi/2000):
    sd = SpiroData()
    for i in range(n): sd.add(spiro(R,a,b,loops,offset=offset*i,spacing=spacing)) 
    return sd

# def roll_orig(x1,y1,x2,y2,a,b,offset=0,guard=0,invert=False):
#     '''roll in straight line from (x1,y1) to (x2,y2)
#     using wheel of diameter a and pen position b.
#     offset is the start angle off the vertical for the pen, in radians.
#     invert keyword controls sense of wheel location:  default
#     is above and/or to the right.  invert=True is the opposite.
#     '''
#     R=sqrt((x2-x1)**2+(y2-y1)**2) - 2*guard # roll distance
#     A=arctan2(y2-y1,x2-x1)                  # roll angle
#     t=np.linspace(0,R/a,1000)               # angle through which the wheel rolls
# 
#     iv = -1 if invert else 1
# 
#     xs=x1-iv*a*sin(A)+guard*cos(A)
#     ys=y1+iv*a*cos(A)+guard*sin(A)
# 
#     sd = SpiroData()
#     sd.x = xs+a*t*cos(A) +iv*b*sin(t+offset)
#     sd.y = ys+a*t*sin(A) +   b*cos(t+offset)  # consistent with spiro
#     sd.p = t+offset
#     
#     return sd

def roll(x1,y1,x2,y2,a,b,offset=0,start_guard=0,end_guard=0,invert=False):
    '''roll in straight line from (x1,y1) to (x2,y2)
    using wheel of diameter a and pen position b.
    offset is the start angle off the vertical for the pen, in radians.
    invert keyword controls sense of wheel location:  default
    is above and/or to the right.  invert=True is the opposite.
    '''
    R=sqrt((x2-x1)**2+(y2-y1)**2) - (start_guard+end_guard)  # roll distance
    A=arctan2(y2-y1,x2-x1)                                   # roll angle
    t=np.linspace(0,R/a,1000)           # angle through which the wheel rolls

    iv = -1 if invert else 1

    # do we have to swap to end_guard on inversion?
    
    xs=x1-iv*a*sin(A)+start_guard*cos(A)
    ys=y1+iv*a*cos(A)+start_guard*sin(A)

    if invert: t *= -1

    sd = SpiroData()
    sd.x = xs+iv*a*t*cos(A) + b*sin(t+offset)
    sd.y = ys+iv*a*t*sin(A) + b*cos(t+offset) 
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
    sd.p = t+phi  # this "offset" angle no longer connects to rolling
        
    return sd

def cos_angle(a,b,c):
    return arccos( (a**2+b**2-c**2) / (2*a*b) )

def corner_guard(wheel_size=0,corner_angle=pi/2,):
    return wheel_size/tan(corner_angle/2)

def rot_2D(angle):
    '''Matrix will rotate a coordinate by angle_rads cw'''
    return array([ [ cos(angle), sin(angle) ],
                   [-sin(angle), cos(angle)  ] ])

def rot_coords(angle_rads,coords):
    cc = np.empty((coords.shape[0],2))
    for i in range(cc.shape[0]):
        cc[i] = np.matmul(rot_2D(angle_rads),coords[i])

    return cc

def spiro_line_orig(R=60,a=12,b=7.2,orient=0,loops=60,n=1,fold=False, invert=False):

    cc = rot_coords(orient,array([ [-R/2,0], [R/2,0] ]))

    # evenually, calculate rotation angles around each corner
    rot_angle=pi
    if (fold): rot_angle = rot_angle - 2*pi

    sd = SpiroData()
    
    offset=0
    
    for i in range(loops):
        
        for c in range(cc.shape[0]):
        
            cn=(c+1) % cc.shape[0]
            
            sd.add(roll(cc[c,0],cc[c,1],cc[cn,0],cc[cn,1],a,b,offset,invert=invert))  # cycloids roll
            offset=sd.pc()
        
            sd.add(rotate(cc[cn,0],cc[cn,1],sd.xc(),sd.yc(),rot_angle)) # roll over upper right
            offset+=rot_angle
        
    return sd

def spiro_line(R=60,a=12,b=7.2,orient=0,offset=0,loops=60,n=1,fold=False, invert=False):
    coords=array([ [-R/2,0], [R/2,0] ])
    return spiro_polygon(coords,a,b,orient,
                         offset=offset,loops=loops,fold=fold,inside=False)  # invert doesn't work

def spiro_eq_triangle(R=60,a=12,b=7.2,orient=0,offset=0,loops=60,n=1,fold=False,inside=False):
    ytop = R*sin(pi/3.0)
    coords = array([ [-R/2,-ytop/3], [0,2*ytop/3], [R/2,-ytop/3] ])
    return spiro_polygon(coords,a,b,orient,
                         offset=offset,loops=loops,fold=fold,inside=inside)

def spiro_square(R=60,a=12,b=7.2,orient=0,offset=0,loops=60,fold=False,inside=False):
    coords = array([ [-R/2,R/2], [R/2,R/2], [R/2,-R/2], [-R/2,-R/2] ])
    return spiro_polygon(coords,a,b,orient,
                         offset=offset,loops=loops,fold=fold,inside=inside)

def spiro_ngon(n,R=60,a=12,b=7.2,orient=0,offset=0,loops=1,fold=False,inside=False):
    coords = np.empty((n,2))
    for i in range(n):
        theta = -2*pi*i/n
        coords[i,0]=R*cos(theta)
        coords[i,1]=R*sin(theta)
    return spiro_polygon(coords,a,b,orient,
                         offset=offset,loops=loops,fold=fold,inside=inside)

def corner_angles(coords,inside=False):
    '''find the angle between adjacent pairs of coords'''
    ba = np.empty(coords.shape[0])
    unit_z = -1 if inside else 1
    for c0 in range(coords.shape[0]):
        c1 = (c0+1) % coords.shape[0]
        c2 = (c0+2) % coords.shape[0]
        v1 = coords[c1]-coords[c0]
        v2 = coords[c2]-coords[c1]
        arccos_arg = v1.dot(v2) / sqrt(v1.dot(v1)*v2.dot(v2))
        # protect against out of range arccos arguments (due to precision error)
        if   (arccos_arg >  1): ba[c0]=0
        elif (arccos_arg < -1): ba[c0]=pi
        else:                   ba[c0]=arccos(arccos_arg)
        # get orientation of first and second vectors
        if (np.cross(v1,v2).dot(unit_z)<=0): ba[c0]*=-1       # v2 veers away from v1:  -angle for rotation
        else:                                ba[c0]=pi-ba[c0] # v2 veers towards v1: corner angle

    return ba
            
def spiro_polygon(coords,wheel,pen,orient=0,loops=1,offset=0,fold=False,inside=False):

    cc = rot_coords(orient,coords)
    ba = corner_angles(cc,inside)
    
    bump = [ 0 for i in range(len(ba)) ]

    for c in range(ba.shape[0]):
        if ba[c]>0:
            bump[c] = corner_guard(wheel,ba[c])
            ba[c]=0  # to indicate no rotation
        else:
            ba[c]*=-1 # rotation angles
            
    sd = SpiroData()
    
    for i in range(loops):
        
        for c in range(cc.shape[0]):
        
            cp=(c+cc.shape[0]-1) % cc.shape[0]
            cn=(c+1) % cc.shape[0]

            sd.add(roll(cc[c,0],cc[c,1],cc[cn,0],cc[cn,1],wheel,pen,offset,
                        start_guard=bump[cp],end_guard=bump[c],invert=inside)) 
            offset=sd.pc()

            if ba[c]>0:
                if inside: rot_angle= -ba[c]
                else:      rot_angle=  ba[c]
                if fold:
                    rot_angle=ba[c]+2*pi if inside else ba[c]-2*pi
                sd.add(rotate(cc[cn,0],cc[cn,1],sd.xc(),sd.yc(),rot_angle)) # roll over upper right
                offset+=rot_angle
    
    return sd

def poly_heart(width=40,depth=20,height=5,wheel=2.2,pen=1.0,orient=0,offset=0,loops=1,
               fold=False,inside=False,guarded=True):
    coords = array([ [0,-depth], [-width/2,-height/2], [-width/2+width/12,0], [-width/6,height],
                     [0,0], [width/6,height], [width/2-width/12,0], [width/2,-height/2] ])
    return spiro_polygon(coords,wheel,pen,orient,
                         offset=offset,loops=loops,fold=fold,inside=inside)

def heart(x0=0,y0=0,width=40,depth=20,wheel=2.2,pen=1.0,loops=1,offset=0.0,
          inside=False,fold=False,guarded=True):

    sd = SpiroData()

    g=1 if guarded else 0
    o=offset
    
    for k in range(loops):

        if inside:

            ba=corner_angles(np.array([ [x0,y0-depth], [x0-width/2,y0], [x0-width/2,y0+1] ]),inside=True)
            cg=corner_guard(wheel,ba[0])
            
            sd.add(roll(x0,y0-depth,x0-width/2,y0,wheel,pen,offset=o,
                        start_guard=g*corner_guard(wheel,pi/2),end_guard=g*cg,
                        invert=True))
            sd.add(spiro_arc(x0-width/4,y0,-pi/2,width/4,wheel,pen,loops=0.5,offset=sd.pc(),
                             start_guard=g*cg,
                             invert=True))
            
            o = sd.pc()
            rot_angle = pi if fold else -pi
            sd.add(rotate(x0,y0,sd.xc(),sd.yc(),rot_angle))
            sd.add(spiro_arc(x0+width/4,y0,-pi/2,width/4,wheel,pen,loops=0.5,offset=o+rot_angle,
                             end_guard=g*cg,
                             invert=True))
            sd.add(roll(x0+width/2,y0,x0,y0-depth,wheel,pen,offset=sd.pc(),
                        start_guard=g*corner_guard(wheel,pi-pi/4),
                        end_guard=g*corner_guard(wheel,pi/2),
                        invert=True))
            o=sd.pc()

        else:
            
            sd.add(roll(x0,y0-depth,x0-width/2,y0,wheel,pen,offset=o))
            o = sd.pc()
            rot_angle = pi/4 - 2*pi if fold else pi/4
            sd.add(rotate(x0-width/2,y0,sd.xc(),sd.yc(),rot_angle))

            ca=cos_angle(width/4+wheel,width/4+width/4,width/4+wheel)

            sd.add(spiro_arc(x0-width/4,y0,-pi/2,width/4,wheel,pen,loops=0.5,offset=o+rot_angle,
                             end_guard_angle=g*ca))

            ca=cos_angle(width/4+width/4,width/4+wheel,width/4+wheel)

            sd.add(spiro_arc(x0+width/4,y0,-pi/2,width/4,wheel,pen,loops=0.5,offset=sd.pc(),
                             start_guard_angle=g*ca))
            o = sd.pc()
            rot_angle = pi/4 - 2*pi if fold else pi/4
            sd.add(rotate(x0+width/2,y0,sd.xc(),sd.yc(),rot_angle))
            sd.add(roll(x0+width/2,y0,x0,y0-depth,wheel,pen,offset=o+rot_angle))
            o = sd.pc()
            rot_angle = pi/2 - 2*pi if fold else pi/2
            sd.add(rotate(x0,y0-depth,sd.xc(),sd.yc(),rot_angle))
            o += rot_angle

    return sd

