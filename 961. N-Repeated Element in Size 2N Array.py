#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        i = 0
        A = sorted(A)
        j = 1
        while i<len(A):
            if A[i] == A[j]:
                return A[i]
            i+=1
            j+=1
        
sol = Solution()
A = [3,3,1,2]
sol.repeatedNTimes(A)

