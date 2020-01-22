#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def kangaroo(x1, v1, x2, v2):
    if ( x2 > x1 and v2 > v1 ) or ( x1 > x2 and v1 > v2 ):
        return "NO"
    for i in range(10000):
        if x1 + v1 + i == x2 + v2 + i:
            return "YES"
        x1 += v1
        x2 += v2
    return "NO"

x1 = 0
v1 = 2
x2 = 5
v2 = 3
kangaroo(x1, v1, x2, v2)

