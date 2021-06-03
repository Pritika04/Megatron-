#!/usr/bin/env python
# coding: utf-8

# # Q: FACTORS THAT INFLUENCE WHETHER OR NOT THE POLITICAL CANDIDATE WINS THE ELECTION

# In[74]:


import pandas as pd
from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import confusion_matrix 
from sklearn.metrics import classification_report 
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score 
import matplotlib.pyplot as plt 


# In[75]:


# Load the data
df = pd.read_csv("election_data.csv")
print(df)


# In[76]:


# Dropping un-related columns 
df.drop(["Election-id"], inplace=True, axis=1)


# In[77]:


# Shape of the dataframe 
df.shape


# In[78]:


# Removing any NA values from the dataframe
df = df.dropna()
df.shape


# In[79]:


# Dividing the data into an input and output variable 
X = df.iloc[:, 1:]
Y = df.iloc[:, 0]


# In[80]:


# Logistic regression and fit the model
classifier = LogisticRegression()
classifier.fit(X,Y)


# In[81]:


# Predict for x dataset 
y_pred = classifier.predict(X)


# In[82]:


y_pred_df = pd.DataFrame({"Actual":Y, "Predicted":y_pred})


# In[83]:


print(y_pred_df)


# In[84]:


# Build the confusion matrix
confusion_matrix = confusion_matrix(Y, y_pred)
print(confusion_matrix )


# In[85]:


# Calculation model's accuracy 
((3+6)/(3+1+6))*100


# In[86]:


# Classification report
print(classification_report(Y, y_pred))


# In[95]:


# ROC CURVE
fpr, tpr, thresholds = roc_curve(Y, classifier.predict_proba(X)[:,1])
auc = roc_auc_score(Y, y_pred)

plt.plot(fpr, tpr, color="red", label="logit model (area=%0.2f)" %auc)
plt.plot([0,1], [0,1], "k--")
plt.xlabel("False Positive Rate or [1 - True Negative Rate]")
plt.ylabel("True Positive Rate")


# In[96]:


auc 


# In[ ]:





# In[ ]:




