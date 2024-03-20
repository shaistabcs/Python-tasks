'''
● Create a new Python file in the Dropbox folder for this task, and call it
dob_task.py.
● In your Python file, write a program that reads the data from the text file
provided (DOB.txt) and prints it out in two different sections in the format
displayed below'''


# To Open the text file
with open('DOB.txt', 'r') as file:
    lines = file.readlines()

# Initialize lists to store names and dates of birth
names = []
dob = []

# Splitting each line into names and dates of birth
for line in lines:
    parts = line.split()  # Splitting the line into words assuming space as a delimiter
    print(parts) # extra line of code to see how the words are separated 
    name = ' '.join(parts[:-3])  # Assuming the name is the first part
    date_of_birth = ' '.join(parts[-3:])  # Assuming date of birth is the last three parts
    names.append(name)
    dob.append(date_of_birth)

# Prints out names only
print("Names")
for name in names: 
    print(name)

# Prints out dates of birth only
print("\nDates of Birth")
for date in dob:
    print(date)