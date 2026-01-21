print("side note:") #side note
print("""Hello
      Thato
      ,
      How
      are
      you
      ?""")

print("Day 7: Strings Basics") #Day 7
#Concept
#Strings are text wrapped in quotes. Python can access individual characters using index numbers
#(starting at 0).
#Memory Hook
#"A string is a row of letters with numbered seats, starting at seat 0."
#Guided Example
name = "Python"
print(name[0])
print(name[1])
print(name[-1])
#Output:
#P
#y
#n
#Try This Variation
#Access the third character of your name.
#Thinking Challenges

#🟢 Easy: What will this print?

#word = "Hello"
#print(word[0]) 
#print(word[4])

#output: H
#output: o

#🟡 Medium: Fix this code:

#text = "Python"
#print(text[10])
#print(text[0)

text = "Python"
print(text[5])
print(text[0])

#🔴 Hard: Write code that:
# Store your full name in a variable
# Print the first letter
# Print the last letter
# Print the middle letter (estimate if even length)

name = "BigbosS"
print(name[0])
print(name[6])
print(name[3])



print("Day 8: String Operators")
#Day 8 - String operators

#Concept
#You can join strings with + and repeat them with * .

#Memory Hook
#"String operators: + glues words together, * is the copy machine."

#Guided Example
#first = "Hello"
#ast = "World"

#print(first + " " + last)
#print("Ha" * 3)
#Output:
#Hello World
#HaHaHa

#Try This Variation
#Create a line separator by printing "-" * 20
#Thinking Challenges

#🟢 Easy: Predict the output:
#print("Python" + "!")
#print("=" * 5)

#     Python!
#     =====

#🟡 Medium: Fix this code to print "Hello World":
#word1 = "Hello"
#word2 = "World"
#print(word1 word2)

word1 = "Hello"
word2 = "World"
print(word1 +" "+ word2)

#🔴 Hard: Create a formatted header:
# Should print:
# ====================
# Welcome to Python
# ====================
# Use variables and string operators

x = "Welcome"
y = "to"
z = "Python"
print(20 * '=')
print(x+' '+y+' '+z)
print(20 * '=')

print("Day 9: string slicing")
#Day 9 - string slicing

#Concept
#Slicing extracts a portion of a string using [start:end] . End is not included.

#Memory Hook
#"Slicing is cutting a sandwich: start index is included, end index is not."

#Guided Example

#word = "Python"
#print(word[0:3])
#print(word[2:5])
#print(word[:3])
#print(word[3:])
#Output:
#Pyt
#tho
#Pyt
#hon

#Try This Variation
#Extract "gram" from "Programming"
#Thinking Challenges#

#🟢 Easy: What will this print?
#text = "Hello"
#print(text[1:4])

#ell

#🟡 Medium: Fix this code to extract "World":
#sentence = "Hello World"
#print(sentence[6,11])

sentence = "Hello World"
print(sentence[6:])

#🔴 Hard: Write code that:
# Store: "Programming"
# Extract and print: first 3 letters
# Extract and print: last 3 letters
# Extract and print: middle 4 letters

red = "Programming"
print(red[:3]) #or [0:3]
print(red[8:])
print(red[3:7])

##e.g slicing
name = "HELLO"
print(name[1:4])

name = "HELLO"
print(name[1:5])

print(name[1:-1])

name = "HELLO"
print(name[1:])


print("day 10: String Formatting")

#Concept
#F-strings let you insert variables directly into strings using {} .

#Memory Hook
#"F-strings are templates: write the sentence, put variables in curly braces {}."

#Guided Example
#name = "Alex"
#age = 21
#print(f"My name is {name}")
#print(f"I am {age} years old")
#print(f"{name} is {age} years old")
#Output:
#My name is Alex
#I am 21 years old
#Alex is 21 years old
#Try This Variation
#Create an f-string with 3 variables.
#Thinking Challenges

#🟢 Easy: What will this print?
#city = "London"
#print(f"I live in {city}")

#I live in London

#🟡 Medium: Fix this code:
#name = "Sam"
#age = 25
#print(f"name is age years old")
age = 25
name ="Sam"
print(f"{name} is {age} years old")

#🔴 Hard: Create a profile card:
# Store: name, age, city, hobby
# Print formatted like:
# ==================
# Name: Alex
# Age: 21
# City: London
# Hobby: Coding
# ==================
name = "Alex"
age = 21
city = "London"
hobby = "Coding"

print("="*18)
print(f" Name:{name} \n Age:{age} \n City:{city} \n Hobby:{hobby}")
print("="*18)


#Testing string comparing ops
print("HH"=="HH")
print("HH"=="hH")


#🎯 The Challenge
#1
full_name = "Alex Bingo"
birth_year = 1801
current_year = 2026
city = "Earth"
favourite_programming_word= "Error"
#2
first_name = (full_name[0:4])
last_name = (full_name[5:])
first_letters = (favourite_programming_word[:2])
last_letters = (favourite_programming_word[3:])

#3
age = (current_year-birth_year)
age_and_word_length = (age + len(favourite_programming_word))

print("="*18)
print("PROFILE SUMMARY")
print("="*18)
print(f"Name      :{first_name} {last_name}")
print(f"Initials  :{first_letters}.{last_letters}")
print(f"Age       :{age}")
print(f"Code tag  :{age_and_word_length}")
print("="*18)

#Self test
#Slicing shown in choosing a specific part of words
#A single formated exercised where each code runs on its own line
#There is no comparison

#comparison
print(first_name == last_name)


#  Days 6-10 Consolidation Exercises
#Exercise 1 — Fill in the Blanks
# Create a string variable
#text = _____
# Print first character
#print(text[_____])
# Print last 3 characters
#print(text[_____:_____])
# Create formatted output
#name = "Alex"
#print(f"Hello, {_____}")
#Constraint: Write from scratch. No copy-paste from earlier code.

text = "Python"
print(text[0:1])

print(text[3:])

name = "Alex"
print(f"Hello, {name}")

#Exercise 2 — Build Combining Days 6-10
#Create a program that:
#Stores first name and last name separately
#Uses string operators to combine them
#Extracts initials using indexing (e.g., "A.S.")
#Prints formatted: "Full Name: Alex Smith (A.S.)"
#Constraint: Write from scratch.

name = "Chicken"
surname = " Salad"
names = (name + surname)
initial_name = (name[0:1])
initial_surname = (surname[1:2])
intitials = f"{initial_name}.{initial_surname}"
print(f"Full name: {names}({intitials})")


#Exercise 3 — Build Combining Days 1-10
#Create a complete profile program:
#Variables: first name, last name, age, birth year, favorite word
#Use string slicing to get initials
#Use f-strings to format output
#Calculate age verification (2025 - birth year)
#Print formatted summary with calculations
#Constraint: Write from scratch. No copy-paste.

#already did that on the challenge above.

print("Day 11: String Methods")

print("           hello world       ".strip()) 

print("#A#hello world#A#".strip("#A")) 
