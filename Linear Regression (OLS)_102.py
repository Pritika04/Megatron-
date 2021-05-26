#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Q1: Predict delivery time using sorting time

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("delivery_time.csv")
df.columns = ["Delivery_Time","Sorting_Time"]

plt.plot(df["Sorting_Time"], df["Delivery_Time"], "bo")
plt.xlabel("SORTING TIME")
plt.ylabel("DELIVERY TIME")

df.corr()

import statsmodels.formula.api as smf 
model = smf.ols("Delivery_Time~Sorting_Time", data=df).fit()

pred = model.predict(df.iloc[:,1])

plt.plot(df["Sorting_Time"], pred, color="black");


# In[6]:


# Q1: Predict delivery time using sorting time - improving accuracy this time

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("delivery_time.csv")
df.columns = ["Delivery_Time","Sorting_Time"]

plt.plot(df["Sorting_Time"], df["Delivery_Time"], "bo")
plt.xlabel("SORTING TIME")
plt.ylabel("DELIVERY TIME")

df.corr()

import statsmodels.formula.api as smf 
model2 = smf.ols("Delivery_Time~np.log(Sorting_Time)", data=df).fit()

model2.params
model2.summary()

pred2 = model2.predict(df.iloc[:,1])

plt.plot(df["Sorting_Time"], pred2, color="green");


# In[4]:


# Q2: Predict the salary based on experience

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Salary_Data.csv")

plt.plot(df["YearsExperience"],df["Salary"], "ro")
plt.xlabel("YEARS OF EXPERIENCE -->")
plt.ylabel("SALARY -->")

df.corr()

import statsmodels.formula.api as smf 
model = smf.ols("Salary~YearsExperience", data=df).fit()

model.params
model.summary()

pred = model.predict(df.iloc[:,0])

plt.plot(df["YearsExperience"],pred,color="black");


# In[3]:


# Q2: Predict the salary based on experience (now, with a different data set)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Salary_Data.csv")

plt.plot(df["YearsExperience"],df["Salary"], "ro")
plt.xlabel("YEARS OF EXPERIENCE -->")
plt.ylabel("SALARY -->")

df.corr()

import statsmodels.formula.api as smf 
model = smf.ols("Salary~YearsExperience", data=df).fit()

model.params
model.summary()

series_1 = pd.Series([2,3,5,10,15,20])
df = pd.DataFrame(series_1,columns=["YearsExperience"])

pred = model.predict(df)

plt.plot(df["YearsExperience"],pred,color="black");


# In[ ]:





# In[ ]:




