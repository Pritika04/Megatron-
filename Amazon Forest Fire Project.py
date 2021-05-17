#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

org_ad = pd.read_csv("amazon1.csv", thousands='.')
ad = org_ad.copy() 

ad2 = ad.dropna(subset=["number"])
ad2 = ad2.replace(0,np.nan) 

fire_month = ad2.groupby("month").agg({"number":sum})

months_unique = list(ad2.month.unique())
fire_month = fire_month.reindex(months_unique,axis=0)

fire_month.reset_index(level=0,inplace=True)

plt.figure(1)
plt.figure(figsize=(25,15))

plt.bar(fire_month["month"],fire_month["number"])
plt.title("AMAZON FOREST FIRES OVER THE MONTHS (1998-2017)",fontsize=17)
plt.xlabel("Months",fontsize=15)
plt.ylabel("Number of forest fires",fontsize=15)

for i, num in enumerate(fire_month['number']):
    plt.text(
        i,
        num + 10000,
        num,
        ha='center',
        fontsize=15)


# In[ ]:




