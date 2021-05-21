#!/usr/bin/env python
# coding: utf-8

# In[32]:


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

df_top = df.groupby("Country").agg({"New_cases":sum})
df_top_ten = df_top.nlargest(5,"New_cases")

df_top_ten.reset_index(level=0,inplace=True)

plt.figure(figsize=(15,5))
explode = (0.1,0.05,0.1,0.1,0.1)
plt.pie(df_top_ten["New_cases"],explode=explode,labels=df_top_ten["Country"],autopct='%1.1f%%', wedgeprops={"edgecolor":"0", "linewidth":1.5}, textprops={"fontsize":13},counterclock=True)
plt.legend(title="Legend",loc="upper right",bbox_to_anchor=(1,0,1,1))
plt.title("Top 5 Countries Hit by Covid-19 (since 2020)");


# In[ ]:





# In[ ]:




