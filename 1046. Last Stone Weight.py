#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
We have a collection of rocks, each rock has a positive integer weight.

Each turn, we choose the two heaviest rocks and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

- If x == y, both stones are totally destroyed;
- If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.

At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

 

Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
 

Note:

1. 1 <= stones.length <= 30
2. 1 <= stones[i] <= 1000
'''


# In[ ]:


class Solution(object):
    @staticmethod
    def lastStoneWeight(nums):
        """
        :type stones: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        else:
            y = max(nums)
            y_idx = nums.index(y)
            nums.pop(y_idx)
        if len(nums) == 0:
            return y
        else:
            x = max(nums)
            x_idx = nums.index(x)
            nums.pop(x_idx)
        if x != y:
            val = abs(y-x)
            nums.insert(y_idx,val)
            return Solution.lastStoneWeight(nums)
        elif len(nums) == 1:
            return nums[0]
        else:
            return Solution.lastStoneWeight(nums)
        
        
nums = [2,7,4,1,8,1]
Solution.lastStoneWeight(nums)

