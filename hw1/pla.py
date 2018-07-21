# -*- coding: utf-8 -*-
"""
Created on Sun Jul 08 09:23:15 2018

@author: jm
"""
from numpy import *

def loadDataSet(fileName):
    fr = open(fileName)
    datMat0 = [];datMat1 = []
    for line in fr.readlines():
        curLine = line.strip().split()
        fltLine = map(float, curLine)
        fltLine.insert(-1, 1.0)
        datMat0.append(fltLine[:-1])
        datMat1.append(fltLine[-1])
    return datMat0, datMat1

def sign(x):
    if x <= 0:
        return -1
    else:
        return 1
    
def pla(datMat0, datMat1):
    datMat0 = matrix(datMat0)
    #datMat1 = matrix(datMat1)
    w0 = matrix([0.0, 0.0, 0.0, 0.0, 0.0])
    isFinished = 0
    step = 0
    correctCount = 0
    while(isFinished == 0):  
        correctCount = 0
        for i in range(len(datMat0)):
            if sign((w0*datMat0[i].T.tolist())[0][0]) != datMat1[i]:
                w0 += int(datMat1[i]) * datMat0[i]
                step += 1
                break
            else: 
                correctCount += 1
                if correctCount == len(datMat1): 
                    isFinished = 1
                    break
    print "total step: ", step
    return w0
            
    
    

datMat0, datMat1 = loadDataSet('hw1_15_train.txt')
#datMat0, datMat1 = loadDataSet('hw1Temp.txt')
w = pla(datMat0, datMat1)
