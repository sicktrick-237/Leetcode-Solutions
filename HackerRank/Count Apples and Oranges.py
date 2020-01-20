#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def countApplesAndOranges(s, t, a, b, apples, oranges):
    acnt = 0
    bcnt = 0
    for each in apples:
        if each > 0:
            if (each + a) >= s and (each + a) <= t:
                acnt += 1

    for every in oranges:
        if every < 0:
            if (every + b) >= s and (every + b) <= t:
                bcnt += 1
    print(acnt)
    print(bcnt)
    
    
s = 7
t = 11
a = 5
b = 15
apples = [-2, 2, 1]
oranges = [5, -6]
countApplesAndOranges(s, t, a, b, apples, oranges)

