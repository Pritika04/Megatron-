#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier as KNC 


# In[4]:


iris = pd.read_csv("iris.csv")
print(iris.head())


# In[8]:


# Classifying input and output column names 
ip_columns = ["Sepal.Length","Sepal.Width","Petal.Length","Petal.Width"]
op_column  = ["Species"]
print(ip_columns, op_column)


# In[9]:


# Splitting data into train and test
Xtrain,Xtest,ytrain,ytest = train_test_split(iris[ip_columns],iris[op_column],test_size=0.3, random_state=0)


# In[10]:


# for 3 nearest neighbours 
neigh = KNC(n_neighbors= 3)


# In[12]:


pred_neigh = neigh.fit(Xtrain,ytrain).predict(Xtest)


# In[15]:


np.mean(pred_neigh==ytest.values.flatten())


# In[48]:


# running KNN algorithm for 3 to 50 nearest neighbours(odd numbers) and storing the accuracy values 
train,test = train_test_split(iris,test_size = 0.2) 
acc = []
for i in range(3,50,2):
    neigh = KNC(n_neighbors=i)
    neigh.fit(train.iloc[:,0:4],train.iloc[:,4])
    train_acc = np.mean(neigh.predict(train.iloc[:,0:4])==train.iloc[:,4])
    test_acc = np.mean(neigh.predict(test.iloc[:,0:4])==test.iloc[:,4])
    acc.append([train_acc,test_acc])


# In[49]:


# train accuracy plot 
plt.plot(np.arange(3,50,2),[i[0] for i in acc],"bo-")

# test accuracy plot
plt.plot(np.arange(3,50,2),[i[1] for i in acc],"ro-")

plt.legend(["train","test"])

plt.xlabel("Number of Neighbors")
plt.ylabel("Accuracy");


# In[ ]:




