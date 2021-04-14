# Exercise 1: Print the first n natural numbers.
n = input("Please enter how many natural numbers you would like: ")
for x in range(1,int(n)+1,1):
    print(x)

# Exercise 2: Display the numbers from the list that are divisble by 5, and if there are numbers greater than 150, stop the loop.
list = [12,15,32,42,55,75,122,132,150,180,200]
for x in list: 
    if x % 5 == 0 and x < 150:
        print(x)

# Exercise 3: Reverse the given list.
list = [10,20,30,40,50]
new_list = []
for x in range(-1, -len(list)-1,-1):
    new_list.append(list[x])
print(new_list)

# Exercise 4: Merge two lists and convert it to a dictionary.
keys = ["ten","twenty","thirty"]
values = [10,20,30]
dict = {}
for x in range(len(keys)):
    dict[keys[x]] = values[x]
print(dict)

# Exercise 5: Create a new dictionary by extracting the keys from the given dictionary.
sample_dict = {"Name":"Kelly","Age":25,"Salary":8000,"City":"New York"}
keys = ["Name","Salary"]
new_dict = {}
for x in range(len(keys)):
    var1=keys[x]
    if sample_dict.get(var1):
        new_dict[keys[x]] = sample_dict.get(var1)
print(new_dict)


# Exercise 6: Get the key of the minimum value in the dictionary.
sample_dict = {"Physics":82,"Maths":65,"History":75}
num_list = []
for x in sample_dict.values():
    num_list.append(x)
print(num_list)
new_num_list = sorted(num_list)
for keys,values in sample_dict.items():
    if new_num_list[0] == values:
        print(keys)

# Exercise 6: Get the key of the minimum value in the dictionary.
sample_dict = {"Physics":82,"Maths":65,"History":75}
num_list = []
for x in sample_dict.values():
    num_list.append(x)
print(num_list)
new_num_list = sorted(num_list)
for keys,values in sample_dict.items():
    if new_num_list[0] == values:
        print(keys)
        
# Exercise 7: Get the minimum value.
string = "Pooja"
print(min(string.lower()))
list = ["Pooja","Pritika","Aryan","Vivek"]
print(min(list))
sample_dict = {"Physics":82,"Maths":65,"History":75}
key=min(sample_dict,key=sample_dict.get)
print(key,sample_dict.get(key))

# Exercise 8: Remove 20 from the list.
list = [5,10,20,15,30,20,35,20]
for x in list:
    if x == 20:
        list.remove(x)
print(list)

# Exercise 9: You have a string, "Welcome to USA. usa is awesome." Find the occurrence of 'USA' irrespective of the case.
string = "Welcome to USA. usa is awesome."
count = 0
string_lower = string.lower()
for x in string_lower.split():
    if "usa" in x:
        count += 1
print("USA Count = " + str(count))

# Exercise 10: Reverse a given string.
string = "Hello"
print(string[::-1])

# Exercsie 11: Whenever there is a '-', split the string.
string = "Emma - is - a - good - girl."
print(string.split("-"))

# Exercise 12: Get the smallest number from a list.
def small_num(list):
    return min(list)
print(small_num([1,2,3,4,5]))

# Exercise 13: Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
sample_list = ['abc', 'xyz', 'aba', '1221']
count = 0
for item in sample_list:
    if len(item) >= 2 and item[0] == item[-1]:
        count += 1
print(count)

# Exercise 14: Write a Python program to shift last element to first position and first element to last position in a given list.
og_list = [1, 2, 3, 4, 5, 6, 7]
first_ele = og_list[0]
og_list[0] = og_list[-1]
og_list[-1] = first_ele
print(og_list)

# Exercise 15: Write a Python program to find the specified number of largest products from two given list, multiplying an element from each list.
list_1 = [1, 2, 3, 4, 5, 6]
list_2 = [3, 6, 8, 9, 10, 6]
new_list = []
for item in list_1:
    for x in list_2:
        new_list.append(item*x)
sorted_new_list = sorted(new_list,reverse=True)
print(sorted_new_list)
n = input("How many greatest products do you want?")
print(sorted_new_list[0:int(n)])

# Exercise 16: Write a Python program to find the maximum and minimum value of the three given lists. 
list_1 = [2, 3, 5, 8, 7, 2, 3]
list_2 = [4, 3, 9, 0, 4, 3, 9]
list_3 = [2, 1, 5, 6, 5, 5, 4]
new_list = []
for x in list_1:
    new_list.append(x)
for x in list_2:
    new_list.append(x)
for x in list_3:
    new_list.append(x)
sorted_new_list = sorted(new_list)
print(sorted_new_list[0])
print(sorted_new_list[-1])

# Exercise 17: Write a Python program to find the item with maximum occurrences in a given list.
og_list = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
new_dict = {}
for item in og_list:
    if item in new_dict:
        new_dict[item] += 1
    else: 
        new_dict[item] = 1
for key,value in new_dict.items():
    k = max(new_dict.values())
print("Item with maximum occurences -->")
print(new_dict[k])