#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    @staticmethod
    def findMedianSortedArrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = sorted(nums1 + nums2)
        le = len(nums)
        if le%2 == 0:
            return float((nums[le//2]+nums[(le//2)-1]))/2
        return float(nums[le//2])
        
nums1 = [1,2]
nums2 = [3]
Solution.findMedianSortedArrays(nums1,nums2)

