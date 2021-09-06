#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Write a code to input a string, and identify the longest palindromic substring, and its length. 
from operator import itemgetter 

str_in = str(input("Input string: "))
ori_len = len(str_in)
list_ori = []
list_str = []
list_len = []


def palindrome(string):
    new_string = string[::-1]
    if string == new_string:
        return[string, len(string)]
    if string != new_string:
        return[string, 0]
    
for x in range(len(str_in)):
    for y in range(x+1, len(str_in)+1):
        list_ori.append(palindrome(str_in[x:y]))

list_str = list(map(itemgetter(0), list_ori))
list_len = list(map(itemgetter(1), list_ori))

pos = list_len.index(max(list_len))

print("\n")
print("String list: ", list_str)
print("\n")
print("Length list: ", list_len)
print("\n")
print("Longest palindrome substring: ", list_str[pos])
print("\n")
print("Length of longest palindrome substring: ", max(list_len))


# In[ ]:




