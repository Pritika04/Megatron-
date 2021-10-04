#!/usr/bin/env python
# coding: utf-8

# # QUESTION:

# In[ ]:


# Mahima has been experimenting with a new style of art. She stands in front of a canvas and, using her brush, flicks drops of 
# paint onto the canvas. When she thinks she has created a masterpiece, she uses her 3D printer to print a frame to surround the
# canvas. Your job is to help Mahima by determining the coordinates of the smallest possible rectangular frame such that each 
# drop of paint lies inside the frame. Points on the frame are not considered inside the frame. Input Specification The first 
# line of input contains the number of drops of paint, N, where 2 < N < 100 and N is an integer. Each of the next N lines 
# contain exactly two positive integers X and Y separated by one comma (no spaces). Each of these pairs of integers represents 
# the coordinates of a drop of paint on the canvas. Assume that X < 100 and Y < 100, and that there will be at least two 
# distinct points. The coordinates (0, 0) represent the bottom-left corner of the canvas. For 12 of the 15 available marks, X 
# and Y will both be two-digit integers. Output Specification Output two lines. Each line must contain exactly two non-negative 
# integers separated by a single comma (no spaces). The first line represents the coordinates of the bottom-left corner of the 
# rectangular frame. The second line represents the coordinates of the top-right corner of the rectangular frame. Sample Input 
# 5 44,62 34,69 24,78 42,44 64,10 Output for Sample Input 23,9 65,79.   


# In[8]:


lst = []
X_list = []
Y_list = []

N = input("Number of dots: ")

for x in range(int(N)):
    x_y_input = input()
    X,Y=x_y_input.split(',')
    X_list.append(X)
    Y_list.append(Y)

x_min = min(X_list)
x_min_pos = X_list.index(x_min)
y_min = Y_list[x_min_pos]

x_max = max(X_list)
x_max_pos = X_list.index(x_max)
y_max = Y_list[x_max_pos]

print(X_list,Y_list)
print("Minimum coordinate: ", int(x_min)-1, ", ", int(y_max)-1)
print("Maximum coordinate: ", int(x_max)+1, ", ", int(y_min)+1)


# In[ ]:




