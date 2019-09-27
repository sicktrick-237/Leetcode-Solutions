#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import string
class Solution(object):
    @staticmethod
    def uniqueMorseRepresentations(words): 
        """
        :type words: List[str]
        :rtype: int
        """
        code_map = {}
        trans = []
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for idx,val in enumerate(list(string.ascii_lowercase)):
            code_map[val] = code[idx]
        for word in words:
            str = ''
            for each in word:
                str += code_map[each]
            trans.append(str)
        return len(set(trans))
    
    def morseRep(words): 
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        trans = []
        for word in words:
            str = ''
            for each in word:
                str += code[alpha.index(each)]
            trans.append(str)
        return len(set(trans))
words = ["gin", "zen", "gig", "msg"]
Solution.uniqueMorseRepresentations(words)

