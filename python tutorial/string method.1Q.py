#1Q.Write a Python program to Count all letters, digits, and special symbols from the given string 

#Input = “P@#yn26at^&i5ve” 

input_str = "P@#yn26at^&i5ve"

chars = digits = symbols = 0

for char in input_str:
    if char.isalpha():
        chars += 1
    elif char.isdigit():
        digits += 1
    else:
        symbols += 1

print(f"Chars = {chars} Digits = {digits} Symbol = {symbols}")
