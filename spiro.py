from SpiroData import *
import numpy as np
from numpy import sin,cos,arctan2,arccos,pi,sqrt,tan,array

class Wheel:   # might consider making "spacing" part of the Wheel's data

    def __init__(self,radius=3.0, pen=2.0, offset=0):
        self.r = radius # radius of the wheel
        self.m = pen    # marker position
        self.o = offset # cw angle from the vertical

def spiro(R=10,wheel=Wheel(4,3.5,0.0),loops=5,
          slide = lambda t: 1,
          spacing=pi/4000,orient=0):
    return spiro_arc(x0=0,y0=0,orient=orient,R=R,wheel=wheel,loops=loops,
                     slide=slide,
                     spacing=spacing,invert=True,reverse=False)

def spiro_arc(x0=0,y0=0,orient=0,R=10.0,wheel=Wheel(4,3.5,0),
              loops=1,spacing=pi/4000,
              slide = lambda t: 1,
              start_guard=0,end_guard=0,start_guard_angle=0,end_guard_angle=0,
              invert=False,reverse=False):  
    '''roll on the outside (inside if invert=True) of an arc
    centered on x0, y0, with radius, starting at orientation of
    orient radians cw from the vertical.  Arc has length loops * 2pi
    Direction of motion can be reversed by setting reverse=True
    '''
    iv = -1 if invert else 1
    sd = SpiroData()

    a = wheel.r
    b = wheel.m
    offset = wheel.o
    
    # work out guard effects:  change in arc-length
    if start_guard_angle==0:  start_guard_angle = start_guard/(R+iv*a)
    if end_guard_angle==0:    end_guard_angle   = end_guard/(R+iv*a)

    t=np.linspace(0.0,(2*pi*R/a)*loops-(start_guard_angle+end_guard_angle)*R/a,int(loops/spacing))

    p = t
    
    guard_offset_angle=start_guard_angle
    
#    guard_offset_angle=end_guard_angle if False else start_guard_angle  # work this out later

    theta_factor = iv * a/R * slide(t)
    phi_factor   = 1
    
    # work out start_guard and end_guard effects in invert and reverse situations

    if invert:
        phi_factor   *= -1
        theta_factor *= -1
    if reverse:
        phi_factor   *= -1
        theta_factor *= -1
    
    guard_offset_angle=start_guard_angle
    
#    guard_offset_angle=end_guard_angle if False else start_guard_angle  # work this out later

    p     = phi_factor   * t + offset
    theta = theta_factor * t + orient + guard_offset_angle
    r     = R + iv * a
    
    sd.t=t
    sd.x=x0+r*sin(theta) + b*sin(p)
    sd.y=y0+r*cos(theta) + b*cos(p)
    sd.p=p
    
    return sd

def spiro_steps(R=10,wheel=Wheel(4,3.5,0),loops=1,n=10,offset=pi/10,spacing=pi/2000):
    sd = SpiroData()
    for i in range(n):
        wheel.o = offset*i
        sd.add(spiro(R=R,wheel=wheel,loops=loops,spacing=spacing)) 
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

def roll(x1,y1,x2,y2,wheel,start_guard=0,end_guard=0,invert=False):
    '''roll in straight line from (x1,y1) to (x2,y2) using circular wheel
    invert keyword controls sense of wheel location:  default
    is above and/or to the right.  invert=True is the opposite.
    '''
    
    a = wheel.r
    b = wheel.m
    offset = wheel.o
    
    D=sqrt((x2-x1)**2+(y2-y1)**2) - (start_guard+end_guard)  # roll distance
    A=arctan2(y2-y1,x2-x1)                                   # roll angle
    t=np.linspace(0,2*pi*(D/(2*pi*a)),1000)                  # angle through which the wheel rolls
    
    iv = -1 if invert else 1

    phi_factor = 1
    time_factor = iv * a

    if invert:
        phi_factor  *= -1
        time_factor *= -1
        
    # do we have to swap to end_guard on inversion?

    xs = x1 - iv * a * sin(A) + start_guard * cos(A)
    ys = y1 + iv * a * cos(A) + start_guard * sin(A)

    p = phi_factor * t + offset
    
    sd = SpiroData()
    
    sd.x = xs + time_factor * t * cos(A) + b * sin(p)
    sd.y = ys + time_factor * t * sin(A) + b * cos(p) 
    sd.p = p
    sd.t = t
    
    return sd

def rotate(x0,y0,xr,yr,angle):
    '''rotate the coordinate (xr,yr) about the
    origin (x0,y0) by angle
    '''
    t=np.linspace(0.0,np.abs(angle),int(500*np.abs(angle)/pi))
    r=sqrt((xr-x0)**2+(yr-y0)**2)
    phi=arctan2(xr-x0,yr-y0)

    p = t
    
    if (angle<0):
        p *= -1

    p += phi
    
    sd = SpiroData()
    
    sd.x = x0+r*sin(p)
    sd.y = y0+r*cos(p)
    sd.p = p
    sd.t = t
        
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

def spiro_line_orig(R=60,wheel=Wheel(12,7.2),orient=0,loops=60,n=1,fold=False, invert=False):

    cc = rot_coords(orient,array([ [-R/2,0], [R/2,0] ]))

    # evenually, calculate rotation angles around each corner
    rot_angle=pi
    if (fold): rot_angle = rot_angle - 2*pi

    sd = SpiroData()
    
    offset=0
    
    for i in range(loops):
        
        for c in range(cc.shape[0]):
        
            cn=(c+1) % cc.shape[0]
            
            sd.add(roll(cc[c,0],cc[c,1],cc[cn,0],cc[cn,1],wheel,invert=invert))  # cycloids roll        
            sd.add(rotate(cc[cn,0],cc[cn,1],sd.xc(),sd.yc(),rot_angle)) # roll over upper right
            wheel.o += rot_angle
        
    return sd

def spiro_line(R=60,wheel=Wheel(12,7.2,0),orient=0,loops=60,n=1,fold=False, invert=False):
    coords=array([ [-R/2,0], [R/2,0] ])
    return spiro_polygon(coords,wheel,orient,loops=loops,fold=fold,inside=False)  # invert doesn't work

def spiro_eq_triangle(R=60,wheel=Wheel(12,7.2,0),orient=0,loops=60,n=1,fold=False,inside=False):
    ytop = R*sin(pi/3.0)
    coords = array([ [-R/2,-ytop/3], [0,2*ytop/3], [R/2,-ytop/3] ])
    return spiro_polygon(coords,wheel,orient,loops=loops,fold=fold,inside=inside)

def spiro_square(R=60,wheel=Wheel(12,7.2),orient=0,loops=60,fold=False,inside=False):
    coords = array([ [-R/2,R/2], [R/2,R/2], [R/2,-R/2], [-R/2,-R/2] ])
    return spiro_polygon(coords,wheel,orient,loops=loops,fold=fold,inside=inside)

def spiro_cross(width=30,height=30,fwidth=1/3,fheight=1/3,base=1/3,
                wheel=Wheel(0.01,0),orient=0,loops=1,
                fold=False,inside=False):
    (x0,x1,x2,x3) = (-width/2, -fwidth*width/2, fwidth*width/2, width/2)
    (y0,y1,y2,y3) = (height*(-base-fheight/2), -height*fheight/2, height*fheight/2, height*(1-fheight/2-base))
    coords = array([ [x0,y2], [x1,y2], [x1,y3], [x2,y3], [x2,y2], [x3,y2],
                     [x3,y1], [x2,y1], [x2,y0], [x1,y0], [x1,y1], [x0,y1] ])
    return spiro_polygon(coords,wheel,orient=orient,loops=loops,fold=fold,inside=inside)
    
def spiro_ngon(n,R=60,wheel=Wheel(12,7.2),orient=0,loops=1,fold=False,inside=False):
    coords = np.empty((n,2))
    for i in range(n):
        theta = -2*pi*i/n
        coords[i,0]=R*cos(theta)
        coords[i,1]=R*sin(theta)
    return spiro_polygon(coords,wheel,orient,loops=loops,fold=fold,inside=inside)
    
def spiro_nstar(n,r1=30,r2=0.5,wheel=Wheel(0.01,0),
                orient=0,loops=1,fold=False,inside=False):
    coords = np.empty((2*n,2))
    for i in range(0,n):
        theta1 = -2*pi*i/n
        theta2 = -(2*i+1)*pi/n
        coords[2*i,0]=r1*cos(theta1)
        coords[2*i,1]=r1*sin(theta1)
        coords[2*i+1,0]=r2*r1*cos(theta2)
        coords[2*i+1,1]=r2*r1*sin(theta2)
        
    return spiro_polygon(coords,wheel,orient,
                         loops=loops,fold=fold,inside=inside)

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
            
def spiro_polygon(coords,wheel,orient=0,loops=1,fold=False,inside=False):

    cc = rot_coords(orient,coords)
    ba = corner_angles(cc,inside)
    
    bump = [ 0 for i in range(len(ba)) ]

    for c in range(ba.shape[0]):
        if ba[c]>0:
            bump[c] = corner_guard(wheel.r,ba[c])
            ba[c]=0  # to indicate no rotation
        else:
            ba[c]*=-1 # rotation angles
            
    sd = SpiroData()
    
    for i in range(loops):
        
        for c in range(cc.shape[0]):
        
            cp=(c+cc.shape[0]-1) % cc.shape[0]
            cn=(c+1) % cc.shape[0]

            sd.add(roll(cc[c,0],cc[c,1],cc[cn,0],cc[cn,1],wheel,
                        start_guard=bump[cp],end_guard=bump[c],invert=inside)) 
            wheel.o=sd.pc()

            if ba[c]>0:
                if inside: rot_angle= -ba[c]
                else:      rot_angle=  ba[c]
                if fold:
                    rot_angle=ba[c]+2*pi if inside else ba[c]-2*pi
                sd.add(rotate(cc[cn,0],cc[cn,1],sd.xc(),sd.yc(),rot_angle)) # roll over upper right
                wheel.o+=rot_angle
    
    return sd

def poly_heart(width=40,depth=20,height=5,wheel=Wheel(2.2,1.0),orient=0,loops=1,
               fold=False,inside=False,guarded=True):
    coords = array([ [0,-depth], [-width/2,-height/2], [-width/2+width/12,0], [-width/6,height],
                     [0,0], [width/6,height], [width/2-width/12,0], [width/2,-height/2] ])
    return spiro_polygon(coords,wheel,orient,loops=loops,fold=fold,inside=inside)

def heart(x0=0,y0=0,width=40,depth=20,wheel=Wheel(2.2,1.0),loops=1,
          inside=False,fold=False,guarded=True):

    sd = SpiroData()

    g=1 if guarded else 0
    
    for k in range(loops):

        if inside:

            ba=corner_angles(np.array([ [x0,y0-depth], [x0-width/2,y0], [x0-width/2,y0+1] ]),inside=True)
            cg=corner_guard(wheel.r,ba[0])
            
            sd.add(roll(x0,y0-depth,x0-width/2,y0,wheel,
                        start_guard=g*corner_guard(wheel.r,pi/2),end_guard=g*cg,invert=True))
            wheel.o=sd.pc()
            sd.add(spiro_arc(x0-width/4,y0,-pi/2,width/4,wheel,loops=0.5,start_guard=g*cg,invert=True))
            
            wheel.o = sd.pc()
            rot_angle = pi if fold else -pi
            sd.add(rotate(x0,y0,sd.xc(),sd.yc(),rot_angle))
            wheel.o += rot_angle
            sd.add(spiro_arc(x0+width/4,y0,-pi/2,width/4,wheel,loops=0.5,end_guard=g*cg,invert=True))
            wheel.o = sd.pc()
            sd.add(roll(x0+width/2,y0,x0,y0-depth,wheel,
                        start_guard=g*corner_guard(wheel.r,pi-pi/4),
                        end_guard=g*corner_guard(wheel.r,pi/2),
                        invert=True))
            wheel.o=sd.pc()

        else:
            
            sd.add(roll(x0,y0-depth,x0-width/2,y0,wheel))
            wheel.o = sd.pc()
            rot_angle = pi/4 - 2*pi if fold else pi/4
            sd.add(rotate(x0-width/2,y0,sd.xc(),sd.yc(),rot_angle))

            ca=cos_angle(width/4+wheel.r,width/4+width/4,width/4+wheel.r)
            wheel.o += rot_angle
            
            sd.add(spiro_arc(x0-width/4,y0,-pi/2,width/4,wheel,loops=0.5,end_guard_angle=g*ca))

            ca=cos_angle(width/4+width/4,width/4+wheel.r,width/4+wheel.r)
            wheel.o = sd.pc()
            sd.add(spiro_arc(x0+width/4,y0,-pi/2,width/4,wheel,loops=0.5,start_guard_angle=g*ca))
            wheel.o = sd.pc()
            rot_angle = pi/4 - 2*pi if fold else pi/4
            sd.add(rotate(x0+width/2,y0,sd.xc(),sd.yc(),rot_angle))
            wheel.o += rot_angle
            sd.add(roll(x0+width/2,y0,x0,y0-depth,wheel))
            wheel.o = sd.pc()
            rot_angle = pi/2 - 2*pi if fold else pi/2
            sd.add(rotate(x0,y0-depth,sd.xc(),sd.yc(),rot_angle))
            wheel.o += rot_angle

    return sd

