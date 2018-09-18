# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 21:12:41 2018

@author: jm
"""

from numpy import *
import numpy as np
import matplotlib.pyplot as plt

def loadDataSet(fileName):
    fr = open(fileName)
    X = []; Y = []
    for line in fr.readlines():
        curLine = line.split()
        fltLine = map(float, curLine)
        fltLine.insert(0,1.0)
        X.append(fltLine[:-1])
        Y.append(fltLine[-1:])
    return matrix(X), matrix(Y)
    
def calW(X, Y, lamb):
    row, col = shape(X)
    return (X.T*X +lamb*eye(col)).I*X.T*Y

def calError(X, Y, W):
    Yt = sign(X*W)
    Yt[Yt == 0] = -1
    return float(sum(Yt != Y)) / len(Y)

X, Y = loadDataSet('hw4_train.txt')
Xtest, Ytest = loadDataSet('hw4_test.txt')
#Ein = []; Eout = []
#L = list(np.arange(-10,3,1))
#for lamb in range(-10,3):
#    Wreg = calW(X, Y, lamb)
#    errin = calError(X, Y, Wreg)
#    errout = calError(Xtest, Ytest, Wreg)
#    Ein.append(errin)
#    Eout.append(errout)
#plt.plot(L, Ein)
#plt.plot(L,Eout)

L = list(np.arange(-10,3,1))
Etrain = []; Eval = [];Eout = []
Xtrain = X[:120]; Xval = X[120:]
Ytrain = Y[:120]; Yval = X[120:]
for lamb in range(-10,3):
    Wreg = calW(Xtrain, Ytrain, lamb)
    errTrain = calError(Xtrain, Ytrain, Wreg)
    errVal = calError(Xval, Yval, Wreg)
    errOut = calError(Xtest, Ytest, Wreg)
    Etrain.append(errTrain)
    Eval.append(errVal)
    Eout.append(errOut)
plt.plot(L, Etrain)
plt.plot(L, Eval)
plt.plot(L, Eout)