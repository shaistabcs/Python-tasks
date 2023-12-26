
#The following code will give you the required output with single for loop but i still need help how to avoid four lines of print statement.


given_number = int(input("Enter a number which is even to print out star pattern: \n"))
##kornia = ivy.transpile()

if given_number % 2==0: # If number is even.
    stars = "*"
    for i in range(0 ,5):
        print(stars)
        stars = stars +"*"
    print(stars[0:4])
    print(stars[0:3])
    print(stars[0:2])
    print(stars[0:1])
else:
    print("you have not entered an even number")

#Here i have left a separate code that can execute the same output if we remove print statement above from lines 5 to 8
#but the following code contains another for loop as well.

#stars = "****"
#for i in range(0 ,4):
   # index = 4-i  # i goes from 0 to 10 in this loop
   # print(stars[0:index])

#I have generated two types of code that gives the same result but i still cant find the solution in order to print out indexing from right to left in one line.
#output result:
#*
#**
#***
#****
#*****
#****
#***
#**
#*