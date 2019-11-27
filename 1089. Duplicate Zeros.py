#!/usr/bin/env python
# coding: utf-8

# Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.
# 
# Note that elements beyond the length of the original array are not written.
# 
# Do the above modifications to the input array in place, do not return anything from your function.
# 
# Example 1:
# 
# Input: [1,0,2,3,0,4,5,0]
# Output: null
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

# In[ ]:


class Solution(object):
    @staticmethod
    def duplicateZeros(arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        l = len(arr)
        i = 0
        while i<l:
            if arr[i] == 0:
                arr.insert(i,0)
                arr.pop(-1)
                i += 1
            i +=1
            
arr = [1,0,2,3,0,4,5,0]
Solution.duplicateZeros(arr)

