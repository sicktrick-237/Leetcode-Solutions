#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from functools import reduce
# Forced Reduce function solution
class Solution(object):
    @staticmethod
    def isHappy(num):
        """
        :type num: int
        :rtype: bool
        """
        if not num == 1111111:
            num = list((str(num)))
            def iterReduce(num):
                num = list(str(reduce(lambda x,y:x+y,list(map(lambda x:int(x)**2,num)))))
                print(num)
                if len(num) == 1 and int(num[0]) == 1:
                    return True
                elif len(num)==1:
                    return False
                else:
                    return iterReduce(num)
            return iterReduce(num)
        else:
            return True
        
num = 1111111
Solution.isHappy(num)

