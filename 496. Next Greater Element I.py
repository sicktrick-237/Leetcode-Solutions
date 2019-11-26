#!/usr/bin/env python
# coding: utf-8

# In[50]:


class Solution(object):
    @staticmethod
    def nextGreaterElement(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        temp = []

        for each in nums1:
            newarr = nums2[nums2.index(each)+1:]
            if newarr:
                flg = True
                for i in range(len(newarr)):
                    if each < newarr[i]:
                        temp.append(newarr[i])
                        flg = False
                        break
                if flg:
                    temp.append(-1)
            else:
                temp.append(-1)
        return temp
    
    
nums1 = [2,4]
nums2 = [1,2,3,4]
Solution.nextGreaterElement(nums1, nums2)

