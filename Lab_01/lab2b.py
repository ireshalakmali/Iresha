'''
Name: Iresha Lakmali
Student ID: 162279236

'''
#allow user to enter their income
income = int(input("Enter your gross income: "))

#allow user to enter the number of dependents
dependents = int(input("Enter the number of dependents: "))

#As the question, each dependent multiply with 20000, then there is a deduction from gross income
dependent_deduction = dependents*2000

#it is common amount that deduct from gross income
standard_deduction = 10000

#this is how taxable income calculate
taxable_income = income - (dependent_deduction+standard_deduction)

#calculate the tax according to the gross income
if income >= 64000:
    result = taxable_income * 0.25 
    

elif (64000 > income ) and (income >= 32000):
    result = taxable_income * 0.15 

else:
    result = taxable_income * 0.1 


# finally, according to the tax, the total tax will be dispaly
if result < 0:
    total_tax = 0
    print ("The income tax is $"+str(total_tax))
else:
    total_tax = result
    print ("The income tax is $"+str(total_tax))


    
