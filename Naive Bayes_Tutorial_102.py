#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix


# In[2]:


salary = pd.read_csv("SalaryData.csv")
print(salary.head())


# In[6]:


# Dropping unnecessary columns 
salary1 = salary.drop("education", axis=1)
print(salary1)


# In[10]:


# Label Encoding 
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

salary1['workclass'] = le.fit_transform(salary1['workclass'])
salary1['maritalstatus'] = le.fit_transform(salary1['maritalstatus'])
salary1['occupation'] = le.fit_transform(salary1['occupation'])
salary1['relationship'] = le.fit_transform(salary1['relationship'])
salary1['race'] = le.fit_transform(salary1['race'])
salary1['sex'] = le.fit_transform(salary1['sex'])
salary1['native'] = le.fit_transform(salary1['native'])

print(salary1)


# In[11]:


# Classifying input and output column names 
ip_columns = ['age', 'workclass', 'educationno', 'maritalstatus', 'occupation', 'relationship', 'race', 'sex', 'capitalgain','capitalloss', 'hoursperweek', 'native']
op_columns = ["Salary"]


# In[12]:


# Splitting data into train and test
Xtrain,Xtest,ytrain,ytest = train_test_split(salary1[ip_columns],salary1[op_columns],test_size=0.3, random_state=0)


# In[13]:


# Initialising algorithms for Naive Bayes 
ignb = GaussianNB()
imnb = MultinomialNB()


# In[14]:


# Building and predicting at the same time 
pred_gnb = ignb.fit(Xtrain,ytrain).predict(Xtest)
pred_mnb = imnb.fit(Xtrain,ytrain).predict(Xtest)


# In[15]:


# Confusion matrix GaussianNB model
confusion_matrix(ytest,pred_gnb) # GaussianNB model


# In[16]:


pd.crosstab(ytest.values.flatten(),pred_gnb) # confusion matrix 


# In[23]:


np.mean(pred_gnb==ytest.values.flatten()) # Mean


# In[ ]:





# In[18]:


# Confusion matrix MultinomialNB model
confusion_matrix(ytest,pred_mnb) # MultinomialNB model


# In[19]:


pd.crosstab(ytest.values.flatten(),pred_mnb) # confusion matrix 


# In[20]:


np.mean(pred_mnb==ytest.values.flatten()) # Mean


# In[ ]:




