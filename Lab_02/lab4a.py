'''
Name: Iresha Lakmali
Student ID: 162279236


'''

from random import randint

secret = randint(1,10)

while True : 
    user_guess = input("Enter a number between 1 and 10:  ")
    if user_guess.isnumeric():
        
        if (int(user_guess) == secret):
            print ("Correct! You win")
            break
        
        elif int(user_guess) < 1 or int(user_guess) > 10:
                print("Error: not a number or out of bounds.")
            
        
        else:
             print("Sorry, try again.")
        
    else :
        print("Error: not a number or out of bounds.")

    
