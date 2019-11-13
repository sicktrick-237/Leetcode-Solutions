#!/usr/bin/env python
# coding: utf-8

# In[17]:


class Solution(object):
    @staticmethod
    def validMountainArray(mt):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(mt) == 0:
            return False
        mid = max(mt)
        if mid == mt[-1] or mid == mt[0]:
            return False
        low = mt[:mt.index(mid)]
        high = mt[mt.index(mid) + 1:]
        if len(low) != len(set(low)) or len(high) != len(set(high)) or mid in low or mid in high:
            return False
        i,j = 0,1
        while i < len(low)-1:
            if low[i] < low[j]:
                i+=1
                j+=1
            else:
                return False

        i,j = 0,1
        while i < len(high)-1:
            if high[i] > high[j]:
                i+=1
                j+=1
            else:
                return False
        return True
mt = [0,3,2,1]
Solution.validMountainArray(mt)

