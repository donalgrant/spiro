from numpy import sin,cos,empty,array,matmul,linspace

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
