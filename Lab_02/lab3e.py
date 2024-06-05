'''
Name: Iresha Lakmali
Student ID: 162279236

Sample Output

Enter the answer to 1 + 6, press 's' to skip or 'q' to quit: 27
Incorrect. Try again.
Enter the answer to 1 + 6, or press 's' to skip or 'q' to quit: 7
Correct! You have been awarded 1 point!"
Next question...
Enter the answer to 2 + 18, or press 's' to skip: s
Question skipped. 0 points awarded.
Enter the answer to 17 + 5, or press 's' to skip: q
Quiz over. You scored 50.0%.


'''

from random import randint

total = 0
grade = 0
count = 0

while True:
    num1 = randint(1,10)
    num2 = randint(1,10)
    secret = num1+num2

    user_input = input("Enter the answer to " + str(num1) + " + " + str(num2) + "," + "press 's' to skip or 'q' to quit: ")

    
    
    if user_input == 'q':
            grade += 1
            percentage=(grade/grade+count)*100
            print("Quiz over. You scored " + str(percentage) + "%")
            break

    
    elif user_input == 's':
            print("Question skipped. 0 points awarded") 
            count += 0   

    else:
           
            if int(user_input) == secret:
                print("Correct! You have been awarded 1 point!")
                print("Next question...")
                total += 1
               
            else:      
                print("Incorrect. Try again.")


    
            


   
   





