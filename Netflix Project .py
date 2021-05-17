#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

org_nd = pd.read_csv("Netflix_data.csv")
nd = org_nd.copy() 

# Drop all of the unnecessary columns: 
nd = nd.drop(["Profile Name","Attributes","Supplemental Video Type","Bookmark","Latest Bookmark"], axis=1)

# Convert string to datetime and timedelta type:
nd.dtypes
nd["Start Time"] = pd.to_datetime(nd["Start Time"],utc=True)

nd = nd.set_index("Start Time")
nd.index = nd.index.tz_convert("Asia/Kolkata")
nd = nd.reset_index()

nd["Duration"] = pd.to_timedelta(nd["Duration"])

# Filtering strings using substrings:
show = nd[nd["Title"].str.contains("Black Money Love", regex=False)]
show = show[show["Duration"]> "0 days 00:01:00"]

# Time spent watching the show:
show["Duration"].sum()

# When do we watch the show:
show["weekday"] = show["Start Time"].dt.weekday # what days of the week had the show been watched
show["hour"] = show["Start Time"].dt.hour # at what time had the show been watched 

show["weekday"] = pd.Categorical(show["weekday"], categories=[0,1,2,3,4,5,6], ordered=True) # To plot from Monday to Sunday
show_by_day = show["weekday"].value_counts() 
show_by_day = show_by_day.sort_index()

show["hour"] = pd.Categorical(show["hour"], categories=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23], ordered=True)
show_by_hour = show["hour"].value_counts() 
show_by_hour = show_by_hour.sort_index()

plt.figure(1)
plt.figure(figsize=(20,10))
plt.xticks(show_by_hour)

plt.subplot(211)
plt.bar(x=show_by_day.index,height=show_by_day)
plt.title("Black Money Love episodes watched by day!",fontsize=15)
plt.xlabel("Views by day, Mon to Sun")
plt.ylabel("Number of episodes watched")

#show_by_day.plot(kind='bar', figsize=(20,10), title="Black Money Love episodes watched by day!")

plt.subplot(212)
plt.bar(x=show_by_hour.index,height=show_by_hour,color="green")
plt.title("Black Money Love episodes watched by hour!",fontsize=15)
plt.xlabel("Views watched by hour, AM to PM")
plt.ylabel("Number of episodes watched")

#show_by_hour.plot.bar(figsize=(20,10), title="Black Money Love episodes watched by hour", x="24 Hours")


# In[ ]:





# In[ ]:




