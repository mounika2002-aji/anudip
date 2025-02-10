#5Q.Python program to check the validity of password input by users

import re

# Function to check password validity
def check_password_validity(password):
    # Check if the password meets all the criteria using regular expressions
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    
    if not re.search("[a-z]", password):
        return "Password must contain at least one lowercase letter."
    
    if not re.search("[A-Z]", password):
        return "Password must contain at least one uppercase letter."
    
    if not re.search("[0-9]", password):
        return "Password must contain at least one digit."
    
    if not re.search("[@#$%^&+=]", password):
        return "Password must contain at least one special character (@, #, $, %, ^, &, +, =)."
    
    return "Password is valid."

# Input from the user
password = input("Enter your password: ")

# Check the password validity and print the result
print(check_password_validity(password))





