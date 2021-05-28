#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf 
from statsmodels.graphics.regressionplots import influence_plot


# In[3]:


# Reading the data
cars = pd.read_csv("Cars (2) (5).csv")
print(cars.head())


# In[4]:


cars.info()


# In[5]:


# Checking for missing values 
cars.isna().sum()


# In[6]:


# Correlation matrix 
cars.corr()


# In[7]:


# Scatterplot between variables along with histograms 
pd.plotting.scatter_matrix(cars, figsize=(20,15));


# # PREPARING A MODEL 

# In[9]:


# Building the model 
model = smf.ols("MPG~WT+VOL+SP+HP", data=cars).fit()


# In[10]:


# Coefficients 
model.params 


# In[11]:


# t and p-Values
print(model.tvalues, '\n', model.pvalues)


# In[13]:


# R-squared values 
(model.rsquared, model.rsquared_adj)


# # SIMPLE LINEAR REGRESSION MODELS

# In[14]:


ml_v = smf.ols("MPG~VOL", data=cars).fit()
print(ml_v.tvalues, ml_v.pvalues)


# In[15]:


ml_W = smf.ols("MPG~WT", data=cars).fit()
print(ml_W.tvalues, ml_W.pvalues)


# In[16]:


ml_wv = smf.ols("MPG~WT+VOL", data=cars).fit()
print(ml_wv.tvalues, ml_wv.pvalues)


# In[26]:


rsq_hp = smf.ols("HP~WT+VOL+SP", data=cars).fit().rsquared
vif_hp = 1/(1-rsq_hp)

rsq_wt = smf.ols("WT~HP+VOL+SP", data=cars).fit().rsquared
vif_wt = 1/(1-rsq_wt)

rsq_v = smf.ols("VOL~HP+WT+SP", data=cars).fit().rsquared
vif_v = 1/(1-rsq_v)

rsq_sp = smf.ols("SP~HP+WT+VOL", data=cars).fit().rsquared
vif_sp = 1/(1-rsq_sp)

# Storing VIF values in a dataframe
d1 = {"Variables":["HP","WT","VOL","SP"], "VIF":[vif_hp,vif_wt,vif_v,vif_sp]}
vid_df = pd.DataFrame(d1)
print(vid_df)


# # HIGH INFLUENCE POINTS 

# In[30]:


influence_plot(model)


# # From the above plot, it is evident that the outliers/influencers are 70 and 76

# In[32]:


cars[cars.index.isin([70,76])]


# In[33]:


# See the differences in all the other variables
print(cars.head())


# # IMPROVING THE MODEL

# In[34]:


# Load the data
cars_new = pd.read_csv("Cars (2) (5).csv")
print(cars.head())


# In[43]:


# Discard the data points which are influencers and reasign the row number (reset_index())
car1 = cars_new.drop(cars_new.index[[70,76]], axis=0).reset_index()


# In[36]:


# Drop the original index
car1 = car1.drop(["index"], axis=1)


# In[37]:


print(car1)


# # BUILD MODEL 

# In[40]:


# Exclude variable "WT" and generate R-Squared and AIC values
final_ml_v = smf.ols("MPG~VOL+HP+SP", data=car1).fit()
(final_ml_v.rsquared, final_ml_v.aic)


# In[42]:


# Exclude variable "VOL" and generate R-Squared and AIC values
final_ml_WT = smf.ols("MPG~WT+HP+SP", data=car1).fit()
(final_ml_WT.rsquared, final_ml_WT.aic)


# # Since final_ml_v gives a higher r-squared value, we will use final_ml_v for our predictions 

# # PREDICTIONS

# In[44]:


# New data for prediction: 
new_df = pd.DataFrame({'HP':40,"VOL":95,"SP":102,"WT":35}, index=[1])


# In[52]:


# OLD MODEL PREDICTION - 
model.predict(new_df)


# In[53]:


model.predict(cars.iloc[0:5,])


# In[54]:


model.predict(cars)


# In[55]:


# NEW MODEL PREDICTION - 
final_ml_v.predict(new_df) 


# In[56]:


final_ml_v.predict(cars_new.iloc[0:5,])


# In[61]:


final_ml_v.predict(cars_new) 


# In[ ]:




