#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import numpy as np

left = pd.DataFrame({"key":["foo1","foo2","bar1"], "lval":[1,2,3], "fruits":["apple","banana","watermelon"]}, index=["A","B","C"])
right = pd.DataFrame({"key":["foo1","foo2","bar2"], "rval":[3,4,5], "vegetables":["cabbage","potato","carrot"]}, index=["A","B","C"])

print(pd.merge(left,right,on="key",indicator=True))

print(" ")

print(pd.merge(left,right,on="key", how='inner',indicator=True))

print(" ")

print(pd.merge(left,right,on="key", how='outer',indicator=True))

print(" ")

print(pd.merge(left,right,on="key", how='left',indicator=True))

print(" ")

print(pd.merge(left,right,on="key", how='right',indicator=True))


# In[37]:


import pandas as pd
import numpy as np

student_data1 = pd.DataFrame({"student_id":["S1","S2","S3","S4","S5"], "Name":["Danniella Fenton","Ryder Storey","Bryce Jensen","Ed Bernal","Kwame Morin"], "Marks":[200,210,190,222,199]})
student_data2 = pd.DataFrame({"student_id":["S4","S5","S6","S7","S8"], "Name":["Scarlette Fisher","Carla Williamson","Dante Morse","Kaiser William","Madeeha Preston"], "Marks":[201,200,198,219,201]})
exam_data = pd.DataFrame({"student_id":["S1","S2","S3","S4","S5","S6","S7","S8","S9","S10","S11","S12","S13"],"exam_id":[23,45,12,67,21,55,70,33,14,56,83,88,12]})

# join the two given dataframes along rows and assign all data.
print(pd.concat([student_data1,student_data2]))

print(" ")

# join the two given dataframes along columns and assign all data.
print(pd.concat([student_data1,student_data2], axis=1))

print(" ")

# join the two given dataframes along rows and merge with another dataframe along the common column id.
result = pd.concat([student_data1,student_data2])
print(pd.merge(result,exam_data,on="student_id"))

print(" ")

# join the two dataframes using the common column of both dataframes.
print(pd.merge(student_data1,student_data2,on="student_id"))

print(" ")

# join (left join) the two dataframes using keys from left dataframe only
print(pd.merge(student_data1,student_data2,on="student_id",how="left"))

print(" ")

# join two dataframes using keys from right dataframe only
print(pd.merge(student_data1,student_data2,on="student_id",how="right"))

print(" ")

# merge two given datasets using multiple join keys
print(pd.merge(student_data1,student_data2,on=["student_id","Marks"]))


# In[ ]:




