# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 02:47:37 2019

@author: omkar.kadam
"""
def camelcase(s):
    i = 0
    for each in s:
        if each.isupper():
            i += 1
    return i+1


s = 'saveChangesInTheEditor'
result = camelcase(s)
print(result)