#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    @staticmethod
    def reverseOnlyLetters(string):
        """
        :type S: str
        :rtype: str
        """
        alpha = list('abcdefghijklmnopqrstuvwxyz')
        newstr = ''
        for each in string:
            if each.lower() in alpha:
                newstr += each

        newstr = list(newstr[::-1])
        cnt = 0
        rtstring = ''
        for idx,val in enumerate(string):
            if val.lower() not in alpha:
                newstr.insert(idx,string[idx])
        return "".join(newstr)        
S = "Test1ng-Leet=code-Q!"
Solution.reverseOnlyLetters(S)

