#!/usr/bin/env python
# coding: utf-8

# In[16]:


# For reading data set
# importing necessary libraries
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


# reading a csv file using pandas library
wcat=pd.read_csv("wc-at.csv")
print(wcat.head(5))

#plt.hist(wcat.Waist)
#plt.boxplot(wcat.Waist,0,"rs",0)


#plt.hist(wcat.AT)
#plt.boxplot(wcat.AT)

#plt.plot(wcat.Waist,wcat.AT,"bo");plt.xlabel("Waist");plt.ylabel("AT")

wcat.corr()
#wcat.AT.corr(wcat.Waist) # # correlation value between X and Y
#np.corrcoef(wcat.AT,wcat.Waist)

# For preparing linear regression model we need to import the statsmodels.formula.api
import statsmodels.formula.api as smf
model=smf.ols("AT~Waist",data=wcat).fit()

# For getting coefficients of the varibles used in equation
model.params

# P-values for the variables and R-squared value for prepared model
model.summary()

model.conf_int(0.05)


pred = model.predict(wcat.iloc[:,0]) # Predicted values of AT using the model
print(pred)

# Visualization of regresion line over the scatter plot of Waist and AT
# For visualization we need to import matplotlib.pyplot
import matplotlib.pylab as plt
plt.scatter(x=wcat['Waist'],y=wcat['AT'],color='red');plt.plot(wcat['Waist'],pred,color='black');plt.xlabel('WAIST');plt.ylabel('TISSUE')


# In[15]:


# Transforming variables for accuracy
model2 = smf.ols('AT~np.log(Waist)',data=wcat).fit()
model2.params
model2.summary()
#print(model2.conf_int(0.01)) # 99% confidence level
#pred2 = model2.predict(pd.DataFrame(wcat['Waist']))
#pred2.corr(wcat.AT)
# pred2 = model2.predict(wcat.iloc[:,0])
#pred2
#plt.scatter(x=wcat['Waist'],y=wcat['AT'],color='green');plt.plot(wcat['Waist'],pred2,color='blue');plt.xlabel('WAIST');plt.ylabel('TISSUE')


# In[35]:


# For reading data set
# importing necessary libraries
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

nwd = pd.read_csv("NewspaperData.csv")

plt.plot(nwd.daily,nwd.sunday,"bo");plt.xlabel("Daily");plt.ylabel("Sunday")

nwd.corr()

import statsmodels.formula.api as smf
model = smf.ols("sunday~daily",data=nwd).fit()

model.params

series_1 = pd.Series([1500,3000])
df = pd.DataFrame(series_1,columns=["daily"])
pred = model.predict(df) # Predicted values of AT using the model

plt.scatter(x=nwd['daily'],y=nwd['sunday'],color='red');plt.plot(df['daily'],pred,color='black');plt.xlabel('DAILY');plt.ylabel('SUNDAY')


# In[ ]:




