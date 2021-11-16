#!/usr/bin/env python
# coding: utf-8

# # QUESTION:

# In[1]:


# Q: We often include emoticons in our text messages to indicate how we are feeling. The three consecutive characters :-) 
# indicate a happy face and the three consecutive characters :-( indicate a sad face. Write a program to determine the overall 
# mood of a message.

# Input: There will be one line of input that contains between 1 and 255 characters. 

# The output is determined by the following rules:

# If the input line does not contain any happy or sad emoticons, output none.
# Otherwise, if the input line contains an equal number of happy and sad emoticons, output unsure.
# Otherwise, if the input line contains more happy than sad emoticons, output happy.
# Otherwise, if the input line contains more sad than happy emoticons, output sad.


# In[8]:


input_str = ":-):-)?"
happy = ":-)"
sad = ":-("
hap_counter = 0
sad_counter = 0

input_split = input_str.split(":-)")
print(input_split)

for x in range(0, len(input_split)):
    if (happy in input_split[x]):
        hap_counter += 1
    if (sad in input_split[x]):
        sad_counter += 1

print(hap_counter, sad_counter)


# In[18]:


input_str = "This:-(is str:-(:-(ange te:-)xt"
happy = ":-)"
sad = ":-("


happy_counter = input_str.count(happy)
sad_counter = input_str.count(sad)

if (happy_counter == 0 and sad_counter == 0):
    print("None")
elif (happy_counter == sad_counter):
    print("Unsure")
elif (happy_counter > sad_counter):
    print("Happy")
else:
    print("Sad")


# In[ ]:




