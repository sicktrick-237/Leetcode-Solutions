#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    @staticmethod
    def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        temp = x
        dig = 0
        while x > 0:
            dig = dig*10 + x%10
            x = x//10
        if temp == dig:
            return True
        return False
    @staticmethod
    def isPalindromeWithStr(x):
        """
        :type x: int
        :rtype: bool
        """
        i = 0
        j = -1
        x = str(x)     
        while i < len(x)/2:
            if x[i] != x[j]:
                return False
            i += 1
            j -= 1
        return True
num = 71217    
Solution.isPalindrome(num)

