#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    @staticmethod
    def toGoatLatin(string):
        """
        :type S: str
        :rtype: str
        """
        string = string.split()
        latin_str = ''
        vowels = ['a','e','i','o','u']
        for i in range(len(string)):
            if string[i][0].lower() not in vowels:
                latin_str += string[i][1:]+string[i][0]+'ma'+(i+1)*'a'+' '
                continue
            latin_str += string[i]+'ma'+(i+1)*'a'+' '    
        return latin_str.strip()
    
string = "The quick brown fox jumped over the lazy dog"
Solution.toGoatLatin(string)

