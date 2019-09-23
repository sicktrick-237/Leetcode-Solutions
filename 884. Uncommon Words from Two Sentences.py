#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    @staticmethod
    def uncommonFromSentences(A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        lststring = (A+" "+B).split(" ")
        return list(filter(lambda x:lststring.count(x) == 1,lststring))
            
A = 'apple apple'
B = 'sour'
Solution.uncommonFromSentences(A,B)

