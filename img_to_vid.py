"""
Created on Wed Oct 21 12:03:38 2020
@author: ISH KAPOOR
"""
import cv2
import numpy as np
import glob
img_array = []
for filename in glob.glob('C:/Users/ISH KAPOOR\Desktop/Cartoon Git Project/Cartoon_Babbar_Frame/*.png'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)

out = cv2.VideoWriter('Babbar_Cartoon.mp4', cv2.VideoWriter_fourcc(*'DIVX'), int(60), size)

for i in range(len(img_array)):
    out.write(img_array[i])
    print(i)

out.release()