# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 23:27:55 2019

@author: Administrator
"""
import math

#初始变量（使用统计判别作业习题数据）
w1=[[0,0],[2,0],[2,2],[0,2]]
w2=[[4,4],[6,4],[6,6],[4,6]]
p1=0.5
p2=0.5
#均值
m1=np.mean(w1,0)
m2=np.mean(w2,0)
#协方差
c1=np.cov(w1,rowvar=0)
c2=np.cov(w2,rowvar=0)

x=input("please input x:")
y=input("please input y:")
p=[int(x),int(y)]
d1=math.log(p1)-0.5*math.log(np.linalg.det(c1))-0.5*(p-m1)*np.mat(c1).I*np.reshape((p-m1),(2,1))
d2=math.log(p2)-0.5*math.log(np.linalg.det(c2))-0.5*(p-m2)*np.mat(c2).I*np.reshape((p-m2),(2,1))
if d1>d2:
    print("It belongs to w1")   
else: 
    print("It belongs to w2")    
    
