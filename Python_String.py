# Exercise 1: Given a string of odd length greater than 7, return a new string made of the middle three characters of a given String.
def string(word):
    a = len(word)
    middle_in = int(a/2)
    print("The middle 3 characters are: " + (word[middle_in - 1 : middle_in + 2]))
string("HelloWorld")

# Exercise 2: Given two strings, concatenate them, remove any whitespace, and print initials in uppercase.
def string(word1, word2):
    result1 = word1.strip() 
    result2 = word2.strip()
    result3 = result1[0] + result2[0]
    return result3.upper()
print(string("Pooja", " Agarwal"))

# Exercise 3: Given two strings, s1 and s2, create a new string by appending s2 in the middle of s1
def string(s1, s2):
    a = len(s1)
    middle_in = int(a/2)
    print(s1[0:middle_in] + s2 + s1[middle_in:])
string("Pooja","Agarwal")

# Exercise Question 4: Given two strings, s1, and s2 return a new string made of the first, middle, and last characters each input string. And then, return a new string made of the two middle characters of each input string. 
def mid_string(s1):
    a = len(s1)
    middle_in = int(a/2)
    return middle_in

s3="America"
s4="London"
a=mid_string(s3)
b=mid_string(s4)
print("Exercise 1: "+ s3[0]+s4[0]+s3[a]+s4[b]+s3[-1]+s4[-1])

print("Exercise 2: " + s3[a] + s3[a+1] + s4[b] + s4[b+1])

# Exercise 5: Count the number of times "is" appears in the string, and if it's more than 1, print "Pooja", else print "Agarwal"
string1 = "This is music."
a = string1.count("is")
if a > 1:
    print("Pooja")
else:
    print("Agarwal")

# Exercise 6: Count all lower case, upper case, digits, and special symbols from a given string
word = "WaterIsBlue01"
lower_count = 0
upper_count = 0
number_count = 0
special_count = 0
for letter in word:
    if letter.islower():
        lower_count += 1
    elif letter.isupper():
        upper_count += 1 
    elif letter.isnumeric():
        number_count += 1
    else:
        special_count += 1
print("Lower case count: " + str(lower_count))
print("Upper case count: " + str(upper_count))
print("Number case count: " + str(number_count))
print("Special symbol count: " + str(special_count))

# Exercise 7: Arrange string characters such that lowercase letters should come first
word = "PaPaIsBOreD"
lower_string = ''
upper_string = ''
for letter in word:
    if letter.islower():
        lower_string += letter
    else: 
        upper_string += letter
print(lower_string + upper_string)

# Exercise 8: String characters balance Test. We’ll assume that a String s1 and s2 is balanced if all the chars in the s1 are there in s2. characters’ position doesn’t matter.
s1 = "ABEC"
s2 = "DDBAE"
count = 0
for letter in s2:
    for char in s1: 
        if char == letter:
            count += 1
if count >= len(s1):
    print("Letter found")
else:
    print("Letter not found")
