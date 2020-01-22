#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def countingValleys(n, s):
    u = 0
    d = 0
    v = 0
    gl = 0


    for step in s:
        if gl == 0 and step == "D":
            v += 1
            gl = -1
        if gl == 0 and step == "U":
            gl = 1
        if step == "D":
            d += 1
        elif step == "U":
            u += 1
        if u - d == 0:
            gl = 0
            u = 0
            d = 0
    return v

n = 8 
s = "UUDDDDUUUDDDUU"
countingValleys(n, s)

