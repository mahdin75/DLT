import cv2

def open_image(file):
    img = cv2.imread(file)
    return img
