#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Solution(object):
    i = 0
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if self.i < len(nums2):
            if 0 in nums1:
                nums1[nums1.index(0)] = nums2[self.i]
                self.i += 1
                return Solution.merge(self,nums1,m,nums2, n)
        nums1.sort()
        return nums1
sol = Solution()   
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3
sol.merge(nums1,m, nums2, n)


# In[ ]:




