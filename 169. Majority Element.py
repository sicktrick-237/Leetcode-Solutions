#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    @staticmethod
    def majorityElement(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        vals = set(nums)
        return list(filter(lambda x:nums.count(x)>len(nums)/2,vals))[0]
        
            
nums = [2,2,1,1,1,2,2]
Solution.majorityElement(nums)

