#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
s = pd.Series([11,12,13], index=["A","B","C"])
print(s['C'])


# In[ ]:


# Write a Pandas program to sort a given Series
s = pd.Series([100,300,400,200,500])
print("Original series: ")
print(s)
print("New series: ")
print(s.sort_values(ignore_index=False,ascending=False))


# In[ ]:


# Write a Pandas program to add some data to an existing Series.
s = pd.Series([10,20,70,27,94])
s = s.append(pd.Series(50), ignore_index=True)
print(s)


# In[ ]:


# Write a Pandas program to create a subset of a given series based on value and condition.
s = pd.Series([14,50,30,25,67,49,36])
print("Original series: ")
print(s)
print("New series: ")
print(s[s<50])


# In[ ]:


# Write a Pandas program to change the order of index of a given series.
s = pd.Series([1,2,3,4,5], index=["A","B","C","D","E"])
print("Original series: ")
print(s)
s = s.reindex(index=["B","D","E","A","C"])
print("New series: ")
print(s)


# In[ ]:


# Write a Pandas program to create the mean and standard deviation of the data of a given Series.
s = pd.Series([1,2,3,4,5,6,7,8,9,10])
print("Original series: ")
print(s)
print("Mean of the series: ")
print(s.mean())
print("Standard deviation of the series: ")
print(s.std())


# In[ ]:


# Write a Pandas program to get the items of a given series not present in another given series.
s1 = pd.Series([1,2,3,4,5])
s2 = pd.Series([2,4,6,8,10])
print("Common items: ")
print(s1[s1.isin(s2)])
print("Items in s1 not in s2: ")
print(s1[~s1.isin(s2)])


# In[ ]:


# Write a Pandas program to get the items which are not common of two given series.
s1 = pd.Series([1,2,3,4,5])
s2 = pd.Series([2,4,6,8,10])
print("Uncommon items: ")
print(s1[~s1.isin(s2)], s2[~s2.isin(s1)])


# In[ ]:


# Write a Pandas program to compute the minimum, 25th percentile, median, 75th, and maximum of a given series.
import numpy as np
s1 = pd.Series([23,56,10,74,97])
print(s1)
print("Minimum, 25th Percentile, Median, 75th Percentile, Maximum ")
result= np.percentile(s1, q=[0,25,50,75,100])
print(result)


# In[2]:


# Write a Pandas program to calculate the frequency counts of each unique value of a given series.
import pandas as pd
s1 = pd.Series([1,3,5,8,5])
print(s1.value_counts())


# In[11]:


# Write a Pandas program to find the positions of numbers that are multiples of 5 of a given series.
s1 = pd.Series([1,3,5,4,3,5,7,9,10,2])
s2 = s1[s1 % 5 == 0]
print(s2.index)


# In[ ]:




