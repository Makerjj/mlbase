# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 10:01:14 2018

@author: jm
"""

import numpy as np
from numpy import *
import random


def genData():
    x = np.random.uniform(-1, 1, 20)
    y = sign(x)
    y[y == 0] = -1
    prop = np.random.uniform(0 ,1, 20)
    y[prop >= 0.8] *= -1
    return x, y

# 单维度决策树桩算法
def decision_stump(X, Y):
    theta = np.sort(X)
    num = len(theta)
    Xtemp = np.tile(X, (num, 1))#n行1列的X
    ttemp = np.tile(np.reshape(theta, (num, 1)), (1, num))
    #reshape：将theta变为num维,每维一个元素，tile：在行上重复一次，列上重复num次
    ypred = np.sign(Xtemp - ttemp)
    ypred[ypred == 0] = -1
    err = np.sum(ypred != Y, axis=1)
    if np.min(err) <= num-np.max(err):
        return 1, theta[np.argmin(err)], float(np.min(err))/num
    else:
        return -1, theta[np.argmax(err)], float((num-np.max(err)))/num

def multi_decision_stump(X, Y):
    raw, col = shape(X)
    err = zeros((col,)); s = zeros((col,)); theta = zeros((col,))
    for i in range(col):
        s[i], theta[i], err[i] = decision_stump(X[:, i], Y[:,0])
    pos = np.argmin(err)
    return pos, s[pos], theta[pos], err[pos]

def loadDataSet(filename):
    fr = open(filename)
    X = []; Y = []
    for line in fr.readlines():
        curLine = line.strip().split()
        fltLine = map(float, curLine)
        X.append(fltLine[:-1])
        Y.append(fltLine[-1:])
    return array(X), array(Y)
   

totalin = 0.0; totalout = 0.0
for i in range(5000):
    X, Y = genData()
    theta = np.sort(X)
    s, theta, errin = decision_stump(X, Y)
    errout = 0.5+0.3*s*(math.fabs(theta)-1)
    totalin += errin
    totalout += errout
print('训练集平均误差: ', totalin/5000)
print('测试集平均误差: ', totalout/5000)
    
X, Y = loadDataSet('hw2_train.txt')
Xtest, Ytest = loadDataSet('hw2_test.txt')
pos, s, theta, Ein = multi_decision_stump(X, Y)
print('训练集误差: ', Ein)
ypred = s*np.sign(Xtest[:, pos]-theta)
ypred[ypred == 0] = -1
row, col = Ytest.shape
Eout = float(np.sum(ypred != Ytest.reshape(row,)))/len(ypred)
print('测试集误差: ', Eout)