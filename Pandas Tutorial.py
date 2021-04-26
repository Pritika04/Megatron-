#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pandas 


# In[21]:


import pandas as pd 
s = pd.Series(5, index=["A","B","C","D","E"])
print(s)


# In[30]:


dict = {"Hello":1,"World":2,"My":3,"Name":4,"Is":5}
s = pd.Series(dict, index=["A",'B','C','D','E'])
print(s)


# In[34]:


# Converting Pandas series to a Python list. 
s = pd.Series(["A","B","C","D","E"])
print(s)
print(s.tolist())


# In[40]:


# Write a Pandas program to add, subtract, multiple and divide two Pandas Series.
s1 = pd.Series([2,4,6,8,10])
s2 = pd.Series([1,3,5,7,9])
print("Addition: ")
print(s1 + s2)
print("Subtraction: ")
print(s1-s2)
print("Multiplication: ")
print(s1*s2)
print("Division: ")
print(s1/s2)


# In[43]:


# Write a Pandas program to compare the elements of the two Pandas Series
s1 = pd.Series([1,4,7,8,0])
s2 = pd.Series([1,2,5,4,9])
print("s1 is greater than s2: ")
print( s1 > s2)
print("s1 is smaller than s2: ")
print( s1 < s2)
print("s1 is equal to s2: ")
print( s1 == s2)


# In[48]:


# Write a Pandas program to change the data type of given a column or a Series.
s1 = pd.Series(['100', '200', 'python', '300.12', '400'])
print("Original series: ")
print(s1)
s2 = pd.to_numeric(s1, errors="coerce")
print("New series: ")
print(s2)


# In[ ]:




