#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    @staticmethod
    def reverseWords(s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(((s.strip()).split())[::-1])
        
s = "a good   example"
Solution.reverseWords(s)

