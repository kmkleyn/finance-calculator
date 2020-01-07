#The purpose of this program is to allow the user to choose between and use 2 different financial calculators.
#One calculator will calculate interest on an investment.
#The other calculator will calculate interest on a bond.

#To do the calculations it is necessary to import the math module.
import math

#First, the user will choose between the 2 calculators.
calculator = input('''Choose either 1 for 'investment' or 2 for 'bond' from the menu below to proceed:
\n
investment      - to calculate the amount of interest you'll earn on interest
bond            - to calculate the amount you'll have to pay on a home loan
Enter your choice: ''')

#If the user's first input is invalid, the program will print an error message. 
while calculator != "1" and calculator != "2":
        print("ERROR: you have not entered a valid option. Please try again.")
        calculator = input('''Choose either 1 for 'investment' or 2 for 'bond' from the menu below to proceed:
\n
investment      - to calculate the amount of interest you'll earn on interest
bond            - to calculate the amount you'll have to pay on a home loan
Enter your choice: ''')

#This code will run if the user selects 'investment'
#The user will be asked to input the following: initial deposit, interest rate p.a. and length of investment in years.
#The user must then choose whether they want to calculate simple or compound interest.
#The calculation will be made and the result printed to the user.
if calculator == "1":
    deposit = float(input("Enter the amount you are depositing: R"))
    interest_rate = float(input("Enter your interest rate (please exclude the '%' sign): ")) / 100
    years = float(input("Enter the number of years you plan to invest for: "))
    interest = input('''Choose the type of interest you would like to calculate from the menu below to proceed:
Enter 1 for 'simple'
Enter 2 for 'compound'
Enter your choice: ''')

    #This code will print an error message if the user's input is invalid.
    while interest != "1" and interest != "2":
        print("ERROR: You have not entered a valid option. Please try again.")
        interest = input('''Choose the type of interest you would like to calculate from the menu below to proceed:
Enter 1 for 'simple'
Enter 2 for 'compound'
Enter your choice: ''')
    
    #This code will run if the user selects 'simple' interest.
    if interest == "1":
        interest_calc = deposit * (1 + interest_rate * years)
        
    #This code will run if the user selects 'compound' interest.
    else:
        interest_calc = deposit * math.pow((1 + interest_rate) , years)
        
    #This prints out the investment total to the user.
    print(f"Your investment will reach the following amount: R{interest_calc:.2f}.")

#This code will run if the user selects 'bond'.
#The user will be asked to input the following: present house value, interest rate p.a. and number of months to repay the bond.
#The calculation will be made and the result printed to the user.
else:
    pres_house_value = float(input("Enter the current value of the house: R"))
    interest_rate = float(input("Enter your interest rate (please exclude the '%' sign): ")) / 100
    months = float(input("Enter the number of months you plan to repay the bond: "))
    monthly_interest = interest_rate / 12
    bond_repayment = (pres_house_value * monthly_interest) / (1 - (1 + monthly_interest) **-months) 
    print(f"Your monthly bond repayment is R{bond_repayment:.2f}")
