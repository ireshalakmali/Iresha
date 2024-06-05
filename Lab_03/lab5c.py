import random


animals = ['snake', 'hamster', 'scorpion', 'beaver', 'mosquito', 'camel', 'vulture', 'horse', 'python', 'capybara' ]
secret = random.choice(animals)

print("I'm thinking of an animal. Can you guess what it is?")

while True : 
    user_guess= input("Enter a letter or a guess. Press enter to quit:")
    if (user_guess == ""):
        break
    if(user_guess == secret) :
        print ("You win!")

    if user_guess in secret:
        print ("Yes, my word contains that letter.")
    else: 
        print("Sorry, my word doesn't contain that letter.")




