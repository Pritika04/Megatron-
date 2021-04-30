#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
import numpy as np

s = pd.Series([1,45,68,100,100], index=["A","B","C","D","E"])
s1 = pd.Series([6,7,8,9,10], index=["A","B","C","D","E"])
s2 = pd.Series([1,1,2,2,3,np.nan])
s3 = pd.Series(["cat","bat","song"])

print(s.div(s1))
print(" ")
print(s.divide(s1))
print(" ")
print(s.drop(labels=["A","E"]))
print(" ")
print(s2.drop_duplicates(keep='first'))
print(" ")
print(s2.dropna())
print(" ")
print(s2.duplicated())
print(" ")
print(s.eq(s1))
print(" ")
print(s.equals(s1))
print(" ")
print(s.filter(items=["A","B"]))
print(" ")
print(s.head(3))
print(" ")
print(s.tail(3))
print(" ")
print(s.isin(s2))
print(" ")
print(s2.isna())
print(" ")
for index,value in s.items():
    print(index,value)
print(" ")
print(s.nlargest(3))
print(" ")
print(s.nsmallest(3))
print(" ")
print(s2.nunique())
print(" ")
print(s3.pop(0))
print(" ")
print(s.rank(ascending=False, method='max'))


# In[ ]:




