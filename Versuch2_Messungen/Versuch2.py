# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 14:17:22 2024

@author: al871sch
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt

from skimage.color import rgb2gray

cap = cv2.VideoCapture(0)
cap.set(3, 960)
cap.set(4, 544)


print("frame width: " + str(cap.get(3)))
print("frame height: " + str(cap.get(4)))
print("--------------------------------")
print("brightness: " + str(cap.get(10)))
print("contrast: " + str(cap.get(11)))
print("saturation: " + str(cap.get(12)))
print("--------------------------------")
print("gain: " + str(cap.get(14)))
print("exposure: " + str(cap.get(15)))
print("--------------------------------")
print("white balance: " + str(cap.get(17)))


#while(True):
#for i in range(1,11):
    #ret, frame = cap.read()
    #grayscale = rgb2gray(frame)
    #fig, ax = plt.subplots(figsize=(8, 4))
    #ax.imshow(grayscale, cmap=plt.cm.gray)
    #ax.set_title("Grayscale")
    #plt.show()
    #cv2.imwrite("versuch_2_dunkelbild" + str(i) + ".png", frame)
    
ret, frame = cap.read()
grayscale = rgb2gray(frame)
fig, ax = plt.subplots(figsize=(8, 4))
ax.imshow(grayscale, cmap=plt.cm.gray)
ax.set_title("Grayscale")
plt.show()
cv2.imwrite("versuch_2_graukeil_exp_-5.5.png", frame)

cap.release()
cv2.destroyAllWindows()



