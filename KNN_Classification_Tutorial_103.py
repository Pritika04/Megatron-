#!/usr/bin/env python
# coding: utf-8

# # Use a KNN Model to predict the accuracy for the type of glass in the dataset

# In[5]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier as KNC 


# In[6]:


# Import the data
glass = pd.read_csv("Glass.csv")
print(glass.head())


# In[19]:


# Splitting the data into training and test data
train, test = train_test_split(glass, test_size=0.25)


# In[20]:


# Setting the number of neighbours
neigh = KNC(n_neighbors=3)


# In[21]:


# Building the algorithm 
neigh.fit(train.iloc[:,0:9], train.iloc[:,9])


# In[22]:


# Train accuracy 
train_acc = np.mean(neigh.predict(train.iloc[:,0:9])==train.iloc[:,9])
print(train_acc)


# In[23]:


# Test accuracy 
test_acc = np.mean(neigh.predict(train.iloc[:,0:9])==train.iloc[:,9])
print(test_acc)


# In[31]:


# Running the KNN algorithm for 3 to 50 nearest neighbours to find out the most accurate values
acc =[]

for i in range(3,50,3):
    neigh = KNC(n_neighbors=i)
    neigh.fit(train.iloc[:,0:9], train.iloc[:,9])
    train_acc = np.mean(neigh.predict(train.iloc[:,0:9])==train.iloc[:,9])
    test_acc = np.mean(neigh.predict(test.iloc[:,0:9])==test.iloc[:,9])
    acc.append([train_acc, test_acc])


# In[32]:


# Plotting an accuracy graph for visualization
x = np.arange(3,50,3)
plt.plot(x,[i[0] for i in acc],"go-")
plt.plot(x,[i[1] for i in acc],"yo-")

plt.legend(["train", "test"])
plt.xlabel("Number of Neighbors")
plt.ylabel("Accuracy")
plt.title("KNN Classification - Train and Test data Accuracy");


# In[ ]:





# In[ ]:




