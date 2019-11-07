# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 17:25:54 2019

@author: User
"""
import logRegression 
from numpy import *
import matplotlib.pyplot as plt
import time
 
def loadData():
    y=open("q1y.dat")
    train_x = []
    train_y = []
    fileIn = open('q1x.dat')
    for line in fileIn.readlines():
        lineArr = line.strip().split()
        #print(lineArr)
        train_x.append([float(lineArr[0]), float(lineArr[1])])
        #train_x.append(float(lineArr[0]))
 
    for line in y.readlines():
        lineArry = line.strip().split()
		#train_x.append([1.0, float(lineArr[0]), float(lineArr[1])])
        train_y.append(float(lineArry[0]))
    return mat(train_x),mat(train_y).transpose()

def loadtestData():
    y=open("q2y.dat")
    test_x = []
    #test_y = []
    fileIn = open('q2x.dat')
    for line in fileIn.readlines():
        for line in y.readlines():
            lineArr = line.strip().split()
            lineArry = line.strip().split()
        #print(lineArr)
            test_x.append([float(lineArr[0]),float(lineArry[0])])
        #train_x.append(float(lineArr[0]))
 
    #for line in y.readlines():
        #lineArry = line.strip().split()
		#train_x.append([1.0, float(lineArr[0]), float(lineArr[1])])
        #test_x.append(float(lineArry[0]))
    return mat(test_x)
 
 
## step 1: load data
print ("step 1: load data...")
train_x, train_y = loadData()
test_x ,test_y = train_x, train_y 
 
## step 2: training...
print ("step 2: training...")
opts = {'alpha': 0.001, 'maxIter': 20, 'optimizeType': 'gradDescent'}
#train_x, train_y = loadData()
#test_x = train_x; test_y = train_y
optimalWeights = logRegression.trainLogRegres(train_x, train_y, opts)
 
## step 3: testing
#print ("step 3: testing...")
accuracy = logRegression.testLogRegres(optimalWeights, test_x, test_y)
 
## step 4: show the result
#print ("step 4: show the result...")	
print ('The classify accuracy is: %.3f%%' % (accuracy * 100))
logRegression.showLogRegres(optimalWeights, train_x, train_y) 

weights=[[0.22562134],[1.20125983]]
t_x=loadtestData()
result=ones((100, 1))
for i in range(100):
    if sigmoid(t_x[i, :] * weights)<=0.5:
        result[i]=0
print(result)
