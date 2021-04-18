#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Task: Enter 2 numbers into a GUI, and using a button, calculate their sum, and display it in a new window. 

from tkinter import *
window = Tk()
window.title("Sum Calculator")
window.geometry("250x250")

def do():
    num1 = num1_entry.get()
    num2 = num2_entry.get()
    total = int(num1) + int(num2)
    
    window2 = Tk()
    
    sum_label = Label(window2, text=("Sum: " + str(total)))
    sum_label.pack(anchor="w")
    
    window2.mainloop()

num1_label = Label(window, text="Entr the first number: ")
num1_label.pack(anchor="w")

num1_entry = Entry(window)
num1_entry.pack(anchor="w")

num2_label = Label(window, text="Enter the second number: ")
num2_label.pack(anchor="w")

num2_entry = Entry(window)
num2_entry.pack(anchor="w")

sum_button = Button(window, text="Sum!", command=do)
sum_button.pack()

window.mainloop()


# In[ ]:




