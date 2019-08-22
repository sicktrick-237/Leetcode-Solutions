# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 07:27:52 2019

@author: Omkar Kadam
434. Number of Segments in a String
"""

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst = (s.strip()).split(" ")
        cnt = 0
        for each in lst:
            if each:
                cnt += 1
        return cnt
        
string = "    "
sol = Solution()
sol.countSegments(string)