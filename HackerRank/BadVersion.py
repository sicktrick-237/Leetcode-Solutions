# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 08:49:58 2019

@author: user
"""



def calcrange(n):
    iterativevalue = 0
    if n < 10:
        print(n)
        return 
    else:
        digits = [int(x) for x in str(n)]
        for i in range(0,len(digits)):
            iterativevalue += digits[i]
        print(iterativevalue)
        calcrange(iterativevalue)
                
n = 534
result = calcrange(n)
print(result)