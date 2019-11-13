#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from collections import Counter
class Solution(object):
    @staticmethod
    def isAnagram(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count_s,count_t = Counter(s),Counter(t)
        if len(count_s) == len(count_t):
            for each in count_t:
                if count_s[each] != count_t[each]:
                    return False
            return True
        return False
    
s = 'a'
t = 'b'
Solution.isAnagram(s,t)

