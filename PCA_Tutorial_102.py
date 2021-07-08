#!/usr/bin/env python
# coding: utf-8

# # PCA

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 


# In[3]:


wine = pd.read_csv("wine.csv")
print(wine.head())
print(wine.shape)


# In[4]:


from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale 


# In[5]:


# Considering only numerical data
wine_num = wine.iloc[:, 1:]
wine_num.head(5)


# In[10]:


# Normalizing the numerical data
wine_normal = scale(wine_num)

pca = PCA(n_components=3)
pca_values = pca.fit_transform(wine_normal)

print(np.mean(wine_normal))
print(np.std(wine_normal))


# In[11]:


# Creating a dataframe from the pca values
pca_values_df = pd.DataFrame(data=pca_values, columns=["PCA_1", "PCA_2", "PCA_3"])
print(pca_values_df.head())


# In[12]:


# The amount of variance that each PCA explains 
var = pca.explained_variance_ratio_
var 


# In[ ]:





# # Clustering 

# In[13]:


# Normalization function
def norm_func(x):
    y = (x-x.mean())/(x.std())
    return(y)


# In[14]:


# Normalized dataframe
df_norm = norm_func(wine.iloc[:,1:])
df_norm_pca = norm_func(pca_values_df.iloc[:,1:])


# In[15]:


# Import additional libraries for converting dataframe and creating a dendrogram respectively 
from scipy.cluster.hierarchy import linkage 
import scipy.cluster.hierarchy as sch 


# In[16]:


# Identify the type of the 'normalized dataframe'
type(df_norm)
type(df_norm_pca)


# In[17]:


# Converting the dataframe into a numpy format 
help(linkage)
z = linkage(df_norm, method="complete", metric="euclidean")
z_pca = linkage(pca_values_df, method="complete", metric="euclidean")


# In[18]:


# Creating the dendrogram for the original 'wine' dataframe
plt.figure(figsize=(15,5))
plt.title("Hierarchical Cluster Dendrogram")
plt.xlabel("Index")
plt.ylabel("Distance")

sch.dendrogram(z, leaf_rotation=0, leaf_font_size=8.,);


# In[19]:


# Creating the dendrogram for the pca values 
plt.figure(figsize=(15,5))
plt.title("Hierarchical Cluster Dendrogram")
plt.xlabel("Index")
plt.ylabel("Distance")

sch.dendrogram(z_pca, leaf_rotation=0, leaf_font_size=8.,);


# In[21]:


# Applying AgglomerativeClustering to choose 3 clusters from the dendrogram 
from sklearn.cluster import AgglomerativeClustering 
h_complete = AgglomerativeClustering(n_clusters=3, linkage="complete", affinity="euclidean").fit(df_norm)
h_complete_pca = AgglomerativeClustering(n_clusters=3, linkage="complete", affinity="euclidean").fit(pca_values_df)


# In[22]:


# Creating a series with the three clusters 
cluster_labels = pd.Series(h_complete.labels_)
print(cluster_labels)

cluster_labels_pca = pd.Series(h_complete_pca.labels_)
print(cluster_labels_pca)


# In[34]:


# Creating a new column and assigning it to a new column in the original dataframe 
wine["Clust"] = cluster_labels 
wine.head()
print(wine)


# In[35]:


# Creating a new column and assigning it to a new column in the original dataframe 
pca_values_df["Clust"] = cluster_labels_pca
pca_values_df.head()
print(pca_values_df)


# In[37]:


# Getting aggregate mean of each cluster
print(wine.iloc[:,:].groupby(wine.Clust).mean())
print(" ")
print(pca_values_df.iloc[:,:].groupby(pca_values_df.Clust).mean())


# In[38]:


# Creating a new csv file with the cluster
wine.to_csv("Wine_Clusters.csv", encoding="utf-8")
pca_values_df.to_csv("Wine_PCA_Clusters.csv", encoding="utf-8")


# In[ ]:





# In[ ]:




