#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
Problem Statement :
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
1 2 3
4 5 6
9 8 9 
The left-to-right diagonal = 1+5+9 = 15. 
The right to left diagonal = 3+5+9 = 17. 
Their absolute difference is |15-17| = 2.
'''

# Square Matrix Traversal and use of abs()

x = int(input("Enter Matrix Row Size"))
y = int(input("Enter Matrix Column Size"))

matrix = []

for i in range(x):
    temp = []
    for j in range(y):  
        tempVar = int(input("Enter :"+str(i)+str(j))+" ")
        temp.append(tempVar)
    matrix.append(temp)

leftToRight = 0
rightToLeft = 0
for i in range(x):
    for j in range(y):
        # For leftToRight Diagonal the elements are M00, M11, M22, M33, M44 i.e. row = columns
        if i==j:
            leftToRight += matrix[i][j]
            print("leftToRight",leftToRight)
        # For rightToLeft Diagonal condition is row = numberOfRows – column-1.
        if (i+j)==(y-1):
            rightToLeft += matrix[i][j]
            print("rightToLeft",rightToLeft)
difference = leftToRight - rightToLeft
abs(difference) 
# abs will return the absolute value of any number. Absolute value is always a non-negative number.

