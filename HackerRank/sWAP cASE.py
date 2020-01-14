#!/usr/bin/env python
# coding: utf-8

# In[20]:


# Using FOR Loop without using swapcase()
string = input("Enter Some String : ")
temp = ''
for each in string:
    if each.isupper() == True :
        temp = temp + each.lower()
    elif each.islower() == True :
        temp = temp + each.upper()
    else:
        temp = temp + each # For spaces
print(temp)

