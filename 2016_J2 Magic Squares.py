#!/usr/bin/env python
# coding: utf-8

# # QUESTION:

# In[ ]:


# Q: Magic Squares are square arrays of numbers that have the interesting property that the numbers in each column, and in each 
# row, all add up to the same total. Given a 4×4 square of numbers, determine if it is a magic square.

# Input Specification: The input consists of four lines, each line having 4 space-separated integers.

# Output Specification: Output either magic if the input is a magic square, or not magic if the input is not a magic square.

# Example: 16 3 2 13
#          5 10 11 8
#          9 6 7 12
#          4 15 14 1

# Output: Magic Square 


# In[1]:


import numpy as np

array_1 = []

for x in range(4):
    row = []
    print("Enter row-wise entries: ")
    for y in range(4):
        row.append(int(input()))
    array_1.append(row)

array = np.array(array_1)

row_list = []
col_list = []

for x in array:
    row_sum = 0
    for y in x:
        row_sum += y
    row_list.append(row_sum)
print(row_list)
    
array_trans = array.T

for x in array_trans:
    col_sum = 0
    for y in x:
        col_sum += y
    col_list.append(col_sum)
print(col_list)

if row_list == col_list:
    print("Magic Square!")
else:
    print("Not a Magic Square!")


# In[ ]:





# In[ ]:




