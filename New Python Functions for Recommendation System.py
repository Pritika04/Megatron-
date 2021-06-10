#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import numpy as np


# In[13]:


# Load the data
df = pd.read_csv("Movie.csv")
print(df.head())


# In[14]:


# Finding out the number of unique users in the dataset
len(df.userId.unique())


# In[15]:


# Finding out the number of unique movies in the dataset 
len(df.movie.unique())


# In[16]:


# Converting each of the movie into a column with 'rating' as values and 'userId' as index
movies_df = df.pivot(index="userId", columns="movie", values="rating").reset_index(drop=True)
print(movies_df)


# In[18]:


# Converting 'movie' column into 'userId' 
movies_df.index = df.userId.unique()
print(movies_df)


# In[19]:


# Replace all 'NaN' values with a '0'
movies_df.fillna(0, inplace=True)
print(movies_df)


# In[20]:


# Importing libraries to calculate similarities between users
from sklearn.metrics import pairwise_distances
from scipy.spatial.distance import cosine, correlation


# In[21]:


# Calculating similarities between users 
user_sim = 1 - pairwise_distances(movies_df.values, metric='cosine')
print(user_sim)


# In[24]:


# Store the results in a dataframe
user_sim_df = pd.DataFrame(user_sim)


# In[26]:


# Set index and column names as userid
user_sim_df.index = df.userId.unique()
user_sim_df.columns = df.userId.unique()


# In[27]:


user_sim_df.iloc[0:5,0:5]


# In[28]:


# Converting the diagonals to '0.0' for better comparison 
np.fill_diagonal(user_sim, 0)
user_sim_df.iloc[0:5,0:5]


# In[30]:


# Finding out the most similar users 
user_sim_df.idxmax(axis=1)[0:5]


# In[ ]:




