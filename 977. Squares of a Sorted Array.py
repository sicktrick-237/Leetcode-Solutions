#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    @staticmethod
    def sortedSquares(A):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = 0
        nums = []
        while i<len(A):
            A[i] *=A[i]
            i+=1
        
        return sorted(A)
                
A = [-7,-3,2,3,11]
Solution.sortedSquares(A)

