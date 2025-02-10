#4Q.Accept numbers using input() function until the user enters 0. If user input 0 then break the while loop and display the sum of all the numbers
total = 0

while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total += num

print("Sum of all numbers:", total)
