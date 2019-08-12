#!/usr/bin/env python
# coding: utf-8

# In[103]:


class Solution(object):
    def usingStrip(self, string):
            string = string.strip()
            if string:
                string = string.split(" ")
                return len(string[-1])
            else:
                return 0
  
                        
string ="Hello World"
sl = Solution()
num = sl.usingStrip(string)
print(num)


# In[ ]:




