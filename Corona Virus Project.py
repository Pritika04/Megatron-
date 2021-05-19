#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
import numpy as np
import os 
import urllib
import matplotlib.pyplot as plt

path = "C:"
url = "https://covid19.who.int/WHO-COVID-19-global-data.csv"
file_path = os.path.join(path, "\Python_P","covid")

os.makedirs(file_path, exist_ok=True)
csv_path = os.path.join(file_path,"who-covid-19-global-data.csv")
urllib.request.urlretrieve(url,csv_path)

df_org = pd.read_csv(csv_path)
df = df_org.copy()


df["Date_reported"] = pd.to_datetime(df["Date_reported"])
df["Year"] = df["Date_reported"].dt.year
df["Month"] = df["Date_reported"].dt.month
df["Month_Name"] = np.where(df.Month == 1, "January", (np.where(df.Month == 2, "February",(np.where(df.Month == 3, "March",(np.where(df.Month == 4, "April",(np.where(df.Month == 5, "May",(np.where(df.Month == 6, "June", (np.where(df.Month == 7, "July", (np.where(df.Month == 8, "August", (np.where(df.Month == 9, "September", (np.where(df.Month == 10, "October", (np.where(df.Month == 11, "November", (np.where(df.Month == 12, "December", "")))))))))))))))))))))))

df_india = df[(df["Country"].str.contains("India")) & (df["Year"] == 2021)]
df_month = df_india.groupby("Month_Name").agg({"New_cases":sum, "New_deaths":sum})

months_unique = list(df.Month_Name.unique())
df_month = df_month.reindex(months_unique,axis=0)
df_month.reset_index(level=0,inplace=True)

fig, ax = plt.subplots(figsize=(10,5))
ax.set_title("Covid-19 Cases in India in 2021", fontsize=15)
ax.set_xlabel("Months", fontsize=13)

ax.plot(df_month["Month_Name"],df_month["New_cases"],"g")
ax.tick_params(axis='y', labelcolor="green")
ax.set_yticks(np.arange(100000,7000000,step=1000000))
ax.set_ylabel("New Cases in Millions", fontsize=13)

ax2 = ax.twinx()

ax2.plot(df_month["Month_Name"],df_month["New_deaths"],"r")
ax2.tick_params(axis='y', labelcolor="red")
ax2.set_yticks(np.arange(5000,700000,step=50000))
ax2.set_ylabel("New Deaths in thousands", fontsize=13)


# In[ ]:





# In[ ]:




