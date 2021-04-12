# Exercise 1: Sort dicitonaries by keys.
dict = {1:"Pooja",3:"Aryan",2:"Pritika",4:"Vivek"}
new_dict = {}
for key in sorted(dict):
    new_dict[key] = dict[key]
print(new_dict)

# Exercise 2: Sort the list
list = ["P","Pr","A","V"]
new_list = []
new_list = sorted(list)
print(new_list)

# Exercise 3: Handling missing keys in dictionaries.
dict = {"India":91,"Australia":25,"Nepal":977}
print(dict.get("Japan","Not found"))

# Exercise 4: To find the sum of all the values in a dictionary.
dict = {"A":100,"B":200,"C":300}
sum = 0
for key in dict:
    sum += dict[key]
print(sum)

# Exercise 5: Find the length of the dictionary.
dict = {"A":1,"B":2,"C":3}
print(len(dict))

# Exercise 6: Find the size of the dictionary.
dict = {"A":1,"B":2,"C":3}
print(dict.__sizeof__())

# Exercise 7: Merge two dictionaries.
dict = {"a":10,"b":8}
dict_2 = {"d":6,"c":4}
new_dict = dict
for keys,values in sorted(dict_2.items()):
    new_dict[keys] = values
print(new_dict)

# Exercise 8: Insert a new key/value at the start of the dictionary.
dict = {"a":1,"b":2}
dict_2 = {"d":4,"c":3}
new_dict = dict_2
for keys,values in dict.items():
    new_dict[keys] = values
print(new_dict)

# Exercise 9: Replace words from dictionary.
dict = {"Pooja":"Cats","Aryan":"dogs"}
string = "Pooja and Aryan are friends."
z = ''
string_2 = ''
for x in string.split():
    z = dict.get(x,x) 
    string_2 += ' ' + z
print(string_2)

# Exercise 10: Count the frequency of each letter in a string.
string = "Cats and dogs are friends."
new_dict = {}
for letter in string.lower():
    if letter in new_dict:
        new_dict[letter] += 1
    else:
        new_dict[letter] = 1 
print(new_dict)