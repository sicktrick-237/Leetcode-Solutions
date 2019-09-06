#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
class Solution(object):
    @staticmethod
    def isPalindrome(string):
        """
        :type s: str
        :rtype: bool
        """
        original = (re.sub(r'\W+','',string)).lower()
        i = 0
        j = -1
        while i <len(original)/2:
            if original[i] == original[j]:
                j -=1
                i +=1
            else:
                return False
        return True
string = "A man, a plan, a canal: Panama"
Solution.isPalindrome(string)

