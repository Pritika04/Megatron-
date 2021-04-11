# Exercise 1: Ask user to give integer inputs to make a list. Store only even values given and print the list.
n = input("How many numbers would you like to input? ")
ori_list = []
new_list = []
print("Please enter " + str(n) + " numbers:")
for x in range(int(n)):
    ori_list.append(input())
for x in ori_list:
    if int(x) % 2 == 0:
        new_list.append(x)
print(new_list)

# Exercsie 2: Python program to print even length words in a string.
def even_string(string):
    new_string = ''
    string_split = string.split()
    for word in string_split:
        if len(word) % 2 == 0:
            new_string += ''.join(word)
    return("Updated string: " + new_string)
print(even_string("Hola word!"))

# Exercsie 3: Python | Sum of number digits in List
def num_sum(list):
    sum = 0
    for char in list:
            sum += char
    return sum
print(num_sum([4,45,5,6]))

# Exercsie 4: Reverse a given list.
list = ["World!" , "Hello"]
reverse_list = []
for x in range(-1,len(list)-1,1):
    reverse_list.append(list[x])
print(reverse_list)

# Exercise 5: Slicing of list.
MyList = ["p","r","o","b","e"]
# Print 'p'
print(MyList[0])
# Print 'p' and 'o'
print(MyList[0] + MyList[2])
# Print the last character 
print(MyList[-1])
# Print 'r','o','b'
print(MyList[1:4])
# Print from the start of the list to 'b'
print(MyList[:4])
# Print from the second element to the last
print(MyList[1:])
# Print all the characters in the list
print(MyList[:]) 

# Exercise 6: Operations on a list
odd = [1,3,5,7]
even = [2,4,6,8]
# Add the two lists together. Result = [3,7,11,7]
new_list = []
for x in range(len(even)):
    new_list.append(odd[x] + even[x])
new_list.append(odd[-1])
print(new_list)
# Concatenate list.
print(odd + even)
# Repeat the odd list thrice.
print(odd * 3)
# Repeat each element thrice in the odd list.
new_list = []
for x in odd:
    aa = []
    aa.append(x)
    new_list.append(aa * 3)
print(new_list)
# Concatenate the two lists, index wise. Result = [12,34,56,7]
new_list = []
for x in range(len(even)):
    new_list.append(str(odd[x]) + str(even[x]))
new_list.append(odd[-1])
print(new_list)
# Square of the numbers in the even list.
square_list = []
for x in even:
    square_list.append(x**2)
print(square_list)
# Result = [18,36,54,72]
new_list = []
for x in range(len(odd)):
    if x == 0:
        new_list.append(str(odd[x]) + str(even[x-1]))
    if x > 0:
        new_list.append(str(odd[x]) + str(even[-x-1]))
print(new_list)

# Exercise 7: Reverse a list 2.0
list = [1,3,5,7,9,11,13]
print(list[::-1]) 

# Exercise 8: Remove an empty string for a list of strings
list_1 = ["Pooja"," ","Agarwal"," ","is"," ", "intelligent."]
new_list = []
for x in list_1:
    if x != " ":
        new_list.append(x)
print(new_list)

# Exercise 9: Replace a string with another, in a list.
list = ["Pooja","Agarwal","is", "intelligent."]
replace_string = "Aryan"
string_to_replace = "Pooja"
new_list = []
for x in list:
    if x == string_to_replace:
        new_list.append(replace_string)
    else:
        new_list.append(x)
print(new_list)

# Exercise 10: Pass a list in a function, and print its elements.
def list_function(list):
    for x in range(len(list)):
        print(list[x])
list_function(["Hello","World!"])

# Exercise 11: In a given list, swap the first and last elements.
list = ["Pritika.","name","is","My"]
v1 = list[0]
list[0] = list[-1]
list[-1] = v1
print(list)

# Exercise 12: Print the largest element in the given list.  
list = [3,1,5]
list.sort()
print(list[-1])

# Exercise 13: Check if the element exists in the list. 
list = [3,1,5]
test_element = 7
count = 0
for x in list:
    if test_element == x:
        count += 1
if count >=1:
    print("Element found")
else:
    print("Element not found")

# Exercise 14: Print the duplicate elements in a list.
list = [1,1,3,5,5]
new_list = []
for x in list:
    if list.count(x) > 1:
        new_list.append(x)
for x in new_list:
    if new_list.count(x) > 1:
        new_list.remove(x)
print(new_list)

# Exercise 15: The groups_per_user function receives a dictionary, which contains group names with the list of users. Users can belong to multiple groups. Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values.
def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for group in group_dictionary.keys():
		# Now go through the users in the group
		for users in group_dictionary[group]:
		  lst = []
		  for group in group_dictionary.keys():
		    if users in group_dictionary[group] and users not in lst:
		      lst.append(group)
		  user_groups[users] = lst
	return user_groups
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary


print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))

# Exercise 16: Taylor and Rory are hosting a party. They sent out invitations, and each one collected responses into dictionaries, with names of their friends and how many guests each friend is bringing. Each dictionary is a partial list, but Rory's list has more current information about the number of guests. Fill in the blanks to combine both dictionaries into one, with each friend listed only once, and the number of guests from Rory's dictionary taking precedence, if a name is included in both dictionaries. Then print the resulting dictionary.
def combine_guests(guests1, guests2):
  # Combine both dictionaries into one, with each key listed 
  # only once, and the value from guests1 taking precedence
  new_dict = {}
  new_dict = Taylors_guests
  for key,value in guests1.items():
    new_dict[key] = value
  return new_dict

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))

# Exercise 17: Use a dictionary to count the frequency of letters in the input string. Only letters should be counted, not blank spaces, numbers, or punctuation. Upper case should be considered the same as lower case. For example, count_letters("This is a sentence.") should return {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}.
def count_letters(text):
  result = {}
  # Go through each letter in the text
  for letter in text.lower():
    # Check if the letter needs to be counted or not
    if letter.isalpha():
      if letter in result:
        result[letter] += 1
      else:
        result[letter] = 1
    # Add or increment the value in the dictionary
  return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}