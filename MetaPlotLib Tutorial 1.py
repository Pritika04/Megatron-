#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install matplotlib


# In[26]:


import matplotlib.pyplot as plt 
plt.plot(["January","April","July","October"],[20,40,60,80],'r')
plt.ylabel("Facts")
plt.xlabel("Months")


# In[34]:


import matplotlib.pyplot as plt
x1 = [1,2,3,4]
x2 = [3,6,9,12]
x3 = [15,16,17,18]
y1 = [1,2,3,4]
y2 = [2,4,6,8]
y3 = [10,11,12,13]
plt.plot(x1,y1,'r',x2,y2,'go',x3,y3,'y*')


# In[48]:


import matplotlib.pyplot as plt
plt.figure(1)
x1 = [1,2,3,4]
x2 = [3,6,9,12]
x3 = [15,16,17,18]
y1 = [1,2,3,4]
y2 = [2,4,6,8]
y3 = [10,11,12,13]
plt.subplot(311)
plt.plot(x1,y1,'r^')
plt.title("New Graph 311")
plt.grid(True)

plt.subplot(312)
plt.plot(x2,y2,'b*')
plt.title("New Graph 312")

plt.subplot(313)
plt.plot(x3,y3,'yo')
plt.title("New Graph 313")


# In[87]:


import matplotlib.pyplot as plt
x1 = [1,2,3,4]
y1 = [1,2,3,4]

plt.plot(x1,y1,'r^')
plt.title("Hello World!",fontsize=18,color="purple",weight="heavy",family="serif")
plt.xlabel("Ice-Cream",fontsize=15,color="blue",fontstyle="italic",family="serif")
plt.ylabel("Temperature",fontsize=15,color="green",fontstyle="italic",family="serif")
plt.grid(True)
plt.text(2.1,1.75,"Mean")
plt.annotate("Median",xy=(3.05,3),xytext=(3.75,2.5),arrowprops=dict(facecolor="black"))
ax = plt.axes()
ax.set_facecolor("yellow")


# In[ ]:




