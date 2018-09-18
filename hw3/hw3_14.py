# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 20:10:14 2018

@author: jm
"""

import matplotlib.pyplot as plt
from numpy import *
import numpy as np

#def sign(x):
#    if x <= 0:
#        return -1
#    else:
#        return 0

def genData(num):
    x1 = np.random.uniform(-1,1,num)
    x2 = np.random.uniform(-1,1,num)
    x = np.c_[x1,x2]
    x = np.c_[np.ones((num,1)),x]
    y = sign(np.power(x1,2)+np.power(x2,2)-0.6)
    y[y == 0] = -1
    pos = np.random.permutation(num)
    y[pos[0: int(round(0.1*num))]] *= -1
    y = y.reshape((num,1))
    #return np.matrix(x), np.matrix(y)
    return x,y

def linear_regression():
    x, y = genData(1000)
    y = matrix(y)
    z = matrix(transform(x))
    wlin = np.linalg.inv(z.T*z)*z.T*y
    return wlin, z, y
        
def transform(x):
    raw, col = x.shape
    xTrans = (np.zeros((raw, 6)))
    xTrans[:,0] = 1
    xTrans[:,1] = x[:,1]
    xTrans[:,2] = x[:,2]
    xTrans[:,3] = x[:,1]*x[:,2]
    xTrans[:,4] = x[:,1]**2
    xTrans[:,5] = x[:,2]**2
    return xTrans

def error_rate(): 
    totalerr = 0.0
    wtotal = matrix(zeros((6,1)))
    errhist = []
    for i in range(1000):
        wlin,x,y = linear_regression() 
        wtotal += wlin
        #print wlin
        ytest = np.sign(x.dot(wlin))
        err = float(np.sum(ytest!=y))/1000
        totalerr += err
        errhist.append(err)
    print totalerr/1000
    print wtotal/1000
    plt.hist(errhist)
    
error_rate()
#for i in range(1000):
#    print error_rate()
x, y = genData(1000)
