#!/usr/bin/env python
# coding: utf-8

# # Q: Creating a decision tree for the iris dataset

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder#for train test splitting
from sklearn.model_selection import train_test_split#for decision tree object
from sklearn.tree import DecisionTreeClassifier#for checking testing results
from sklearn.metrics import classification_report, confusion_matrix#for visualizing tree 
from sklearn.tree import plot_tree


# In[2]:


# Load the data
iris = pd.read_csv("iris.csv")
print(iris.head())


# In[3]:


iris.shape


# In[7]:


iris.isnull().any()


# In[8]:


output_target = iris["Species"]
iris_new = iris.copy()
iris_new = iris_new.drop("Species", axis=1)
print(iris_new.head())


# In[9]:


x = iris_new


# In[12]:


le = LabelEncoder()
output_target = le.fit_transform(output_target)
output_target


# In[14]:


y = output_target


# In[18]:


X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)
print("Training split input = ", X_train.shape)
print("Testing split input = ", X_test.shape)


# In[29]:


# Defining the decision tree algorithm
dtree = DecisionTreeClassifier(criterion = "gini", max_depth=3)
dtree.fit(X_train, y_train)
print("Decision Tree Classifier Created")


# In[30]:


# Predicting the values of the test data
y_pred = dtree.predict(X_test)
print("Classification Report - \n", classification_report(y_test, y_pred))


# In[31]:


print(confusion_matrix(y_test, y_pred))


# In[34]:


# Visualising the decision tree
plt.figure(figsize = (10,10))
dec_tree = plot_tree(decision_tree = dtree, feature_names = iris_new.columns, class_names = ["setosa", "vercicolor", "verginica"], filled = True, precision = 4, rounded = True)


# In[ ]:




