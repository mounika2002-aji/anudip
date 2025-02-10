#3Q.Write a python program finding the factorial of a given number using a while loop.
num = int(input("Enter a number: "))
factorial, i = 1, 1

while i <= num:
    factorial *= i
    i += 1

print("Factorial:", factorial)
