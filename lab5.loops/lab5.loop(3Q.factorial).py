#3Q.Write a python program finding the factorial of a given number using a while loop.

# Function to find factorial using while loop
def factorial(num):
    result = 1
    # Check if the number is negative, zero, or positive
    if num < 0:
        return "Factorial does not exist for negative numbers."
    elif num == 0:
        return 1
    else:
        while num > 1:
            result *= num
            num -= 1
        return result

# Input from the user
num = int(input("Enter a number: "))

# Find the factorial and print the result
print(f"The factorial of {num} is {factorial(num)}")
