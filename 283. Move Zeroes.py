#!/usr/bin/env python
# coding: utf-8

# In[5]:


class Solution(object):
    @staticmethod
    def moveZeroes(nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        cnt = nums.count(0)
        while 0 in nums:
            nums.remove(0)
        while cnt > 0:
            nums.append(0)
            cnt -=1
nums = [0,1,0,3,12]
Solution.moveZeroes(nums)

