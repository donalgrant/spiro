from SpiroData import *
import numpy as np
from numpy import sin,cos,arctan2,arccos,pi,sqrt,tan,array,arctan,empty,linspace
from Ellipse import *
from SpiroGeometry import *
from Ring import *

def eIe(ring=Ellipse(20,0.5,0,0),
                       wheel=Ellipse(3,0.5,2,0),
                       loops=1,
#                       slide = lambda t: 1,   # original code
                       slide=None,
                       start_guard=0,end_guard=0,
                       start_guard_angle=0,end_guard_angle=0,
                       ppl=4000,inside=True,reverse=False,object=0):  
    '''roll on the inside (outside if inside=False) of an *elliptical* arc
    centered on x0, y0, with radius, starting at orientation of
    orient radians cw from the vertical given by ring.o; initial position of
    wheel given by ring.po.  Arc has length loops * ellipse_circum
    
    '''

    sd = SpiroData()

    RC = ring.c

    t=linspace(0,loops,int(loops*ppl))
    if reverse:  t *= -1
    
    iv = -1 if inside else 1
    
    # work out start_guard and end_guard effects
    # in invert and reverse situations

    p   = t * ring.c / wheel.c * 2 * pi + wheel.o 
    rp  = array([ wheel.r(phi) for phi in p ])
    
    '''  # original code
    arc = array([ wheel.arc(p[0],phi) for phi in p ])
    ring_phi = array([ ring.phi_at_arc(iv * arc_i * slide(arc_i), ring.po)
                       for arc_i in arc])
    '''
    
    arc = slide_arc(array([ wheel.arc(p[0],phi) for phi in p ]),slide)
    ring_phi = array([ ring.phi_at_arc(iv * arc_i, ring.po) for arc_i in arc])
    ring_r   = array([ ring.r(phi) for phi in ring_phi ])
    ring_n   = array([ ring.normal_at_phi(phi) for phi in ring_phi ])

    # coordinate of contact
    
    cx = ring_r * sin(ring_phi)  
    cy = ring_r * cos(ring_phi)

    # normal at point of contact

    wheel_n = array([ wheel.normal_at_phi(phi) for phi in p ])
    
    # unrotated ellipse center coord

    ucx = cx + iv * rp * sin(-p)
    ucy = cy + iv * rp * cos(-p)

    # unrotated ellipse pen coord

    upx = ucx + wheel.m * sin(wheel.po)
    upy = ucy + wheel.m * cos(wheel.po)

    # rotate ellipse center and pen positions to align wheel normal with ring normal

    pp = empty((ring_n.shape[0],2))
    
    for i in range(ring_n.shape[0]):
        pp[i] = rot_about(array([cx[i],cy[i]]),wheel_n[i]+ring_n[i],
                          array([ [upx[i],upy[i]] ]))
        
    # coordinate of pen

    sd.t = t
    sd.p = p
    sd.o = full((int(loops*ppl)),object)
    sd.s = t//ppl

    sd.x = pp[:,0]
    sd.y = pp[:,1]

    sd.fx = cx
    sd.fy = cy
    sd.v  = np.full((sd.n()),1)

    
    sd.rotate(ring.o).move(ring.O[0],ring.O[1])
    
    return sd

def eIc(ring=Ring(10),wheel=Ellipse(3,0.5,2,0,0),
                      loops=1,ppl=1000,inside=True,object=0,slide=None):
    return elliptical_arc(ring.O[0],ring.O[1],ring.o,ring.r,wheel=wheel,
                          loops=loops,spacing=1/ppl,inside=inside,
                          pen_offset=wheel.po,object=object,slide=slide)

def elliptical_arc(x0=0,y0=0,orient=0,R=10.0,wheel=Ellipse(3,0.5,2,0),
                   loops=1,spacing=pi/4000,inside=True,pen_offset=0,object=0,slide=None):  
    '''roll on the outside (inside if invert=True) of an arc
    centered on x0, y0, with radius, starting at orientation of
    orient radians cw from the vertical.  Arc has length loops * 2pi
    Todo:  Direction of motion can be reversed by setting reverse=True
    '''

    sd = SpiroData()

    RC = circum(R)

    N = int(loops/spacing)
    t=linspace(0.0,wheel.phi_at_arc(RC*loops),N)

    iv = -1 if inside else 1
    
    # work out start_guard and end_guard effects in invert and reverse situations

    p   = t + wheel.o
    rp  = array([ wheel.r(phi) for phi in p ])

    arc = slide_arc( array([ wheel.arc(p[0],phi) for phi in p ]), slide  )
    '''
    arc_orig = array([ wheel.arc(p[0],phi) for phi in p ])
    darc = arc_orig[1:N]-arc_orig[0:N-1]
    for j in range(darc.shape[0]):
        darc[j] *= array_val(slide,j)
    arc = arc_orig[0]+np.append(0,darc.cumsum())
    '''
    theta = iv * arc / R + orient

    # coordinate of contact
    
    cx = R * sin(theta)
    cy = R * cos(theta)

    # normal at point of contact

    normal = array([ wheel.normal_at_phi(phi) for phi in p ])
    
    # unrotated ellipse center coord

    ucx = cx + iv * rp * sin(-p)
    ucy = cy + iv * rp * cos(-p)

    # unrotated ellipse pen coord

    upx = ucx + wheel.m * sin(pen_offset)
    upy = ucy + wheel.m * cos(pen_offset)

    # rotate ellipse center and pen positions to align normal with ring radial

    pp = empty((theta.shape[0],2))
    
    for i in range(theta.shape[0]):
        pp[i] = rot_about(array([cx[i],cy[i]]),normal[i]+theta[i],array([ [upx[i],upy[i]] ]))
        
    # coordinate of pen

    sd.t = t
    sd.p = p
    sd.o = full((int(loops/spacing)),object)
    sd.s = (t*spacing).astype(int)

    sd.x = pp[:,0]
    sd.y = pp[:,1]

    sd.fx = cx
    sd.fy = cy
    sd.v  = np.full((sd.n()),1)


    return sd.move(x0,y0)

def roll_ellipse(x1,y1,x2,y2,ellipse,start_guard=0,end_guard=0,invert=False,ppl=1000,object=0,segment=0):
    '''roll in straight line from (x1,y1) to (x2,y2) using ellipse.
    invert keyword controls sense of wheel location:  default
    is above and/or to the right.  invert=True is the opposite.
    '''
    
    C = ellipse.c
    a = ellipse.a
    b = ellipse.m
    offset = ellipse.o

    R=sqrt((x2-x1)**2+(y2-y1)**2) - (start_guard+end_guard)  # roll distance
    A=arctan2(y2-y1,x2-x1)                                   # roll angle

    pf = ellipse.phi_at_arc(R,ellipse.o)
    t=linspace(0,pf,ppl)                 # angle through which the wheel rolls
    
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
    sd.o = full((ppl),object)
    sd.o = full((ppl),segment)
    sd.fx = linspace(x1,x2,sd.x.shape[0]) # should really include guards, but usually subtle effect
    sd.fy = linspace(y1,y2,sd.y.shape[0]) # ditto
    sd.v  = np.full((sd.n()),1)

    
    return sd

def integral_ellipticals(n,e_ring,e_wheel,ring_angle=pi/4,
                         min_pen=0.4,max_pen=1.0,
                         min_po=0.0,max_po=pi/2,
                         rounds=9,circuits=8,inside=True,ppl=1000):
    S = SpiroData()
    ring=Ellipse(major=20,eccen=e_ring,offset=ring_angle)
    nwr = rounds / circuits
    a = major_from_circum(ring.c/nwr,e_wheel)
    if n==1:
        return eIe(ring,Ellipse(a,e_wheel,min_pen*a,0,pen_offset=min_po),inside=inside,loops=circuits,ppl=ppl)
    for i in range(n):
        m  = min_pen + (max_pen-min_pen)*i/(n-1)
        po = min_po  + (max_po -min_po) *i/(n-1)
        wheel = Ellipse(a,e_wheel,m*a,0,pen_offset=po)
        S.add(eIe(ring,wheel,inside=inside,loops=circuits,object=i,ppl=ppl))

    return S
