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

def alternate_case_characters(input_str):
    result = ""
    for i, char in enumerate(input_str):
        if i % 2 == 0:
            result += char.upper()
        else:
            result += char.lower()
    return result

def alternate_case_words(input_str):
    words = input_str.split()
    result_words = []
    for i, word in enumerate(words):
        if i % 2 == 0:
            result_words.append(word.lower())
        else:
            result_words.append(word.upper())
    return ' '.join(result_words)

# Example 1: Alternate case characters
input_str1 = "Hello World"
result1 = alternate_case_characters(input_str1)
print("Alternate Case Characters:", result1)

# Example 2: Alternate case words
input_str2 = "I am learning to code"
result2 = alternate_case_words(input_str2)
print("Alternate Case Words:", result2)
