# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 03:58:57 2019

@author: omkar.kadam
"""



def searchInsert(nums,e): # 6% faster
    if nums:
        if e in nums:
            return nums.index(e)
        else:
            i = 0
            while(i<len(nums)):
                if nums[i] > e:
                    return nums.index(nums[i])
                elif nums[i] < e and i == len(nums)-1:
                    return nums.index(nums[i])+1
                i += 1
                
def searchInsertalternate(nums,e): # 65% faster
    if e in nums:
        return nums.index(e)
    else:
        for each in nums:
            if each > e:
                return nums.index(each)
        return len(nums)
    return 


def thirdAlternative(nums,target): # 66% faster
    sizeoflist = len(nums)
    flag = 1
    for i in range(0,sizeoflist):
        if nums[i] == target:
            return i
        elif target < nums[i]:
            return i
        else:
            flag = 0
    if flag == 0:
        return sizeoflist          
        
nums = [2,3,4,6]
e = 5
idx = searchInsertalternate(nums,e)
print(idx)