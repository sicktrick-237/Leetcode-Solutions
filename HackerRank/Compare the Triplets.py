#!/usr/bin/env python
# coding: utf-8

# In[7]:


def compareTriplets(a, b):
    score = [0, 0]
    for idx,val in enumerate(a):
        if val > b[idx]:
            score[0] += 1
            continue
        if val < b[idx]:
            score[1] += 1
            continue
    return score

a = [5,4,6]
b = [6,4,2]
compareTriplets(a, b)

