# Exercise 1: Create a function, 'skip_elements' which returns a list containing every other element from an input list, starting from the first element. Use the enumerate function. 
def skip_elements(elements):
	# code goes here
	new_list = []
	for index,name in enumerate(elements):
		if index % 2 == 0:
			new_list.append(name)
	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

# Exercise 2: Create a function to return the name and email address of the person. 
def emails(people):
    result = []
    for name,email_id in people:
        result.append("{} <{}>".format(name,email_id))
    return result
print(emails([("Pooja Agarwal", "def@gmail.com"), ("Aryan Agarwal", "abc@gmail.com")]))

# Exercise 3: The odd_number function returns a list of odd numbers between 1 and n, inclusively. Use list comprehension to achieve this. 
def odd_numbers(n):
	return [x for x in range(0,n+1) if x % 2 != 0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []

# Exercise 4: Given a list of filenames, we want to rename all the files with the extension hpp to the extension h. To do this, we would like to generate a new list called newfilenames, consisting of the new filenames. 
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
newfilenames = []
for filename in filenames:
    if filename.endswith("hpp"):
        x = filename.replace("hpp", "h")
        newfilenames.append((x))
    else:
        newfilenames.append((filename))

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

# Exercise 5: Let's create a function that turns text into pig latin: a simple text transformation that modifies each word moving the first character to the end and appending "ay" to the end.
def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split()
  for word in words:
    # Create the pig latin word and add it to the list
    say += word[1:] + word[0] + "ay"
    say += ' '
    # Turn the list back into a phrase
  return say
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

# Exercise 6: The group_list function accepts a group name and a list of members, and returns a string with the format: group_name: member1, member2, … For example, group_list("g", ["a","b","c"]) returns "g: a, b, c". 
def group_list(group, users):
  members = group + ": " + ", ".join([str(elem) for elem in users])
  return members

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"

# Exercise 7: Program to check if a string contains any special character.
def string_check(string):
    letter_count = 0
    num_count = 0
    string1 = string.strip()
    string2 = string1.split()
    string3 = "".join(string2)
    for word in string3:
        for letter in word:
            if letter.isalpha():
                letter_count += 1
            elif letter.isnumeric():
                num_count += 1
    if (letter_count + num_count) < len(string3):
        print("Yes, the string contains a special character")
    else: 
        print("No, the string doesn't contain any special characters")
string_check("Hello everyone")

# Exercise 8: Python program to split and join a string
def string_conversion(string):
    string1 = string.split()
    string2 = "".join(string1)
    return string2
print(string_conversion("H ello"))

# Exercise 9: Swap the commas with full stops. 
string = "Hello,,,, We,lcome. s.ir"
string2 = string.replace(",","!")
string3 = string2.replace(".",",")
string4 = string3.replace("!",".")
print(string4)

# Exercise 10: Remove the i-th character from the input given by the user.
string = "Hello i"
index = input("Please enter the index value: ")
print(string[0:int(index)] + string[int(index)+1:])

# Exercise 11: Write a program that takes your full name as input and displays the abbreviations of the first and middle names except the last name which is displayed as it is. For example, if your name is Robert Brett Roser, then the output should be R.B.Roser.
def name_input(first_name, middle_name, last_name):
    return("{:.1s}. {:.1s}. {}".format(first_name, middle_name, last_name))
print(name_input("Robert", "Brett", "Roser"))











