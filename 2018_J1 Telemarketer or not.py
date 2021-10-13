#!/usr/bin/env python
# coding: utf-8

# # QUESTION:

# In[1]:


# Q: Here at the Concerned Citizens of Commerce (CCC), we have noted that telemarketers like to use seven-digit phone numbers 
# where the last four digits have three properties. Looking just at the last four digits, these properties are:

# the first of these four digits is an 8 or 9;
# the last digit is an 8 or 9;
# the second and third digits are the same.
# For example, if the last four digits of the telephone number are 8229, 8338, or 9008, these are telemarketer numbers.

# Write a program to decide if a telephone number is a telemarketer number or not, based on the last four digits. If the number 
# is not a telemarketer number, we should answer the phone, and otherwise, we should ignore it.


# In[15]:


N = input("Input phone number:")
lst = []
counter = 0

for x in N[3:]:
    lst.append(x)

if (int(lst[0]) == 8 or int(lst[0]) == 9) and (int(lst[3]) == 8 or int(lst[3]) == 9):
    counter += 2
if lst[1] == lst[2]:
    counter +=1

if counter == 3:
    print("Telemarketer's number. Do NOT pick!")
else:
    print("Safe to pick!")


# In[ ]:





# In[ ]:




