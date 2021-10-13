#!/usr/bin/env python
# coding: utf-8

# # QUESTION:

# In[ ]:


# You supervise a small parking lot which has N parking spaces. Yesterday, you recorded which parking spaces were occupied by 
# cars and which were empty. Today, you recorded the same information. How many of the parking spaces were occupied both 
# yesterday and today? 

# Input Specification: The first line of input contains the integer N (1≤N≤100). The second and third lines of input contain N 
# characters each. The second line of input records the information about yesterday's parking spaces, and the third line of 
# input records the information about today's parking spaces. Each of these 2N characters will either be C to indicate an 
# occupied space or . to indicate it was an empty parking space.

# Output Specification: Output the number of parking spaces which were occupied yesterday and today.

# Sample Input:
# 5
# CC..C
# .CC..

# Sample Output:
# 1


# In[6]:


N = int(input("Number of parking spaces: "))
lst_yes = []
lst_tod = []
occ_counter = 0

for x in range(N):
    info = input("Yesterday: ")
    lst_yes.append(info)

for x in range(N):
    info = input("Today: ")
    lst_tod.append(info)
    
for x in range(0,N-1):
    if lst_yes[x] == lst_tod[x]:
        if (lst_yes[x] == "C" or lst_tod == "C"):
            occ_counter += 1

print("Common occupied parking spaces: ", occ_counter)


# In[ ]:




