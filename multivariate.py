import numpy as np
from scipy.stats import multivariate_normal
import matplotlib.pyplot as pit
from skimage import io
from math import *
import numpy.matlib

image=io.imread("duck.jpg")

train2 = np.array([[180,150],[255,226,100]])
train3 = np.array([[0,109,154],[100,225,255]])


for i in image:
    tmp = np.cov(train2,rowvar=False)
    cov2 = np.diag(np.diag(tmp))
    tmp2 = np.cov(train3,rowvar=False)
    cov3 = np.diag(np.diag(tmp2))
    rP = multivariate_normal.pdf(image[i],mean=train2.mean(axis=0),cov=cov2)
    rN = multivariate_normal.pdf(image[i],mean=train3.mean(axis=0),cov=cov3)
    
    if rP.all()>=rN.all():
        image[i]=(255,0,0)
    else:
        image[i]=0
    
