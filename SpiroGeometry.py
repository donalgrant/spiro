import sys
import numpy as np
from numpy import sin,cos,tan,empty,array,matmul,linspace,geomspace,full
from numpy import abs,pi,sqrt,arctan2,arccos,arcsin,diff,zeros,flip
from scipy.spatial.transform import Rotation as R
from scipy.interpolate import make_interp_spline


def array_val(a,i):
    '''Generic function to extract an element of an array, with
    wrapping on the element number.  If what is passed is a scalar,
    then the scalar itself is returned.'''
    
    return a[i%len(a)] if hasattr(a,"__len__") else a

def array_or_scalar_len(a):
    return len(a) if hasattr(a,"__len__") else 1

def rot_2D(angle):
    '''Matrix will rotate a coordinate by angle_rads cw'''
    return array([ [ cos(angle), sin(angle) ],
                   [-sin(angle), cos(angle)  ] ])

def rot_coords(angle_rads,coords):
    cc = empty((coords.shape[0],2))
    for i in range(cc.shape[0]):
        cc[i] = matmul(rot_2D(angle_rads),coords[i])

    return cc

def rot_about(origin,angle,coords):
    cc = empty((coords.shape[0],2))
    for i in range(cc.shape[0]):
        cc[i] = matmul(rot_2D(angle),coords[i]-origin)+origin
    return cc

def rotmat3D(axis,theta):  return R.from_rotvec(theta*axis).as_matrix()

def rot3D(xyz,rot_matrix):
    cc = empty((xyz.shape[0],3))
    for i in range(cc.shape[0]):
        cc[i] = matmul(rot_matrix,xyz[i])
    return cc

def rotX(xyz,theta): return rot3D(xyz,rotmat3D(array([1,0,0]),theta))
def rotY(xyz,theta): return rot3D(xyz,rotmat3D(array([0,1,0]),theta))
def rotZ(xyz,theta): return rot3D(xyz,rotmat3D(array([0,0,1]),theta))

def path_diffs(x,y): return sqrt(diff(x)**2+diff(y)**2)
def path_length(x,y): return sqrt(diff(x)**2+diff(y)**2).cumsum()
    
def line(end_pt,npts=20):

    cc = empty((npts,2))
    
    if abs(end_pt[1,0]-end_pt[0,0]) < 1.0e-8:
        cc[:,0] = full((npts),end_pt[0,0]) # linspace(0,npts) * 0 + end_pt[0,0]
        cc[:,1] = linspace(end_pt[0,1],end_pt[1,1],npts)
    else:
        cc[:,0] = linspace(end_pt[0,0],end_pt[1,0],npts)
        cc[:,1] = end_pt[0,1] + (end_pt[1,1]-end_pt[0,1]) / (end_pt[1,0]-end_pt[0,0]) * (cc[:,0] - end_pt[0,0])

    return cc

def dist(end_pt):
    return sqrt((end_pt[1,0]-end_pt[0,0])**2+(end_pt[1,1]-end_pt[0,1])**2)

def dir(end_pt):
    return arctan2(end_pt[1,1]-end_pt[0,1],end_pt[1,0]-end_pt[0,0])

def intersect(p1,p2,d1,d2,tol=1.0e-3):
    '''
    find the coordinate of the intersection of two lines through
    coordinates p1 and p2, respectively, and with angles ccw wrt
    horizontal of d1 and d2, respectively.  tol sets the minimum
    angle difference between d1 and d2 to find an intersection.
    '''
    if abs((d1 % pi) - (d2 % pi)) < tol:    # near-identical slopes
#        print('near-identical slopes:  ',d1,d2)
        pc = None
        '''
        if d1 % pi == pi/2:
            if p2[1]==p1[1]:
                pc = (p1+p2)/2.0
            else:
                print('    no intersection')
                pc = None
        else:
            m1 = tan(d1)
            print('   slope is ',m1)
            if (p2[1]-p1[1]) == m1*(p2[0]-p1[0]):
                print('    avg coord')
                pc = (p1+p2)/2.0
            else:
                print('    no intersection')
                pc = None
        '''
    else:  # non-identical slopes
#        print('-->slopes are different')
        if   d1 % pi == pi/2:  # vertical n1 slope
#            print('    d1 is vertical:  ',d1)
            m2 = tan(d2)
#            print('    m2: ',m2)
            pc = array([ p1[0], m2*(p1[0]-p2[0])+p2[1] ])
        elif d2 % pi == pi/2:  # vertical n2 slope
#            print('    d2 is vertical:  ',d2)
            m1 = tan(d1)
#            print('    m1: ',m1)
            pc = array([ p2[0], m1*(p2[0]-p1[0])+p1[1] ])
        else:
            m1 = tan(d1)
            m2 = tan(d2)
#            print('    m1, m2: ',m1,m2)
            xc = (p2[1]-p1[1] + m1*p1[0] + m2*p2[0]) / (m1-m2)
            yc = m1*xc - m1*p1[0] + p1[1]
            pc = array([ xc, yc ])
            
    return pc


def arc_on_center(center,radius,arc_subtended,angle_offset=0,npts=20,to_origin=0):
    cc = empty((npts,2))
    for i in range(npts):
        angle = (i/(npts-1)-0.5)*arc_subtended
        cc[i,0] = radius*(cos(angle)-1+to_origin)
        cc[i,1] = radius*sin(angle)
    return rot_coords(angle_offset,cc)+center

def arc_between_pts(end_pt,arc_subtended,npts=20):
    cc = empty((npts,2))
    if arc_subtended == 0:  return line(end_pt,npts)
    invert=True if arc_subtended<0 else False
    D=dist(end_pt)
    return arc(end_pt,abs((D/2)/sin(arc_subtended/2)),invert=invert,npts=npts)
        
def arc(end_pt,radius,invert=False,npts=20):

    cc = empty((npts,2))

    sign = -1 if invert else 1
    
    D = dist(end_pt)
    theta = arctan2(end_pt[1,0]-end_pt[0,0],end_pt[1,1]-end_pt[0,1])

    if radius < D/2:
        print(f'Illegal radius={radius} < D/2={D/2} with pi/theta={pi/theta}')
        return

    yc = D/2
    
    if (radius == yc):  # protect against precision-induced float-error in sqrt
        xc = 0
    else:
        xc = sqrt(radius**2-(D/2)**2)

    phi = arcsin(D/(2*radius))
    
    for i in range(npts):
        p = 2*phi*(i/(npts-1) - 0.5)
        cc[i,0] = sign*(xc - radius*cos(p))
        cc[i,1] = yc + radius*sin(p)

    cr  = rot_about(array([0,0]),theta,cc)  # rotate by -theta
    cr += end_pt[0]   # move to beginning of line (arc)

    return cr

def cot(radians): return 0 if radians==pi/2 else 1/tan(radians)

def par_diag(oangle,asym):
    c = (1+asym)/(1-asym)
    return arctan2(1.0,c*c+cot(oangle))

def rot_and_shift(coords,rot,xy_offset):
    cc = rot_about([0,0], rot, coords)
    for i in range(cc.shape[0]):  cc[i] -= xy_offset
    return cc
    
def tcoords(oangle,asym=0,fb=0,fh=0,prot=0):
    '''unit-area triangle with origin angle oangle and asymmetry angle asym; pre-rotate cw by prot rads'''
    a = (1+asym)/2 * (pi-oangle)
    d = cot(oangle)+cot(a)
    h = sqrt(2.0/d)
    b = sqrt(2*d)
    coords = array([ [0,0], [b,0], [h*cot(oangle),h] ])
    xy = array([b*fb,h*fh])
    return rot_and_shift( coords, prot, xy )

def pcoords(oangle,asym=0,fb=0,fh=0,prot=0):
    '''unit-area parallelogram with origin angle oangle and asymmetry asym; pre-rotate by prot rads;
       fb, fh are base/height offsets'''

    c = (1+asym)/(1-asym)
    a = c
    h = 1 / a
    b = h / sin(oangle)
    coords = array([ [0,0], [a,0], [a+b*cos(oangle),h], [b*cos(oangle),h] ])
    xy = array([b*fb,h*fh])
    return rot_and_shift( coords, prot, xy )
    
def dcoords(oangle,asym=0,fb=0,fh=0,prot=0):  
    '''just a dot -- stand in for frame_only calls'''
    return array([ [0,0] ])

def ngon_coords(n,asym=0,fb=0,fh=0,prot=0):  # vertices on the unit circle
    coords = empty((n,2))
    for i in range(n):
        theta = -2*pi*i/n
        coords[i,0]=cos(theta)
        coords[i,1]=sin(theta)
    xy = array([fb,fh])
    return rot_and_shift( coords, prot, xy )

def nstar_coords(n,asym=0.5,fb=0,fh=0,prot=0):  # vertices on the unit circle
    coords = empty((2*n,2))
    r2=asym
    for i in range(0,n):
        theta1 = -2*pi*i/n
        theta2 = -(2*i+1)*pi/n
        coords[2*i,0]=cos(theta1)
        coords[2*i,1]=sin(theta1)
        coords[2*i+1,0]=r2*cos(theta2)
        coords[2*i+1,1]=r2*sin(theta2)
    xy = array([fb,fh])
    return rot_and_shift( coords, prot, xy )
        
def eccen_from_flat(f):  return sqrt(2*f-f*f)
def eradius(eccen,phi):  return sqrt((1-eccen**2)/(1-(eccen*cos(phi))**2))

# reverse the original order to make consistent with other Xcoords functions
# added offsets to use with on_frame function
def ecoords(npts=50,eccen=0.0,fb=0,fh=0,prot=0):
    '''unit-semi-major ellipse.  Can scale coords by semi-major axis'''
    cc = empty((npts,2))
    phi = linspace(0,2*pi,npts)
    ur = eradius(eccen,phi)
    cc[:,0]=ur*cos(phi)
    cc[:,1]=ur*sin(phi)
    return rot_and_shift( cc, prot, array([fb,fh]) )

def ellipse_between_pts(end_pt,eccen,npts=50):

    cc = empty((npts,2))

    D = dist(end_pt)
    theta = arctan2(end_pt[1,0]-end_pt[0,0],end_pt[1,1]-end_pt[0,1])

    phi = linspace(0,2*pi,npts)
    a = D/2
    r = a*eradius(eccen,phi)

    cc[:,0] = r*cos(phi)
    cc[:,1] = r*sin(phi)
    
    cr  = rot_about(array([0,0]),-theta,cc)  # rotate by -theta
    cr += (end_pt[0]+end_pt[1])/2           # move ellipse to center of pts

    return cr

def cos_angle(a,b,c):
    return arccos( (a**2+b**2-c**2) / (2*a*b) )

'''
parameters: factor=1 (uniform), reverse=False, flip=True, option='linear','geometric','fibonacci','sinusoid', repeat=1, scale=max-path (1 if not given)
'''

def fibonacci(n):
    if n<3:  return 1
    x1 = 1
    x2 = 1
    for j in range(n-2):
        (x1,x2) = (x2,x1+x2)
    return x2
        
    
def frame_sampling(n,parm=1.0,spacing='linear',reverse=False,deramp=False,repeat=1):

    dn = 2*repeat if deramp else repeat
    
    match spacing:
        case 'linear':     x = linspace(1,1+parm,n//dn)
        case 'geometric':  x = geomspace(1,1+parm,n//dn)
        case 'sinusoid':   x = array([ 1.0 + parm*sin(pi*j/(2*n//dn)) for j in range(0,n//dn) ])
        case 'fibonacci':  x = array([ fibonacci(j+1) for j in range(n//dn) ])  # parm is ignored
        case _:
            print("***Error -- not a valid spacing")
            sys.exit()

    if reverse:  x = np.flip(x)
    if deramp:  x = np.append(x,flip(x))

    s = array([])
    for j in range(repeat):
        s = np.append(s,x)
        
    c = s.cumsum()
    return c/c[-1]


def slide_arc(arc_orig,slide=None):
    if slide is None:
        return arc_orig
    N = arc_orig.shape[0]
    darc = arc_orig[1:N]-arc_orig[0:N-1]
    for j in range(N-1):
        darc[j] *= array_val(slide,j)
    return arc_orig[0]+np.append(0,darc.cumsum())
