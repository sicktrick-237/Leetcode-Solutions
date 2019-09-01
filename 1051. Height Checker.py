#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    @staticmethod
    def heightChecker(nums):
        """
        :type heights: List[int]
        :rtype: int
        """
        i = 0
        og_nums = nums[:]
        nums.sort()
        for idx,val in enumerate(nums):
            if val != og_nums[idx]:
                i += 1
        return i
        

nums = [1,1,4,2,1,3]
Solution.heightChecker(nums)

