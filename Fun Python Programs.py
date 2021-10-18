#!/usr/bin/env python
# coding: utf-8

# # QUESTION:

# In[ ]:


# Write a program to calculate the sum of series up to n term. For example, if n =5, the series 
# will become 2 + 22 + 222 + 2222 + 22222 = 24690


# In[16]:


N = input("Enter iterating number: ")
n = int(input("Enter number of terms: "))
total = 0
temp = N

for x in range(n):
    total += int(N)
    N += temp
    
print(total)


# In[ ]:





# # QUESTION:

# In[5]:


# Write a program to print the following pattern using the for loop and make the program versatile:
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *


# In[26]:


N = int(input("Pattern Number: "))

for x in range(N):
    for y in range(x+1):
        print("*", end=" ")
    print("\r")
    if x == (N-1):
        for w in range((N-1),0,-1):
            for z in range(w,0,-1):
                print("*", end=" ")
            print("\r")


# In[ ]:





# In[ ]:





# In[ ]:




