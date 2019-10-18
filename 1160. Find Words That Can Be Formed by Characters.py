#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    @staticmethod
    def countCharacters(words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        fal = False
        cnt = 0
        for each in words:
            st = list(chars)
            for val in each:
                if val in st:
                    st.remove(val)
                    fal = True
                    continue
                fal = False
                break
            if fal:
                cnt += len(each)
        return cnt
                
words  = ["cat","bt","hat","tree"]
chars = 'atach'
Solution.countCharacters(words,chars)

