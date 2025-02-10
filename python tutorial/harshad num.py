# Q8. Write a function that checks if the given number is a Harshad number 
# A number is a Harshad number it is divisible by it's sum of digits
# ex. 18 is Harshad number --> 1 + 8 = 9, 18 is divisible by 9
def is_harshad(number):
    digit_sum = sum(int(digit) for digit in str(number))
    return number % digit_sum == 0

print(is_harshad(18))
print(is_harshad(19))
