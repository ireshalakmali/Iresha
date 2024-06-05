'''
Name: Iresha Lakmali
Student ID: 162279236

Sample Output

Circle Area Calculator
Enter a radius between 0 and 1999. Press Enter to exit: 2
Radius: 2. Area: 12.566370614359172.
Enter a radius between 0 and 1999. Press Enter to exit: ten
Error: ten is not a number.
Enter a radius between 0 and 1999. Press Enter to exit: 17
Radius: 17. Area: 907.9202768874502.
Enter a radius between 0 and 1999. Press Enter to exit: 2001
Error: 2001 is out of range.
Enter a radius between 0 and 1999. Press Enter to exit: 
Exiting...


'''

import math

def circle_area(radius):
    return math.pi*radius**2

if __name__ == "__main__":
    print("Circle Area Calculator")