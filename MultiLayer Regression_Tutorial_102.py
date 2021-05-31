#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.graphics.regressionplots import influence_plot
import statsmodels.formula.api as smf
import numpy as np


# In[2]:


#Read the data
cars = pd.read_csv("../input/cars12345/Cars (2).csv")
cars.head()


# In[3]:


cars.info()


# In[4]:


#check for missing values
cars.isna().sum()


# # Correlation Matrix

# In[5]:


cars.corr()


# # Scatterplot between variables along with histograms

# In[6]:


#Format the plot background and scatter plots for all the variables
sns.set_style(style='darkgrid')
sns.pairplot(cars)


# # Preparing a model

# In[7]:


#Build model
import statsmodels.formula.api as smf 
model = smf.ols('MPG~WT+VOL+SP+HP',data=cars).fit()


# In[8]:


#Coefficients
model.params


# In[9]:


#t and p-Values
print(model.tvalues, '\n', model.pvalues)


# In[10]:


#R squared values
(model.rsquared,model.rsquared_adj)


# # Simple Linear Regression Models

# In[11]:


ml_v=smf.ols('MPG~VOL',data = cars).fit()  
#t and p-Values
print(ml_v.tvalues, '\n', ml_v.pvalues)  


# In[12]:


ml_w=smf.ols('MPG~WT',data = cars).fit()  
print(ml_w.tvalues, '\n', ml_w.pvalues)  


# In[13]:


ml_wv=smf.ols('MPG~WT+VOL',data = cars).fit()  
print(ml_wv.tvalues, '\n', ml_wv.pvalues)  


# # Calculating VIF

# In[14]:


rsq_hp = smf.ols('HP~WT+VOL+SP',data=cars).fit().rsquared  
vif_hp = 1/(1-rsq_hp) # 16.33

rsq_wt = smf.ols('WT~HP+VOL+SP',data=cars).fit().rsquared  
vif_wt = 1/(1-rsq_wt) # 564.98

rsq_vol = smf.ols('VOL~WT+SP+HP',data=cars).fit().rsquared  
vif_vol = 1/(1-rsq_vol) #  564.84

rsq_sp = smf.ols('SP~WT+VOL+HP',data=cars).fit().rsquared  
vif_sp = 1/(1-rsq_sp) #  16.35

# Storing vif values in a data frame
d1 = {'Variables':['Hp','WT','VOL','SP'],'VIF':[vif_hp,vif_wt,vif_vol,vif_sp]}
Vif_frame = pd.DataFrame(d1)  
Vif_frame


# # Residual Analysis

# ## Test for Normality of Residuals (Q-Q Plot)

# In[15]:


import statsmodels.api as sm
qqplot=sm.qqplot(model.resid,line='q') # line = 45 to draw the diagnoal line
plt.title("Normal Q-Q plot of residuals")
plt.show()


# In[16]:


list(np.where(model.resid>10))


# ## Residual Plot for Homoscedasticity

# In[17]:


def get_standardized_values( vals ):
    return (vals - vals.mean())/vals.std()


# In[18]:


plt.scatter(get_standardized_values(model.fittedvalues),
            get_standardized_values(model.resid))

plt.title('Residual Plot')
plt.xlabel('Standardized Fitted values')
plt.ylabel('Standardized residual values')
plt.show()


# ## Residual Vs Regressors

# In[19]:


fig = plt.figure(figsize=(15,8))
fig = sm.graphics.plot_regress_exog(model, "VOL", fig=fig)
plt.show()


# In[20]:


fig = plt.figure(figsize=(15,8))
fig = sm.graphics.plot_regress_exog(model, "SP", fig=fig)
plt.show()


# In[21]:


fig = plt.figure(figsize=(15,8))
fig = sm.graphics.plot_regress_exog(model, "HP", fig=fig)
plt.show()


# In[22]:


fig = plt.figure(figsize=(15,8))
fig = sm.graphics.plot_regress_exog(model, "WT", fig=fig)
plt.show()


# # Model Deletion Diagnostics

# ## Detecting Influencers/Outliers

# ## Cook’s Distance

# In[23]:


model_influence = model.get_influence()
(c, _) = model_influence.cooks_distance


# In[24]:


#Plot the influencers values using stem plot
fig = plt.subplots(figsize=(20, 7))
plt.stem(np.arange(len(cars)), np.round(c, 3))
plt.xlabel('Row index')
plt.ylabel('Cooks Distance')
plt.show()


# In[25]:


#index and value of influencer where c is more than .5
(np.argmax(c),np.max(c))


# ## High Influence points

# In[26]:


from statsmodels.graphics.regressionplots import influence_plot
influence_plot(model)
plt.show()


# In[27]:


k = cars.shape[1]
n = cars.shape[0]
leverage_cutoff = 3*((k + 1)/n)


# #### From the above plot, it is evident that data point 70 and 76 are the influencers

# In[28]:


cars[cars.index.isin([70, 76])]


# In[29]:


#See the differences in HP and other variable values
cars.head()


# # Improving the model

# In[30]:


#Load the data
cars_new = pd.read_csv("../input/cars12345/Cars (2).csv")


# In[31]:


#Discard the data points which are influencers and reasign the row number (reset_index())
car1=cars_new.drop(cars_new.index[[70,76]],axis=0).reset_index()


# In[32]:


#Drop the original index
car1=car1.drop(['index'],axis=1)


# In[33]:


car1


# # Build Model

# In[34]:


#Exclude variable "WT" and generate R-Squared and AIC values
final_ml_V= smf.ols('MPG~VOL+SP+HP',data = car1).fit()


# In[35]:


(final_ml_V.rsquared,final_ml_V.aic)


# In[36]:


#Exclude variable "VOL" and generate R-Squared and AIC values
final_ml_W= smf.ols('MPG~WT+SP+HP',data = car1).fit()


# In[37]:


(final_ml_W.rsquared,final_ml_W.aic)


# ##### Comparing above R-Square and AIC values, model 'final_ml_V' has high R- square and low AIC value hence include variable 'VOL' so that multi collinearity problem would be resolved.

# # Cook’s Distance

# In[38]:


model_influence_V = final_ml_V.get_influence()
(c_V, _) = model_influence_V.cooks_distance


# In[39]:


fig= plt.subplots(figsize=(20,7))
plt.stem(np.arange(len(car1)),np.round(c_V,3));
plt.xlabel('Row index')
plt.ylabel('Cooks Distance');


# In[40]:


#index of the data points where c is more than .5
(np.argmax(c_V),np.max(c_V))


# In[41]:


#Drop 76 and 77 observations
car2=car1.drop(car1.index[[76,77]],axis=0)


# In[42]:


car2


# In[43]:


#Reset the index and re arrange the row values
car3=car2.reset_index()


# In[44]:


car4=car3.drop(['index'],axis=1)


# In[45]:


car4


# In[46]:


#Build the model on the new data
final_ml_V= smf.ols('MPG~VOL+SP+HP',data = car4).fit()


# In[47]:


#Again check for influencers
model_influence_V = final_ml_V.get_influence()
(c_V, _) = model_influence_V.cooks_distance


# In[48]:


fig= plt.subplots(figsize=(20,7))
plt.stem(np.arange(len(car4)),np.round(c_V,3));
plt.xlabel('Row index')
plt.ylabel('Cooks Distance');


# In[49]:


#index of the data points where c is more than .5
(np.argmax(c_V),np.max(c_V))


# #### Since the value is <1 , we can stop the diagnostic process and finalize the model

# In[50]:


#Check the accuracy of the mode
final_ml_V= smf.ols('MPG~VOL+SP+HP',data = car4).fit()


# In[51]:


(final_ml_V.rsquared,final_ml_V.aic)


# ## Predicting for new data

# In[52]:


#New data for prediction
new_data=pd.DataFrame({'HP':40,"VOL":95,"SP":102,"WT":35},index=[1])


# In[53]:


final_ml_V.predict(new_data)


# In[54]:


final_ml_V.predict(cars_new.iloc[0:5,])


# In[55]:


pred_y = final_ml_V.predict(cars_new)


# In[56]:


pred_y

