from numpy import sin,cos,empty,array,matmul

def rot_2D(angle):
    '''Matrix will rotate a coordinate by angle_rads cw'''
    return array([ [ cos(angle), sin(angle) ],
                   [-sin(angle), cos(angle)  ] ])

def rot_coords(angle_rads,coords):
    cc = empty((coords.shape[0],2))
    for i in range(cc.shape[0]):
        cc[i] = matmul(rot_2D(angle_rads),coords[i])

    return cc
