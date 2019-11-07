# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 17:05:25 2019

@author: User
"""

#################################################
# logRegression: Logistic Regression
# Author : zouxy
# Date   : 2014-03-02
# HomePage : http://blog.csdn.net/zouxy09
# Email  : zouxy09@qq.com
#################################################
 
from numpy import *
import matplotlib.pyplot as plt
import time
 
 
# calculate the sigmoid function
def sigmoid(inX):
	return 1.0 / (1 + exp(-inX))
 
 
# train a logistic regression model using some optional optimize algorithm
# input: train_x is a mat datatype, each row stands for one sample
#		 train_y is mat datatype too, each row is the corresponding label
#		 opts is optimize option include step and maximum number of iterations
def trainLogRegres(train_x, train_y, opts):
	# calculate training time
	startTime = time.time()
 
	numSamples, numFeatures = shape(train_x)
	alpha = opts['alpha']; maxIter = opts['maxIter']
	weights = ones((numFeatures, 1))
    
	for k in range(maxIter):
		if opts['optimizeType'] == 'gradDescent': # gradient descent algorilthm
			output = sigmoid(train_x * weights)
            
			error = train_y - output
			weights = weights + alpha * train_x.transpose() * error
		elif opts['optimizeType'] == 'stocGradDescent': # stochastic gradient descent
			for i in range(numSamples):
				output = sigmoid(train_x[i, :] * weights)
				error = train_y[i, 0] - output
				weights = weights + alpha * train_x[i, :].transpose() * error
		elif opts['optimizeType'] == 'smoothStocGradDescent': # smooth stochastic gradient descent
			# randomly select samples to optimize for reducing cycle fluctuations 
			dataIndex = range(numSamples)
			for i in range(numSamples):
				alpha = 4.0 / (1.0 + k + i) + 0.01
				randIndex = int(random.uniform(0, len(dataIndex)))
				output = sigmoid(train_x[randIndex, :] * weights)
				error = train_y[randIndex, 0] - output
				weights = weights + alpha * train_x[randIndex, :].transpose() * error
				del(dataIndex[randIndex]) # during one interation, delete the optimized sample
		else:
			raise NameError('Not support optimize method type!')
	print(output)
	result=ones((numSamples, 1))
	for i in range(numSamples):
		if output[i]<=0.5:
			result[i]=0
		
   
	print ('Congratulations, training complete! Took %fs!' % (time.time() - startTime))
	print("the Prediction results is...{}".format(result))
	return weights
	return output
 
 
# test your trained Logistic Regression model given test set
def testLogRegres(weights, test_x, test_y):
	numSamples, numFeatures = shape(test_x)
	matchCount = 0
	for i in range(numSamples):
		predict = sigmoid(test_x[i, :] * weights)> 0.5
		#predict = sigmoid(test_x[i, :] * weights)[0, 0] > 0.5
		if predict == bool(test_y[i, 0]):
			matchCount += 1
	accuracy = float(matchCount) / numSamples
	return accuracy
 
 
# show your trained logistic regression model only available with 2-D data
def showLogRegres(weights, train_x, train_y):
	# notice: train_x and train_y is mat datatype
	numSamples, numFeatures = shape(train_x)
	Z=ones((numSamples, 1))
	if numFeatures != 2:
		print ("Sorry! I can not draw because the dimension of your data is not 2!")
		return 1
 
	# draw all samples
	for i in range(numSamples):
		if int(train_y[i, 0]) == 0:
			plt.plot(train_x[i, 0], train_x[i, 1], 'or')
		elif int(train_y[i, 0]) == 1:
			plt.plot(train_x[i, 0], train_x[i, 1], 'ob')
	#for i in range(numSamples):
		#if sigmoid(train_x[i, :] * weights)>0.5:
			#Z[i]=1
		#else:
			#Z[i]=0
	#plt.contourf(train_x,Z, cmap=plt.cm.Spectral)
    
   # x_min, x_max = train_x[:, 0].min() - .5, train_x[:, 0].max() + .5
    #y_min, y_max = train_x[:, 1].min() - .5, train_x[:, 1].max() + .5
    #h = 0.01
    #xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
   # print(xx)
   # print(yy)
 
# 用预测函数预测一下
    #Z = pred_func(np.c_[xx.ravel(), yy.ravel()])
    #Z = Z.reshape(xx.shape)
    
 
# 然后画出图
    #plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral)
	min_x = min(train_x[:, 0])[0, 0]
	max_x = max(train_x[:, 0])[0, 0]
	weights = weights.getA()
	#print(weights)# convert mat to arrayprint(weights)
	y_min_x = float(-weights[0] * min_x) / weights[1]
	y_max_x = float(-weights[0] * max_x) / weights[1]
	plt.plot([min_x, max_x], [y_min_x, y_max_x], '-g')
	plt.xlabel('X1'); plt.ylabel('X2')
	plt.show()