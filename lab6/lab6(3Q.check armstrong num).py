#3Q.Python program to check if a given number is an Armstrong number

# Function to check if a number is an Armstrong number
def is_armstrong(num):
    # Convert the number to a string to easily find the number of digits
    num_str = str(num)
    num_digits = len(num_str)
    
    # Calculate the sum of each digit raised to the power of the number of digits
    total = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum is equal to the original number
    if total == num:
        return True
    else:
        return False

# Input from the user
num = int(input("Enter a number: "))

# Check if the number is an Armstrong number and print the result
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
