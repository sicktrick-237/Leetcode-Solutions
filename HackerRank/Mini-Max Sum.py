# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 03:32:48 2019

@author: omkar.kadam
"""

def minmax(arr):    
    minnum = 0
    for i in range(0,len(arr)-1):
        minnum += arr[i]
    maxnum = 0
    for j in range(1,len(arr)):
        maxnum += arr[j]
    print(minnum,maxnum)

def maxmin(arr):
    minnum = sum(arr) - (sum(arr)-min(arr))
    print(minnum)


arr = [7,69,2,221,8974]
arr.sort()
minmax(arr)
maxmin(arr)

    