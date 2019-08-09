# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 02:04:09 2019

@author: omkar.kadam
"""
i = 0
sr = ''
def toLowerCase(string):
    i = 0
    keys = list(set(string))
    while(i<len(keys)):
        if keys[i].isupper():
            string = string.replace(keys[i],keys[i].lower())
        i += 1
    return string


def alternateSoltion(str):
    keys = set(str)
    for key in keys:
        if key.isupper():
            str = str.replace(key,key.lower())
    return str


string = "Hello Leetcode"

stri = alternateSoltion(string)
print(stri)