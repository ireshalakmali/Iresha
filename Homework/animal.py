def my_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

if __name__ == "__main__":
    user_numbers = []
    print("AVERAGE CALCULATOR")
    while True:
        user_input = input("Enter a number to add to your sum. Pressing Enter will exit. ")
        if user_input == "":
            break
        else: 
            user_numbers.append(int(user_input))
    num_sum = my_sum(user_numbers)
    num_length = len(user_numbers)
    average = num_sum / num_length
    print(f"Total sum is: {num_sum}. Total count is: {num_length}. Average for this list is: {average}.")
    print("Thank you for using average calculator.")