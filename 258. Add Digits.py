#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from functools import reduce

class Solution(object):
    @staticmethod
    def addDigits(num):
        """
        :type num: int
        :rtype: int
        """
        cnt = reduce(lambda x,y:int(x)+int(y),list(str(num)))
        if len(str(cnt)) > 1:
            return Solution.addDigits(cnt)
        return cnt
num = 38
Solution.addDigits(num)

