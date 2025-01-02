#2Q.two variables and print that which variable is largest using ternary operato
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

largest = a if a > b else b
print(f"The largest number is: {largest}")
