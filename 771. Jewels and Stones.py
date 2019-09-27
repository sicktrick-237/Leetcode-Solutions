#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    @staticmethod
    def numJewelsInStones(J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum(map(lambda x:S.count(x),J))
    
    def numJewels(J,S):
        cnt = 0
        for each in J:
            if each in S:
                cnt += S.count(each) 
        return cnt

J = "aA"
S = "aAAbbbb"
Solution.numJewelsInStones(J,S)

