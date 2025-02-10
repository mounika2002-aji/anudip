#3Q.Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN” 

Output: 

UpperCase : 5 

LowerCase : 18 

NumberCase : 5 

SpecialCase : 11
input_str = "Hell0 W0rld ! 123 * # welcome to pYtHoN"

uppercase = lowercase = digits = special_chars = 0

for char in input_str:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1
    elif char.isdigit():
        digits += 1
    else:
        special_chars += 1

print(f"UpperCase : {uppercase}")
print(f"LowerCase : {lowercase}")
print(f"NumberCase : {digits}")
print(f"SpecialCase : {special_chars}")
