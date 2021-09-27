#!/usr/bin/env python
# coding: utf-8

# # Question: 

# In[ ]:


# Professor Santos has decided to hide a secret formula for a new type of biofuel. She has, however, left a sequence of coded 
# instructions for her assistant. Each instruction is a sequence of five digits which represents a direction to turn and the 
# number of steps to take. The first two digits represent the direction to turn: • If their sum is odd, then the direction to 
# turn is left. • If their sum is even and not zero, then the direction to turn is right. • If their sum is zero, then the 
# direction to turn is the same as the previous instruction. The remaining three digits represent the number of steps to take 
# which will always be at least 100. Your job is to decode the instructions so the assistant can use them to find the secret 
# formula. Input Specification There will be at least two lines of input. Each line except the last line will contain exactly 
# five digits representing an instruction. The first line will not begin with 00. The last line will contain 99999 and no 
# other line will contain 99999.  


# In[1]:


n = input("Enter the number of codes: ")

print(" ")

for x in range(int(n)):
    sum_codes = 0
    print(" ")
    code_num = input("Enter the code: ")
    y = int(str(code_num)[2])
    lst = map(int, str(y))
    for i in lst:
        sum_codes = sum_codes + i
        if sum_codes % 2 == 0:
            x = "right"
            print("Direction: ", "right")
        elif sum_codes % 2 != 0:
            x = "left"
            print("Direction: ", "left")
        elif sum_codes == 0:
            print(x)
    print("Number of steps: ", int(str(code_num)[-3:]))


# In[ ]:





# In[ ]:




