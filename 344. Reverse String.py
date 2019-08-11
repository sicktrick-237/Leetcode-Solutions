# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 06:31:57 2019

@author: Omkar Kadam
"""


class Solution(object):
    @staticmethod
    def reverseString(s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i = 0
        j = -1
        while(i<int(len(s)/2)):
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            j -= 1
            i += 1
        
s = ["h","e","l","l","o","o"]
Solution.reverseString(s)
