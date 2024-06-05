
'''
Name: Iresha Lakmali
Student ID: 162279236

Sample Output

Guess a number between 1 and 10: 3
Sorry, that's not it.
Guess a number between 1 and 10: 5
Sorry, that's not it.
Guess a number between 1 and 10: 7
Correct! You win.

'''
from random import randint

secret = randint(1,10)

while True : 
    user_guess = int(input("Guess a number between 1 and 10: "))
    if (user_guess == secret):
        break
        

    else :
        print ("Sorry, that's not it.")
print ("Correct! You win.")
