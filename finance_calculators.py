import math
print("***************Finance Calculator***************")
print("Please enter your selection from the below option: ")    
print("1. Investment - to calculate the amount of interest you'll earn on your investment")
print("2. Bond - to calculate the amount youu'll have to pay to your house loan")
calculation_type = input("Please choose one either \'investment\' or \'Bond\' calculation  ")
calculation_type = calculation_type.lower() #This line will accept upper and lower case inputs
if calculation_type == "investment": # if the user chooses investment so the following code will generate
    deposite=float(input("please enter the amount of money you are depositing ")) #I choose float because some numbers will be in floating point
    interest_rate=float(input("please enter the interest rate "))
    number_years=float(input("please enter the number of years that you are planning to invest "))
    r=float(interest_rate/100) # extra calculation where interest rate is going to be divided by 100
    interest=input("please type whether you want \'simple\' interest or \'compound\' interest  ")
    interest=interest.lower() # again this line will accept both upper and lower case of simple and compound inputs by user
    #if user selects Simple interest then the following code will be executed and if compound is selected then it will jump to compound formula
    if interest == "simple":
        #Simple Interest Formula
        total_interest=float(deposite*(r*number_years))
        end_balance=float(deposite+total_interest)
        print("The total simple interest only is calculated and the amount is ",total_interest)
        print("The total end balance with simple interest is ",end_balance)
    elif interest == "compound":
        # compound interest formula
        v=float(interest_rate/100) # extra calculation where interest rate is divided by 100.
        compound_interest=float(deposite*math.pow((1+v),number_years))
        print("The total compound interest is calculated and the amount is ", compound_interest)
    else:
        print("no selection is made Try Again") # if user inputs another word it will print this error messege
#if user inputs bond to calculate at the start of program then the following code will generate
elif calculation_type == "bond":
    house_value=float(input("please enter the present value of the house "))
    current_interest=float(input("please enter the current interest rate "))
    repay_monthes=float(input("Enter number of monthes they plan to take to repay the bond "))
    i=float(current_interest/100)/12
    Bond_repayment=float((i*house_value)/(1-(1+i)**(-repay_monthes)))
    print ("Your monthly bond repayment will be ", Bond_repayment)
else:
    print ("no selection is made") # if user does not select investment or bond then this line will print