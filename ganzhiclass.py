# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 13:37:43 2019

@author: Administrator
"""
import numpy as np
b=np.array([[1,1,0,1],
   [1,0,1,1],
   [1,0,0,1],
   [0,0,0,1],
   [0,0,1,-1],
   [0,1,1,-1],
   [0,1,0,-1],
   [1,1,1,-1]])
w=np.array([0,0,0,0])

def ganzhiclass(b,c,k,w):
    while k<8:
        for i in range(8):
            t=b[i].reshape(1,4)
            if np.dot(t,w)>0:
                #w=w
                i=i+1
                k=k+1
                print(w)
            else:
                w=w+c*b[i]
                k=0
                i=i+1
            
    return w

print(ganzhiclass(b,1,0,w))