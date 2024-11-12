import numpy as np

#ponts: first>>>second

def conformal2d(first,second,points):
    i = 0
    A = []
    y = []
    while i<len(first):
        A.append([first[i][0],-first[i][1],1,0])
        A.append([first[i][1],first[i][0],0,1])
        y.append(second[i][0])
        y.append(second[i][1])
        i += 1
    y = np.matrix(y).transpose()
    A = np.matrix(A)
    C = (np.linalg.inv(A.transpose()*A))*A.transpose()*y
    i = 0
    A = []
    print first
    print second
    while i<len(points):
        A.append([points[i][0],-points[i][1],1,0])
        A.append([points[i][1],points[i][0],0,1])
        i += 1
    pointsInSecond = (A*C).tolist()
    res = []
    i = 0
    while i<len(points):
        res.append([pointsInSecond[2*i][0],pointsInSecond[2*i+1][0]])
        i += 1
    return res
