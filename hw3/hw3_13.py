# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 14:31:53 2018

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
    return matrix(x), matrix(y)

def linear_regression():
    x, y = genData(1000)
    wlin = np.linalg.inv(x.T*x)*x.T*y
    return wlin, x, y
        
def error_rate(): 
    totalerr = 0.0
    errhist = []
    for i in range(1000):
        wlin,x,y = linear_regression()      
        ytest = np.sign(x.dot(wlin))
        err = float(np.sum(ytest!=y))/1000
        totalerr += err
        errhist.append(err)
    print totalerr/1000
    plt.hist(errhist)
    
error_rate()
#for i in range(1000):
#    print error_rate()
#x, y = genData(1000)