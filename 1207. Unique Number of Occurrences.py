#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    @staticmethod
    def uniqueOccurrences(arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        uniq = set(arr)
        lst = []
        for each in uniq:
            if arr.count(each) in lst:
                return False
            lst.append(arr.count(each))
        return True
        
nums = [-3,0,1,-3,1,1,1,-3,10,0]
Solution.uniqueOccurrences(nums)

