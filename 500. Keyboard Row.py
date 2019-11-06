#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    @staticmethod
    def findWords(words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyboard = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],['z', 'x', 'c', 'v', 'b', 'n', 'm']]
        key_map = {}
        i = 0
        while i <len(words):
            if words[i][0].lower() in keyboard[0]:
                key_map[words[i]] = 0
            elif words[i][0].lower() in keyboard[1]:
                key_map[words[i]] = 1
            elif words[i][0].lower() in keyboard[2]:
                key_map[words[i]] = 2
            i +=1
        realwrds = []
        for word in words:
            wrd = True
            for each in word:
                if each.lower() not in keyboard[key_map[word]]:
                    wrd = False
                    break
            if wrd == True:
                realwrds.append(word)
        return realwrds      
                
words = ["Hello", "Alaska", "Dad", "Peace"]
Solution.findWords(words)

