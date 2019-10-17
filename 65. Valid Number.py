#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    @staticmethod
    def isNumber(s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            float(s)
            ans = True
        except:
            return False
        
        return ans
    
    
s = " 95a54e53"
Solution.isNumber(s)

