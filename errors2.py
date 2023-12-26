# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" # Runtime error as the word Lion is not defined 
animal_type = "cub"
number_of_teeth = 16

full_spec = "There is a " + animal + " It has " + str(number_of_teeth) + " teeth and it has " + animal_type + " shape" 
# The above line had logical and runtime error.
# As it does not make sense while printing and cannot concatenate str with integers

print (full_spec) # missing parenthesis (syntax error)

