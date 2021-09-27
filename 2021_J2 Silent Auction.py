#!/usr/bin/env python
# coding: utf-8

# # Question: 

# In[ ]:


# A charity is having a silent auction where people place bids on a prize without knowing anyone else’s bid. Each bid includes 
# a person’s name and the amount of their bid. After the silent auction is over, the winner is the person who has placed the 
# highest bid. If there is a tie, the person whose bid was placed first wins. Your job is to determine the winner of the silent 
# auction. Input Specification The first line of input contains a positive integer N, where 1 ≤ N ≤ 100, representing the 
# number of bids collected at the silent auction. Each of the next N pairs of lines contains a person’s name on one line, and 
# the amount of their bid, in dollars, on the next line. Each bid is a positive integer less than 2000. The order of the input 
# is the order in which bids were placed. Output Specification Output the name of the person who has won the silent auction. 
# Sample Input 1 3 Ahmed 300 Suzanne 500 Ivona 450 Output for Sample Input 1 Suzanne. 


# In[ ]:


name_list = []
max_bid_list = []

n = input("Enter the number of bids: ")

for x in range(int(n)):
    max_bid = input("Bid value: ")
    max_bid_list.append(max_bid)
    name = input("Name: ")
    name_list.append(name)

pos_max = max_bid_list.index(max(max_bid_list))

print(max(max_bid_list), name_list[pos_max])


# In[ ]:


name_list = []
max_bid_list = []

n = input("Enter the number of bids: ")

for x in range(int(n)):
    max_bid = input("Bid value: ")
    max_bid_list.append(max_bid)
    name = input("Name: ")
    name_list.append(name)


for x in max_bid_list:
    if x == max(max_bid_list):
        pos_max = max_bid_list.index(x)
        break 

print(max_bid_list[pos_max], name_list[pos_max])


# In[ ]:




