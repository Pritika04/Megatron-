#!/usr/bin/env python
# coding: utf-8

# # Q: Create clusters for the Airlines Dataset

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[ ]:


airlines_df = pd.read_csv("Airlines .csv")
print(airlines_df.head())


# In[ ]:


# Normalization Function 
def norm_func(x):
    y = (x-x.mean())/(x.std())
    return y


# In[ ]:


# Normalized dataframe 
df_norm = norm_func(airlines_df.iloc[:, 1:])
print(df_norm.head())


# In[ ]:


# Importing additional libraries for converting dataframe and creating dendrogram respectively
from scipy.cluster.hierarchy import linkage 
import scipy.cluster.hierarchy as sch 


# In[ ]:


# Identify the normal dataframe type
type(df_norm)


# In[ ]:


# Convert the normal dataframe into numpy format
help(linkage)
z = linkage(df_norm, method="complete", metric="euclidean")


# In[ ]:


# Creating the dendrogram 
plt.figure(figsize=(15,5))
plt.title("Hierarchical Cluster Dendrogram")
plt.xlabel("Index")
plt.ylabel("Distance")

sch.dendrogram(z, leaf_rotation=1, leaf_font_size=8.); 


# In[ ]:


help(linkage)


# In[ ]:


# Applying AgglomerativeClustering
from sklearn.cluster import AgglomerativeClustering 
h_complete = AgglomerativeClustering(n_clusters=4, linkage="complete", affinity="euclidean").fit(df_norm)


# In[ ]:


# Creating a series with the clusters
cluster_labels = pd.Series(h_complete.labels_)
print(cluster_labels)


# In[ ]:


# Creating a new column and assigning it to a new column
airlines_df["Clust"] = cluster_labels
airlines_df = airlines_df.iloc[:, [12,0,1,2,3,4,5,6,7,8,9,10,11]]
print(airlines_df)


# In[ ]:


# Getting aggregate mean for each cluster
airlines_df.iloc[:, 2:].groupby(airlines_df).mean()


# In[ ]:


# Creating a new csv with the clusters
airlines_df.to_csv("Airlines_Clusters.csv")


# In[ ]:




