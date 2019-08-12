#!/usr/bin/env python
# coding: utf-8

# In[103]:


class Solution(object):
    def lengthOfLastWord(self, string):
        """
        :type s: str
        :rtype: int
        """
        i = -1
        l = len(string)
        if ' ' == string:
            return 0
        elif l == 1:
            return 1
        elif ' ' not in string:
            return len(string)
        else:
            string = string.split(" ")
            while(-(l)-1 != i):
                if string[i] != '':
                    return len(string[i])
                else:
                    i -= 1
            return 0
  
                        
string ="Hello World"
sl = Solution()
num = sl.lengthOfLastWord(string)
print(num)


# In[ ]:




