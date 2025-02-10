#2Q.Python program to check if the given string is a palindrome 

# Function to check if the string is a palindrome
def is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    s = s.replace(" ", "").lower()
    
    # Check if the string is equal to its reverse
    if s == s[::-1]:
        return True
    else:
        return False

# Input from the user
string = input("Enter a string: ")

# Check if the string is palindrome and print the result
if is_palindrome(string):
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.')


