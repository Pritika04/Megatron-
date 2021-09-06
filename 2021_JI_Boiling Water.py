#!/usr/bin/env python
# coding: utf-8

# # QUESTION BELOW

# In[ ]:


# At sea level, atmospheric pressure is 100 kPa and water begins to boil at 100◦C. As you go above sea level, atmospheric 
# pressure decreases, and water boils at lower temperatures. As you go below sea level, atmospheric pressure increases, and 
# water boils at higher temperatures. A formula relating atmospheric pressure to the temperature at which water begins to boil 
# is P = 5 × B − 400 where P is atmospheric pressure measured in kPa, and B is the temperature at which water begins to boil 
# measured in ◦C. Given the temperature at which water begins to boil, determine atmospheric pressure. Also, determine if you 
# are below sea level (-1) , at sea level (0), or above sea level (1). Note that the science of this problem is generally 
# correct but the values of 100◦C and 100 kPa are approximate and the formula is a simplification of the exact relationship 
# between water’s boiling point and atmospheric pressure. 


# In[3]:


templist = []
for x in range(0,5):
    temp = int(input("Temperature:"))
    P = 5*temp - 400
    print("Atmospheric Pressure = ", P, "KPa")
    if P > 100:
        print(1)
    if P < 100:
        print(-1)
    if P == 100:
        print(0)
    templist.append(temp)
print("\n")
print(templist)


# In[ ]:




