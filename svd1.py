# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 19:11:13 2019

@author: Administrator
"""  
import matplotlib.pyplot as plt
from scipy.sparse.linalg import svds, eigs
from scipy.sparse import csc_matrix
data_path = 'out.as-caida20071105'
rows = []
cols = []
values = []
file= open(data_path,'r')
for line in file:
    row,col = list(map(int, line.strip().split()))
    rows.append(row)
    cols.append(col)
    values.append(1)
    rows.append(col)
    cols.append(row)
    values.append(1)
sparse_matrix = csc_matrix((values, (rows, cols)), dtype=float)
#a=np.array(sparse_matrix)
#sparse_matrix=sparse_matrix+a
U1,sigma1,VT1=svds(sparse_matrix,10)


for i in range(0,9,2):
    
    u0=U1[:,i]
    u1=U1[:,i+1]
    plt.scatter(u0,u1,s=0.1,c='#000000')
    #样式设置
    plt.xlabel('u{}'.format(i+1))
    plt.ylabel('u{}'.format(i+1+1))
    plt.xlim(xmax=0.05,xmin=-0.05)
    plt.ylim(ymax=0.1,ymin=-0.1)
    plt.axvline(x=0, color='#000000', linestyle='--')
    plt.axhline(y=0, color='#000000', linestyle='--')
    plt.xticks([])
    plt.yticks([])
    #保存
    plt.savefig('svd1u{}.png'.format(i), dpi=300)
    plt.show()
    
#plot v scatter 
for j in range(0,9,2):
    
    v0=VT1[j,:]
    v1=VT1[j+1,:]
    plt.scatter(v0,v1,s=0.1,c='#000000')
    #样式设置
    plt.xlabel('v{}'.format(j+1))
    plt.ylabel('v{}'.format(j+1+1))
    plt.xlim(xmax=0.05,xmin=-0.05)
    plt.ylim(ymax=0.1,ymin=-0.1)
    plt.axvline(x=0,color='#000000', linestyle='--')
    plt.axhline(y=0,color='#000000', linestyle='--')
    plt.xticks([])
    plt.yticks([])
    #保存
    plt.savefig('svd1v{}.png'.format(j), dpi=300)
    plt.show()
    