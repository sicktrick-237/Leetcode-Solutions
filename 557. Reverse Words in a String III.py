#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    @staticmethod
    def reverseWords(string):
        i = 0
        st = []
        for each in string.split():
            each = "".join(each[::-1])
            st.append(each)
        string = " ".join(st)
        return string

string = "Let's take LeetCode contest"
Solution.reverseWords(string)

