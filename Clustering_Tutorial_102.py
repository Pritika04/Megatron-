#!/usr/bin/env python
# coding: utf-8

# # Q: Create clusters for the Crime Dataset  

# In[20]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[21]:


df = pd.read_csv("crime_data.csv")
crime_df = df.rename(columns = {"Unnamed: 0" : "Country"})
print(crime_df.head())


# In[22]:


# Normalization function:
def norm_func(x):
    y = (x-x.mean())/(x.std())
    return(y)


# In[23]:


# Normalized dataframe
df_norm = norm_func(crime_df.iloc[:,1:])
print(df_norm.head())


# In[24]:


# Importing additional libraries for converting dataframe and creating dendrogram respectively
from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch


# In[25]:


# Identify the normal dataframe type
type(df_norm)


# In[26]:


# Converting the dataframe into numpy format
help(linkage)
z = linkage(df_norm, method="complete", metric="euclidean")


# In[30]:


# Creating the dendrogram
plt.figure(figsize=(15,5))
plt.title("Hierarchical Cluster Dendrogram")
plt.xlabel("Index")
plt.ylabel("Distance")

sch.dendrogram(z, leaf_rotation=1, leaf_font_size=8.);


# In[31]:


help(linkage)


# In[38]:


# Applying Agglomerative Clustering
from sklearn.cluster import AgglomerativeClustering 
h_complete = AgglomerativeClustering(n_clusters=4, linkage="complete", affinity="euclidean").fit(df_norm )


# In[39]:


# Creating a series with the clusters
cluster_labels = pd.Series(h_complete.labels_)
print(cluster_labels)


# In[45]:


# Creating a new column and assigning it to a new column 
crime_df["Clust"] = cluster_labels
crime_df = crime_df.iloc[:, [5,0,1,2,3,4]]
print(crime_df.head())


# In[46]:


# Getting aggregate mean for each cluster
crime_df.iloc[:, 2:].groupby(crime_df.Clust).mean()


# In[47]:


# Creating a new csv with the cluster
crime_df.to_csv("Crime_data_cluster.csv", encoding="utf-8")


# In[ ]:




