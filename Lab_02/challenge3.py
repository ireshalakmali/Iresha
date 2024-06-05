'''
Name: Iresha Lakmali
Student ID: 162279236

CHALLENGE TASK: Binary Converter

'''
#Start with a decimal number to allow to user to input
decimal = int(input("Enter a decimal number: "))

#get the binary as a string
binary = " "

while decimal > 0 :
    #Divide that number by 2,remainder of that division will be either 0 or 1
    remainder = decimal % 2
    #get that number and convert to string and add to previously initialized binary
    binary = str(remainder) + binary
    #Divide the quotient by 2 ag 
    decimal = decimal // 2

    print("Binary number of relevant decimal number = ", binary)
