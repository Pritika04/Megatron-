#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt 

months = ["January","April","July","October"]
revenue = [10,20,30,40]
color = ["yellow","pink","green","blue"]

plt.bar(x=months,height=revenue,width=0.5,bottom=5,align="center",color=color,linewidth=3,edgecolor="black")
plt.title("Revenue Generated Quaterly!",weight="heavy",fontsize=15)
plt.xlabel("Months")
plt.ylabel("Revenue in $")


# In[11]:


import matplotlib.pyplot as plt 

months = ["January","April","July","October"]
revenue = [10,20,30,40]
color = ["yellow","pink","green","blue"]

plt.barh(months,revenue,color=color,linewidth=3,edgecolor="black")
plt.title("Revenue Generated Quaterly!",weight="heavy",fontsize=15)
plt.xlabel("Revenue in $")
plt.ylabel("Months")


# In[32]:


import matplotlib.pyplot as plt 

months = ["January","February","March"]
food = [10,5,12]
transport = [20,10,15]
rent = [30,20,30]

plt.bar(months,food,width = 0.4,color="red",label="Food")
plt.bar(months,transport,width = 0.4,bottom=food,color="orange",label="Transport")
plt.bar(months,rent,width = 0.4,bottom=transport,color="yellow",label="Rent")

plt.title("Monthly Expenditure!",weight="heavy",fontsize=15)
plt.xlabel("Months",fontsize=13)
plt.ylabel("Expenditure",fontsize=13)
plt.legend()


# In[ ]:




