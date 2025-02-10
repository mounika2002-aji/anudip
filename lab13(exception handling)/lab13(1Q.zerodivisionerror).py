#1Q.write a python programe to handle a ZeroDivisionError exception when dividing a number by zero.

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    return result

# Example usage
num1 = 10
num2 = 0
division_result = divide_numbers(num1, num2)

# Display the result
print(division_result)
