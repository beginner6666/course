# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 11:36:01 2019

@author: User
"""
#全篇m==1,p表示数组中的元素个数

#插入排序算法
def insort(array,m,p):
    #range并不能到达p,只能到p-1
    if p==m:
       return  array
    for i in range(m,p):
        temp = array[i]
        index = i
        while index>0 and array[index-1]>temp:
            array[index] = array[index-1]
            index -= 1
        array[index] = temp
    return array
        
#划分        
def partition(a,m,p) :
    v=a[m-1]
    low1 = [j for j in a[m-1:p] if j < v]
    high1 = [s for s in a[m-1:p] if s > v]
    a=low1+[v]+high1
    #print(a)
    return len(low1)
   # return a
 
#m=1  ,p代表数组元素个数 
def select(a,m,p,k):
    r=5
    if p-m+1<=r:
        insort(a,m,p)
        return m+k-1
    else:
        n=p-m+1
        for i in range(int(n/r)):
            insort(a,m+(i)*r,m+(i+1)*r-1)
            a[m+i-1],a[m+(i)*r+int(r/2)-1]=a[m+(i)*r+int(r/2)-1],a[m+i-1]
        
        j=select(a,m,m+int(n/r)-1,int(n/r/2))
        a[m-1],a[j]=a[j],a[m-1]
        #print(a)
        
        
        #j=p+1
        #基准前面的个数
    leftnum=partition(a,m,p)
   # print(leftnum)
    #print (a)
    if leftnum==k:
        return leftnum
    if leftnum>k:
        return select(a,m,leftnum-1,k)
    else:
        return select(a,leftnum+1,p,k-leftnum)
            #k=k-(j-m+1)
            #m=j+1
    #a2=a[a1:]


s1=(a[4:])
s2=a[:4]    
if __name__ == '__main__':
    a=[8,4,5,6,7,9,2,11]
    print(select(a,1,8,4))
   # print(a[leftnum])
    #s=a1-1
    #s1=a[:s]
    #s2=a[a1:]
    #print(s1)