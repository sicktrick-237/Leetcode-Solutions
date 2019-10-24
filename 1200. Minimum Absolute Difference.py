#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    @staticmethod
    def minimumAbsDifference(arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr = sorted(arr)
        low_diff = arr[-1]
        i = 0
        j = 1
        while j<len(arr):
            cnt = abs(arr[i]-arr[j])
            if cnt < low_diff:
                low_diff = cnt
            i += 1
            j += 1

        i = 0
        j = 1
        lsts = []
        while j<len(arr):
            val = abs(arr[i]-arr[j])
            if val == low_diff:
                lsts.append([arr[i],arr[j]])     
            i+=1
            j+=1

        return lsts
    
    
arr = [3,8,-10,23,19,-4,-14,27]
Solution.minimumAbsDifference(arr)

