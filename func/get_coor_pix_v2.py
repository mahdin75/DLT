import cv2
import numpy as np
from tkFileDialog import askopenfilename
import matplotlib.pyplot as plt

def getCoorV2(imR,imL,m):

    fig = plt.figure()
    a=fig.add_subplot(1,2,1)
    imgplot = plt.imshow(imR)
    a=fig.add_subplot(1,2,2)
    imgplot = plt.imshow(imL)

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
            plt.close()
            print 'finished'
    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    fig.show()

     #https://stackoverflow.com/questions/17149646/matplotlib-force-plot-display-and-then-return-to-main-code
    return res
