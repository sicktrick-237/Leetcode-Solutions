# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 05:40:41 2019

@author: sicktrick-237
"""
class Solution():
    @staticmethod
    def searchInsert(nums,target):
        sizeoflist = len(nums)
        flag = 1
        for i in range(0,sizeoflist):
            if nums[i] == target:
                return i
            elif target < nums[i]:
                return i
            else:
                flag = 0
        if flag == 0:
            return sizeoflist
            
        
nums = [1,2,5,6]
targ = 4
result = Solution.searchInsert(nums,targ)
print(result)