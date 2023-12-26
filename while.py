print("This program is going to ask the user to enter a number\nand then prints out each number and then it calculates the average of the number ")
avg = []
while True:
    ask_user =float(input("Please enter a number: "))
    if ask_user==-1: #if user inputs -1 then program will terminate
        break
    else:
        avg.append(float(ask_user)) # The user inputs will be added in the list
        average = sum(avg)/(len(avg)) #Average formula

print (avg) # This line will print out the numbers entered by user in a list
print (average) # This line will print the average