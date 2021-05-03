#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dataframe - two dimensional data structure


# In[31]:


import pandas as pd

d = {"Fruits I":["apple","banana","grapes"], "Fruits II":["mango","watermelon","strawberry"]}

df = pd.DataFrame(d)

print(df) # Entire table
print(" ")
print(df.loc[0]) # One row
print(" ")
print(df.loc[[0,1]]) # Multiple rows
print(" ")
print(df["Fruits I"]) # One column 
print(" ")
print(df[["Fruits I","Fruits II"]]) # Multiple columns
print(" ")
print(df[0:2]) # All columns, but only the first two rows of data. 
print(" ")
print(df.iloc[[1]]) # Printing rows using index
print(" ")
print(df.iloc[[1,2]]) # Printing multiple rows using index
print(" ")
print(df.iloc[[0,1],[0]]) # Printing a combination of rows and columns using index
print(" ")
print(df.iloc[0:2])
print(" ")
print(df.iloc[0:2,0])


# In[46]:


import pandas as pd

d = {"Fruits I":["apple","banana","grapes","guava"], "Fruits II":["mango","watermelon","strawberry","blueberry"], "Fruits III":["peach","plum","melon","raspberry"]}

df = pd.DataFrame(d)

print(df)
print(" ")
print(df.iloc[0:3])
print(" ")
print(df.iloc[-3:-1])
print(" ")
print(df.iloc[[0,-1]])
print(" ")
print(df.iloc[0:3,0])
print(" ")
print(df.iloc[0:3,0:2])


# In[73]:


import pandas as pd

cd = pd.read_csv("Company_Data.csv")

print(cd.head(10))
print(" ")
print(cd.tail(10))
print(" ")
print(cd.shape)
print(" ")
print(cd.iloc[0:2,7])
print(" ")
print(cd.iloc[:,0:3])
print(" ")
print(cd.iloc[-1:])
print(" ")
print(cd.iloc[[0,200]])
print(" ")
print(cd.at[0,"Sales"])
print(" ")
print(cd.columns)
print(" ")
print(cd.ndim)
print(" ")
print(cd.size)
print(" ")
print(cd.values)       
print(" ")
cd["India"]=pd.Series(["Yes","Yes","No","Yes","No","Yes"])
print(cd)
del cd["India"]
print(cd)


# In[ ]:




