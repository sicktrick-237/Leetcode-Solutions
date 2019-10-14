#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    @staticmethod
    def numSmallerByFrequency(queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        s = 'hello'
        bets = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
        def calFreq(s,bets):
            num = bets[s[0]]
            char = ''
            for each in s:
                if bets[each] <= num:
                    num = bets[each]
                    char = each
            return s.count(char)
        qnums = [calFreq(query,bets) for query in queries]
        wnums = [calFreq(word,bets) for word in words]
        chars = []
        for each in qnums:
            cnt = 0
            for every in wnums:
                if each < every:
                    cnt += 1
            chars.append(cnt)
        return chars
queries = ["bbb","cc"]
words = ["a","aa","aaa","aaaa"]
Solution.numSmallerByFrequency(queries,words)

