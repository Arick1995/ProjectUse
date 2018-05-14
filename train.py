import numpy as np
from scipy.stats import multivariate_normal
import matplotlib.pyplot as pit
from skimage import io
from math import *
import numpy.matlib


train2 = np.array([[10,30],[20,40],[30,50]])
xy1 = np.array([20,45])
xy2 = np.array([45,20])

tmp = np.cov(train2,rowvar=False)
cov2 = np.diag(np.diag(tmp))
r1 = multivariate_normal.pdf(xy1,mean=train2.mean(axis=0),cov=cov2)
r2 = multivariate_normal.pdf(xy2,mean=train2.mean(axis=0),cov=cov2)
print(r1,r2)
