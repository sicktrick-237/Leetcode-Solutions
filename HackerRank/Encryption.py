#!/usr/bin/env python
# coding: utf-8

# In[151]:


def encryption(s):
    s = s.replace(" ","")
    rt = math.sqrt(len(s))
    row = math.floor(rt)
    col = math.ceil(rt)
    
    # enstr = ""
    lstfr = []
    i = 0
    
    while i < len(s):
        temp = []
        for e in range(col):
            try:
                temp.append(s[i])
                i += 1
            except:
                break
        lstfr.append(temp)
        
        
    finalstr = ""
    for i in range(len(lstfr[0])):
        for each in lstfr:
            try:
                finalstr += each[i]
            except:
                continue
        finalstr += " "
        
    return finalstr.strip()

s = "if man was meant to stay on the ground god would have given us roots"
encryption(s)

