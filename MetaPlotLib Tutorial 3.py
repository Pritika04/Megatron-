#!/usr/bin/env python
# coding: utf-8

# In[9]:


import matplotlib.pyplot as plt
import numpy as np 

data = [[30,25,50,20],[40,23,15,17],[35,22,45,19]]
X = np.arange(4)
plt.bar(X+0,data[0],color="b",width=0.25)
plt.bar(X+0.25,data[1],color="r",width=0.25)
plt.bar(X+0.5,data[2],color="g",width=0.25)


# In[24]:


import matplotlib.pyplot as plt
import numpy as np 

data = [[30,25,50,20],[40,23,15,17],[35,22,45,19]]
c = ["pink","indigo","purple"]
gap = 0.8/len(data)

for i,row in enumerate(data):
    X = np.arange(len(row))
    plt.bar(X+i*gap,row,width=gap,color=c[i])
    
plt.title("Revenue generated monthly!")
plt.xlabel("Months")
plt.ylabel("Revenue in $")

plt.tick_params(axis="x",color="yellow",direction="out",length=10,width=3)


# In[50]:


import matplotlib.pyplot as plt

data = [5,25,50,20]
marks = ["Math","Physics","Chemistry","Biology"]
c = ["yellow","pink","blue","indigo"]

plt.pie(data,labels=marks,colors=c,startangle=90,shadow=True)
plt.legend(title="Marking Scheme",loc="upper right",bbox_to_anchor=(1,0,0.5,1))
plt.title("Grade 10 Average Subject Marks!")


# In[65]:


import matplotlib.pyplot as plt

X = [21,22,23,4,5,6,77,8,9,10,31,32,33,34,35,36,37,18,49,50,100]
num_bins = 5
plt.hist(X,num_bins,facecolor="yellow",edgecolor="black",linewidth=5)
plt.title("Frequency of Marks!",fontsize=15)
plt.xlabel("Mark Range")
plt.ylabel("Number of Students")


# In[ ]:




