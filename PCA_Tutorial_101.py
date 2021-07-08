#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[58]:


uni = pd.read_csv("Universities_PCA.csv")
print(uni.shape)
print(uni.describe())
print(" ")
print(uni.head())


# In[18]:


from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale 


# In[19]:


# Considering only numerical data
uni_1 = uni.iloc[:,1:]
uni_1.head(4)


# In[49]:


# Normalizing the numerical data
uni_normal = scale(uni_1)

pca = PCA(n_components = 2)
pca_values = pca.fit_transform(uni_normal)

print(np.mean(uni_normal))
print(np.std(uni_normal))


# In[50]:


# Creating a dataframe from the pca_values 
pca_values_df = pd.DataFrame(data = pca_values, columns=["PCA_1", "PCA_2"])
print(pca_values_df.head())


# In[54]:


# The amount of variance that each PCA explains 
var = pca.explained_variance_ratio_
var


# In[60]:


# plot between PCA1 and PCA2 
x = pca_values[:,0]
y = pca_values[:,1]
print(x)
#z = pca_values[:2:3]
plt.scatter(x,y,color=["red"])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




