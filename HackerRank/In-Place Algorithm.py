# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 05:03:51 2019

@author: Omkar Kadam
"""

'''
In-Place Algorithm :
An in-place algorithm is an algorithm that does not need an extra space and produces an output 
in the same memory that contains the data by transforming the input ‘in-place’. 
However, a small constant extra space used for variables is allowed.

'''
i = 0
j = -1
def reverselist(arr):
    temp = 0
    global i
    global j
    if i < len(arr)/2:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i +=1
        j -=1
        reverselist(arr)
    
       
if __name__ == "__main__": 
    arr = [1, 2, 3, 4, 5, 6, 7] 
    n = len(arr) 
    reverselist(arr)