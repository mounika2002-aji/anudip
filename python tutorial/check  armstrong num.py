#Q6. Write a function to check if given number is Armstrong or no return True if given number is Armstrong, False otherwise
def is_armstrong(number):
    digits = str(number)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    return total == number
print(is_armstrong(153))
print(is_armstrong(9474))
print(is_armstrong(123))
