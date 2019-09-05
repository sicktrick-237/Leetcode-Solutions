#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    @staticmethod
    def singleNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = 0
        for each in nums:
            temp ^= each
        return temp
    
    

nums = [1,2,2,1,3,4,5,4,5]
Solution.singleNumber(nums)

