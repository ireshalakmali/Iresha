'''
Name: Iresha Lakmali
Student ID: 162279236

'''
#allow user to enter a decimal number between 0.0 to 0.9
num1 = float(input("Enter a decimal number between 0.0 to 0.9: "))

#round to the nearest integer and print it
if (num1<0.5):
    num2 = int(num1)
    print (num2)

elif (num1>=0.5):
    num2 = int(num1)+1
    print(num2)

else:
    print("error")

#allow user to enter any number
num = float(input("Enter a decimal number: "))

#round to the nearest integer and print it
number = int(num)
print (number)


