#!/usr/bin/env python
# coding: utf-8

# # Q: Prepare a prediction model for the Profit of data. 

# In[46]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf 
from statsmodels.graphics.regressionplots import influence_plot 


# In[47]:


df = pd.read_csv("Startups_50.csv")
df.columns = ["RD_Spend","Administration","Marketing_Spend","State","Profit"]
print(df.head())


# In[48]:


df.isna().sum()


# In[53]:


df.drop("State", axis=1)


# # Correlation Matrix 

# In[54]:


df.corr()


# In[55]:


df.info()


# # First Model 

# In[56]:


model_1 = smf.ols("Profit~RD_Spend+Administration+Marketing_Spend", data=df).fit()


# In[57]:


model_1.params 


# In[58]:


print(model_1.tvalues, '\n', model_1.pvalues)


# In[59]:


(model_1.rsquared, model_1.rsquared_adj)


# # High Influence Points 

# In[60]:


influence_plot(model_1)


# In[61]:


df_new = df.copy()
print(df_new.head())


# In[62]:


df_new_1 = df_new.drop(df_new.index[[48,49]], axis=0).reset_index()
df_new_1 = df_new_1.drop(['index'], axis=1)
print(df_new_1.shape)


# In[63]:


model_2 = smf.ols("Profit~RD_Spend+Administration+Marketing_Spend", data=df_new_1).fit()


# In[64]:


model_2.params


# In[65]:


print(model_2.tvalues, "\n", model_2.pvalues)


# In[45]:


print(model_2.rsquared, model_2.rsquared_adj)


# In[68]:


pred = model_2.predict(df_new_1)
print(pred)


# In[76]:


plt.scatter(x=df_new_1["RD_Spend"], y=df_new_1["Profit"], color="black", label="Original Profit")
plt.plot(df_new_1["RD_Spend"], pred, color="red", label="Predicted Profit")
plt.xlabel("Money Spent on R&D", fontsize=15)
plt.ylabel("Profit", fontsize=15)
plt.title("PROFIT PREDICTION MODEL", fontsize=18)
plt.legend()


# In[ ]:




