'''Practical Task 2
Follow these steps:
● Create a new Python file in this folder called replace.py.
● Save the sentence: “The!quick!brown!fox!jumps!over!the!lazy!dog.” as a
single string.
○ Reprint this sentence as “The quick brown fox jumps over the lazy
dog.” using the replace() function to replace every “!” exclamation
mark with a blank space.
○ Reprint that sentence as: “THE QUICK BROWN FOX JUMPS OVER
THE LAZY DOG.” using the upper() function
○ Reprint the sentence in reverse.'''

string="The!quick!brown!fox!jumps!over!the!lazy!dog."
print (string)  # first output of the same string

sentence=(string.replace('!'," ")) # ! is replaced by space and a new string is assigned to variable sentence

print(sentence) # second output of the string without ! mark

print(sentence.upper()) # third output of the senctence with upper case using upper function
