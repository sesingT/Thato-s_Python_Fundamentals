print("side note:") #side note
print("""Hello
      Thato
      ,
      How
      are
      you
      ?""")

print("Day 7:") #Day 7
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



print("Day 8:")
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

#

#🟡 Medium: Fix this code to print "Hello World":
#word1 = "Hello"
#word2 = "World"
#print(word1 word2)



#🔴 Hard: Create a formatted header:
# Should print:
# ====================
# Welcome to Python
# ====================
# Use variables and string operators



print("Day 9:")
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

#

#🟡 Medium: Fix this code to extract "World":
#sentence = "Hello World"
#print(sentence[6,11])

#

#🔴 Hard: Write code that:
# Store: "Programming"
# Extract and print: first 3 letters
# Extract and print: last 3 letters
# Extract and print: middle 4 letters

##e.g slicing
name = "HELLO"
print(name[1:4])

name = "HELLO"
print(name[1:5])

print(name[1:-1])

name = "HELLO"
print(name[1:])


print("day 10")