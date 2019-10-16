#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    @staticmethod
    def addStrings(num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        nums = {48: 0, 49: 1, 50: 2, 51: 3, 52: 4, 53: 5, 54: 6, 55: 7, 56: 8, 57: 9}
        res1 = sum(nums[ord(e)]*10**i for i, e in enumerate(list(num1)[::-1]))
        res2 = sum(nums[ord(e)]*10**i for i, e in enumerate(list(num2)[::-1]))
        return str(res1+res2)
    
    
num1 = '123'
num2 = '456'
Solution.addStrings(num1,num2)

