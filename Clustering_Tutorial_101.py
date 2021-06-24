#!/usr/bin/env python
# coding: utf-8

# # Q: Create clusters for the University dataset. 

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


uni = pd.read_csv("Universities.csv")
print(uni.head())


# In[3]:


# Normalization function
def norm_func(x):
    y = (x-x.mean())/(x.std())
    return(y)


# In[4]:


# Normalized dataframe
df_norm = norm_func(uni.iloc[:,1:])


# In[5]:


# Import additional libraries for converting dataframe and creating a dendrogram respectively 
from scipy.cluster.hierarchy import linkage 
import scipy.cluster.hierarchy as sch 


# In[6]:


# Identify the type of the 'normalized dataframe'
type(df_norm)


# In[7]:


# Converting the dataframe into a numpy format 
help(linkage)
z = linkage(df_norm, method="complete", metric="euclidean")


# In[8]:


# Creating the dendrogram 
plt.figure(figsize=(15,5))
plt.title("Hierarchical Cluster Dendrogram")
plt.xlabel("Index")
plt.ylabel("Distance")

sch.dendrogram(z, leaf_rotation=0, leaf_font_size=8.,);


# In[9]:


help(linkage)


# In[10]:


# Applying AgglomerativeClustering to choose 3 clusters from the dendrogram 
from sklearn.cluster import AgglomerativeClustering 
h_complete = AgglomerativeClustering(n_clusters=3, linkage="complete", affinity="euclidean").fit(df_norm)


# In[17]:


# Creating a series with the three clusters 
cluster_labels = pd.Series(h_complete.labels_)
print(cluster_labels)


# In[26]:


# Creating a new column and assigning it to a new column
uni["Clust"] = cluster_labels 
uni = uni.iloc[:,[7,0,1,2,3,4,5,6]]
uni.head()
print(uni)


# In[28]:


# Getting aggregate mean of each cluster
uni.iloc[:,2:].groupby(uni.Clust).mean()


# In[29]:


# Creating a new csv file with the cluster
uni.to_csv("University_Clusters.csv", encoding="utf-8")


# In[ ]:




