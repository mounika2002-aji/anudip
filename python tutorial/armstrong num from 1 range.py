# Q7. Write a function to print all the Armstrong number from 1 to given range
def print_armstrong_numbers(limit):
    for number in range(1, limit + 1):
        digits = str(number)
        power = len(digits)
        total = sum(int(digit) ** power for digit in digits)
        if total == number:
            print(number)
print_armstrong_numbers(800)
