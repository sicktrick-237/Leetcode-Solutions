#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def findAndReplacePattern(self,words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def mapping(ars):
            ars = list(ars)
            unqiue_vals = []
            mapping= {}
            cnt = 0
            string = ''
            for each in ars:
                if each not in mapping:
                    mapping[each] = cnt
                    cnt +=1
            for i in range(len(ars)):
                string += str(mapping[ars[i]])
            return string
        pattern = mapping(pattern)
        combs = [mapping(each) for each in words]
       
        return [words[i] for i in range(len(combs)) if combs[i] == pattern]
        
        
words = ["abc","cba","xyx","yxx","yyx"]
pattern = "abc"
sol = Solution()
sol.findAndReplacePattern(words,pattern)

