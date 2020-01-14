#!/usr/bin/env python
# coding: utf-8

# In[8]:


'''
Platform : HackerRank
PROBLEM STATEMENT : 
If your niece is turning 4 years old, and the cake will have 4 candles of height 4, 4, 1, 3.
She will be able to blow out 2 candles successfully, 
since the tallest candles are of height 4 and there are 2 such candles.

Complete the function birthdayCakeCandles in the editor below.
It must return an integer representing the number of candles she can blow out.

Input :
4
3 2 1 3

Output :
2

'''
# Max(list) returns max element from the list


def birthdayCakeCandles(candles):
    maxHeight = max(candles)
    totalCandles = 0
    for each in candles:
        if each == maxHeight:
            totalCandles += 1
    return totalCandles
    
ch = int(input("How many candles you want to put"))
candles = []
for each in range(ch):
    candle = int(input("Candle height ? : "))
    candles.append(candle)
birthdayCakeCandles(candles)

