"""
Created on Mon Nov 16 00:43:07 2020
@author: ISH KAPOOR
"""
import cv2
import numpy as np

def cartoon_maker(img_name):

    img = cv2.imread(img_name)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    color = cv2.bilateralFilter(img, 9, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask = edges)

    return cartoon

for i in range(0, 133):
    frames = "Babbar_Frame/frame"+str(i)+".png"
    print("Reading Frame-"+str(i))
    cartoon_img = cartoon_maker(frames)
    name = "Cartoon_img_"+str(i)+".png"
    cv2.imwrite(name, cartoon_img)
    print("Creating Cartoon "+name+" "+str(i))

cv2.waitKey(0)
cv2.destroyAllWindows()