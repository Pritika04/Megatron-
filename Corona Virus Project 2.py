#!/usr/bin/env python
# coding: utf-8

# In[19]:


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
df_world = df[df["Year"] == 2021]
df_india_month = df_india.groupby("Month_Name").agg({"New_cases":sum})
df_world_month = df_world.groupby("Month_Name").agg({"New_cases":sum})

months_unique = list(df.Month_Name.unique())
df_india_month = df_india_month.reindex(months_unique,axis=0)
df_india_month.reset_index(level=0,inplace=True)

months_unique2 = list(df.Month_Name.unique())
df_world_month = df_world_month.reindex(months_unique2,axis=0)
df_world_month.reset_index(level=0,inplace=True)

fig, ax = plt.subplots(figsize=(9,4))
ax.set_title("Covid-19 Cases in India vs the World (2021)", fontsize=15)
ax.set_xlabel("Months", fontsize=13)

ax.plot(df_india_month["Month_Name"],df_india_month["New_cases"],"g")
ax.tick_params(axis='y', labelcolor="green")
ax.set_yticks(np.arange(100000,7000000,step=900000))
ax.set_ylabel("New Cases in Millions in India", fontsize=13)

ax2 = ax.twinx() 

ax2.plot(df_world_month["Month_Name"],df_world_month["New_cases"],"r")
ax2.tick_params(axis='y', labelcolor="red")
ax2.set_yticks(np.arange(1000000,22000000,step=4000000))
ax2.set_ylabel("New Cases in Billions in the World", fontsize=13)


# In[17]:


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

df_india = df[(df["Country"].str.contains("India"))]

world_sum = df["New_cases"].sum()
india_sum = df_india["Cumulative_cases"].tail(1)

covid_data = [india_sum,world_sum]
covid_data_labels = ["India","World"]
covid_colors = ["yellow","orange"]
explode = (0.1,0)

plt.figure(figsize=(15,5))
plt.pie(covid_data,explode = explode, labels=covid_data_labels,colors=covid_colors, autopct='%.0f%%', wedgeprops={"edgecolor":"0", "linewidth":1.5}, textprops={"fontsize":13})
plt.legend(title="Legend",loc="upper right",bbox_to_anchor=(1,0,0.5,1))
plt.title("COVID-19 in India as a % of the World", fontsize=15)


# In[ ]:




