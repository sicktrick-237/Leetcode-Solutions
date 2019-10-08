#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    @staticmethod
    def maxNumberOfBalloons(text):
        """
        :type text: str
        :rtype: int
        """
        cnt = 0 
        vals = {'b':0,'a':0,'l':0,'o':0,'n':0}
        for each in vals:
            vals[each] = text.count(each)
        try:
            for i in range(1,vals['b']+1):
                if i <= vals['a'] and i <= vals['n'] and vals['l'] >= i*2 and vals['o'] >= i*2:
                    cnt +=1
            return cnt
        except:
            return 0
text =  "leetcode"   
Solution.maxNumberOfBalloons(text)

