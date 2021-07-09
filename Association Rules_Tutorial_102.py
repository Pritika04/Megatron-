#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from apyori import apriori 
import matplotlib.pyplot as plt


# In[6]:


movies_data = pd.read_csv("movies_association.csv")
print(movies_data.head())
print(movies_data.shape)


# In[8]:


# Convert dataframe into list
records = []
for i in range(0,10):
    records.append([str(movies_data.values[i,j]) for j in range(0, 5)])

print(records)


# In[23]:


# Fitting the data to the algorithm
association_rules = apriori(records, min_support=0.01, min_confidence=0.2, min_lift=3, min_length=2)


# In[24]:


# Converting associations into a list
association_rules = list(association_rules)


# In[25]:


# Number of rules 
print(len(association_rules))


# In[19]:


print(association_rules[0])


# In[ ]:




