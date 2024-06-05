'''
Name: Iresha Lakmali
Student ID: 162279236

Sample Output

Enter the answer to 12 + 14, or press 's' to skip: 27
Incorrect. Try again.
Enter the answer to 12 + 14, or press 's' to skip: 26
Correct! You have been awarded 1 point!"
Next question...
Enter the answer to 23 + 8, or press 's' to skip: s
Question skipped. 0 points awarded.
Enter the answer to 30 + 13, or press 's' to skip: 43
Correct! You have been awarded 1 point!"
Next question...
Enter the answer to 17 + 27, or press 's' to skip: 44
Correct! You have been awarded 1 point!"
You received a grade of 75.0%.

'''


num = 0
num1 = 0
num2 = 0
num3 = 0
total = 0


while num != 26:
 user_input1 = input("Enter the answer to 12 + 14, or press 's' to skip: ")

 if user_input1 == 's':
  break
 else:
  num = int(user_input1)
  
 if num != 26:
  print("Incorrect. Try again.")
  
 else:
  print("Correct! You have been awarded 1 point!")
  total += 1
print("Next question...")



while num1 !=31:
 user_input2 =input("Enter the answer to 23 + 8, or press 's' to skip: ")

 if user_input2 == 's':
  print("Question skipped. 0 points awarded.")
  break
 else:
  num1 = int(user_input2)

  if num1 != 31:
   print("Incorrect. Try again.")
  else:
   print("Correct! You have been awarded 1 point!")
   total+=1
  print("Next question...")



while num2 !=43:
  user_input3 =input("Enter the answer to 30 + 13, or press 's' to skip: ") 

  if user_input3 == 's':
   break
  else:
   num2 = int(user_input3)

  if num2 != 43:
    print("Incorrect. Try again.")
  else:
    print("Correct! You have been awarded 1 point!")
    total+=1
  print("Next question...")


while num3 !=44:
  user_input4 =input("Enter the answer to 17 + 27, or press 's' to skip: ") 

  if user_input4 == 's':
   break
  else:
   num3 = int(user_input4)

  if num3 != 44:
    print("Incorrect. Try again.")
  else:
    print("Correct! You have been awarded 1 point!")
    total+=1
  print("Next question...")
  percentage=((total/4)*100)

print("You received a grade of " + str(percentage)+ "%.")