#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd
import numpy as np

wa = pd.read_csv("word_alcohol.csv")

# alcohol consumption details by the 'Americas' in the year '1985'
f1 = wa[(wa["WHO region"]=="Americas") & (wa["Year"]==1985)]
print(f1)

print(" ")

# alcohol consumption details in the year '1986' where WHO region is 'Western Pacific' and country is 'VietNam'
f2 = wa[(wa["Year"]==1986) & (wa["WHO region"]=="Western Pacific") & (wa["Country"]=="Viet Nam")]
print(f2)

print(" ")

# alcohol consumption details in the year '1986' or '1989' where WHO region is 'Americas' 
f3 = wa[(wa["WHO region"]=="Americas") & ((wa["Year"]==1986) | (wa["Year"]==1989))]
print(f3)

print(" ")

# alcohol consumption details in the year '1986' or '1989' where WHO region is 'Americas' or 'Europe'
f4 = wa[((wa["Year"]==1986) | (wa["Year"]==1989)) & ((wa["WHO region"]=="Americas") | (wa["WHO region"]=="Europe"))]
print(f4)

print(" ")

# find out the 'WHO region, 'Country', 'Beverage Types' in the year '1986' or '1989' where WHO region is 'Americas' or 'Europe'
print(f4[["WHO region","Country","Beverage Types"]])

print(" ")

# find out the records where consumption of beverages per person average >=5 and Beverage Types is Beer
f5 = wa[(wa["Display Value"]>=5) & (wa["Beverage Types"]=="Beer")]
print(f5)

print(" ")

# find out the records where consumption of beverages per person average >=4 and Beverage Types is Beer, Wine, Spirits
f6 = wa[(wa["Display Value"]>=4) & (wa["Beverage Types"].isin(["Beer","Wine","Spirits"]))]
print(f6)

print(" ")

# where WHO region contains "Ea" substring from world alcohol consumption dataset
f7 = wa[wa["WHO region"].str.contains("Ea")]
print(f7)

print(" ")

# where WHO region matches with multiple values (Africa, Eastern Mediterranean, Europe)
f8 = wa[wa["WHO region"].isin(["Africa","Eastern Mediterranean","Europe"])]
print(f8)

print(" ")

# average consumption of beverages per person from .5 to 2.50
f9 = wa[(wa["Display Value"]>0.5) & (wa["Display Value"]<2.5)]
print(f9)

print(" ")

# average consumption of wine per person greater than 2
f10 = wa[(wa["Beverage Types"]=="Wine") & (wa["Display Value"]>2)]
print(f10)

print(" ")

# select consecutive columns and also select rows with Index label 0 to 9 with some columns
f11 = wa.iloc[:, 2:5]
print(f11)

print(" ")

# select rows with Index label 0 to 9 with some columns
f12 = wa.loc[0:9,["Country","Beverage Types"]]
print(f12)

print(" ")

# rename all and only some of the column names 
f13 = wa.rename(columns = {"WHO region":"WHO_region", "Display Value":"Display_Value"}, inplace=True)
print(wa)

print(" ")

# filter all records starting from the 'Year' column, access every other column from world alcohol consumption dataset.
f14 = wa.loc[:, "Year"::2]  # or, f14 = wa.iloc[:, 0::2]
print(f14)

print(" ")

# filter all records starting from the 2nd row, access every 5th row from world alcohol consumption dataset
f15 = wa.iloc[1::5]
print(f15)


# In[ ]:




