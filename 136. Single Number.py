# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 00:01:46 2019

@author: omkar.kadam
"""
def findSingleElement(nums):
    i = 0
    if len(nums) == 1:
        return nums[0]
    nums.sort()
    while(i<len(nums)):
        print(nums)
        try:
            if nums[i] in nums[i+1:]:
                print("in if")
                i += 1
                continue
            elif nums[i-1] == nums[i]:
                print("in elif")
                i += 1
                continue
            else:
                print("in else")
                return nums[i]
        except:
            print("in except")
            return nums[-1]


def uniqueElement(nums):
    for i in range(1,len(nums)):
        print(str(nums[0])+" XOR "+str(nums[i]) + " = ")
        nums[0] ^= nums[i]
        print(nums[0])
    return nums[0]
    
    
nums = [2,1,1,7,2]
num = uniqueElement(nums)
a = 9
b = 7

print(num)