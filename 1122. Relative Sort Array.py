#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    @staticmethod
    def relativeSortArray(arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        arr3 = []
        for each in arr2:
            cnt = arr1.count(each)
            i = 0
            while i<cnt:
                arr3.append(each)
                arr1.remove(each)
                i+=1
                
        arr1.sort()        
        return (arr3+arr1)
    
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [3]
Solution.relativeSortArray(arr1,arr2)

