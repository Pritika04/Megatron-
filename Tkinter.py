#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import*
window = Tk()
# Adding features to the window 
window.title("Test 1")
window.geometry("250x250")
window.minsize(100,100)
window.maxsize(300,300)
window.config(bg="Light Blue")

# Adding a label to the GUI 
# Features of a label: background; foreground; borderwidth; relief(sunken, groove, solid, raised, flat, ridge); font
# Features of pack(): anchor(n,s,e,w,ne,nw,se,sw); external padding - padx,pady; internal padding - ipadx,ipady; fill=(X,Y,BOTH) 
label_1 = Label(window, text="Python",bg="Black",fg="yellow",font=("Times New Roman",30,"bold"),width=250,height=250,borderwidth=20,relief="sunken")
label_1.pack()

window.mainloop()


# In[ ]:


from tkinter import*

window = Tk()
window.title("Test 2")
window.geometry("250x250")

# Adding a label to the window
name_label = Label(window, text="Name: ")
name_label.pack(anchor="w")

# Adding an entry box to the window
name_entry = Entry(window)
name_entry.pack(anchor="w")

window.mainloop()


# In[ ]:


from tkinter import*

window = Tk()
window.title("Test 2")
window.geometry("250x250")

def do():
    name = name_entry.get()
    contact = contact_entry.get()
    address = address_entry.get()
    
    window2 = Tk()
    
    label1 = Label(window2, text=("Name: " + name))
    label1.pack(anchor="w")
    
    label2 = Label(window2, text=("Contact: " + contact))
    label2.pack(anchor="w")
    
    label3 = Label(window2, text=("Address: " + address))
    label3.pack(anchor="w")
    
    window.destroy()
    
    window2.mainloop()

# Creating an entry form 
name_label = Label(window, text="Name: ")
name_label.pack(anchor="w")

name_entry = Entry(window)
name_entry.pack(anchor="w")

contact_label = Label(window, text="Contact: ")
contact_label.pack(anchor="w")

contact_entry = Entry(window, text="Contact: ")
contact_entry.pack(anchor="w")

address_label = Label(window, text="Address: ")
address_label.pack(anchor="w")

address_entry = Entry(window)
address_entry.pack(anchor="w")

# Adding a button to your tkinter window
Button1 = Button(window, text="Get the info!", command=do)
Button1.pack(anchor="se")

window.mainloop()


# In[ ]:


# Task: Making a tkinter GUI which checks a database (which in this case is a dictionary) every time a user logs in and tells them if they have an account or not. 

from tkinter import *

window = Tk()

users = {"user1":"pass1", "user2":"pass2", "user3":"pass3", "user4":"pass4", "user5":"pass5"}

def do():
    username = user_entry.get()
    password = pass_entry.get()
    check = 0
    
    for key,value in users.items():
        if key == username and value == password:
            print("You have an account!")
            check += 1
    if check == 0:
        print("You don't have an account")

user_label = Label(window, text="Username:")
user_label.pack(anchor="w")

user_entry = Entry(window)
user_entry.pack(anchor="w")

pass_label = Label(window, text="Password:")
pass_label.pack(anchor="w")

pass_entry = Entry(window)
pass_entry.pack(anchor="w")

button1 = Button(window, text="Submit!", command=do)
button1.pack()

window.mainloop()


# In[ ]:


# Task: Making a tkinter GUI which checks a database (which in this case is a dictionary) every time a user logs in and tells them if they have an account or not.
# Task2: Display the information in a message box - either 'you have an account' as an info box or 'you don't have an account' as an error box
 
from tkinter import *
from tkinter import messagebox

window = Tk()

users = {"user1":"pass1", "user2":"pass2", "user3":"pass3", "user4":"pass4", "user5":"pass5"}

def do():
    username = user_entry.get()
    password = pass_entry.get()
    check = 0
    
    for key,value in users.items():
        if key == username and value == password:
            messagebox.showinfo("Congratulations!","You have an account.")
            check += 1
    if check == 0:
        messagebox.showerror("Error!","You don't have an account.")

user_label = Label(window, text="Username:")
user_label.pack(anchor="w")

user_entry = Entry(window)
user_entry.pack(anchor="w")

pass_label = Label(window, text="Password:")
pass_label.pack(anchor="w")

pass_entry = Entry(window)
pass_entry.pack(anchor="w")

button1 = Button(window, text="Submit!", command=do)
button1.pack()

window.mainloop()


# In[ ]:




