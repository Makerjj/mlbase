# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 14:02:29 2018

@author: jm
"""

from numpy import *
import numpy as np

def loadDataSet(filename):
    fr = open(filename)
    X = []; Y = []
    for line in fr.readlines():
        curLine = line.split()
        fltLine = map(float, curLine)
        fltLine.insert(0,1.0)
        X.append(fltLine[:-1])
        Y.append(fltLine[-1:])
    #X = matrix(X)
    #X = X.c_(ones((len(X),1)),X)
    return matrix(X), matrix(Y)

def sigmoid(z):
    return 1 / (1 + exp(-z))

#def gradient(X, Y, W):
#    raw, col = X.shape
#    #W = zeros((col, 1))
#    sum = zeros((1,col))
#    for i in range(raw):
#        tmp = sigmoid(-Y[i,0] * W.T * X[i].T)
#        sum += tmp*(-Y[i,0]*X[i])
#    return sum / raw
    

def gradient2(X, Y, W):
     X = array(X);Y = array(Y); W = array(W)
     raw, col = shape(X)
     sum = (-Y*X).T.dot(sigmoid((-Y*(X.dot(W)))))
     return matrix(sum / raw)

def logistic_regression(X, Y, T, eta):
    raw, col = X.shape
    W = zeros((col,1))
    for t in range(T):
        grad = gradient2(X, Y, W)
        W = W - eta*grad
    return W

def calError(X, Y, W):
    errCount = 0.0
    n = len(X)
    for i in range(n):
        #tmp = sigmoid(W*X[i].T)
        #hx = sign(tmp.A[0][0])
        hx = sign(W.T*X[i].T)
        if hx <= 0: hx = -1
        if hx != Y[i,0]:
            errCount += 1
    return errCount / n



X, Y = loadDataSet("hw3_train.txt")
X2, Y2 = loadDataSet("hw3_test.txt")
W = logistic_regression(X, Y, 2000, 0.001)
W2 = logistic_regression(X, Y, 2000, 0.01)
Ein = calError(X,Y,W)
Eout = calError(X2, Y2, W)
Ein2 = calError(X,Y,W2)
Eout2 = calError(X2, Y2, W2)
print Ein, Eout
print Ein2, Eout2