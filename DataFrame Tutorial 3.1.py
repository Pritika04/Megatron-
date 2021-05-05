#!/usr/bin/env python
# coding: utf-8

# In[33]:


import pandas as pd
import numpy as np

cd = pd.read_csv("Company_Data.csv")

print(cd)
print(" ")
print(cd[cd["Age"]>50]) # Condition where 'Age'>50
print(" ")
print(cd[cd["Age"].isin([55,65])]) # Condition to give the rows where 'Age' is either 55 or 65
print(" ")
cd_1 = cd.copy()
print(cd_1)
print(" ")
pd.isna(cd)
print(" ")
cd_2 = cd[cd["ShelveLoc"].isin(["Good","Bad"])]
print(cd_2.shape)
cd_3 = cd[(cd.ShelveLoc=="Good") & (cd.Population>200)]
print(cd_3.shape)
cd_4 = cd[cd["ShelveLoc"].str[0] == "B"]
print(cd_4)
cd_5 = cd[cd["ShelveLoc"].str.len()>4]
print(cd_5)


# In[57]:


import pandas as pd
import numpy as np

wa = pd.read_csv("word_alcohol.csv")

print(wa)
print(" ")
print(wa.iloc[0:2,0:2])
print(" ")
print(wa.sample(5))
print(" ")
pd.isna(wa)
print(wa.dropna())
print(" ")
print(wa.drop_duplicates("WHO region"))
print(" ")
filter_1 = wa[(wa["Year"]==1987) | (wa["Year"]==1989)]
print(filter_1['Display Value'].sum())


# In[ ]:





# In[ ]:




