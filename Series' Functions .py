#!/usr/bin/env python
# coding: utf-8

# In[60]:


import pandas as pd
import numpy as np 

s = pd.Series([23,56,78,100,54], index=["A","B","C","D","E"], name="Test")
s1 = pd.Series([34,14,78,19,39], index=["A","B","C","D","E"])

def pooja(x):
    return x**2

# Transpose: 
print(s.T)

# Data Type:
print(s.dtype)

# Slicing by location:
print(s.iloc[-3:])

# Name:
print(s.name)

# Dimension:
print(s.ndim)

# Shape(rows and columns):
print(s.shape)

# Number of elements:
print(s.size)

# Gives only the values:
print(s.values)

# Append: 
print(s.append(s1, ignore_index=True))

# Calling a function:
print(s.apply(pooja))

# Returning index of the maximum value:
print(s.argmax())

# Returning index of the minimum value:
print(s.argmin())

# Returning the label index of the maximum value:
print(s.idxmax())

# Returning the label index of the minimum value:
print(s.idxmin())

# Checking each element with a criteria:
print(s.between(20,30, inclusive=False))

# Combining two series:
print(s1.combine(s,max,fill_value=0))

# Compare:
print(s.compare(s1, keep_shape=True, keep_equal=True))

# Making a copy of the series: 
x = s.copy()
print(x)

# Count(non-null):
print(s.count())

# Statistical description:
print(s.describe())

# Calculates the difference between elements:
print(s.diff(periods=1))


# In[ ]:





# In[ ]:




