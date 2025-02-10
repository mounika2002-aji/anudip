#2Q.Write a python program to check whether a number is palindrome or not?

# Function to check if a number is a palindrome
def is_palindrome(num):
    # Convert the number to a string
    num_str = str(num)
    
    # Check if the string is equal to its reverse
    if num_str == num_str[::-1]:
        return True
    else:
        return False

# Input from the user
num = int(input("Enter a number: "))

# Check if the number is palindrome and print the result
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
