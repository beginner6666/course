# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 08:33:25 2019

@author: User
"""
#归并排序
def merge(a, b):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1

    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)

    return c

def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    middle = int(len(lists)/2)
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    return merge(left, right)

#二分法查找
def find(a,u):
    left=0
    right = len(a)
    while left<=right:
        mid=int((left+right)/2)
        if u==a[mid]:
            return a[mid]
        if u>a[mid]:
            left=mid+1
        else:
            right=mid-1

#求两个集合的交
def intersection(a,b):
    c1=[]
    a=merge_sort(a)
    for i in range(len(b)):
        if find(a,b[i])==b[i]:
            c1.append(b[i])
    return c1
        
    


a = [4, 7, 8, 3, 5, 9,12,6]
b=[5,1]
print (intersection(a,b))

