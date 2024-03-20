'''
● Create a file called student_register.py
● Write a program that allows a user to register students for an exam venue.
● First, ask the user how many students are registering.
● Create a for loop that runs for that number of students.
● Each time the loop runs the program should ask the user to enter the
next student ID number.
● Write each of the ID numbers to a text file called reg_form.txt
● Include a dotted line after each student ID because this document will be
used as an attendance register, which the students will sign when they
arrive at the exam venue.'''

# First Ask the user for the number of students those are registering
num_students = int(input("How many students are registering? "))

# Open the file in write mode to create or overwrite the existing content
with open('reg_form.txt', 'w') as file:
    # Create a for loop that runs for the number of students
    for i in range(num_students):
        # Ask the user to enter the next student ID number
        student_id = input(f"Enter Student ID for student {i+1}: ")
        
        # Write the student ID to the file along with a dotted line
        file.write(f"{student_id}\n{'.'*30}\n")

print("Registration complete. Please Check reg_form.txt for the exam students register.")
