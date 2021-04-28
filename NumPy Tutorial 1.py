#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np

s2 = pd.Series([10,30,50,20])
s3 = pd.Series([40,60,70,80,90])

# NumPy Maths Functions: 
    # Addition 
print("Addition")
print(np.add(s2,s3))
    # Multiplication 
print("Multiplication")
print(np.multiply(s2,s3))
    # Subtraction
print("Subtraction")
print(np.subtract(s2,s3))
    # Division
print("Division")
print(np.divide(s2,s3))
    # Power 
print("Power of")
print(np.power(s2,s3))
    # Modulus
print("Modulus")
print(np.mod(s3,s2))
    # Remainder
print("Remainder")
print(np.remainder(s2,s3))
    # Reciprocal 
print("Reciprocal")
print(np.reciprocal(s2))
    # Mean
print("Mean")
print(np.mean(s2))
    # Standard Deviation
print("Standard Deviation")
print(np.std(s2))
    # Median
print("Median")
print(np.median(s2))
    # Percentile
print("Percentile")
print(np.percentile(s2, q=[0,25,50,75,100]))


# In[ ]:


import pandas as pd
import numpy as np

s1 = pd.Series(["Apple:is:bAd","boy","Cat","Dog","elephant"])
s4 = pd.Series(["ab","aaaoy","cat","elf"])

# NumPy String Operations
    # Capitalisation
print("Capitalisation: ")
print(np.char.capitalize(s1[0]))
    # Title 
print("Title: ")
print(np.char.title(s1[0]))
    # Upper 
print("Upper: ")
print(np.char.upper(s1[0]))
    # Lower 
print("Lower: ")
print(np.char.lower(s1[0]))
    # Split string 
print("Split string : ")
print(np.char.split(s1[0],":"))
    # Swap Case
print("Swap case: ")
print(np.char.swapcase(s1[0]))
    # Strip
print("Strip: ")
print(np.char.strip(s1[0]))
    # Compare two strings
print("String comparison: ")
print(np.char.equal(s1[1],s4[1]))
print(np.char.less(s1[3],s4[0]))
    # String count
print("String count: ")
print(np.char.count(s4[1],"a"))
    # Endswith 
print("Endswith: ")
print(np.char.endswith(s4[0],"t"))
    # Find
print("Find: ")
print(np.char.find(s1[0],"a"))
print(np.char.find(s1[0],"t",3))


# In[3]:


import pandas as pd
import numpy as np

s5 = pd.Series([3,2,8,7,6,9,5,1,4])
s6 = pd.Series(["A","p","U","t","r","s","v","g","Y"])

    # Sort 
print("Sort: ")
print(np.sort(s5))
    # Searching 
print("Searching: ")
print(np.argmax(s5))
print(np.argmin(s5))
print(np.where(s5 %5==0))


# In[14]:


# Write a Pandas program to extract items at given positions of a given series.
s = pd.Series([3,2,8,7,6,9,5,1,4])
element_pos = [2,4,6]
print(s.take(element_pos))


# In[ ]:





# In[ ]:




