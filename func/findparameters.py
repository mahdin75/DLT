###### We should use sympy
import numpy as np

def findParameters(GCP,GCPpixelR,GCPpixelL):

    # create observation vector an design matrix
    y = []
    A = []
    i = 0
    while i<6:     #6 is number of control point
        y.append(GCPpixelR[i][0]) #x of Right image
        y.append(GCPpixelR[i][1]) #y of Right image
        y.append(GCPpixelL[i][0]) #x of Left image
        y.append(GCPpixelL[i][1]) #y of Left image

        A.append([GCP[i][1], GCP[i][2], GCP[i][3], 1, 0, 0, 0, 0,
         -GCP[i][1]*GCPpixelR[i][0], -GCP[i][2]*GCPpixelR[i][0], -GCP[i][3]*GCPpixelR[i][0],
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ])

        A.append([0, 0, 0, 0, GCP[i][1], GCP[i][2], GCP[i][3], 1,
         -GCP[i][1]*GCPpixelR[i][1], -GCP[i][2]*GCPpixelR[i][1], -GCP[i][3]*GCPpixelR[i][1],
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ])

        A.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        GCP[i][1], GCP[i][2], GCP[i][3], 1,0, 0, 0, 0,
         -GCP[i][1]*GCPpixelL[i][0], -GCP[i][2]*GCPpixelL[i][0], -GCP[i][3]*GCPpixelL[i][0]])

        A.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, GCP[i][1], GCP[i][2], GCP[i][3], 1,
         -GCP[i][1]*GCPpixelL[i][1], -GCP[i][2]*GCPpixelL[i][1], -GCP[i][3]*GCPpixelL[i][1]])

        i += 1

    #save pixels for later
    #f = open('pixels.txt','wb')
    #f.write(str(GCPpixelR)+'+'+str(GCPpixelL))
    #f.close()

    y = np.matrix(y)
    y = y.transpose()
    A = np.matrix(A)
    L = (np.linalg.inv(A.transpose()*A))*A.transpose()*y

    print L

    #save L for later
    #f = open('parameters.txt','wb')
    #f.write(str(L))
    #f.close()
    
    return L
