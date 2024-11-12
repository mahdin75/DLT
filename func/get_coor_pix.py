import cv2
import numpy as np
from tkFileDialog import askopenfilename
import matplotlib.pyplot as plt

def getCoor(f,m):
    global res
    res = []
    global n
    n = 0
    def onclick(event):
        global n
        global res
        if n<m :
            if event.dblclick:
                print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
                ('double' if event.dblclick else 'single', event.button,
                event.x, event.y, event.xdata, event.ydata))
                res.append([event.xdata,event.ydata])
                n = n + 1
        else:
            print 'finished'            
    
    fig, ax = plt.subplots()
    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    imgplot = plt.imshow(f)
    plt.show(block=False) #https://stackoverflow.com/questions/17149646/matplotlib-force-plot-display-and-then-return-to-main-code
    return res
