from numpy import sin,cos,empty,array,matmul,linspace,abs,pi,sqrt,arctan2,arccos,arcsin

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

def line(end_pt,npts=20):

    cc = empty((npts,2))
    
    if abs(end_pt[1,0]-end_pt[0,0]) < 1.0e-8:
        cc[:,0] = linspace(0,npts) * 0 + end_pt[0,0]
        cc[:,1] = linspace(end_pt[0,1],end_pt[1,1],npts)
    else:
        cc[:,0] = linspace(end_pt[0,0],end_pt[1,0],npts)
        cc[:,1] = end_pt[0,1] + (end_pt[1,1]-end_pt[0,1]) / (end_pt[1,0]-end_pt[0,0]) * (cc[:,0] - end_pt[0,0])

    return cc

def dist(end_pt):
    return sqrt((end_pt[1,0]-end_pt[0,0])**2+(end_pt[1,1]-end_pt[0,1])**2)

def arc_on_center(center,radius,arc_subtended,angle_offset=0,npts=20,to_origin=0):
    cc = empty((npts,2))
    for i in range(npts):
        angle = (i/(npts-1)-0.5)*arc_subtended
        cc[i,0] = radius*(cos(angle)-1+to_origin)
        cc[i,1] = radius*sin(angle)
    return rot_coords(angle_offset,cc)+center
        
def arc(end_pt,radius,invert=False,npts=20):

    cc = empty((npts,2))

    sign = -1 if invert else 1
    
    D = dist(end_pt)
    theta = arctan2(end_pt[1,0]-end_pt[0,0],end_pt[1,1]-end_pt[0,1])

    if radius < D/2:
        print('Illegal radius < D/2')
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

def eccen_from_flat(f):  return sqrt(2*f-f*f)
def eradius(eccen,phi):  return sqrt((1-eccen**2)/(1-(eccen*cos(phi))**2))

def ecoords(eccen,npts=50):
    '''unit-semi-major ellipse.  Can scale coords by semi-major axis'''
    cc = empty((npts,2))
    phi = linspace(0,2*pi,npts)
    ur = eradius(eccen,phi)
    cc[:,0]=ur*cos(phi)
    cc[:,1]=ur*sin(phi)
    return cc

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
