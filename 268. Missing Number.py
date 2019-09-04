#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def missingNumber(nums):
    num = len(nums)
    return int(((num*(num+1))/2) - sum(nums))
    # Using Gauss Reduction Formula to find the missing value
    # i = n(n+1)/2
    
        
nums = [3,0,1]
nums = set(nums)
missingNumber(nums)

