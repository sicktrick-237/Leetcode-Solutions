# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 07:29:24 2019

@author: Omkar Kadam
"""

class Solution(object):
    @staticmethod
    def plusOne(digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        string = ''
        for each in digits:
            string += str(each)
        digits = [int(each) for each in str(int(string)+1)]
        return digits 
    
digits = [4,3,2,9]
Solution.plusOne(digits)