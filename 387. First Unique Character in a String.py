# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 07:37:29 2019

@author: Omkar Kadam
"""


def firstUniqChar(s):
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            return s.find(s[i])
    return -1



def recursiveMe(s):
    i = 0
    while(i<len(s)<26):
        if s.count(s[i]) == 1:
            return s.find(s[i])
        else:
            i += 1
            continue
    if i == len(s):
        return -1
    else:
        return -1





def recursiveUs(s):
    global i
    if i < len(s):
        if s.count(s[i]) == 1:
            return s.find(s[i])
        else:
            i += 1
            return recursiveUs(s)
    elif 1 == len(s):
        return 0
    elif 0 == len(s):
        return -1
    else:
        return -1
    
s = "aaab"
count = recursiveMe(s)
print(count)