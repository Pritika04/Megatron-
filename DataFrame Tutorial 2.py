#!/usr/bin/env python
# coding: utf-8

# In[41]:


import pandas as pd
import numpy as np

cd = pd.read_csv("Company_Data.csv")

print(cd.head(5))# First 5 rows.
print(" ")
print(cd.tail(5)) # Last 5 rows.
print(" ")
print(cd.loc[:,["Income","Age"]]) # Two columns 
print(" ")
print(cd.iloc[0:3,0:2]) # First 3 rows, and first 2 columns
print(" ")
print(cd.iloc[:,0]) # All rows and first column
print(" ")
print(cd["Age"].mean()) # Mean for the 'Age' column
print(" ")
print(cd.axes)
print(" ")
print(cd.axes[0]) # 0 = rows
print(" ")
print(cd.axes[1]) # 1 = columns
print(" ")
print(cd.apply(np.sum,axis=0)) # Sum of data row-wise
print(" ")
print(cd[["Age","Price"]].mean()) 
print(" ")
print(cd.describe())
print(" ")
print(cd["Age"].value_counts())
print(" ")
print(cd.set_index("Age"))


# In[34]:


import pandas as pd
import numpy as np

d = {"Yes":[50,20,60,70,90,100,43,56,78,23,79], "No":[131,54,23,80,100,4,32,56,78,10,101]}
df = pd.DataFrame(d)

fruits = pd.DataFrame({"Apple":[10,20], "Banana":[30,40]})
new_fruits = fruits.rename(index={0:"2017 Sales:", 1:"2018 Sales:"})

print(new_fruits)
print(" ")
print(df.iloc[0,0])
print(" ")
print(df.iloc[:,0])
print(" ")
print(df.iloc[0:3,0])
print(" ")
print(df.tail(5))


# In[ ]:




