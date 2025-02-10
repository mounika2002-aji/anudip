#1Q.Write a python program to reverse a number using a while loop.

# Function to reverse a number
def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10  # Extract the last digit
        reversed_num = reversed_num * 10 + digit  # Build the reversed number
        num //= 10  # Remove the last digit from num
    return reversed_num

# Taking user input for the number
num = int(input("Enter a number: "))

# Calling the reverse_number function to reverse the number
reversed_num = reverse_number(num)

# Displaying the result
print(f"The reversed number is: {reversed_num}")
