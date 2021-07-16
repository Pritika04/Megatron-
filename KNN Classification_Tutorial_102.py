#!/usr/bin/env python
# coding: utf-8

# # Use a KNN Model to predict the accuracy for the type of animal in the dataset

# In[2]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier as KNC 


# In[3]:


# Import the data
zoo = pd.read_csv("Zoo.csv")
print(zoo.head())


# In[5]:


# Dropping unnecessary columns 
zoo_new = zoo.drop("animal name", axis=1)
print(zoo_new)


# In[15]:


# Splitting the data into training and test data
train, test = train_test_split(zoo_new, test_size=0.2)


# In[29]:


# Setting the number of neighbours
neigh = KNC(n_neighbors=3)


# In[30]:


# Building the algorithm 
neigh.fit(train.iloc[:,0:16], train.iloc[:,16])


# In[31]:


# Train accuracy 
train_acc = np.mean(neigh.predict(train.iloc[:,0:16])==train.iloc[:,16])
print(train_acc)


# In[32]:


# Test accuracy 
test_acc = np.mean(neigh.predict(test.iloc[:,0:16])==test.iloc[:,16])
print(test_acc)


# In[56]:


# Running the KNN algorithm for 3 to 50 nearest neighbours to find out the most accurate values
acc =[]

for i in range(3,50,6):
    neigh = KNC(n_neighbors=i)
    neigh.fit(train.iloc[:,0:16], train.iloc[:,16])
    train_acc = np.mean(neigh.predict(train.iloc[:,0:16])==train.iloc[:,16])
    test_acc = np.mean(neigh.predict(test.iloc[:,0:16])==test.iloc[:,16])
    acc.append([train_acc, test_acc])


# In[59]:


# Plotting an accuracy graph for visualization
x = np.arange(3,50,6)
plt.plot(x,[i[0] for i in acc],"bo-")
plt.plot(x,[i[1] for i in acc],"ro-")

plt.legend(["train", "test"])
plt.xlabel("Number of Neighbors")
plt.ylabel("Accuracy")
plt.title("KNN Classification - Train and Test data Accuracy");


# In[ ]:




