# Exercise 1: The "toc" dictionary represents the table of contents for a book. Fill in the blanks to do the following: 	1) Add an entry for Epilogue on page 39. 	2) Change the page number for Chapter 3 to 24. 	3) Display the new dictionary contents. 	4) Display True if there is Chapter 5, False if there isn't.

toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc["Epilogue"] = 39 # Epilogue starts on page 39
toc["Chapter 3"] = 24 # Chapter 3 now starts on page 24
print(toc) # What are the current contents of the dictionary?
if "Chapter 5" in toc: # Is there a Chapter 5?
    print("True")
else:
    print("False") 

# Exercise 2: Complete the code to iterate through the keys and values of the cool_beasts dictionary. Remember that the items method returns a tuple of key, value for each element in the dictionary.
cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for animal,limbs in cool_beasts.items():
    print("{} have {}".format(animal,limbs))

# Exercise 3: In Python, a dictionary can only hold a single value for a given key. To workaround this, our single value can be a list containing multiple values. Here we have a dictionary called "wardrobe" with items of clothing and their colors. Fill in the blanks to print a line for each item of clothing with each color, for example: "red shirt", "blue shirt", and so on.
wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for cloth in wardrobe:
    for color in wardrobe[cloth]:
        print(color, cloth)

# Exercise 4: The add_prices function returns the total price of all of the groceries in the  dictionary. Fill in the blanks to complete this function.
def add_prices(basket):
	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for price in groceries.values():
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
		total += price
	# Limit the return value to 2 decimal places
	return round(total, 2)  

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44

# Exercise 5: Question 1
The email_list function receives a dictionary, which contains domain names as keys, and a list of users as values. Fill in the blanks to generate a list that contains complete email addresses (e.g. diana.prince@gmail.com).
def email_list(domains):
	emails = []
	for domain,users in domains.items():
	  for user in users:
	    emails.append(user + "@" + domain)
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

# Exercise 6: Write a program to find the sum of all elements of a list.
def sum_elements(list):
    sum = 0
    for x in list:
        sum += x
    return("The sum is: " + str(sum))
print(sum_elements([2,3,4]))

# Exercise 7: Write a program to find the product of all elements of a list.
def product_elements(list):
    product = 1
    for x in list:
        product *= x
    return("The product is: " + str(product))
print(product_elements([2,3,4]))

# Exercise 8: Find largest and smallest elements of a list.
def element_size(list):
    largest = -100
    smallest = 1000
    for x in list:
        if x > largest:
            largest = x
        if x < smallest:
            smallest = x
    return("The largest num = " + str(largest) + " ; The smallest num = " + str(smallest))

print(element_size([-3, -4, 10])) 

# Exercise 9: Write a program to print sum, average of all numbers, smallest and largest element of a list.
def calculations(list):
    largest = -100
    smallest = 1000
    sum = 0
    length = len(list)
    for x in list:
        sum += x
        if x > largest:
            largest = x
        if x < smallest:
            smallest = x
    print("Sum: " + str(sum))
    print("Avg: " + str(sum/length))
    print("Largest num: " + str(largest))
    print("Smallest num: " + str(smallest))
(calculations([2,3,4]))

# Exercise 10: Make a list by taking 10 input from user. Now delete all repeated elements of the list.
list_input = []
new_list = []
print("Please enter 10 numbers: ")
for x in range(10):
    list_input += input()
for x in list_input:
    if new_list.count(x) == 0:
        new_list += x
print("Updated list: " + str(new_list))

# Exercise 11: 