#!/usr/bin/env python
# coding: utf-8

# Given a matrix A, return the transpose of A.
# 
# The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.

# In[ ]:


class Solution(object):
    @staticmethod
    def transpose(M):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(M)
        n = len(M[0])
        M1 = []
        
        for j in range(n):
            Mtemp = []
            for i in range(m):
                Mtemp.append(M[i][j])
            M1.append(Mtemp)
            
        return M1
    
M = [[1,2,3],[4,5,6],[7,8,9]]
Solution.transpose(M)

