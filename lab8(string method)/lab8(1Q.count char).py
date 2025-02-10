#1Q.Write a Python program to Count all letters, digits, and special symbols from the given string 

#Input = “P@#yn26at^&i5ve” 

#Output: Chars = 8 Digits = 2 Symbol = 3

# Function to count letters, digits, and special symbols
def count_elements(string):
    char_count = sum(char.isalpha() for char in string)  # Count letters
    digit_count = sum(char.isdigit() for char in string)  # Count digits
    symbol_count = len(string) - char_count - digit_count  # Count special symbols
    
    print(f"Chars = {char_count} Digits = {digit_count} Symbol = {symbol_count}")

# Given input
input_string = "P@#yn26at^&i5ve"
count_elements(input_string)
