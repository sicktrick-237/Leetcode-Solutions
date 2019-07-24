# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 07:35:23 2019

@author: Omkar Kadam
"""
'''
Problem Statement :

Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

Solution : 

Beats 99.73% of the online submissions 

'''

class Solution(object):
    @staticmethod
    def removeElement(nums,val):
            if val in nums:
                nums.remove(val) 
                Solution.removeElement(nums,val)
            if nums:
                return len(nums)
            
            
            



nums = [1,5,2,6,2,8]
nums.sort()
val = 2
result = Solution.removeElement(nums,val)
print(result)