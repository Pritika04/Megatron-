#!/usr/bin/env python
# coding: utf-8

# In[33]:


import pandas as pd
import numpy as np

sd = pd.DataFrame({"school":["s001","s002","s003","s001","s002","s004"], "class":["V","V","VI","VI","V","VI"], "name":["Alberto Franco","Gino Mcneil","Ryan Parkes","Eesha Hinton","Gino Mcneil","David Parkes"],  "DOB":["15/05/2002","17/05/2002","16/02/1999","25/09/1998","11/05/2002","15/09/1997"], "age":[12,12,14,14,13,12], "height":[172,192,186,167,151,159], "weight":[35,32,33,30,31,32], "address":["street1","street2","street3","street1","street2","street4"]}, index=["S1","S2","S3","S4","S5","S6"])
print(sd)

print(" ")

result = sd.groupby("school") # split the dataframe into groups based on school code
for x,y in result:
    print("Group:")
    print(x)
    print(y)
print(" ")

print(type(result)) # check the type of GroupBy object.

print(" ")

# split the following dataframe by school code and get mean, min, and max value of age for each school
    # For one function/Solution 1
print(sd.groupby("school")["age"].min())

print(" ")

    # For multiple solutions/Solution 2
print(sd.groupby("school").agg({"age":["min","max","mean"]}))

print(" ")

# split the dataframe into groups based on school code and class
result = sd.groupby(["school","class"])
for x,y in result:
    print("Group:")
    print(x)
    print(y)
    
print(" ")

#  split the dataframe into groups based on school code and cast grouping as a list
result = sd.groupby("school")
print(list(result))

print(" ")

# split the dataframe into groups based on single column and multiple columns, and find the size of the grouped data
result1 = sd.groupby("school")
print("Grouping by one column: ")
print(result1.size())
print(" ")
result2 = sd.groupby(["school","class"])
print("Grouping by multiple columns: ")
print(result2.size())

print(" ")

# split the dataframe into groups based on school code and call a specific group with the name of the group
result = sd.groupby("school")
print("Call school code 's001':")
print(result.get_group("s001"))
print(" ")
print("Call school code 's002':")
print(result.get_group("s002"))


# In[ ]:





# In[ ]:




