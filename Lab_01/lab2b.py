'''
Name: Iresha Lakmali
Student ID: 162279236

'''
income = int(input("Enter your gross income: "))
dependents = int(input("Enter the number of dependents: "))
dependent_deduction = dependents*2000
standard_deduction = 10000
taxable_income = income - (dependent_deduction+standard_deduction)

if income >= 64000:
    result = taxable_income * 0.25 
    

elif (64000 > income ) and (income >= 32000):
    result = taxable_income * 0.15 

else:
    result = taxable_income * 0.1 

if result < 0:
    total_tax = 0
    print ("The income tax is $"+str(total_tax))
else:
    total_tax = result
    print ("The income tax is $"+str(total_tax))


    
