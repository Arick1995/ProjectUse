````java```
 #-*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from skimage import io,util
import numpy as np

logo = io.imread('C:/Users/tkustaff/Desktop/chrome-os-logo.jpg')

logo_grey = io.imread('C:/Users/tkustaff/Desktop/chrome-os-logo.jpg',as_grey=True)
logo_grey = util.img_as_ubyte(logo_grey)

size = logo.shape
size_grey = logo_grey.shape
print(logo.shape)
print(size_grey)

height,width,depth = logo.shape

height_grey = size_grey[0]
width_grey = size_grey[1]

io.imsave("C:/Users/tkustaff/Desktop/logo.jpg",logo_grey)
