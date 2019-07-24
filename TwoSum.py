# -*- coding: utf-8 -*-
"""
Problem Statement: 
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

EXAMPLE: 
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

URL: https://leetcode.com/problems/two-sum/
"""
import time
class Solution(object):
    @staticmethod
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        for i in range(0,length):
            for j in range(i,length):
                # To Reduce the Number of Iterations over unmatched values
                temp = nums[i] + nums[j]
                if temp == target:
                    if i != j:
                        return(i,j)

start_time = time.time()
arrayofnum = [5,8,3,7,30]
finalval = 37      
boo = Solution.twoSum(arrayofnum,finalval)
if boo != '':
    print("Success")
    print(boo)
    print("--- %s seconds ---" % (time.time() - start_time))