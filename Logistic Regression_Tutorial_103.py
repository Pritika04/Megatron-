#!/usr/bin/env python
# coding: utf-8

# # Q: Predicting whether or not the client has subscribed to a term deposit

# In[130]:


import pandas as pd
from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import confusion_matrix 
from sklearn.metrics import classification_report 
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import LabelEncoder 
import matplotlib.pyplot as plt 


# In[131]:


# Load the data
df = pd.read_csv("bank_data_final.csv")
print(df.head())


# In[132]:


# Shifting and inserting 'y' column to the first position 
first_col = df.pop("y")
df.insert(0, "y", first_col)
print(df)


# In[133]:


# Converting values in columns to categorical data 
df = pd.get_dummies(df, prefix = ["Job"], columns = ["job"])
df = pd.get_dummies(df, prefix = ["Marital"], columns = ["marital"])
df = pd.get_dummies(df, prefix = ["Edu"], columns = ["education"])
df = pd.get_dummies(df, prefix = ["Con"], columns = ["contact"])
df = pd.get_dummies(df, prefix = ["Mon"], columns = ["month"])
df = pd.get_dummies(df, prefix = ["Pot"], columns = ["poutcome"])
df = pd.get_dummies(df, prefix = ["def"], columns = ["default"])
df = pd.get_dummies(df, prefix = ["house"], columns = ["housing"])
df = pd.get_dummies(df, prefix = ["loan"], columns = ["loan"])

le = LabelEncoder()
df.y = le.fit_transform(df.y)
print(df)


# In[134]:


# Shape of the dataframe 
df.shape


# In[135]:


# Dividing data into input and output variable
X = df.iloc[:, 1:]
Y = df.iloc[:, 0]


# In[136]:


# Logistic Regression and fit the model 
classifier = LogisticRegression()
classifier.fit(X,Y)


# In[137]:


# Predict for x dataset
y_pred = classifier.predict(X)


# In[138]:


y_pred_df = pd.DataFrame({"Actual":Y, "Predicted":y_pred})


# In[139]:


# Converting string values to categorical values using label encoder
cols = ["Actual", "Predicted"]
y_pred_df[cols] = y_pred_df[cols].apply(LabelEncoder().fit_transform)


# In[140]:


print(y_pred_df)


# In[141]:


# Build the confusion matrix
confusion_matrix = confusion_matrix(Y, y_pred)
print(confusion_matrix)


# In[142]:


# Calculation the model's accuracy
((39140+1181)/(39140+782+4108+1181))*100


# In[143]:


# Classification Report
print(classification_report(Y, y_pred))


# In[144]:


# ROC Curve 
fpr, tpr, thresholds = roc_curve(Y, classifier.predict_proba(X)[:,1])
auc = roc_auc_score(Y, y_pred)

plt.plot(fpr, tpr, color="red", label="logit model (area=%0.2f)" %auc)
plt.plot([0,1], [0,1], "k--")
plt.xlabel("False Positive Rate or [1 - True Negative Rate]")
plt.ylabel("True Negative Rate")


# In[145]:


auc


# In[ ]:




