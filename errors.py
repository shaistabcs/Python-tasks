# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program") # Syntax error - as the print statement needed opening and closing parentheses
print ("\n") # Syntax error or compilation error occurs here as it had TAB space and no parentheses which gives Unexpected indent
    # Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24" # syntax error and runtime error and logical error - unexpected indent that had a TAB space and strings cannot be mixed with integers also it is not equal == to strings
age = int(age_Str) # syntax error - unexpected indent that had a TAB space also called compilation error
print("I'm " + str(age) + " years old.") # Syntax error for Tab space- runtime error and logical error for concatenate strings with integers

    # Variables declaring additional years and printing the total years of age
years_from_now = "3"  # Syntax error for tab space
total_years = age + int(years_from_now) #logical error as numbers has to be integer and runtime error if not integer

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = (total_years * 12)+6 # runtime error as the total variable is not defined and logical error as i have to add 6 months in order to produce 330 months old output

print ("In 3 years and 6 months, I'll be " + str(total_months) + " months old") # syntax error and runtime error- needed parentheses and int to str conversion needed

print ("The total number of years: ", total_years) # syntax error for opening and closing parentheses and comma and logical error
# I printed the total number of years at the end of the code as the output did not make sense before so i arranged it logically 


#HINT, 330 months is the correct answer


