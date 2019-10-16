#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    @staticmethod
    def sortArrayByParity(nums):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i = 0
        part = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                part.insert(0,nums[i])
                continue
            part.append(nums[i])
        return part
nums = [1,0]  
Solution.sortArrayByParity(nums)

