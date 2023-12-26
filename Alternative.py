'''Create a file called alternative.py

Write a program that reads in a string and makes each alternate
character into an upper case character and each other alternate character
a lower case character.
e.g. The string “Hello World” would become “HeLlO WoRlD”

● Now, try starting with the same string but making each alternative word
lower and upper case.
e.g. The string: “I am learning to code” would become “i AM learning
TO code”.

Tip: Using the split() and join() functions will help you here.'''


string= input(" Enter any string here to see the alternative result: ").split()  # string is requested from the user
list_location= " ".join([i.upper() #here each character in the string is manipulated
if x % 2 
else i.lower() 
for x, i in enumerate(string)])

print(list_location)
# I have tried to generate this code and it gives me the same result .
