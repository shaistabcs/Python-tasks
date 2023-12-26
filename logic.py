age=int(input("please enter your age from 1 to 100 to check the condition "))
#print(age)


if age>=40 and age<65:
    print("you are over the hill")

elif age>1 and age <100:  # logical error occurs here where program checks only this condition and does not check further conditions
    print(" your age is ", age) # prints out and the following results when condition is checked.
    
    logical_error=age+5*4/2 # Here is another logical error example.
    print("logical error occurs here age+5*4/2  ", logical_error)

    calculation=(age+5)*4/2 # Logical error correction
    print ("correction of the logical error (age+5)*4/2  ", calculation)

    #print(logical_error*calculation/0) # Runtime Error occurs here if we divide by zero

elif age>=65 and age<100:
    print("Enjoy your retirement")

elif age<13:
    print ("you qualify for the kiddie discount")

elif age==21:
    print ("Congrats on your 21st!")

elif age>=100:
    print("sorry, you are dead.")

else:
    print ("age is but a number")

# The above program contains two logical errors
# First the program will not continue from second elif statement and from line 17
# Because if user inputs the age from 1 to 100 the condition is getting true and the program will terminate after second elif statement.
# So the program will not continue to check elif statements after the second elif condition onwards from line 17
# The first if statement will print out if the user inputs age between 40 and 65
# In order to fix this issue it is a better idea to move down the second elif statement on line 8 to the line 22 or just remove it.
# So that condition will be checked and printed at the end of program or in the last section of if else statements.
# second logical error is on line number 11 as the math calculation is on two different ways but the correct way is on line number 14
# line number 11 is logical error
# line number 14 is correction of logical error

# line number 17 is extra to show runtime error if the whole calculation is divided by zero