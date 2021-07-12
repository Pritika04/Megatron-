#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix


# In[3]:


iris = pd.read_csv("iris.csv")
print(iris.head())


# In[7]:


# Classifying input and output column names 
ip_columns = ["Sepal.Length","Sepal.Width","Petal.Length","Petal.Width"]
op_column  = ["Species"]
print(ip_columns, op_column)


# In[25]:


# Splitting data into train and test
Xtrain,Xtest,ytrain,ytest = train_test_split(iris[ip_columns],iris[op_column],test_size=0.3, random_state=0)


# In[26]:


# Initialising algorithms for Naive Bayes 
ignb = GaussianNB()
imnb = MultinomialNB()


# In[27]:


# Building and predicting at the same time 
pred_gnb = ignb.fit(Xtrain,ytrain).predict(Xtest)
pred_mnb = imnb.fit(Xtrain,ytrain).predict(Xtest)


# In[29]:


# Confusion matrix GaussianNB model
confusion_matrix(ytest,pred_gnb) # GaussianNB model


# In[30]:


pd.crosstab(ytest.values.flatten(),pred_gnb) # confusion matrix 


# In[31]:


np.mean(pred_gnb==ytest.values.flatten()) # 100%


# In[32]:


# Confusion matrix MultinomialNB model
confusion_matrix(ytest,pred_mnb) # MultinomialNB model


# In[34]:


pd.crosstab(ytest.values.flatten(),pred_mnb) # confusion matrix 


# In[35]:


np.mean(pred_mnb==ytest.values.flatten()) # 60%


# In[ ]:




