#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    @staticmethod
    def containsDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return not len(set(nums)) == len(nums)
        

nums = [1,3,4,1,6]
l = len(nums)
Solution.containsDuplicate(nums)

