#!/usr/bin/env python
# coding: utf-8

# In[60]:


def isleap(year):
    day = 0
    if year == 1918:
        return str(13+13)+".09."+str(year)
    if year % 4 == 0 or (year % 400 == 0 or (year % 4 == 0 and not year % 100 == 0)):
        day = 12
    else:
        day = 13
    return str(day)+".09."+str(year)
    
year = 1800
isleap(year)

