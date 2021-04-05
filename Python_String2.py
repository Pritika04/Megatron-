# Exercise 1: Check if the function is a palindrome or not. 
def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	# Traverse through each letter of the input string
	for letter in input_string:
		# Add any non-blank letters to the 
		# end of one string, and to the front
		# of the other string. 
		if letter != " ":
			new_string += letter.lower()
			reverse_string = letter.lower() + reverse_string
	# Compare the strings
	if new_string == reverse_string:
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True


# Exercise 2: Using the format method, convert the given distance in miles, into kilometres, with only 1 decimal place, in the format: "X miles equals Y km"
def convert_distance(miles):
	km = miles * 1.6 
	result = "{} miles equals {:.1f} km".format(miles, km)
	return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km


# Exercise 3: Using the format function, return the first_name and the first initial of the last name followed by a period. 
def nametag(first_name, last_name):
	return("{} {:.1s}.".format(first_name, last_name))

print(nametag("Jane", "Smith")) 
# Should display "Jane S." 
print(nametag("Francesco", "Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc", "Grand-Pierre")) 
# Should display "Jean-Luc G." 

# Exercise 4: Replace the old string in a sentence, with a new string, but only if the sentence ends with the old string. (It is case sensitive). 
def replace_ending(sentence, old, new):
	# Check if the old string is at the end of the sentence 
	if sentence.endswith(old):
		# Using i as the slicing index, combine the part
		# of the sentence up to the matched string at the 
		# end with the new string
		i = len(sentence) - len(old)
		new_sentence = sentence[:i] + new
		return new_sentence

	# Return the original sentence if there is no match 
	return sentence
	
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"


# Exercise 5: Find all occurrences of “USA” in a given string ignoring the case
def word_count(word, find):
    word = word.upper()
    count = word.count(find)
    return count 
print(word_count("Welcome to USA. usa awesome, isn't it?", "USA"))

# Exercise 6: Given a string, return the sum and average of the digits that appear in the string, ignoring all other characters
string = "English = 78 Science = 83 Math = 68 History = 65"
string1 = string.split()
length = len(string1)
sum = 0 
count = 0
average = 0
for x in range(length):
    if string1[x].isnumeric():
        count += 1
        sum += int(string1[x])
average = sum/count
print(("Sum: {}").format(sum))
print(("Average: {}").format(average))

# Exercise 7: Reverse a given string
input_word = "Cat"
reverse_string = ''
for letter in input_word:
    reverse_string = letter + reverse_string 
print(reverse_string)

# Exercise 8: Given a string, print each word, and print the length of it.
def count(name):
    name_split = name.split()
    for x in range(len(name_split)):
        print(name_split[x] + " = " + str(len(name_split[x])))
count("My name is Pooja")

# Exercise 9: Create a function, 'skip_elements' which returns a list containing every other element from an input list, starting from the first element. 
def skip_elements(elements):
	# Initialize variables
	new_list = []
	i = 0

	# Iterate through the list
	for i in range(len(elements)):
		# Does this element belong in the resulting list?
		if i % 2 == 0:
			# Add this element to the resulting list
			new_list.append(elements[i])
		# Increment i
		i += 1

	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []


# Exercise 10: Use tuples to store information about a file: its name, its type, and its size in bytes. Then, return the size in kilobytes (1 KB = 1024 bytes) up to 2 decimal places. 
def file_size(file_info):
	file_name, file_type, file_size = file_info
	return("{:.2f}".format(file_size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21

# Exercise 11: Python program to print even length words in a string
def string_conversion(string):
    word_split = string.split()
    for word in word_split:
        if len(word) % 2 == 0:
            print(word)
string_conversion("I am Muskan")

# Exercise 11: Python program to capitalize the first and last character of each word in a string. 
def capitalization(string):
    y = ''
    for word in string.split():
        result = word.capitalize()
        result2 = word[-1].upper()
        x = result.replace(result[-1],result2)
        y += x + ' '
    return y 
print(capitalization("hello world"))

# Exercise 12: Python program to check if a string has at least one letter and one number
def check_string(string):
    string_count = 0
    number_count = 0
    for word in string.split():
        for letter in word: 
            if letter.isalpha():
                string_count += 1
            elif letter.isnumeric():
                number_count += 1
    if string_count >= 1 and number_count >= 1:
        return "Valid"
    else:
        return "Invalid"
        
print(check_string("Hell3 Worl1"))

# Exercise 13: #Python Program to accept the strings which contains all vowels 
word = "AgpIOhU ghe"
a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0
for letter in word.lower():
    if letter == "a":
        a_count += 1
    elif letter == "e":
        e_count += 1
    elif letter == "i":
        i_count += 1
    elif letter == "o":
        o_count += 1
    elif letter == "u":
        u_count += 1
if (a_count >= 1 and e_count >= 1 and i_count >= 1 and o_count >= 1 and u_count >= 1):
    print("Accepted")
else:
    print("Rejected")

# Exercise 14: Python Program - Return string length without including any whitespaces.
def string_length(word):
    result = ''
    x = word.strip()
    y = x.split()
    for i in y:
        result += i
    return len(result)
print(string_length(" H e l l o "))









