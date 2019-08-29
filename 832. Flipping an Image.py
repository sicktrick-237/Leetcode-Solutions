#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    @staticmethod
    def flipAndInvertImage(arr):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        i = 0
        while i < len(arr):
            k = -1
            j = 0
            while j < int(len(arr[i])/2):
                temp = arr[i][j]
                arr[i][j] = arr[i][k]
                arr[i][k] = temp
                k -= 1
                j += 1
            i +=1
        i = 0    
        while i < len(arr):
            j = 0
            while j < len(arr[i]):
                arr[i][j] = int(not arr[i][j])
                j +=1
            i +=1
        return arr
    
    
arr = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Solution.flipAndInvertImage(arr)


# In[ ]:




