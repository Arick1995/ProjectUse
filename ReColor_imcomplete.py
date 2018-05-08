import matplotlib.pyplot as pit
import os
import numpy as np
from skimage import io
from math import *
import numpy.matlib

def mask_inrange(image,lower,upper):
    for c in range(3):
        tmp_m = (image[: , : , c ]>=lower[c])& (image[:,:,c]<=upper[c])
        if c == 0 :
            m = tmp_m
        else:
            m = tmp_m & m
    return np.logical_not(m)

color = ("red","blue","green")
Bins = 5
image = io.imread("C:/Users/tkustaff/Desktop/ssssss/duck.jpg")
for i,col in enumerate(color):
    histr,num = np.histogram(image[:,:,i],Bins)
    pit.bar(num[:-1],histr,width=10,color=col)
    
RGBrange = [
        ([180,150,0],[255,226,100]),
        ([113,219,238],[26,188,230])
        ]
#
ReColor[0]=[
        ([255,0,0])
        ]
ReColor[1]=[
        ([0,0,255])
        ]
## 
index = 0

img_shape = image.shape
outputs = np.empty(shape=(len(RGBrange),img_shape[0],img_shape[1],img_shape[2]))
output = image.copy()

for(lower,upper) in  RGBrange:
    mask = mask_inrange(image,lower,upper)
    output[mask] = ReColor[index]
    index = index+1
    
io.imsave("ReColor_duck.jpg",output)
            
