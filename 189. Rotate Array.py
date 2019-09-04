#!/usr/bin/env python
# coding: utf-8

# In[12]:


class Solution(object):
    @staticmethod
    def rotate(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        while k!=0:
            temp = nums[-1]
            nums.insert(0,temp)
            nums.pop(-1)
            k -=1
            
nums = [1,2,3,4,5,6,7]
k = 2
Solution.rotate(nums,k)

