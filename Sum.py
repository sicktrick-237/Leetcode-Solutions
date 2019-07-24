# -*- coding: utf-8 -*-
"""
Problem Statement: 
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

EXAMPLE: 
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

URL: https://leetcode.com/problems/two-sum/
"""
def solution():
    a = [5,8,3,7,30]
    defvalue = 33 
    length = len(a)
    for i in range(0,length):
        for j in range(i,length):
            # To Reduce the Number of Iterations over unmatched values
            temp = a[i] + a[j]
            if temp == defvalue:
                return(i,j)
            
            
       
boo = solution()
if boo != '':
    print("Success")
    print(boo)