###### We should use sympy
###### first point from right image
import numpy as np
import sympy as sym
from conformal2d import conformal2d

#GCP is a 2dimensional list
#parameters is a Matrix
#pointPixel is a 2dimensional list

def findCoordinate(pointPixel,GCPpixelR,parameters,GCP):
    print pointPixel
    print GCPpixelR
    print parameters
    print GCP
    grounFirst2d = conformal2d(GCPpixelR,[[t[1],t[2]] for t in GCP],pointPixel)
    firstZ = 0
    for G in GCP:
        firstZ+= G[3]
    firstZ = firstZ/len(GCP)


    l = parameters
    y = []
    y.append(pointPixel[0][0]) #x Right
    y.append(pointPixel[0][1]) #y Right
    y.append(pointPixel[1][0]) #x left
    y.append(pointPixel[1][1]) #y left
    y = sym.Matrix(y)

    X = sym.symbols('X')
    Y = sym.symbols('Y')
    Z = sym.symbols('Z')
    Xsyms = sym.Matrix([X,Y,Z])

    Ysyms = [
    (l[0]*X+l[1]*Y+l[2]*Z+l[3])/(l[8]*X+l[9]*Y+l[10]*Z+1), #x Right
    (l[4]*X+l[5]*Y+l[6]*Z+l[7])/(l[8]*X+l[9]*Y+l[10]*Z+1), #y Right
    (l[11]*X+l[12]*Y+l[13]*Z+l[14])/(l[19]*X+l[20]*Y+l[21]*Z+1), #x left
    (l[15]*X+l[16]*Y+l[17]*Z+l[18])/(l[19]*X+l[20]*Y+l[21]*Z+1)  #y left
    ]
    Ysyms = sym.Matrix(Ysyms)

    Asyms = Ysyms.jacobian(Xsyms)
    xi = sym.Matrix([grounFirst2d[0][0],grounFirst2d[0][1],firstZ])
    print xi

    dx = sym.Matrix([10])
    try:
        while dx.norm()>0.0000000001:
            yi = Ysyms.subs({X:xi[0],Y:xi[1],Z:xi[2]})
            A = Asyms.subs({X:xi[0],Y:xi[1],Z:xi[2]})
            dy = y - yi
            print A.rank()
            dx = ((A.transpose()*A).inv())*A.transpose()*dy
            xi = dx + xi
            print '*'
    except ValueError as e:
        print e
        print 'be careful of doing steps truely'
    return xi
