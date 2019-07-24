# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 07:35:23 2019

@author: Omkar Kadam
"""
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