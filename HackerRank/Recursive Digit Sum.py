#!/usr/bin/env python
# coding: utf-8

# In[3]:


#!/bin/python3

import math
import os
import random
import re
import sys

superdigit = 0
# Complete the superDigit function below.
def superDigit(n, k):
    if len(n) != 0 or len(n) > 0:
        p = n*k
        digit = 0
        if len(p) > 1:
            for i in range(len(p)):
                digit += int(p[i])
            print(digit)
            return superDigit(str(digit), 1)
        else:
            print(p)
            return p
    else:
        return int(p)
    
n = '156'
k = 6
result = superDigit(n,k)
print("Result : " + result)

