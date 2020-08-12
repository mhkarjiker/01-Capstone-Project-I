#******** Introduction *********************

#This is program can calculate either interest
#earned on an investment or monthly bond repayments
#based on the calculator selected by the user

#******** Variable Description *************

#P = principal
#r = interest rate
#t = period in years
#n = number of months
#i = monthly interest rate
#x = monthly loan repayments

import math

#********* Welcome Message *****************

#Request user to select which financial calculator they would like to use

print('''Choose either 'investment or 'bond' from the menu below to proceed:\n
         investment    - to calculate the amount of interest you'll earn on interest
         bond          - to calculate the amount you'll have to pay on a home loan\n''')

calculator = input("Enter option here: ")
calculator = calculator.lower()

if (calculator == "investment") or (calculator == "bond"):
    
    #********* Investment calculator ***********

    if calculator == "investment":
        P = float(input("Please enter the principal amount(R): "))
        r = float(input("Please enter the interest rate(%): "))
        t = float(input("Please enter the period of the investment(years): "))
        interest = input("Please enter whether you would like 'simple' or 'compound' interest: ")
        interest = interest.lower()
        if interest == "simple":
            total_interest = P*(1 + (r/100)*t)
            print(f"The total interest for the investment is R {total_interest:.2f}")
        else:
            total_interest = P*(1 + (r/100))**t
            print(f"The total interest for the investment is R {total_interest:.2f}")

    #********* Bond calculator ****************
            
    else:
        P = float(input("Please enter the present value of the house (rands): "))
        r = float(input("Please enter the annual interest rate( %): "))
        i = (r/100)/12
        n = float(input("Please enter the number of months the bond will repaid: "))
        x = (i*P)/(1 - (1 + i)**(-n))
        print(f"The monthly bond installments is R {x:.2f}")

else:
    print("Invalid Entry. Please try again")
    
