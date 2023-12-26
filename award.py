'''Practical Task 1
Follow these steps:
● Create a new Python file in this folder called award.py.
● Design a program that determines the award a person competing in a
triathlon will receive.
● Your program should read in the times (in minutes) for all three events of a
triathlon, namely swimming, cycling, and running, and then calculate and
display the total time taken to complete the triathlon.
● The award a participant receives is based on the total time taken to
complete the triathlon. The qualifying time for awards is 100 minutes.
Display the award that the participant will receive based on the following
criteria:
Qualifying Criteria Time Range Award
Within the qualifying time. 0 - 100 minutes Provincial Colours
Within 5 minutes of the
qualifying time : 101 - 105 minutes Provincial Half Colours
Within 10 minutes of the qualifying time. 106 - 110 minutes Provincial Scroll
More than 10 minutes off from the qualifying time. 111+ minutes No award'''

#first we need three variables that takes input from a user
swimming=int(input("enter the swimming time in minutes "))
running=int(input("enter the running time in minutes "))
cycling=int(input("enter the cycling time in minutes "))

#second we have to add all three values together
duration=swimming+running+cycling

print (duration) #extra print statement to see the duration result
if duration <=100:
    print("you have won a provincial colours award and your duration is ",duration," minutes")

elif duration>=101 and duration <=105:
    print("you have won provincial half colours award and the duration is ", duration," minutes")

elif duration>=106 and duration <= 110:
    print("you have won the provincial scroll award and the duration is ", duration," minutes ") 

else :
    print ("no award")