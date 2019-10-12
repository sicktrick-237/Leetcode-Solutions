#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from itertools import permutations
class Solution(object):
    @staticmethod
    def numTilePossibilities(tiles):
        """
        :type tiles: str
        :rtype: int
        """
        cnt = 0
        for i in range(1,len(tiles)+1):
            lst = permutations(list(tiles),i)
            cnt += len(set(lst))
        return cnt
Solution.numTilePossibilities('aab')

