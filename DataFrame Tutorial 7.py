#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pandas as pd
import numpy as np

od = pd.DataFrame({
'ord_no':[70001,70009,70002,70004,70007,70005,70008,70010,70003,70012,70011,70013],
'purch_amt':[150.5,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45, 75.29,3045.6],
'ord_date': ['2012-10-05','2012-09-10','2012-10-05','2012-08-17','2012-09-10','2012-07-27','2012-09-10','2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'],
'customer_id':[3005,3001,3002,3009,3005,3007,3002,3004,3009,3008,3003,3002],
'salesman_id': [5002,5005,5001,5003,5002,5001,5001,5006,5003,5002,5007,5001]})

print(od)

print(" ")

# find the mean, min, and max values of purchase amount (purch_amt) group by customer id (customer_id)
print(od.groupby("customer_id").agg({"purch_amt":["mean","min","max"]}))

print(" ")

# split a dataset to group by two columns and count by each row.
print(od.groupby(["salesman_id","customer_id"]).count())

print(" ")

# group on 'customer_id', 'salesman_id' and then sort sum of purch_amt within the groups.
result = od.groupby(["customer_id","salesman_id"]).agg({"purch_amt":"sum"})
print(result.sort_values("purch_amt"))

print(" ")

# groups based on customer id and create a list of order date for each group.
result = od.groupby("customer_id")["ord_date"].apply(list)
print(result)

print(" ")

# split the following dataframe into groups and calculate monthly purchase amount.
od["ord_month"] = pd.to_datetime(od['ord_date']).dt.month
print(od.groupby("ord_date").agg({"purch_amt":"sum"}))

print(" ")

# split the dataframe into groups, group by month and year based on order date and find the total purchase amount year wise, month wise
od["ord_month"] = pd.to_datetime(od["ord_date"]).dt.month
od["ord_year"] = pd.to_datetime(od["ord_date"]).dt.year
print(od.groupby(["ord_year","ord_month"]).agg({"purch_amt":"sum"}))


# In[ ]:




