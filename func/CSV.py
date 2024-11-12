import csv

def open_csv(filename):
    f = open(filename,'r')
    csvR = csv.reader(f, delimiter =',')
    res = []
    for row in csvR:
        res.append([float(t) for t in row])
    return res
