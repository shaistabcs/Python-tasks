
given_number = int(input("Enter a number which is even to print out star pattern: \n"))


if given_number % 2==0: # If number is even.
    stars = "*"
    for i in range(0 ,10):
        stars = stars + "*"
        print(stars)
        index = 10-i
        print(stars[0:index])
else:
    print("you have entered an odd number")



# I have tried but my code looks like this please see the output..I am close but cant print the actual output using one single loop
# please guide me thank you
#The output result of my code looks like iam close but i still cant figured out.
#please see both files uploaded in dropbos..pattern.py and pattern1.py