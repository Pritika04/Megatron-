#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install apyori 


# In[2]:


import pandas as pd
import numpy as np
from apyori import apriori 
import matplotlib.pyplot as plt


# In[3]:


store_data = pd.read_csv("store_data.csv", header=None)
print(store_data.head())


# In[4]:


# Convert dataframe into list
records = []
for i in range(0,7501):
    records.append([str(store_data.values[i,j]) for j in range(0, 20)])

print(records)


# In[27]:


# Fitting the data to the algorithm
association_rules = apriori(records, min_support=0.0045, min_confidence=0.2, min_lift=3, min_length=2)


# In[28]:


# Converting associations into a list
association_rules = list(association_rules)


# In[29]:


# Number of rules 
print(len(association_rules))


# In[30]:


print(association_rules[0])


# In[ ]:




