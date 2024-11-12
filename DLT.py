#Direct Linear Teansformation(DLT)

import Tkinter as tk
import tkMessageBox
from tkFileDialog import askopenfilename
from func.Image import open_image
from func.CSV import open_csv
from func.get_coor_pix import getCoor
from func.get_coor_pix_v2 import getCoorV2
from func.findparameters import findParameters
from func.findcoordinate import findCoordinate
from PIL import Image, ImageTk #http://effbot.org/tkinterbook/photoimage.htm

class DLT:
    'DLT is main part of my program'
    def __init__(self,root):
        print 'Doc String: '+self.__doc__

        self.imageR = []
        self.imageL = []
        self.GCP = []
        self.parameters = ''
        self.status = {
        'imageL':False,
        'imageR':False,
        'GCPFile':False,
        'GCPPicksL':False,
        'GCPPicksR':False,
        'DLTParameters':False,
        'pointPixel': False,
        }
        self.GCPpixelL = False
        self.GCPpixelR = False

        self.pointPixel = []
        self.pointPixelL = [False]
        self.pointPixelR = [False]

        self.frame = tk.Frame(root)
        self.frame.pack()
        self.frameButtom = tk.Frame(root)
        self.frameButtom.pack( side = tk.BOTTOM )
        self.frameTop = tk.Frame(root)
        self.frameTop.pack( side = tk.TOP )

        self.btn1 = tk.Button(self.frame,text="Pick Left Image",command= lambda: self.filePicker('im1'))
        self.btn2 = tk.Button(self.frame,text="Pick control point on Left Image", command=  lambda: self.pointPicker('im1'))
        self.btn3 = tk.Button(self.frame,text="Pick Right Image",command= lambda: self.filePicker('im2'))
        self.btn4 = tk.Button(self.frame,text="Pick control point on Right Image", command=  lambda: self.pointPicker('im2'))
        self.btn5 = tk.Button(self.frameButtom,text="Pick GCP Coordinates File(.csv)", command=  lambda: self.filePicker('GCP'))
        self.btn6 = tk.Button(self.frameButtom,text="Compute Parameter of DLT", command=  lambda: self.Computation(1))
        self.btn7 = tk.Button(self.frameButtom,text="pick point to compute coordinate", command=  lambda: self.Computation(2))
        self.btn8 = tk.Button(self.frameButtom,text="print coordinate", command=  lambda: self.Computation(3))


        self.canvasL = tk.Canvas(self.frameTop,width=250, height=255, bg='black')
        self.canvasR = tk.Canvas(self.frameTop,width=250, height=255, bg='black')
        self.canvasL.pack(expand=tk.YES, fill=tk.BOTH,side=tk.LEFT)
        self.canvasR.pack(expand=tk.YES, fill=tk.BOTH,side=tk.RIGHT)
        self.rightI = tk.PhotoImage()
        self.leftI = tk.PhotoImage()
        self.image_on_canvasR = self.canvasR.create_image(10, 10, image=self.rightI, anchor=tk.NW)
        self.image_on_canvasL = self.canvasL.create_image(10, 10, image=self.leftI, anchor=tk.NW)

        self.btn1.pack( side = tk.LEFT)
        self.btn2.pack( side = tk.LEFT)
        self.btn3.pack( side = tk.LEFT)
        self.btn4.pack( side = tk.LEFT)

        self.btn5.pack()
        self.btn6.pack()
        self.btn7.pack()
        self.btn8.pack( side = tk.BOTTOM)


    def pointPicker(self,condition):
        if condition == 'im1' and self.status['imageL']==True:
            self.GCPpixelL = getCoor(self.imageL,6)
            self.status['GCPPicksL'] = True
        elif condition == 'im2' and self.status['imageR']==True:
            self.GCPpixelR = getCoor(self.imageR,6)
            self.status['GCPPicksR'] = True
        elif condition == 'im1' and self.status['imageL']==False:
            tkMessageBox.showinfo('image left','First Input Left Images')
        else:
            tkMessageBox.showinfo('image right','First Input right Images')

    #to pick file and manage button commands
    def filePicker(self,condition):
        try:
             f = askopenfilename()
             if condition == 'im1':
                 self.imageL = open_image(f)
                 self.status['imageL'] = True
                 size = 230, 270 #https://stackoverflow.com/questions/273946/how-do-i-resize-an-image-using-pil-and-maintain-its-aspect-ratio
                 im = Image.open(f)
                 im.thumbnail(size, Image.ANTIALIAS)
                 self.leftI = ImageTk.PhotoImage(im)
                 self.canvasL.itemconfig(self.image_on_canvasL, image = self.leftI)
             elif condition == 'im2':
                 self.imageR = open_image(f)
                 self.status['imageR'] = True
                 size = 230, 270 #https://stackoverflow.com/questions/273946/how-do-i-resize-an-image-using-pil-and-maintain-its-aspect-ratio
                 im = Image.open(f)
                 im.thumbnail(size, Image.ANTIALIAS)
                 self.rightI = ImageTk.PhotoImage(im)
                 self.canvasR.itemconfig(self.image_on_canvasR, image = self.rightI)
             elif condition == 'GCP':
                 self.GCP = open_csv(f)
                 self.status['GCPFile'] = True
        except IOError as e:
            print e


    # choose point then compute
    def Computation(self,condition):
        if condition == 1:
            if self.status['GCPPicksL'] and self.status['GCPPicksR'] and self.status['GCPFile']:
                self.parameters = findParameters(self.GCP, self.GCPpixelL, self.GCPpixelR)
                self.status['DLTParameters'] = True
            else:
                tkMessageBox.showinfo('findParameters','First input GCP file \n or pick GCP on the left image \n or pick GCP on the right image ')
        elif condition == 2:
            if self.status['DLTParameters']:
                self.pointPixel = getCoorV2(self.imageR,self.imageL,2)
                self.status['pointPixel'] = True
            else:
                tkMessageBox.showinfo('findCoordinate',"First Compute DLT parameters")
        else:
            if self.status['pointPixel']:
                self.pointPixelR = self.pointPixel[0]
                self.pointPixelL = self.pointPixel[1]
                print str(findCoordinate(self.pointPixel,self.GCPpixelR,self.parameters,self.GCP)) + '\a'
            else:
                tkMessageBox.showinfo('findCoordinate',"which point do you wanna find?\nfirst pick point")
root = tk.Tk()
DLT(root)

root.resizable(width=False,height=False)
root.mainloop()
